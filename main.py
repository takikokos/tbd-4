from types import FunctionType
from PySide2 import QtWidgets
from ui.mainwindow_ui import MainWindow_UI
from ui.sql_table import SQLTableWidget
from db_api.postgres_executor import PostgresExecutor
import sys


class MainWindow(QtWidgets.QWidget, MainWindow_UI):
    def __init__(self):
        super().__init__()
        self.sql_executor = PostgresExecutor("./dev_postgres_conn.conf.json", reuse_conn=True)

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