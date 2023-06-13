from PyQt6 import QtWidgets, QtCore  # Импорт всех виджетов библиотеки
import sys

# --------------------------
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QWidget()
# window.setWindowTitle("Первая программа на PyQt6")
# window.resize(600, 400)
# label = QtWidgets.QLabel("<center>Привет, PyQt6!</center>")
# quit_button = QtWidgets.QPushButton("Закрыть программу")
# vertical_box = QtWidgets.QVBoxLayout()  # QVBoxLayout - создание вертикального контейнера
# vertical_box.addWidget(label)  # добавление виджетов в контейнер
# vertical_box.addWidget(quit_button)  # добавление виджетов в контейнер
# window.setLayout(vertical_box)  # помещает контейнер в окно
# quit_button.clicked.connect(app.quit)
# window.show()  # выводит на экран окно и все компоненты, которые мы ранее в него добавили
# sys.exit(app.exec())
# --------------------------

# ------------OOP Style Window--------------
# print(QtWidgets.QWidget.__bases__)


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, PyQt6!")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.quit_button = QtWidgets.QPushButton("&Закрыть окно")
        self.vertical_box = QtWidgets.QVBoxLayout()
        self.vertical_box.addWidget(self.label)
        self.vertical_box.addWidget(self.quit_button)
        self.setLayout(self.vertical_box)
        self.quit_button.clicked.connect(QtWidgets.QApplication.instance().quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("OOP Style Window")
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
# --------------------------








