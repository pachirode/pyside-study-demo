import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QTextOption, QTextCharFormat, QColor
from PySide6.QtCore import Slot, Qt, QRect


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        # self.setup_ui()
        # self.test_char_format()
        self.test_line_format()

    def setup_ui(self):
        pte = QtWidgets.QPlainTextEdit(self)
        pte.resize(300, 400)
        pte.move(100, 100)

        pte.setPlainText("Test\n" * 100)

        pte.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)  # 自动换行
        pte.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)  # 尽可能当前间换行
        pte.setReadOnly(True)
        pte.setMaximumBlockCount(10)  # 限制最大块数量

    def test_char_format(self):
        pte = QtWidgets.QPlainTextEdit(self)
        pte.resize(300, 400)
        pte.move(100, 100)

        pte.setPlainText("Test\n" * 100)

        char_format = QTextCharFormat()
        char_format.setFontUnderline(True)
        char_format.setUnderlineColor(QColor(0, 128, 128))
        char_format.setFontItalic(True)

        @Slot()
        def test_set_char_format():
            pte.setCurrentCharFormat(char_format)
            pte.setFocus()

        btn = QtWidgets.QPushButton("设置字体", self)
        btn.clicked.connect(test_set_char_format)

    def test_line_format(self):
        pte = QtWidgets.QPlainTextEdit(self)
        pte.resize(350, 400)
        pte.move(150, 80)

        pte.setPlainText("Test\n" * 100)
        pte.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        line_num_widget = QtWidgets.QWidget(self)
        line_num_widget.resize(30, 400)
        line_num_widget.move(120, 80)

        line_num_label = QtWidgets.QLabel(line_num_widget)
        line_num_label.move(0, 5)
        line_nums = "\n".join([str(i) for i in range(1, 101)])
        line_num_label.setText(line_nums)

        @Slot(QRect, int)
        def scroll_line_num(_, dy: int):
            line_num_label.move(line_num_label.x(), line_num_label.y() + dy)

        pte.updateRequest.connect(scroll_line_num)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
