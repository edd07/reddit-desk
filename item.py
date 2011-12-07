# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created: Sun Nov 27 16:37:46 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Item(object):
    def setupUi(self, Item):
        Item.setObjectName(_fromUtf8("Item"))
        Item.resize(712, 209)
        Item.setMinimumSize(QtCore.QSize(0, 100))
        Item.setWindowTitle(QtGui.QApplication.translate("Item", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Item)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonUpvote = QtGui.QPushButton(Item)
        self.buttonUpvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("upvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpvote.setIcon(icon)
        self.buttonUpvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonUpvote.setCheckable(True)
        self.buttonUpvote.setFlat(True)
        self.buttonUpvote.setObjectName(_fromUtf8("buttonUpvote"))
        self.verticalLayout.addWidget(self.buttonUpvote)
        self.labelScore = QtGui.QLabel(Item)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelScore.setFont(font)
        self.labelScore.setText(_fromUtf8(""))
        self.labelScore.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelScore.setObjectName(_fromUtf8("labelScore"))
        self.verticalLayout.addWidget(self.labelScore)
        self.buttonDownvote = QtGui.QPushButton(Item)
        self.buttonDownvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("downvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownvote.setIcon(icon1)
        self.buttonDownvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonDownvote.setFlat(True)
        self.buttonDownvote.setObjectName(_fromUtf8("buttonDownvote"))
        self.verticalLayout.addWidget(self.buttonDownvote)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelTitulo = QtGui.QLabel(Item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitulo.sizePolicy().hasHeightForWidth())
        self.labelTitulo.setSizePolicy(sizePolicy)
        self.labelTitulo.setText(_fromUtf8(""))
        self.labelTitulo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelTitulo.setWordWrap(True)
        self.labelTitulo.setMargin(3)
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.verticalLayout_2.addWidget(self.labelTitulo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelSubreddit = QtGui.QLabel(Item)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelSubreddit.setFont(font)
        self.labelSubreddit.setText(QtGui.QApplication.translate("Item", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSubreddit.setObjectName(_fromUtf8("labelSubreddit"))
        self.horizontalLayout.addWidget(self.labelSubreddit)
        self.labelRedditor = QtGui.QLabel(Item)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelRedditor.setFont(font)
        self.labelRedditor.setText(QtGui.QApplication.translate("Item", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRedditor.setObjectName(_fromUtf8("labelRedditor"))
        self.horizontalLayout.addWidget(self.labelRedditor)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.retranslateUi(Item)
        QtCore.QMetaObject.connectSlotsByName(Item)

    def retranslateUi(self, Item):
        pass

