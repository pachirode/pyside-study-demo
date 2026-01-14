import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setup_ui()
        # self.test_url()
        # self.test_interaction()
        # self.test_buddy()
        self.test_signal()

    def setup_ui(self):
        label = QtWidgets.QLabel("Test label", self)
        label.move(350, 200)
        label.setStyleSheet("background-color: rgb(2, 255, 255);")

    def test_url(self):
        label = QtWidgets.QLabel("<a href='https://github.com'>Github</a>", self)
        label.move(450, 300)
        label.setOpenExternalLinks(True)

    def test_interaction(self):
        label1 = QtWidgets.QLabel("不能和文本交互", self)
        label2 = QtWidgets.QLabel("可用鼠标选择", self)
        label3 = QtWidgets.QLabel("文本可编辑", self)

        label1.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        label2.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        label3.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)  # 添加标志也不生效，QLabel 本身并不支持编辑文本

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)

    def test_buddy(self):
        name_label = QtWidgets.QLabel("&NAME")  # ALT + N 获取焦点
        age_label = QtWidgets.QLabel("&AGE")  # ALT + A 获取焦点
        name_edit = QtWidgets.QLineEdit()
        age_spin_box = QtWidgets.QSpinBox()

        layout = QtWidgets.QFormLayout()
        layout.addRow(name_label, name_edit)
        layout.addRow(age_label, age_spin_box)
        self.setLayout(layout)

        name_label.setBuddy(name_edit)
        age_label.setBuddy(age_spin_box)

    def test_signal(self):
        label_1 = QtWidgets.QLabel()
        label_2 = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label_2)
        layout.addWidget(label_1)
        self.setLayout(layout)
        label_1.setText("<a href='https://github.com'>Github</a>")
        label_2.setText("<a href='https://github.com'>Github</a>")

        label_1.linkHovered.connect(lambda val: print(val))
        label_2.linkActivated.connect(lambda val: print(val))


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(application.exec())
