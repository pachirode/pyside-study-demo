import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Qt


class Window(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()
        self.test_policy()

    def setup_ui(self):
        label = QtWidgets.QLabel("Test\n" * 100)
        self.setWidget(label)

    def test_policy(self):
        plain = QtWidgets.QPlainTextEdit(self)
        plain.resize(800, 600)

        btn = QtWidgets.QPushButton("增加文本", self)
        btn.move(500, 80)

        @Slot()
        def append_text():
            plain.appendPlainText("Test\n")

        btn.clicked.connect(append_text)

        plain.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    def test_corners(self):
        label = QtWidgets.QLabel("角落控件")
        label.setScaledContents(True)
        self.setCornerWidget(label)
        print(self.cornerWidget())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
