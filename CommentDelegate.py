from PySide import QtCore, QtGui

class CommentDelegate(QtGui.QItemDelegate):
     
    def __init__(self, parent=None, *args):
        QtGui.QItemDelegate.__init__(self, parent)
     
    def createEditor(self, parent, styleOption, index):
        widget = QtGui.QWidget(parent)
        verticalLayout = QtGui.QVBoxLayout(CommentDelegate)
        #index.data trae algo
        btnUpvote=QtGui.QPushButton(QtGui.QPixmap('upvote.png'), "", widget)
        btnDownvote=QtGui.QPushButton(QtGui.QPixmap('downvote.png'), "", widget)
        verticalLayout.addItem(btnUpvote)
        verticalLayout.addItem(btnDownvote)
        return widget
     
    def updateEditorGeometry(self,editor, styleOption, index):
         editor.setGeometry(styleOption.rect);
     
    def setEditorData(self, editor, index):
         print 'setEditorData...', index.data(), editor.__class__
         editor.setText(index.data())
