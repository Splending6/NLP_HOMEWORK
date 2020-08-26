from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
from nlp import Ui_Form
from utils.langconv import *
from set_custom import Ui_widget
from playsound import playsound
from test import speech_recognition
from corrector import Corrector
c = Corrector()
c.set_custom_confusion_dict('./my_custom.txt')

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        pix = QPixmap('index.jpg').scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(pix)
        self.pushButton_1.clicked.connect(self.error_detection)
        self.pushButton_2.clicked.connect(self.error_correction)
        self.pushButton_3.clicked.connect(self.set_custom)
        self.pushButton_4.clicked.connect(self.add_speech)
        self.pushButton_5.clicked.connect(self.simplified2traditional)
        self.pushButton_6.clicked.connect(self.play)

    def error_detection(self):
        error_sentences = self.textEdit.toPlainText()
        corrected_sent, err = Corrector.correct(c, error_sentences)
        text = ''
        last = 0
        for i in err:
            text = text + "<font color='black'>" + error_sentences[last:i[2]]
            text = text + "<font color='red'>" + error_sentences[i[2]:i[3]]
            last = i[3]
        text = text + "<font color='black'>" + error_sentences[last:]
        self.textBrowser.setText(text)

    def error_correction(self):
        error_sentences = self.textEdit.toPlainText()
        corrected_sent, err = Corrector.correct(c, error_sentences)
        text = ''
        last = 0
        for i in err:
            text = text + "<font color='black'>" + error_sentences[last:i[3]]
            text = text  + "<font color='red'>"+ '(' + corrected_sent[i[2]:i[3]]+')'
            last = i[3]
        text = text + "<font color='black'>" + error_sentences[last:]
        self.textBrowser.setText(text)

    def set_custom(self):
        self.cus = Set_Custom()
        self.cus.show()

    def add_speech(self):
        f = '1.wav'
        r = speech_recognition(f)
        self.textEdit.setText(r)

    def play(self):
        playsound('1.wav')

    def simplified2traditional(self, flag):
        line = self.textEdit.toPlainText()
        line2 = self.SimplifiedToTraditional(line)
        if line == line2: #说明是繁体
            line2 = self.TraditionalToSimplified(line)
            self.textBrowser.setText(line2)
        else: #说明是简体
            self.textBrowser.setText(line2)

    def TraditionalToSimplified(self, line):  # 繁体转简体
        line = Converter("zh-hans").convert(line)
        return line

    def SimplifiedToTraditional(self, line):  # 简体转繁体
        line = Converter("zh-hant").convert(line)
        return line


class Set_Custom(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        file = './my_custom.txt'
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            data = data.split('\n')
        data2 = []
        for i in data:
            i.split(' ')
            data2.append([i.split(' ')[0], i.split(' ')[1]])
        data2 = np.array(data2)
        row = data2.shape[0]
        col = data2.shape[1]
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        for i in range(row):
            for j in range(col):
                newitem = QTableWidgetItem(data2[i][j])
                self.tableWidget.setItem(i, j, newitem)

