import sys
from PyQt5 import QtWidgets
from Ui_camera import Ui_Form
import os

get_camera_num = '0'

class Test(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def slot1(self):
        #print(get_camera_num)
        #print(type(get_camera_num))
        os.popen('python run.py --camera ' + get_camera_num)
    def slot2(self):
        global get_camera_num
        get_camera_num = self.ui.comboBox.currentText()[-1]
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
