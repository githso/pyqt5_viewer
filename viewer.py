# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 586)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/mozhi/Desktop/图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.FilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.FilePath.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FilePath.setObjectName("FilePath")
        self.gridLayout.addWidget(self.FilePath, 1, 0, 1, 1)
        self.OpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.OpenButton.setObjectName("OpenButton")
        self.gridLayout.addWidget(self.OpenButton, 0, 0, 1, 1)
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 3, 2, 1, 1)
        self.ZoomSld = QtWidgets.QSlider(self.centralwidget)
        self.ZoomSld.setMaximumSize(QtCore.QSize(888880, 25))
        self.ZoomSld.setMinimum(1)
        self.ZoomSld.setMaximum(200)
        self.ZoomSld.setProperty("value", 100)
        self.ZoomSld.setOrientation(QtCore.Qt.Horizontal)
        self.ZoomSld.setObjectName("ZoomSld")
        self.gridLayout.addWidget(self.ZoomSld, 3, 3, 1, 1)
        self.ShowRate = QtWidgets.QLabel(self.centralwidget)
        self.ShowRate.setMaximumSize(QtCore.QSize(999999, 11111111))
        self.ShowRate.setObjectName("ShowRate")
        self.gridLayout.addWidget(self.ShowRate, 3, 1, 1, 1)
        self.ImgPath = QtWidgets.QListWidget(self.centralwidget)
        self.ImgPath.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ImgPath.setViewMode(QtWidgets.QListView.ListMode)
        self.ImgPath.setObjectName("ImgPath")
        item = QtWidgets.QListWidgetItem()
        self.ImgPath.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ImgPath.addItem(item)
        self.gridLayout.addWidget(self.ImgPath, 2, 0, 2, 1)
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setMidLineWidth(20)
        self.Frame.setObjectName("Frame")
        self.ShowLabel = QtWidgets.QLabel(self.Frame)
        self.ShowLabel.setEnabled(True)
        self.ShowLabel.setGeometry(QtCore.QRect(80, 90, 291, 301))
        self.ShowLabel.setMaximumSize(QtCore.QSize(99999, 99999))
        self.ShowLabel.setMouseTracking(False)
        self.ShowLabel.setAutoFillBackground(False)
        self.ShowLabel.setObjectName("ShowLabel")
        self.gridLayout.addWidget(self.Frame, 0, 1, 3, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "hso图片浏览器"))
        self.OpenButton.setText(_translate("MainWindow", "Open"))
        self.DeleteButton.setText(_translate("MainWindow", "删除"))
        self.ShowRate.setText(_translate("MainWindow", "缩放率"))
        __sortingEnabled = self.ImgPath.isSortingEnabled()
        self.ImgPath.setSortingEnabled(False)
        item = self.ImgPath.item(0)
        item.setText(_translate("MainWindow", "sdsdsa 迭代迭代"))
        item = self.ImgPath.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        self.ImgPath.setSortingEnabled(__sortingEnabled)
        self.ShowLabel.setText(_translate("MainWindow", "showlabel"))
