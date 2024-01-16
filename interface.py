import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox

import sqlite3
from world_lvl_one import run


class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True


class Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Найди схожий")
        self.setGeometry(500, 80, 900, 900)

        self.start = QPixmap("1.jpeg")
        self.image = QLabel(self)
        self.image.move(-111, -120)
        self.image.resize(1200, 1200)
        self.image.setPixmap(self.start)

        self.start = QPixmap("picture.png")
        self.image = QLabel(self)
        self.image.move(200, 600)
        self.image.resize(886, 320)
        self.image.setPixmap(self.start)

        self.registration = QPushButton('Регистрация', self)
        self.registration.move(50, 150)
        self.registration.resize(150, 60)
        self.registration.setFont(QFont('Times', 12))

        self.enter = QPushButton('Войти', self)
        self.enter.move(50, 50)
        self.enter.resize(150, 60)
        self.enter.setFont(QFont('Times', 12))

        self.ui_components()  # функция для текста крутящегося
        self.show()

        self.loginDatabase = LoginDatabase('login.db')
        if self.loginDatabase.is_table('USERS'):
            pass
        else:
            self.loginDatabase.conn.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT, REITING TEXT)")
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?, ?)",
                                            ('admin', 'admin', "100"))
            self.loginDatabase.conn.commit()
        self.enter.clicked.connect(self.enter_open_window)
        self.registration.clicked.connect(self.registration_open_window)

    def enter_open_window(self):
        self.close()

        self.enter_example_window = Enter()
        self.enter_example_window.show()

    def registration_open_window(self):
        self.registration_open_window = Registration()
        self.registration_open_window.show()

    def ui_components(self):
        with open('start_text.txt', 'r', encoding='utf-8') as file:
            text = str(file.read())

        label = ScrollLabel(self)
        label.setText(text)
        label.setFont(QFont('Times', 14))
        label.setGeometry(380, 50, 500, 540)


class ScrollLabel(QScrollArea):

    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)

        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)

    def text(self):
        get_text = self.label.text()
        return get_text


class Enter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вход")
        self.setGeometry(600, 450, 700, 300)

        self.text_login = QLabel(self)
        self.text_login.setText("Логин:")
        self.text_login.move(170, 20)
        self.text_login.setFont(QFont('Times', 12))

        self.login = QLineEdit(self)
        self.login.setFont(QFont('Times', 14))
        self.login.move(170, 60)
        self.login.resize(300, 50)

        self.text_password = QLabel(self)
        self.text_password.setText("Пароль:")
        self.text_password.move(170, 120)
        self.text_password.setFont(QFont('Times', 12))

        self.password = QLineEdit(self)
        self.password.setFont(QFont('Times', 14))
        self.password.move(170, 150)
        self.password.resize(300, 50)
        self.password.setEchoMode(QLineEdit.Password)

        self.input = QPushButton('Войти', self)
        self.input.move(170, 210)
        self.input.resize(150, 50)
        self.input.setFont(QFont('Times', 12))
        self.input.clicked.connect(self.loginCheck)

        self.loginDatabase = LoginDatabase('login.db')

    def loginCheck(self):
        username = self.login.text()
        password = self.password.text()
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return msg

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                                                 (username, password))
        if len(result.fetchall()):
            self.close()  # закрываем "своё" окно класса

            self.open_main_window = Main()
            self.open_main_window.show()

            self.loginDatabase.conn.close()
        else:
            msg = QMessageBox.information(self, 'Внимание!', 'Неправильное имя пользователя или пароль.')
            return msg


class Registration(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")
        self.setGeometry(600, 450, 600, 450)

        self.text_name = QLabel(self)
        self.text_name.setText("Имя:")
        self.text_name.move(250, 20)
        self.text_name.setFont(QFont("Times", 12))

        self.name = QLineEdit(self)
        self.name.setFont(QFont('Times', 14))
        self.name.move(130, 50)
        self.name.resize(300, 40)

        self.text_new_login = QLabel(self)
        self.text_new_login.setText("Логин:")
        self.text_new_login.move(250, 95)
        self.text_new_login.setFont(QFont("Times", 12))

        self.new_login = QLineEdit(self)
        self.new_login.setFont(QFont('Times', 14))
        self.new_login.move(130, 130)
        self.new_login.resize(300, 40)

        self.text_new_password = QLabel(self)
        self.text_new_password.setText("Пароль:")
        self.text_new_password.move(250, 175)
        self.text_new_password.setFont(QFont("Times", 12))

        self.new_password1 = QLineEdit(self)
        self.new_password1.setFont(QFont('Times', 14))
        self.new_password1.move(130, 210)
        self.new_password1.resize(300, 40)
        self.new_password1.setEchoMode(QLineEdit.Password)

        self.text_new_password = QLabel(self)
        self.text_new_password.setText("Повторите Пароль:")
        self.text_new_password.move(200, 260)
        self.text_new_password.setFont(QFont("Times", 12))

        self.new_password2 = QLineEdit(self)
        self.new_password2.setFont(QFont('Times', 14))
        self.new_password2.move(130, 300)
        self.new_password2.resize(300, 40)
        self.new_password2.setEchoMode(QLineEdit.Password)

        self.add_new_user = QPushButton('Зарегистрироваться', self)
        self.add_new_user.move(130, 370)
        self.add_new_user.resize(300, 50)
        self.add_new_user.setFont(QFont('Times', 14))
        self.add_new_user.clicked.connect(self.insertData)

        self.loginDatabase = LoginDatabase('login.db')

    def insertData(self):
        username = self.new_login.text()
        password1 = self.new_password1.text()
        password2 = self.new_password2.text()

        if (not username) or (not password1):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return msg

        elif password2 != password1:
            msg = QMessageBox.information(self, 'Внимание!', 'Пароли не одинаковы')
            return msg

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ?", (username,))

        if result.fetchall():
            msg = QMessageBox.information(self, 'Внимание!', 'Пользоватеть с таким именем уже зарегистрирован.')
            return msg

        else:
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?, ?)",
                                            (username, password1, "0"))
            self.loginDatabase.conn.commit()
            self.close()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Основное меню")
        self.setGeometry(500, 80, 900, 900)

        self.start = QPixmap("1.jpeg")
        self.image = QLabel(self)
        self.image.move(-111, -120)
        self.image.resize(1200, 1200)
        self.image.setPixmap(self.start)

        self.start = QPixmap("cat.png")
        self.image = QLabel(self)
        self.image.move(10, 600)
        self.image.resize(300, 300)
        self.image.setPixmap(self.start)

        self.shop = QPushButton("Shop", self)
        self.shop.move(10, 10)
        self.shop.resize(70, 50)
        self.shop.setFont(QFont('Times', 14))
        self.shop.clicked.connect(self.shopping)

        self.example = QPushButton('Rules', self)
        self.example.move(100, 10)
        self.example.resize(140, 50)
        self.example.setFont(QFont('Times', 16))
        self.example.clicked.connect(self.rules_game)

        self.play = QPushButton("Reiting", self)
        self.play.move(270, 10)
        self.play.resize(140, 50)
        self.play.setFont(QFont('Times', 16))
        self.play.clicked.connect(self.reiting)

        self.play = QPushButton("Play>>>>", self)
        self.play.move(700, 350)
        self.play.resize(170, 170)
        self.play.setFont(QFont('Times', 18))
        self.play.clicked.connect(self.playing)

    def reiting(self):
        pass

    def rules_game(self):
        with open('rules_game.txt', 'r', encoding='utf-8') as file:
            text = str(file.read())

        label = ScrollLabel(self)
        label.setText(text)
        label.setFont(QFont('Times', 14))
        label.setGeometry(380, 50, 500, 540)

    def shopping(self):
        pass

    def playing(self):
        self.close()
        run()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    st = Start()
    st.show()
    sys.exit(app.exec())
