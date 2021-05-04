# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageSecrets(object):
    def setupUi(self, ImageSecrets):
        ImageSecrets.setObjectName("ImageSecrets")
        ImageSecrets.resize(489, 340)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Minimum,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageSecrets.sizePolicy().hasHeightForWidth())
        ImageSecrets.setSizePolicy(sizePolicy)
        ImageSecrets.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.central_widget = QtWidgets.QWidget(ImageSecrets)
        self.central_widget.setObjectName("central_widget")
        self.stacked_widget = QtWidgets.QStackedWidget(self.central_widget)
        self.stacked_widget.setGeometry(QtCore.QRect(0, 0, 451, 271))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.stacked_widget.setFont(font)
        self.stacked_widget.setObjectName("stacked_widget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout = QtWidgets.QGridLayout(self.home)
        self.gridLayout.setObjectName("gridLayout")
        self.main_lbl = QtWidgets.QLabel(self.home)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(26)
        self.main_lbl.setFont(font)
        self.main_lbl.setObjectName("main_lbl")
        self.gridLayout.addWidget(self.main_lbl, 0, 0, 1, 2)
        self.encode_btn = QtWidgets.QPushButton(self.home)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.encode_btn.setFont(font)
        self.encode_btn.setObjectName("encode_btn")
        self.gridLayout.addWidget(self.encode_btn, 1, 0, 1, 1)
        self.decode_btn = QtWidgets.QPushButton(self.home)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.decode_btn.setFont(font)
        self.decode_btn.setObjectName("decode_btn")
        self.gridLayout.addWidget(self.decode_btn, 1, 1, 1, 1)
        self.stacked_widget.addWidget(self.home)
        self.encode = QtWidgets.QWidget()
        self.encode.setObjectName("encode")
        self.encode_plain_text_edit = QtWidgets.QPlainTextEdit(self.encode)
        self.encode_plain_text_edit.setGeometry(QtCore.QRect(170, 130, 256, 121))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.encode_plain_text_edit.setFont(font)
        self.encode_plain_text_edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.encode_plain_text_edit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.encode_plain_text_edit.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn,
        )
        self.encode_plain_text_edit.setDocumentTitle("")
        self.encode_plain_text_edit.setPlainText("")
        self.encode_plain_text_edit.setOverwriteMode(True)
        self.encode_plain_text_edit.setBackgroundVisible(False)
        self.encode_plain_text_edit.setObjectName("encode_plain_text_edit")
        self.encode_main_lbl = QtWidgets.QLabel(self.encode)
        self.encode_main_lbl.setGeometry(QtCore.QRect(9, 9, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(26)
        self.encode_main_lbl.setFont(font)
        self.encode_main_lbl.setObjectName("encode_main_lbl")
        self.encode_image_btn = QtWidgets.QPushButton(self.encode)
        self.encode_image_btn.setGeometry(QtCore.QRect(9, 96, 151, 29))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.encode_image_btn.setFont(font)
        self.encode_image_btn.setObjectName("encode_image_btn")
        self.encode_pixmap_lbl = QtWidgets.QLabel(self.encode)
        self.encode_pixmap_lbl.setGeometry(QtCore.QRect(9, 129, 151, 121))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.encode_pixmap_lbl.sizePolicy().hasHeightForWidth(),
        )
        self.encode_pixmap_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.encode_pixmap_lbl.setFont(font)
        self.encode_pixmap_lbl.setStyleSheet("border: 2px dashed")
        self.encode_pixmap_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.encode_pixmap_lbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.encode_pixmap_lbl.setScaledContents(False)
        self.encode_pixmap_lbl.setObjectName("encode_pixmap_lbl")
        self.encode_submit_btn = QtWidgets.QPushButton(self.encode)
        self.encode_submit_btn.setGeometry(QtCore.QRect(166, 96, 261, 29))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.encode_submit_btn.setFont(font)
        self.encode_submit_btn.setObjectName("encode_submit_btn")
        self.stacked_widget.addWidget(self.encode)
        self.decode = QtWidgets.QWidget()
        self.decode.setObjectName("decode")
        self.decode_main_lbl = QtWidgets.QLabel(self.decode)
        self.decode_main_lbl.setGeometry(QtCore.QRect(9, 9, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(26)
        self.decode_main_lbl.setFont(font)
        self.decode_main_lbl.setObjectName("decode_main_lbl")
        self.decode_plain_text_edit = QtWidgets.QPlainTextEdit(self.decode)
        self.decode_plain_text_edit.setGeometry(QtCore.QRect(166, 131, 276, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.decode_plain_text_edit.setFont(font)
        self.decode_plain_text_edit.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn,
        )
        self.decode_plain_text_edit.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff,
        )
        self.decode_plain_text_edit.setReadOnly(True)
        self.decode_plain_text_edit.setObjectName("decode_plain_text_edit")
        self.decode_submit_btn = QtWidgets.QPushButton(self.decode)
        self.decode_submit_btn.setGeometry(QtCore.QRect(166, 96, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decode_submit_btn.setFont(font)
        self.decode_submit_btn.setObjectName("decode_submit_btn")
        self.decode_image_btn = QtWidgets.QPushButton(self.decode)
        self.decode_image_btn.setGeometry(QtCore.QRect(9, 96, 151, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decode_image_btn.setFont(font)
        self.decode_image_btn.setObjectName("decode_image_btn")
        self.decode_copy_tool_btn = QtWidgets.QToolButton(self.decode)
        self.decode_copy_tool_btn.setGeometry(QtCore.QRect(393, 97, 49, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decode_copy_tool_btn.setFont(font)
        self.decode_copy_tool_btn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.decode_copy_tool_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.decode_copy_tool_btn.setAutoRaise(False)
        self.decode_copy_tool_btn.setObjectName("decode_copy_tool_btn")
        self.decode_pixmap_lbl = QtWidgets.QLabel(self.decode)
        self.decode_pixmap_lbl.setGeometry(QtCore.QRect(10, 130, 151, 131))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.decode_pixmap_lbl.sizePolicy().hasHeightForWidth(),
        )
        self.decode_pixmap_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.decode_pixmap_lbl.setFont(font)
        self.decode_pixmap_lbl.setStyleSheet("border: 2px dashed")
        self.decode_pixmap_lbl.setScaledContents(True)
        self.decode_pixmap_lbl.setObjectName("decode_pixmap_lbl")
        self.stacked_widget.addWidget(self.decode)
        ImageSecrets.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(ImageSecrets)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 26))
        self.menubar.setObjectName("menubar")
        self.menu_general = QtWidgets.QMenu(self.menubar)
        self.menu_general.setObjectName("menu_general")
        self.menu_themes = QtWidgets.QMenu(self.menubar)
        self.menu_themes.setObjectName("menu_themes")
        ImageSecrets.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageSecrets)
        self.statusbar.setObjectName("statusbar")
        ImageSecrets.setStatusBar(self.statusbar)
        self.action_encode = QtWidgets.QAction(ImageSecrets)
        self.action_encode.setObjectName("action_encode")
        self.action_decode = QtWidgets.QAction(ImageSecrets)
        self.action_decode.setObjectName("action_decode")
        self.action_exit = QtWidgets.QAction(ImageSecrets)
        self.action_exit.setObjectName("action_exit")
        self.action_home = QtWidgets.QAction(ImageSecrets)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.action_home.setFont(font)
        self.action_home.setObjectName("action_home")
        self.action_light = QtWidgets.QAction(ImageSecrets)
        self.action_light.setObjectName("action_light")
        self.action_dark = QtWidgets.QAction(ImageSecrets)
        self.action_dark.setObjectName("action_dark")
        self.menu_general.addAction(self.action_home)
        self.menu_general.addAction(self.action_encode)
        self.menu_general.addAction(self.action_decode)
        self.menu_general.addAction(self.action_exit)
        self.menu_themes.addAction(self.action_light)
        self.menu_themes.addAction(self.action_dark)
        self.menubar.addAction(self.menu_general.menuAction())
        self.menubar.addAction(self.menu_themes.menuAction())

        self.retranslateUi(ImageSecrets)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ImageSecrets)

    def retranslateUi(self, ImageSecrets):
        _translate = QtCore.QCoreApplication.translate
        ImageSecrets.setWindowTitle(_translate("ImageSecrets", "ImageSecrets"))
        self.main_lbl.setText(_translate("ImageSecrets", "ImageSecrets"))
        self.encode_btn.setText(_translate("ImageSecrets", "Encode"))
        self.decode_btn.setText(_translate("ImageSecrets", "Decode"))
        self.encode_plain_text_edit.setPlaceholderText(
            _translate("ImageSecrets", "Type in the message to encode"),
        )
        self.encode_main_lbl.setText(_translate("ImageSecrets", "Encode"))
        self.encode_image_btn.setText(_translate("ImageSecrets", "Choose image"))
        self.encode_pixmap_lbl.setText(
            _translate("ImageSecrets", "No preview available"),
        )
        self.encode_submit_btn.setText(_translate("ImageSecrets", "Submit"))
        self.decode_main_lbl.setText(_translate("ImageSecrets", "Decode"))
        self.decode_plain_text_edit.setPlaceholderText(
            _translate("ImageSecrets", "Decoded message will appear here."),
        )
        self.decode_submit_btn.setText(_translate("ImageSecrets", "Submit"))
        self.decode_image_btn.setText(_translate("ImageSecrets", "Choose image"))
        self.decode_copy_tool_btn.setText(_translate("ImageSecrets", "Copy"))
        self.decode_pixmap_lbl.setText(
            _translate("ImageSecrets", "No preview available"),
        )
        self.menu_general.setTitle(_translate("ImageSecrets", "general"))
        self.menu_themes.setTitle(_translate("ImageSecrets", "themes"))
        self.action_encode.setText(_translate("ImageSecrets", "encode"))
        self.action_decode.setText(_translate("ImageSecrets", "decode"))
        self.action_exit.setText(_translate("ImageSecrets", "exit"))
        self.action_home.setText(_translate("ImageSecrets", "home"))
        self.action_light.setText(_translate("ImageSecrets", "light"))
        self.action_dark.setText(_translate("ImageSecrets", "dark"))
