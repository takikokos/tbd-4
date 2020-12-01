from typing import Any
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem


class SQLTableWidget():
    '''
        wrapper to add functionality to default QTableWidget
    '''
    def __init__(self, qtable : QTableWidget):
        self.wrapped_table = qtable

    def __getattr__(self, name: str) -> Any:
        if name in self.wrapped_table.__dict__:
            return self.wrapped_table.__getattribute__(name)
        elif name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError

    def show_query_resluts(self, header : list, rows : list) -> None:
        self.wrapped_table.setColumnCount(len(header))
        self.wrapped_table.setRowCount(len(rows))

        for i, c_name in enumerate(header):
            self.wrapped_table.setHorizontalHeaderItem(i, QTableWidgetItem(c_name))
        