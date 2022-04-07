import howdoi
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                               QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTextEdit, QComboBox)
from PySide2.QtGui import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyside2 - HowDoI")

        self.input = QLineEdit()
        self.Question = QLabel()
        self.Question.setText("How do I:")
        self.input.setPlaceholderText("Ask me a question..")

        self.Text = QTextEdit()
        self.Text.setText("/--------------------------------/")
        self.Text.setStyleSheet(f"background-color: #D8E4E1")
        self.Text.setAlignment(Qt.AlignLeft)

        self.button = QPushButton("Search")
        self.button.resize(10, 10)
        self.button.clicked.connect(self.ButtonEvent)

        Engine = QComboBox(self)
        Engine.addItem("google")
        Engine.addItem("bing")
        Engine.addItem("duckduckgo")

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.Question)
        HLayout.addWidget(self.input)
        HLayout.addWidget(self.button)
        HLayout.addWidget(Engine)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(self.Text)

        Container = QWidget()
        Container.setLayout(VLayout)
        Container.setMinimumSize(650, 480)
        self.setCentralWidget(Container)

    def UpdateEngine(self, text):
        self.engine = " -e " + text

    def ButtonEvent(self):
        self.QuestionLabel.setText(howdoi.howdoi(self.input.text() + " -a"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
