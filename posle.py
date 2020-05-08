from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sqlite3
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton )
from functools import partial

class Ui_MainWindow(QWidget):
    def load_Data(self):
        connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"

        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        return

        self.tableWidget.setHorizontalHeaderLabels(
            ('ID', 'NAME', 'EM@IL', 'Phone', 'Description')
        )

    #def delete(self):
        #self.tableWidget.removeRow(self.tableWidget.currentRow())
    def delete(self):
        connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"
        result = connection.execute(query)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                name = data[1]
                mail = data[2]
                telephone = data[3]
                opisanie = data[4]
                result_1 = connection.execute("DELETE FROM feedback_feedback WHERE id=? AND name=? AND  email=? AND phone=? AND description=?",(id, name, mail, telephone, opisanie))
                connection.commit()
                self.load_Data()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 781))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("bg_2.jpg"))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 150, 441, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        ##
        event_witharg = partial(self.on_click, self.pushButton_2)
        self.pushButton_2.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        ##
        event_witharg = partial(self.on_click, self.pushButton_4)
        self.pushButton_4.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        ##
        event_witharg = partial(self.on_click, self.pushButton_3)
        self.pushButton_3.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        ##
        event_witharg = partial(self.on_click, self.pushButton_5)
        self.pushButton_5.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        ##
        event_witharg = partial(self.on_click, self.pushButton_6)
        self.pushButton_6.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        ##
        event_witharg = partial(self.on_click, self.pushButton_7)
        self.pushButton_7.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        ##
        event_witharg = partial(self.on_click, self.pushButton_8)
        self.pushButton_8.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        ##
        event_witharg = partial(self.on_click, self.pushButton_9)
        self.pushButton_9.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        ##
        event_witharg = partial(self.on_click, self.pushButton_10)
        self.pushButton_10.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.LoadData = QtWidgets.QPushButton(self.centralwidget)
        self.LoadData.setGeometry(QtCore.QRect(820, 920, 93, 28))
        self.LoadData.setObjectName("LoadData")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(960, 920, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        ##
        event_witharg = partial(self.on_click, self.pushButton_11)
        self.pushButton_11.clicked.connect(event_witharg)
        ##
        self.LoadData_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadData_2.setGeometry(QtCore.QRect(660, 680, 93, 28))
        self.LoadData_2.setObjectName("LoadData_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(800, 680, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(620, 20, 471, 711))
        self.tableWidget.setStyleSheet("\n"
"\n"
"")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(670, 670, 93, 28))
        self.pushButton_load.setObjectName("pushButton_load")

        self.pushButton_load.clicked.connect(self.load_Data)

        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(800, 670, 93, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.pushButton_delete.clicked.connect(self.delete)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 20, 181, 41))
        self.textBrowser.setStyleSheet("background-color:silver;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    @pyqtSlot()
    def on_click(self, data):
        data.setText("Reserved by :" + self.tableWidget.model().index(0,1).data())
        #self.delete()
        self.tableWidget.removeRow(self.tableWidget.currentRow())
        self.tableWidget.removeRow(0);
        print(data)
        print('PyQt5 button click')


        '''
    def calldelete(self, id):
		connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"
        result = connection.execute(query)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                #name = data[1]
                #mail = data[2]
                #telephone = data[3]
                #opisanie = data[4]
                result = connection.execute("DELETE FROM feedback_feedback WHERE id=? ",(id))
                connection.commit()
                self.load_Data()
'''
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Table5"))

        self.pushButton_4.setText(_translate("MainWindow", "Table2"))
        self.pushButton_3.setText(_translate("MainWindow", "Table6"))
        self.pushButton_5.setText(_translate("MainWindow", "Table4"))
        self.pushButton_6.setText(_translate("MainWindow", "Table1"))
        self.pushButton_7.setText(_translate("MainWindow", "Table3"))
        self.pushButton_8.setText(_translate("MainWindow", "Table7"))
        self.pushButton_9.setText(_translate("MainWindow", "Table8"))
        self.pushButton_10.setText(_translate("MainWindow", "Table9"))
        self.LoadData.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete "))
        self.LoadData_2.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete "))
        self.pushButton_load.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Exotic_Deer</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
