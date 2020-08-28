from viewer import Ui_MainWindow#
import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class PICV(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PICV, self).__init__(parent)
        self.setupUi(self)  # 载入窗口
        self.BeforeOpenFile()
        self.CallBackFunctions()  # 响应函数集合
        self.setMouseTracking(True)
        self.ShowLabel.grabKeyboard()
    def BeforeOpenFile(self):
        #图片列表清空
        #移动图片2列表
        #禁用滑动条
        #禁用删除按钮
        #禁止追踪
        self.zx = 0
        self.zy = 0
        self.ls = []
        self.Inlabel = False
        self.Inframe = False
        self.moveflag = False
        self.loadpic = False
        self.ImgPath.clear()
        self.ZoomSld.setEnabled(False)
        self.FilePath.setEnabled(False)
        self.DeleteButton.setEnabled(False)
        self.centralwidget.setMouseTracking(False)
        self.Frame.setMouseTracking(False)
        self.ShowLabel.setMouseTracking(False)
    def AfterOpenFile(self):  # 激活
        self.loadpic = True
        #控件类
        self.ZoomSld.setEnabled(True)
        self.DeleteButton.setEnabled(True)
        self.ShowLabel.setScaledContents(True)
        #mouseMoveEvent
        self.centralwidget.setMouseTracking(True)
        self.Frame.setMouseTracking(True)
        self.ShowLabel.setMouseTracking(True)

    def CallBackFunctions(self):   # 持续响应函数集合
        self.OpenButton.clicked.connect(self.SetFilePath)
        self.ImgPath.itemSelectionChanged.connect(self.Loading)#项目更改时加载图片
        self.ZoomSld.valueChanged.connect(self.ZoomShow)
        self.DeleteButton.clicked.connect(self.DeleteFile)

    def SetFilePath(self):
        self.FilePath.clear()
        self.ImgPath.clear()
        dirname = QFileDialog.getExistingDirectory(self, "浏览", 'C:/')
        if dirname:
            self.FilePath.setText(dirname)
        else:
            return

        a_list = os.listdir(dirname)
        self.img_list = []
        for i in a_list:
            if i.endswith('.jpg'):
                self.img_list.append(dirname + '/' + i)
        if self.img_list:
            for j in self.img_list:
                self.ImgPath.addItem(j)  # 添加项目
        self.ImgPath.setCurrentItem(self.ImgPath.item(0))

    def DeleteFile(self):
        ind = self.ImgPath.currentRow()
        self.ImgPath.takeItem(ind)  # 可视界面item中删除项
        os.remove(self.img_list[ind])  # 文件删除
        self.img_list.pop(ind)  # 逻辑引用同步

    def Loading(self):#加载图片并确定缩放率
        self.AfterOpenFile()
        self.pic = QPixmap(self.img_list[self.ImgPath.currentRow()])
        self.fixpoint()
    def fixpoint(self):
        self.y = 0
        self.x = 0
        if self.Frame.size().height()/self.pic.size().height() >= self.Frame.size().width()/self.pic.size().width():#取最小的作为缩放率
            r = self.Frame.size().width()/self.pic.size().width()
            self.y = (self.Frame.size().height() - self.pic.size().height() * r) / 2
        else:
            r = self.Frame.size().height()/self.pic.size().height()
            self.x = (self.Frame.size().width() - self.pic.size().width() * r) / 2
        self.ZoomSld.setValue(r * 100)
        self.ZoomShow()

    def ZoomShow(self):#缩放率设置
        r = self.ZoomSld.value() / 100
        temp = self.pic.scaled(self.pic.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.ShowLabel.setGeometry(self.x, self.y, temp.size().width() * r, temp.size().height() * r)
        self.ShowLabel.setPixmap(temp)
        self.ShowRate.setText('缩放率：{:.2f}'.format(r))

    def nofocuslft(self, r):  # 无焦点缩放
        r = r / 100
        temp = self.pic.size() * r
        ratex = (temp.width() - self.ShowLabel.width()) / 2
        ratey = (temp.height() - self.ShowLabel.height()) / 2
        self.x = self.ShowLabel.x() - ratex
        self.y = self.ShowLabel.y() - ratey

    def hasfocuslft(self, r):  # 有焦点缩放
        r = r / 100
        temp = self.pic.size() * r
        ratex = temp.width() / self.ShowLabel.width()
        ratey = temp.height() / self.ShowLabel.height()
        self.x = (self.zx - self.Frame.x())*(1-ratex) + self.ShowLabel.x() * ratex
        self.y = (self.zy - self.Frame.y())*(1-ratey) + self.ShowLabel.y() * ratey

    def mouseDoubleClickEvent(self, e):
        if self.loadpic:
            if self.Inlabel:
                if e.button() == Qt.LeftButton:
                    self.zx = e.x()
                    self.zy = e.y()
                    self.hasfocuslft(self.ZoomSld.value()+50)
                    self.ZoomSld.setValue(self.ZoomSld.value()+50)

    def wheelEvent(self, e):
        if self.loadpic:
            self.zx = e.x()
            self.zy = e.y()
            r = self.ZoomSld.value() + e.angleDelta().y() / 60
            if self.Inlabel:
                self.hasfocuslft(r)
            elif self.Inframe:
                self.nofocuslft(r)
            else:
                pass
            self.ZoomSld.setValue(self.ZoomSld.value() + e.angleDelta().y() / 60)
    #如果你在重写mouseMoveEvent的时候不加setMouseTracking(True)，那么你只有按住鼠标左键移动的时候才会获取值
    #1、要想实现mouseMoveEvent，则需要在构造函数中添加setMouseTrack(true)，直接得到监听事件。
    # #若是setMouseTrack(false),只有鼠标按下才会有mouseMove监听事件响应。
    #调用这个函数后，如想使mouseMoveEvent有效，也就是在鼠标在区域内移动就会触发，而非鼠标按键按下时才触发，注意只能是QWidget，如果是QMainwindow，则无效。

    def mousePressEvent(self, e):
        if self.loadpic:
            if self.Inlabel:
                if e.button() == Qt.LeftButton:
                    self.moveflag = True
                if e.button() == Qt.RightButton:
                    self.fixpoint()

    def mouseMoveEvent(self, e):
        self.centralwidget.setMouseTracking(True)
        self.Frame.setMouseTracking(True)
        self.ShowLabel.setMouseTracking(True)
        if self.loadpic:
            if self.moveflag:
                if len(self.ls) == 2:
                    self.ls.pop(0)
                    self.ls.append(e.localPos().toPoint())
                else:
                    self.ls.append(e.localPos().toPoint())
                    self.ls.append(e.localPos().toPoint())
                delta = self.ls[1]-self.ls[0]
                xy = QPoint(self.ShowLabel.geometry().x(), self.ShowLabel.geometry().y())
                self.ShowLabel.move(xy + delta)
                self.ShowLabel.geometry()
            # 判断光标所在区域

            framel = self.Frame.x()
            framer = self.Frame.x()+self.Frame.width()
            framet = self.Frame.y()
            frameb = self.Frame.y()+self.Frame.height()
            if framel < e.x() < framer and framet < e.y() < frameb:
                self.Inframe = True  # 如果光标在图片区域，而且图片已载入，那么可以使用滚轮
            else:
                self.Inframe = False
            labell = self.ShowLabel.x() + self.Frame.x()
            labelr = self.ShowLabel.x()+self.ShowLabel.width() + self.Frame.x()
            labelt = self.ShowLabel.y() + self.Frame.y()
            labelb = self.ShowLabel.y()+self.ShowLabel.height() + self.Frame.y()
            if labell < e.x() < labelr and labelt < e.y() < labelb:
                self.Inlabel = True  # 如果光标在图片区域，而且图片已载入，那么可以使用滚轮
            else:
                self.Inlabel = False

    def mouseReleaseEvent(self, e):
        self.ls = []           # 拖拽跟踪列表
        self.moveflag = False  # 松手后不可以拖拽图片
        self.x = self.ShowLabel.x()  # 拖拽松手后后确定图片位置
        self.y = self.ShowLabel.y()

    def keyPressEvent(self, e):
        if self.DeleteButton.isEnabled():
            if e.key() == Qt.Key_D:
                self.DeleteFile()
            if e.key() == Qt.Key_Down:
                c = self.ImgPath.currentRow()
                l = len(self.img_list)
                self.ImgPath.setCurrentItem(self.ImgPath.item((c + 1) % l))
            if e.key() == Qt.Key_Up:
                c = self.ImgPath.currentRow()
                l = len(self.img_list)
                self.ImgPath.setCurrentItem(self.ImgPath.item((c - 1) % l))
            if e.key() == Qt.Key_Left:
                r = self.ZoomSld.value() - 3
                self.nofocuslft(r)
                self.ZoomSld.setValue(r)
            if e.key() == Qt.Key_Right:
                r = self.ZoomSld.value() + 3
                self.nofocuslft(r)
                self.ZoomSld.setValue(r)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 添加进程
    ui = PICV()  # 实例化
    ui.show()  # 显示界面
    sys.exit(app.exec_())  # 退出进程

