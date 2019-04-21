import sys
import argparse
from PyQt5 import QtWidgets
from Ui_camera import Ui_Form
from cache import detect_cam ,detect_video
from yolo import YOLO

get_camera_num = '0'
inputfile = ''
outputfile = ''

class Test(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def slot1(self):
        parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
        FLAGS = parser.parse_args()
        print('python run.py --camera ' + get_camera_num)
        detect_cam(YOLO(**vars(FLAGS)), eval(get_camera_num), 2560, 960, "")
    def slot2(self):
        global get_camera_num
        get_camera_num = self.ui.comboBox.currentText()[-1]
    def slot3(self):
        global inputfile
        inputfile, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "Video Files (*.mp4);;All Files (*)")
        if (inputfile == ""):
            print("取消选择")
            return
        self.ui.lineEdit.setText(inputfile)
    def slot4(self):
        global outputfile
        outputfile, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "Video Files (*.mp4);;All Files (*)")
        if (outputfile == ""):
            print("取消选择")
            return
        self.ui.lineEdit_2.setText(outputfile)
    def slot5(self):
        parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
        FLAGS = parser.parse_args()
        print('python run.py --input ' + inputfile + ' --output ' + outputfile)
        detect_video(YOLO(**vars(FLAGS)), inputfile, outputfile)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
