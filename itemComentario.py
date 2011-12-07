# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemComentario.ui'
#
# Created: Mon Nov 28 13:35:53 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ItemComentario(object):
    def setupUi(self, ItemComentario):
        ItemComentario.setObjectName(_fromUtf8("ItemComentario"))
        ItemComentario.resize(712, 64)
        ItemComentario.setMinimumSize(QtCore.QSize(0, 40))
        ItemComentario.setWindowTitle(QtGui.QApplication.translate("ItemComentario", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ItemComentario)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonUpvote = QtGui.QPushButton(ItemComentario)
        self.buttonUpvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("upvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpvote.setIcon(icon)
        self.buttonUpvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonUpvote.setCheckable(True)
        self.buttonUpvote.setAutoExclusive(True)
        self.buttonUpvote.setFlat(True)
        self.buttonUpvote.setObjectName(_fromUtf8("buttonUpvote"))
        self.verticalLayout.addWidget(self.buttonUpvote)
        self.buttonDownvote = QtGui.QPushButton(ItemComentario)
        self.buttonDownvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("downvote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownvote.setIcon(icon1)
        self.buttonDownvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonDownvote.setCheckable(True)
        self.buttonDownvote.setAutoExclusive(True)
        self.buttonDownvote.setFlat(True)
        self.buttonDownvote.setObjectName(_fromUtf8("buttonDownvote"))
        self.verticalLayout.addWidget(self.buttonDownvote)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelRedditor = QtGui.QLabel(ItemComentario)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelRedditor.setFont(font)
        self.labelRedditor.setText(QtGui.QApplication.translate("ItemComentario", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRedditor.setObjectName(_fromUtf8("labelRedditor"))
        self.horizontalLayout.addWidget(self.labelRedditor)
        self.labelScore = QtGui.QLabel(ItemComentario)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelScore.setFont(font)
        self.labelScore.setText(QtGui.QApplication.translate("ItemComentario", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelScore.setObjectName(_fromUtf8("labelScore"))
        self.horizontalLayout.addWidget(self.labelScore)
        self.labelTime = QtGui.QLabel(ItemComentario)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelTime.setFont(font)
        self.labelTime.setText(QtGui.QApplication.translate("ItemComentario", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTime.setObjectName(_fromUtf8("labelTime"))
        self.horizontalLayout.addWidget(self.labelTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.labelComentario = QtGui.QLabel(ItemComentario)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComentario.sizePolicy().hasHeightForWidth())
        self.labelComentario.setSizePolicy(sizePolicy)
        self.labelComentario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelComentario.setWordWrap(True)
        self.labelComentario.setMargin(3)
        self.labelComentario.setObjectName(_fromUtf8("labelComentario"))
        self.verticalLayout_2.addWidget(self.labelComentario)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.retranslateUi(ItemComentario)
        QtCore.QMetaObject.connectSlotsByName(ItemComentario)

    def retranslateUi(self, ItemComentario):
        pass

