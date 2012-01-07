# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submissionItem.ui'
#
# Created: Sat Jan  7 19:58:44 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_submissionItem(object):
    def setupUi(self, submissionItem):
        submissionItem.setObjectName("submissionItem")
        submissionItem.resize(712, 105)
        submissionItem.setMinimumSize(QtCore.QSize(0, 0))
        submissionItem.setAutoFillBackground(True)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(submissionItem)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonUpvote = QtGui.QPushButton(submissionItem)
        self.buttonUpvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonUpvote.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("upvote-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("upvote-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonUpvote.setIcon(icon)
        self.buttonUpvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonUpvote.setCheckable(True)
        self.buttonUpvote.setAutoExclusive(True)
        self.buttonUpvote.setFlat(True)
        self.buttonUpvote.setObjectName("buttonUpvote")
        self.verticalLayout.addWidget(self.buttonUpvote)
        self.labelScore = QtGui.QLabel(submissionItem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.labelScore.setFont(font)
        self.labelScore.setText("")
        self.labelScore.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelScore.setObjectName("labelScore")
        self.verticalLayout.addWidget(self.labelScore)
        self.buttonDownvote = QtGui.QPushButton(submissionItem)
        self.buttonDownvote.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setMaximumSize(QtCore.QSize(20, 20))
        self.buttonDownvote.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("downvote-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("downvote-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonDownvote.setIcon(icon1)
        self.buttonDownvote.setIconSize(QtCore.QSize(15, 14))
        self.buttonDownvote.setCheckable(True)
        self.buttonDownvote.setAutoExclusive(True)
        self.buttonDownvote.setFlat(True)
        self.buttonDownvote.setObjectName("buttonDownvote")
        self.verticalLayout.addWidget(self.buttonDownvote)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTitle = QtGui.QLabel(submissionItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setText("")
        self.labelTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setMargin(3)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_2.addWidget(self.labelTitle)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSubreddit = QtGui.QLabel(submissionItem)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelSubreddit.setFont(font)
        self.labelSubreddit.setObjectName("labelSubreddit")
        self.horizontalLayout.addWidget(self.labelSubreddit)
        self.labelRedditor = QtGui.QLabel(submissionItem)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.labelRedditor.setFont(font)
        self.labelRedditor.setObjectName("labelRedditor")
        self.horizontalLayout.addWidget(self.labelRedditor)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.retranslateUi(submissionItem)
        QtCore.QMetaObject.connectSlotsByName(submissionItem)

    def retranslateUi(self, submissionItem):
        submissionItem.setWindowTitle(QtGui.QApplication.translate("submissionItem", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSubreddit.setText(QtGui.QApplication.translate("submissionItem", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRedditor.setText(QtGui.QApplication.translate("submissionItem", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

