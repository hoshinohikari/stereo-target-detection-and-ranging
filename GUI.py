import sys
from PyQt5 import QtWidgets
from Ui_camera import Ui_Form
import os

get_camera_name = ''

class Test(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def slot1(self):
        process = os.popen('python GUI.py')
        output = process.read()
        self.ui.textBrowser.setText(output)
    def slot2(self):
        global get_camera_name
        get_camera_name = self.ui.comboBox.currentText()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
