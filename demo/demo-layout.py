import sys

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        # self.test_box()
        self.test_from()

    def test_box(self):
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.LeftToRight)
        layout.addWidget(QtWidgets.QPushButton("1"))
        layout.addWidget(QtWidgets.QPushButton("1"))
        layout.addWidget(QtWidgets.QPushButton("1"))
        layout.addWidget(QtWidgets.QPushButton("1"))

        self.setLayout(layout)

    def test_from(self):
        name_le = QtWidgets.QLineEdit()
        name_label = QtWidgets.QLabel("Name: ")

        age_le = QtWidgets.QComboBox()
        age_le.addItems([str(i) for i in range (0, 100)])
        age_label = QtWidgets.QLabel("Age: ")

        layout = QtWidgets.QFormLayout()
        layout.addRow(name_label, name_le)
        layout.addRow(age_label, age_le)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
