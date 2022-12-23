from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('сколько путей всего в игре undertale', '3', '2', 'какие ещё пути?', '5'))
question_list.append(Question('сколько людей упало в подземелье?', '8', '7', '13', '2'))
question_list.append(Question('как зовут правителя подземелья', 'Азгор', 'Ториэль', 'Джерри', 'там нет правителя'))
question_list.append(Question('какого пола наш перонаж', 'неизвестно', 'мужского', 'он монстор', 'женского'))
question_list.append(Question('какая еда лечит больше всего', 'ириского-коричный пирог', 'доброженое', 'жареный снег', 'стейк'))
question_list.append(Question('то там являеться главой королевской стражи', 'Андайн', 'Альфис', 'Папирус', 'Санс'))
question_list.append(Question('кто такой Флауи?', 'цветок', 'человек', 'монстор', 'такого персонажа нет'))
question_list.append(Question('сколько детей было у Ториэль и Азгора', '1родной и 1не родной', '2родных', '0', '2не родных'))
question_list.append(Question('первого человека в подземелье звали', 'чара', 'фриск', 'вова', 'миша'))
question_list.append(Question('кто встречает нас в сноудине?', 'Санс', 'Папирус', 'Андайн', 'Флауи'))
question_list.append(Question('кто такой Меттатон', 'робот', 'монстр', 'человек', 'собака'))
question_list.append(Question('самый нелюбимый монстр в игре', 'джерри', 'ледошляп', 'фрогит', 'темми'))
question_list.append(Question('как зовут создателя игры', 'Тобби фокс', 'Вилиям афтом', 'Лев голиков', 'Киррил Золотов'))
question_list.append(Question('самый загадочный персонаж в игре', 'В.Д.Гастер', 'Санс', 'Альфис', 'Флауи'))
question_list.append(Question('год создания игры', '2015', '2009', '2000', '2020'))
#15-20 ВОПРОСОВ!
app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест по игре undertale') #название

btn_OK = QPushButton('Ответить')
question = QLabel('Вопрос?')
RadioGroupBox = QGroupBox('Варианты ответов:')

rbtn_1 = QRadioButton('1111')
rbtn_2 = QRadioButton('2222')
rbtn_3 = QRadioButton('3333')
rbtn_4 = QRadioButton('4444')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)
RadioGroupBox.setLayout(layout_1)

#панель результата
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('правельно/не правельно')
lb_Correct = QLabel('ответ будет тут')

layot_res = QVBoxLayout()
layot_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layot_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layot_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total,  '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total,  '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()

# добавить все лэйауты на главную линию
window.setLayout(layout_card)
window.total = 0
window.score = 0
btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()