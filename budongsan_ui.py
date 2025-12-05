# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'budongsan.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(560, 661)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 551, 63))
        font = QFont()
        font.setFamilies([u"NanumGothic"])
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(15)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(4, 160, 61, 31))
        font1 = QFont()
        font1.setFamilies([u"NanumGothic"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setMargin(5)
        self.keyword = QLineEdit(Form)
        self.keyword.setObjectName(u"keyword")
        self.keyword.setGeometry(QRect(70, 160, 451, 31))
        font2 = QFont()
        font2.setFamilies([u"NanumGothic"])
        self.keyword.setFont(font2)
        self.keyword_btn = QPushButton(Form)
        self.keyword_btn.setObjectName(u"keyword_btn")
        self.keyword_btn.setGeometry(QRect(10, 590, 131, 41))
        font3 = QFont()
        font3.setFamilies([u"NanumGothic"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.keyword_btn.setFont(font3)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 280, 511, 301))
        self.textBrowser.setFont(font2)
        self.textBrowser.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 8px;")
        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(150, 590, 101, 41))
        font4 = QFont()
        font4.setFamilies([u"NanumGothic"])
        font4.setBold(True)
        self.start_btn.setFont(font4)
        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(320, 590, 101, 41))
        self.reset_btn.setFont(font4)
        self.quit_btn = QPushButton(Form)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setGeometry(QRect(430, 590, 91, 41))
        self.quit_btn.setFont(font4)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 181, 31))
        font5 = QFont()
        font5.setFamilies([u"NanumGothic"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_4.setFont(font5)
        self.label_4.setMargin(5)
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 200, 521, 41))
        self.label_17.setFont(font3)
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 230, 521, 41))
        self.label_18.setFont(font3)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 120, 71, 31))
        self.label_5.setFont(font1)
        self.expire_date = QLabel(Form)
        self.expire_date.setObjectName(u"expire_date")
        self.expire_date.setGeometry(QRect(80, 120, 441, 31))
        self.expire_date.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\uc0bc\uc0bc\uc5e0\ud22c \ub9e4\ubb3c \uc815\ubcf4\uc218\uc9d1 \ud504\ub85c\uadf8\ub7a8", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\uc0bc\uc0bc\uc5e0\ud22c \ub9e4\ubb3c\uc815\ubcf4 \ud06c\ub864\ub9c1 \ud504\ub85c\uadf8\ub7a8</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ud0a4\uc6cc\ub4dc", None))
        self.keyword.setPlaceholderText(QCoreApplication.translate("Form", u"\uc9c0\uc5ed \ud0a4\uc6cc\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694. (\uc608 : \uc0ac\ub2f9,\uac15\ub0a8)", None))
        self.keyword_btn.setText(QCoreApplication.translate("Form", u"\ud83d\udcca\ud0a4\uc6cc\ub4dc \uc124\uc815\ud558\uae30", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("Form", u"\uc5ec\uae30\uc5d0\uc11c \uc9c4\ud589\ud604\ud669\uc744 \ubcf4\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4 :-)", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\ud83d\udd0d \ucd94\ucd9c\uc2dc\uc791", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\ud83d\ude80 \ucd08\uae30\ud654", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"\u274c \uc885\ub8cc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc81c\uc791 : \ud06c\ubabd - \uc798\ub178\ub294\uccab\ub208\u2744\ufe0f", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u26a0\ufe0f \ud0a4\uc6cc\ub4dc\ub97c \ud55c\uac1c\ub9cc \ub123\uc73c\uc154\ub3c4 \ub418\uace0, \ucf64\ub9c8(,)\ub85c \ub744\uc5b4\uc4f0\uae30 \uc5c6\uc774 \uc5f0\uacb0\ud558\uc5ec \uc4f0\uc154\ub3c4 \ub429\ub2c8\ub2e4! \u26a0\ufe0f", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u26a0\ufe0f \ud0a4\uc6cc\ub4dc\uac00 \uc5ec\ub7ec\uac1c\uc778 \uacbd\uc6b0, \ud55c \ud0a4\uc6cc\ub4dc\uc758 \uc791\uc5c5\uc774 \ub05d\ub09c \ud6c4 \ub2e4\ub978 \ud0a4\uc6cc\ub4dc\uc5d0 \ub300\ud574 \uc9c4\ud589\ub429\ub2c8\ub2e4!\u26a0\ufe0f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\ub9cc\ub8cc \ub0a0\uc9dc", None))
        self.expire_date.setText("")
    # retranslateUi

