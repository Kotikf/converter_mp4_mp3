# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.9


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import pathlib
import moviepy.editor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_file.setGeometry(QtCore.QRect(20, 90, 100, 20))
        self.choose_file.setObjectName("choose_file")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(20, 130, 131, 20))
        self.convert.setObjectName("convert")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(170, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setStyleSheet("color: red;")
        self.result.setText("")
        self.result.setObjectName("result")
        self.save_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_file_btn.setGeometry(QtCore.QRect(20, 50, 100, 20))
        self.save_file_btn.setObjectName("save_file_btn")
        self.save_file = QtWidgets.QLineEdit(self.centralwidget)
        self.save_file.setGeometry(QtCore.QRect(140, 50, 301, 20))
        self.save_file.setObjectName("save_file")
        self.add_file = QtWidgets.QComboBox(self.centralwidget)
        self.add_file.setGeometry(QtCore.QRect(140, 90, 300, 20))
        self.add_file.setObjectName("add_file")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.save_file_btn.clicked.connect(self.get_save_path)
        self.choose_file.clicked.connect(self.get_path)
        self.convert.clicked.connect(self.start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_file.setText(_translate("MainWindow", "Выбрать файл(ы)"))
        self.convert.setText(_translate("MainWindow", "Преобразовать в mp3"))
        self.save_file_btn.setText(_translate("MainWindow", "Сохранить в"))

    def get_path(self):
        self.file_list = QFileDialog.getOpenFileNames(None, 'Open file', '/', ('*.mp4'))[0]
        if self.file_list:
            for el in self.file_list:
                self.add_file.addItem(el)
                
    def get_save_path(self):
        self.get_save_path = QFileDialog.getExistingDirectory(None, 'Open Directory', '/')
        if self.get_save_path:
            self.save_file.setText(self.get_save_path)

    def start(self):
        try:
            
            for el in self.file_list:
                self.Convert(str(el))
        except AttributeError:
            pass
        except OSError:
            error = QMessageBox()
            error.setWindowTitle('Неверный путь')
            error.setText('путь для сохранения указан с ошибками')
            error.setIcon(QMessageBox.Warning)

            error.exec_()

    def Convert(self, filename):
        self.video = moviepy.editor.VideoFileClip(filename)
        self.audio = self.video.audio
        self.full_name = os.path.basename(filename)
        self.name = os.path.splitext(self.full_name)[0]
        self.audio.write_audiofile(f'{self.get_save_path}/{self.name}.mp3')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
