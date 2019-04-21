import sys
from PyQt5 import QtWidgets
from Ui_camera import Ui_Form
import os

get_camera_num = '0'
inputfile = ''
outputfile = ''

class Test(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def slot1(self):
        os.popen('python run.py --camera ' + get_camera_num)
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
        os.popen('python run.py --input ' + inputfile + ' --output ' + outputfile)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
