from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 300)
main_win.setWindowTitle('Memory Card')
button = QPushButton('Ответить')
question = QLabel()
#форма с вопросом
RadioGroupBox = QGroupBox()
rbtn1 = QRadioButton()
rbtn2 = QRadioButton()
rbtn3 = QRadioButton()
rbtn4 = QRadioButton()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
#слои главного окна
mainlayout_v1 = QHBoxLayout()
mainlayout_v2 = QHBoxLayout()
mainlayout_v3 = QHBoxLayout()
main_layout = QVBoxLayout()

mainlayout_v1.addWidget(question, alignment = Qt.AlignCenter)
mainlayout_v2.addWidget(RadioGroupBox)
mainlayout_v3.addWidget(button, alignment = Qt.AlignCenter)
#форма с ответами
ResultsGroupBox = QGroupBox('Результаты теста')
#text = QLabel('Самый сложный вопрос в мире!')
res_text = QLabel('Правильно/Неправильно')
results = QLabel('Ответ')
layout_text1 = QHBoxLayout()
layout_text2 = QVBoxLayout()
layout_text3 = QVBoxLayout()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

ask_list = [rbtn1, rbtn2, rbtn3, rbtn4]

layout_text2.addWidget(res_text, alignment = Qt.AlignCenter)
layout_text3.addWidget(results, alignment = Qt.AlignCenter)
layout_text1.addLayout(layout_text2)
layout_text1.addLayout(layout_text3)
ResultsGroupBox.setLayout(layout_text1)
ResultsGroupBox.hide()

#mainlayout_v1.addWidget(text, alignment = Qt.AlignCenter)
mainlayout_v2.addWidget(ResultsGroupBox)

main_layout.addLayout(mainlayout_v1)
main_layout.addLayout(mainlayout_v2)
main_layout.addLayout(mainlayout_v3)
main_win.setLayout(main_layout)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

def show_result():
    RadioGroupBox.hide()
    ResultsGroupBox.show()
    button.setText('Следующий вопрос')

def next_question():
    main_win.cur_q += 1
    if main_win.cur_q == len(qlist):
        main_win.cur_q = 0
    ask(qlist[main_win.cur_q])
    ResultsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(ask_list)
    question.setText(q.question)
    ask_list[0].setText(q.right_answer)
    ask_list[1].setText(q.wrong1)
    ask_list[2].setText(q.wrong2)
    ask_list[3].setText(q.wrong3)
    RadioGroupBox.show()

qlist = []
qlist.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
qlist.append(Question('Какой язык програмирования мы изучаем?', 'Python', 'C++', 'Java', 'PHP'))
qlist.append(Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты'))
qlist.append(Question('Выберите столицу России', 'Москва', 'Санкт-Петербург', 'Германия', 'Путин'))

def check_answer():
    if ask_list[0].isChecked():
        show_correct('Правильно')
        results.setText(qlist[main_win.cur_q].right_answer)
        main_win.score += 1
    else:
        show_correct('Неправильно')
        results.setText(qlist[main_win.cur_q].right_answer)
    button.setText('Следующий вопрос')

def show_correct(res):
    res_text.setText(res)
    RadioGroupBox.hide()
    ResultsGroupBox.show()

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
        main_win.amount_q = main_win.amount_q + 1
        print('Статистика\n-Всего вопросов:', main_win.amount_q, '\n-Правильных ответов:', main_win.score,'\nРейтинг:', main_win.score/main_win.amount_q*100)
        cur_q = randint(0, len(qlist))
    else:
        next_question()

main_win.cur_q = 0
main_win.score = 0
main_win.amount_q = 0
next_question()
button.clicked.connect(click_ok)
main_win.show()
app.exec_()