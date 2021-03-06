# Form implementation generated from reading ui file 'smuc.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_img_lb = QtWidgets.QLabel(self.centralwidget)
        self.player_img_lb.setGeometry(QtCore.QRect(20, 140, 220, 320))
        self.player_img_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.player_img_lb.setText("")
        self.player_img_lb.setObjectName("player_img_lb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.player_name_lb = QtWidgets.QLabel(self.centralwidget)
        self.player_name_lb.setGeometry(QtCore.QRect(20, 80, 471, 40))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        self.player_name_lb.setFont(font)
        self.player_name_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.player_name_lb.setObjectName("player_name_lb")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 140, 241, 321))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 220, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.player_intel_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.player_intel_btn.setFont(font)
        self.player_intel_btn.setObjectName("player_intel_btn")
        self.verticalLayout.addWidget(self.player_intel_btn)
        self.player_str_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_str_btn.setFont(font)
        self.player_str_btn.setObjectName("player_str_btn")
        self.verticalLayout.addWidget(self.player_str_btn)
        self.player_spd_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_spd_btn.setFont(font)
        self.player_spd_btn.setObjectName("player_spd_btn")
        self.verticalLayout.addWidget(self.player_spd_btn)
        self.player_dura_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_dura_btn.setFont(font)
        self.player_dura_btn.setObjectName("player_dura_btn")
        self.verticalLayout.addWidget(self.player_dura_btn)
        self.player_pwr_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_pwr_btn.setFont(font)
        self.player_pwr_btn.setObjectName("player_pwr_btn")
        self.verticalLayout.addWidget(self.player_pwr_btn)
        self.player_combat_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_combat_btn.setFont(font)
        self.player_combat_btn.setObjectName("player_combat_btn")
        self.verticalLayout.addWidget(self.player_combat_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.player_intel_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_intel_lb.setFont(font)
        self.player_intel_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_intel_lb.setObjectName("player_intel_lb")
        self.verticalLayout_2.addWidget(self.player_intel_lb)
        self.player_str_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_str_lb.setFont(font)
        self.player_str_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_str_lb.setObjectName("player_str_lb")
        self.verticalLayout_2.addWidget(self.player_str_lb)
        self.player_spd_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_spd_lb.setFont(font)
        self.player_spd_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_spd_lb.setObjectName("player_spd_lb")
        self.verticalLayout_2.addWidget(self.player_spd_lb)
        self.player_dura_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_dura_lb.setFont(font)
        self.player_dura_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_dura_lb.setObjectName("player_dura_lb")
        self.verticalLayout_2.addWidget(self.player_dura_lb)
        self.player_pwr_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_pwr_lb.setFont(font)
        self.player_pwr_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_pwr_lb.setObjectName("player_pwr_lb")
        self.verticalLayout_2.addWidget(self.player_pwr_lb)
        self.player_combat_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.player_combat_lb.setFont(font)
        self.player_combat_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_combat_lb.setObjectName("player_combat_lb")
        self.verticalLayout_2.addWidget(self.player_combat_lb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.ai_img_lb = QtWidgets.QLabel(self.centralwidget)
        self.ai_img_lb.setGeometry(QtCore.QRect(710, 140, 220, 320))
        self.ai_img_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.ai_img_lb.setText("")
        self.ai_img_lb.setObjectName("ai_img_lb")
        self.ai_name_lb = QtWidgets.QLabel(self.centralwidget)
        self.ai_name_lb.setGeometry(QtCore.QRect(710, 80, 471, 40))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        self.ai_name_lb.setFont(font)
        self.ai_name_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.ai_name_lb.setObjectName("ai_name_lb")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(940, 140, 241, 321))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 220, 321))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ai_intel_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_intel_lb.setFont(font)
        self.ai_intel_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_intel_lb.setObjectName("ai_intel_lb")
        self.verticalLayout_4.addWidget(self.ai_intel_lb)
        self.ai_str_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_str_lb.setFont(font)
        self.ai_str_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_str_lb.setObjectName("ai_str_lb")
        self.verticalLayout_4.addWidget(self.ai_str_lb)
        self.ai_spd_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_spd_lb.setFont(font)
        self.ai_spd_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_spd_lb.setObjectName("ai_spd_lb")
        self.verticalLayout_4.addWidget(self.ai_spd_lb)
        self.ai_dura_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_dura_lb.setFont(font)
        self.ai_dura_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_dura_lb.setObjectName("ai_dura_lb")
        self.verticalLayout_4.addWidget(self.ai_dura_lb)
        self.ai_pwr_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_pwr_lb.setFont(font)
        self.ai_pwr_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_pwr_lb.setObjectName("ai_pwr_lb")
        self.verticalLayout_4.addWidget(self.ai_pwr_lb)
        self.ai_combat_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(20)
        self.ai_combat_lb.setFont(font)
        self.ai_combat_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_combat_lb.setObjectName("ai_combat_lb")
        self.verticalLayout_4.addWidget(self.ai_combat_lb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.player_hand_lb = QtWidgets.QLabel(self.centralwidget)
        self.player_hand_lb.setGeometry(QtCore.QRect(390, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.player_hand_lb.setFont(font)
        self.player_hand_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.player_hand_lb.setObjectName("player_hand_lb")
        self.ai_hand_lb = QtWidgets.QLabel(self.centralwidget)
        self.ai_hand_lb.setGeometry(QtCore.QRect(1080, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.ai_hand_lb.setFont(font)
        self.ai_hand_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ai_hand_lb.setObjectName("ai_hand_lb")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(500, 140, 201, 321))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stat_lb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(22)
        self.stat_lb.setFont(font)
        self.stat_lb.setText("")
        self.stat_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stat_lb.setObjectName("stat_lb")
        self.verticalLayout_5.addWidget(self.stat_lb)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.win_lb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        self.win_lb.setFont(font)
        self.win_lb.setText("")
        self.win_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.win_lb.setObjectName("win_lb")
        self.verticalLayout_5.addWidget(self.win_lb)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.kitty_lb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(24)
        self.kitty_lb.setFont(font)
        self.kitty_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.kitty_lb.setObjectName("kitty_lb")
        self.horizontalLayout_3.addWidget(self.kitty_lb)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.victory_lb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(30)
        self.victory_lb.setFont(font)
        self.victory_lb.setText("")
        self.victory_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.victory_lb.setObjectName("victory_lb")
        self.verticalLayout_5.addWidget(self.victory_lb)
        self.frame.raise_()
        self.player_img_lb.raise_()
        self.label_2.raise_()
        self.player_name_lb.raise_()
        self.ai_img_lb.raise_()
        self.ai_name_lb.raise_()
        self.frame_2.raise_()
        self.label_3.raise_()
        self.player_hand_lb.raise_()
        self.ai_hand_lb.raise_()
        self.win_lb.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.kitty_lb.raise_()
        self.victory_lb.raise_()
        self.stat_lb.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Player"))
        self.player_name_lb.setText(_translate("MainWindow", "Super Hero Name"))
        self.player_intel_btn.setText(_translate("MainWindow", "Intelligence"))
        self.player_str_btn.setText(_translate("MainWindow", "Strength"))
        self.player_spd_btn.setText(_translate("MainWindow", "Speed"))
        self.player_dura_btn.setText(_translate("MainWindow", "Durability"))
        self.player_pwr_btn.setText(_translate("MainWindow", "Power"))
        self.player_combat_btn.setText(_translate("MainWindow", "Combat"))
        self.player_intel_lb.setText(_translate("MainWindow", "###"))
        self.player_str_lb.setText(_translate("MainWindow", "###"))
        self.player_spd_lb.setText(_translate("MainWindow", "###"))
        self.player_dura_lb.setText(_translate("MainWindow", "###"))
        self.player_pwr_lb.setText(_translate("MainWindow", "###"))
        self.player_combat_lb.setText(_translate("MainWindow", "###"))
        self.ai_name_lb.setText(_translate("MainWindow", "Super Hero Name"))
        self.label_8.setText(_translate("MainWindow", "Intelligence"))
        self.label_7.setText(_translate("MainWindow", "Strength"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.label_5.setText(_translate("MainWindow", "Durability"))
        self.label_4.setText(_translate("MainWindow", "Power"))
        self.label.setText(_translate("MainWindow", "Combat"))
        self.ai_intel_lb.setText(_translate("MainWindow", "###"))
        self.ai_str_lb.setText(_translate("MainWindow", "###"))
        self.ai_spd_lb.setText(_translate("MainWindow", "###"))
        self.ai_dura_lb.setText(_translate("MainWindow", "###"))
        self.ai_pwr_lb.setText(_translate("MainWindow", "###"))
        self.ai_combat_lb.setText(_translate("MainWindow", "###"))
        self.label_3.setText(_translate("MainWindow", "Computer"))
        self.player_hand_lb.setText(_translate("MainWindow", "###"))
        self.ai_hand_lb.setText(_translate("MainWindow", "###"))
        self.label_9.setText(_translate("MainWindow", "Winner:"))
        self.label_10.setText(_translate("MainWindow", "Kitty:"))
        self.kitty_lb.setText(_translate("MainWindow", "###"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
