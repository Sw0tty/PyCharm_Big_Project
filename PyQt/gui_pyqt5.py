from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication([])
app.setStyle('fusion')

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(QLabel('Hello PyQt5'))
window.setLayout(layout)



window.show()
app.exec_()
