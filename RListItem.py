from PyQt4 import QtCore, QtGui
import reddit

class RListItem(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__()
        self.addWidget( QtGui.QLabel("blah"))