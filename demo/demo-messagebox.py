import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        # self.test()
        # self.test_set_text()
        # self.test_btn()
        self.test_static()

    def test(self):
        message_box = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Warning,
            "这是一个消息提示框",
            "这是一个模态对话框",
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel,
            self,
        )

        btn = QtWidgets.QPushButton("对话框", self)
        btn.move(200, 200)
        btn.clicked.connect(message_box.open)

    def test_set_text(self):
        message_box = QtWidgets.QMessageBox(self)

        message_box.setText("一般文本")
        message_box.setDetailedText("详细文本")
        message_box.setInformativeText("信息文本")

        btn = QtWidgets.QPushButton("对话框", self)
        btn.move(200, 200)
        btn.clicked.connect(message_box.open)

    def test_btn(self):
        message_box = QtWidgets.QMessageBox(self)

        btn = QtWidgets.QPushButton("对话框", self)
        btn.move(200, 200)
        btn.clicked.connect(message_box.open)

        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
        message_box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.setEscapeButton(message_box.button(QtWidgets.QMessageBox.StandardButton.Cancel))

        # 添加自定义按钮，完全自定义，仅有文本 + 角色
        message_box.addButton("自定义按钮", QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        # 添加的为标准按钮，带有平台一致行为
        message_box.addButton(QtWidgets.QMessageBox.StandardButton.Discard)

        message_box.buttonClicked.connect(lambda btn: print(btn.text()))

    def test_static(self):
        about_btn = QtWidgets.QPushButton("关于程序")
        info_btn = QtWidgets.QPushButton("展示信息")
        warn_btn = QtWidgets.QPushButton("展示警告")
        label = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(about_btn)
        layout.addWidget(info_btn)
        layout.addWidget(warn_btn)
        layout.addWidget(label)
        self.setLayout(layout)

        about_btn.clicked.connect(lambda: QtWidgets.QMessageBox.about(self, "关于程序", "关于程序"))

        @Slot()
        def show_info_dlg():
            res = QtWidgets.QMessageBox.information(
                self,
                "静态方法",
                "info",
                QtWidgets.QMessageBox.StandardButton.Ok,
                QtWidgets.QMessageBox.StandardButton.Cancel,
            )
            label.setText(str(res))
            label.adjustSize()

        info_btn.clicked.connect(show_info_dlg)

        @Slot()
        def show_warn_dlg():
            res = QtWidgets.QMessageBox.warning(
                self,
                "静态方法",
                "warn",
                QtWidgets.QMessageBox.StandardButton.Discard,
            )
            label.setText(str(res))
            label.adjustSize()

        warn_btn.clicked.connect(show_warn_dlg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
