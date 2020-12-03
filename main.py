from types import FunctionType
from typing import Any, Dict, List
from PySide2 import QtWidgets
import PySide2
from PySide2.QtWidgets import QMessageBox, QLabel, QLineEdit, QHBoxLayout
from ui.mainwindow_ui import MainWindow_UI
from ui.creatingrow_ui import CreateRowWindow_UI, Qt, QMetaObject
from ui.sql_table import SQLTableWidget
from db_api.postgres_executor import PostgresExecutor
import sys
import logging
from sql.query_patterns import generate_delete_query, SELECT_ALL_QUERY, generate_update_query, generate_insert_query


def show_dialog(text : str, info : str, buttons : list) -> str:
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.setInformativeText(info)

    button = buttons[0]
    for b in buttons[1:]:
        button |= b

    msgBox.setStandardButtons(button)
    return msgBox.exec_()

class CreateRowWindow(QtWidgets.QWidget, CreateRowWindow_UI):
    def __init__(self, columns : List[str], callback : FunctionType):
        super().__init__()
        self.setupUi(self)
        self.onClose_callback = callback
        self.pressed_add_button = False
        self.pushButton.clicked.connect(self.add_btn_clicked)

        for column_name in columns:            
            label = QLabel(self)
            label.setObjectName(f"{column_name}_label")
            label.setAlignment(Qt.AlignCenter)
            label.setText(f"{column_name} = ")

            edit = QLineEdit(self)
            edit.setObjectName(f"{column_name}_edit")

            hlayout = QHBoxLayout(self)
            hlayout.setObjectName(f"{column_name}_layout")
            hlayout.addWidget(label)
            hlayout.addWidget(edit)
            # hlayout.itemAt(1).widget().childAt(0).text()
            self.data_layout.addLayout(hlayout)

    def add_btn_clicked(self):
        self.pressed_add_button = True
        self.close()
    
    def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
        self.onClose_callback()
        event.accept()

class MainWindow(QtWidgets.QWidget, MainWindow_UI):
    def __init__(self):
        super().__init__()
        self.sql_executor = PostgresExecutor("./dev_postgres_conn.conf.json", reuse_conn=True)
        self.deleted_rows_stash : List[str] = []
        self.updated_values_stash : Dict[str, Dict[str, Any]] = {}
        self.added_rows_stash : List[List[str]] = []
        self.current_table : str = ""

        self.setupUi(self)
        self.rawTableWidget = SQLTableWidget(self.rawTableWidget) # some monkey patching
        self.genTableWidget = SQLTableWidget(self.genTableWidget) # some monkey patching

        self.showEmployee_btn.clicked.connect(self._factory_show_all_data_func(self.rawTableWidget, "employee"))
        self.showJob_btn.clicked.connect(self._factory_show_all_data_func(self.rawTableWidget, "job"))
        self.showSchedule_btn.clicked.connect(self._factory_show_all_data_func(self.rawTableWidget, "job_schedule"))
        self.showWorkload_btn.clicked.connect(self._factory_show_all_data_func(self.rawTableWidget, "workload"))
        
        self.deleteRow_btn.clicked.connect(self._delete_rows)
        self.updateRow_btn.clicked.connect(self._commit_changes)
        self.addRow_btn.clicked.connect(self._add_row)

        self.rawTableWidget.cellChanged.connect(self._table_item_changed)

        self.show()

    def _factory_show_all_data_func(self, output_table_widget : SQLTableWidget, input_table_name : str) -> FunctionType:
        def result_function():
            header = self.sql_executor.get_column_names(input_table_name)
            data, status = self.sql_executor.execute_query(SELECT_ALL_QUERY.format(table_name = input_table_name))
            if status != 0:
                logging.error(f"Error while opening table {self.input_table_name}")
                show_dialog("Не удалось загрузить таблицу", "", [QMessageBox.Ok])
            output_table_widget.show_query_resluts(header, data)
            self.current_table = input_table_name
            self.deleted_rows_stash = []
            self.updated_values_stash = {}
            self.added_rows_stash = []
            logging.info(f"Loaded {len(data)} rows from {input_table_name}")
        
        return result_function

    def _delete_rows(self):
        indexes = [x.row_index for x in self.rawTableWidget.get_selected_items()]
        ids = [self.rawTableWidget.get_sqlid(x.row_index) for x in self.rawTableWidget.get_selected_items()]
        logging.info(f"Adding {len(set(indexes))} row(s) to delete stash")
        self.rawTableWidget.delete_rows(indexes)
        self.rawTableWidget.wrapped_table.clearSelection()
        self.deleted_rows_stash += ids

    def _commit_changes(self):
        if len(self.deleted_rows_stash) == 0 and len(self.updated_values_stash.keys()) == 0\
            and len(self.added_rows_stash) == 0:
            show_dialog("Обновление не требуется", "", [QMessageBox.Ok])
            return

        answer = show_dialog("Обновление данных", 
                            f"Вы уверенны что хотите удалить {len(set(self.deleted_rows_stash))} строк, \
                                обновить {len(self.updated_values_stash.keys())} строк\
                                и добавить {len(self.added_rows_stash)} строк?", 
                            [QMessageBox.Yes, QMessageBox.No])

        if answer == QMessageBox.Yes:
            self.commit_add_stash()
            self.commit_update_stash()
            self.commit_delete_stash()
            self._factory_show_all_data_func(self.rawTableWidget, self.current_table)()
            
    def _table_item_changed(self):
        item = self.rawTableWidget.get_selected_items()
        if len(item) != 1:
            return # suppose cell wasn't changed by user 
        else:
            item = item[0]
        column_name = self.rawTableWidget.get_column_name(item.column_index)
        sql_id = self.rawTableWidget.get_sqlid(item.row_index)
        new_value = item.value if item.value != "" else None
        self.updated_values_stash[sql_id] = self.updated_values_stash.get(sql_id, {})
        self.updated_values_stash[sql_id][column_name] = new_value

    def _add_row(self):
        if self.current_table == "":
            return
        self._dialog = CreateRowWindow(self.sql_executor.get_column_names(self.current_table), self._add_row_callback)
        self.hide()
        self._dialog.show()

    def _add_row_callback(self):
        self.show()
        if self._dialog.pressed_add_button:
            row_values = [data_layout.itemAt(1).wid.text() for data_layout in self._dialog.data_layout.children()]
            self.added_rows_stash.append(row_values)
            self.rawTableWidget.wrapped_table.insertRow(0)
            self.rawTableWidget.set_row_values(0, row_values)

    def commit_delete_stash(self):
        if len(self.deleted_rows_stash) != 0:
            id_column_name = self.rawTableWidget.get_sqlid_column_name()
            query = generate_delete_query(self.current_table, id_column_name, self.deleted_rows_stash)
            _, status = self.sql_executor.execute_query(query)
            if status != 0:
                logging.error(f"Error while deleting from {self.current_table}")
                show_dialog("Ошибка при удалении данных", "", [QMessageBox.Ok])
            else:
                logging.info(f"Deleted {len(self.deleted_rows_stash)} row(s) from {self.current_table}")
            self.deleted_rows_stash = []

    def commit_update_stash(self):
        id_column = self.rawTableWidget.get_sqlid_column_name()
        for sql_id, changes in self.updated_values_stash.items():
            query = generate_update_query(self.current_table, changes, id_column, sql_id)
            _, status = self.sql_executor.execute_query(query)
            if status != 0:
                logging.error(f"Error while updating in {self.current_table}. ID = {sql_id}")
                show_dialog("Ошибка при обновлении данных", "", [QMessageBox.Ok])
            else:
                logging.info(f"Updated {len(self.updated_values_stash.keys())} row(s) in {self.current_table}")
        self.updated_values_stash = {}

    def commit_add_stash(self):
        all_ok = True
        for row_values in self.added_rows_stash:
            query = generate_insert_query(self.current_table, 
                                          self.sql_executor.get_column_names(self.current_table), 
                                          row_values)
            _, status = self.sql_executor.execute_query(query)
            all_ok = all_ok and (status == 0)
            if status == 0:
                self.rawTableWidget.wrapped_table.insertRow(0)
                self.rawTableWidget.set_row_values(0, row_values)
                logging.info(f"Inserted row into {self.current_table}")
            else:
                logging.error(f"Error while inserting into {self.current_table}. Id : {row_values[0]}")
        if not all_ok:
            show_dialog("Ошибки при добавлении данных", "", [QMessageBox.Ok])
        self.added_rows_stash = []

        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())