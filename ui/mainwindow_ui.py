# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow_UI(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 700)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.addRow_btn = QPushButton(self.tab)
        self.addRow_btn.setObjectName(u"addRow_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addRow_btn.sizePolicy().hasHeightForWidth())
        self.addRow_btn.setSizePolicy(sizePolicy1)
        self.addRow_btn.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.addRow_btn)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.updateRow_btn = QPushButton(self.tab)
        self.updateRow_btn.setObjectName(u"updateRow_btn")
        sizePolicy1.setHeightForWidth(self.updateRow_btn.sizePolicy().hasHeightForWidth())
        self.updateRow_btn.setSizePolicy(sizePolicy1)
        self.updateRow_btn.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.updateRow_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.deleteRow_btn = QPushButton(self.tab)
        self.deleteRow_btn.setObjectName(u"deleteRow_btn")
        sizePolicy1.setHeightForWidth(self.deleteRow_btn.sizePolicy().hasHeightForWidth())
        self.deleteRow_btn.setSizePolicy(sizePolicy1)
        self.deleteRow_btn.setMinimumSize(QSize(0, 45))

        self.verticalLayout_4.addWidget(self.deleteRow_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.rawTableWidget = QTableWidget(self.tab)
        self.rawTableWidget.setObjectName(u"rawTableWidget")
        self.rawTableWidget.setMidLineWidth(0)
        self.rawTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.rawTableWidget.setRowCount(0)
        self.rawTableWidget.setColumnCount(0)
        self.rawTableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.rawTableWidget.verticalHeader().setDefaultSectionSize(30)

        self.horizontalLayout_3.addWidget(self.rawTableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.showSchedule_btn = QPushButton(self.tab)
        self.showSchedule_btn.setObjectName(u"showSchedule_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showSchedule_btn.sizePolicy().hasHeightForWidth())
        self.showSchedule_btn.setSizePolicy(sizePolicy2)
        self.showSchedule_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.showSchedule_btn)

        self.showEmployee_btn = QPushButton(self.tab)
        self.showEmployee_btn.setObjectName(u"showEmployee_btn")
        sizePolicy2.setHeightForWidth(self.showEmployee_btn.sizePolicy().hasHeightForWidth())
        self.showEmployee_btn.setSizePolicy(sizePolicy2)
        self.showEmployee_btn.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.showEmployee_btn)

        self.showJob_btn = QPushButton(self.tab)
        self.showJob_btn.setObjectName(u"showJob_btn")

        self.horizontalLayout.addWidget(self.showJob_btn)

        self.showWorkload_btn = QPushButton(self.tab)
        self.showWorkload_btn.setObjectName(u"showWorkload_btn")

        self.horizontalLayout.addWidget(self.showWorkload_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.genTableWidget = QTableWidget(self.tab_2)
        self.genTableWidget.setObjectName(u"genTableWidget")
        self.genTableWidget.setMidLineWidth(0)
        self.genTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.genTableWidget.setRowCount(0)
        self.genTableWidget.setColumnCount(0)
        self.genTableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.genTableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_3.addWidget(self.genTableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.allocationCount_btn = QPushButton(self.tab_2)
        self.allocationCount_btn.setObjectName(u"allocationCount_btn")

        self.horizontalLayout_2.addWidget(self.allocationCount_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442", None))
        self.addRow_btn.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.updateRow_btn.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.deleteRow_btn.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.showSchedule_btn.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.showEmployee_btn.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438", None))
        self.showJob_btn.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.showWorkload_btn.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.allocationCount_btn.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u044c \u043f\u043e \u0441\u0442\u0430\u0432\u043a\u0430\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
    # retranslateUi

