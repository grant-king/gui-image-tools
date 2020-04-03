# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tool_models import ImageTool

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("fish.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.origainal_button = QtWidgets.QPushButton(self.centralwidget)
        self.origainal_button.setGeometry(QtCore.QRect(50, 880, 300, 100))
        self.origainal_button.setObjectName("origainal_button")
        self.bw_button = QtWidgets.QPushButton(self.centralwidget)
        self.bw_button.setGeometry(QtCore.QRect(400, 880, 300, 100))
        self.bw_button.setObjectName("bw_button")
        self.save_bw_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_bw_button.setGeometry(QtCore.QRect(750, 880, 300, 100))
        self.save_bw_button.setObjectName("save_bw_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(1250, 880, 100, 100))
        self.next_button.setObjectName("next_button")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setGeometry(QtCore.QRect(1100, 880, 100, 100))
        self.prev_button.setObjectName("prev_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.custom_setup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.origainal_button.setText(_translate("MainWindow", "Original"))
        self.bw_button.setText(_translate("MainWindow", "Black and White"))
        self.save_bw_button.setText(_translate("MainWindow", "Save B&W"))
        self.next_button.setText(_translate("MainWindow", ">"))
        self.prev_button.setText(_translate("MainWindow", "<"))

    def custom_setup(self):
        self.image_tool = ImageTool()
        self.origainal_button.clicked.connect(self.show_original)
        self.bw_button.clicked.connect(self.show_bw)
        self.save_bw_button.clicked.connect(self.image_tool.save_bw_image)
        self.next_button.clicked.connect(self.show_next)
        self.prev_button.clicked.connect(self.show_previous)

    def show_original(self):
        image = self.image_tool.current_image.color_img
        height, width, channel = image.shape
        line_bytes = 3 * width
        q_img = QtGui.QImage(image, width, height, line_bytes, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.photo.setPixmap(QtGui.QPixmap(q_img))

    def show_bw(self):
        image = self.image_tool.current_image.binary_img
        height, width = image.shape
        line_bytes = 1 * width
        q_img = QtGui.QImage(image, width, height, line_bytes, QtGui.QImage.Format_Grayscale8)
        self.photo.setPixmap(QtGui.QPixmap(q_img))

    def show_next(self):
        self.image_tool.increase_current_image()
        image_shape = self.image_tool.get_current_display_size()
        self.photo.setGeometry(QtCore.QRect(0, 0, image_shape[1], image_shape[0]))
        self.photo.setScaledContents(True)
        self.show_original()

    def show_previous(self):
        self.image_tool.decrease_current_image()
        image_shape = self.image_tool.get_current_display_size()
        self.photo.setGeometry(QtCore.QRect(0, 0, image_shape[1], image_shape[0]))
        self.photo.setScaledContents(True)
        self.show_original()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

