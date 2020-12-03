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
        self.show()

    def _factory_show_all_data_func(self, output_table_widget : SQLTableWidget, input_table_name : str) -> FunctionType:
        def result_function():
            header = self.sql_executor.get_column_names(input_table_name)
            data = self.sql_executor.execute_query(f"SELECT * FROM {input_table_name}")
            output_table_widget.show_query_resluts(header, data)
        
        return result_function

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())