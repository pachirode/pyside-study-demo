import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setup_ui()
        self.test_group()

    def setup_ui(self) -> None:
        self.radio_man = QtWidgets.QRadioButton("男", self)
        self.radio_woman = QtWidgets.QRadioButton("女", self)

        self.radio_man.move(30, 30)
        self.radio_woman.move(30, 60)

    def test_group(self):
        gender_group = QtWidgets.QButtonGroup(self)
        gender_group.addButton(self.radio_man)
        gender_group.addButton(self.radio_woman)

        answer_group = QtWidgets.QButtonGroup(self)
        y = QtWidgets.QRadioButton("yes", self)
        n = QtWidgets.QRadioButton("no", self)
        answer_group.addButton(y)
        answer_group.addButton(n)

        y.move(60, 130)
        n.move(60, 160)


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(application.exec())
