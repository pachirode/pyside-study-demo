import sys

from PySide6 import QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setup_ui()
        self.test_flat()
        self.test_menu()
        self.test_default()

    def setup_ui(self):
        btn = QtWidgets.QPushButton()
        btn.setParent(self)
        btn.setText("set 指定父对象")
        btn.move(20, 20)

    def test_flat(self):
        btn = QtWidgets.QPushButton("扁平化", self)
        btn.setFlat(True)
        btn.move(40, 40)

    def test_menu(self):
        btn = QtWidgets.QPushButton("菜单", self)
        btn.move(60, 60)

        menu = QtWidgets.QMenu(self)
        new_action = QtGui.QAction("新建", self)
        new_action.triggered.connect(lambda: print("新建文件"))
        exit_action = QtGui.QAction("关闭", self)
        exit_action.triggered.connect(lambda: exit())

        open_url_menu = QtWidgets.QMenu("打开网页")
        url_1 = QtGui.QAction("百度", open_url_menu)
        url_1.triggered.connect(lambda: QtGui.QDesktopServices.openUrl("www.baidu.com"))
        open_url_menu.addAction(url_1)

        menu.addAction(new_action)
        menu.addAction(exit_action)
        menu.addSeparator()
        menu.addMenu(open_url_menu)

        btn.setMenu(menu)
        btn_show = QtWidgets.QPushButton("展开菜单", self)
        btn_show.move(60, 80)
        btn_show.clicked.connect(btn.showMenu)

    def test_default(self):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setText("测试默认按钮")
        cancel_btn = msg_box.addButton(QtWidgets.QMessageBox.StandardButton.Cancel)
        ok_btn = msg_box.addButton(QtWidgets.QMessageBox.StandardButton.Ok)

        msg_box.buttonClicked.connect(lambda btn: print(btn.text()))

        btn = QtWidgets.QPushButton("展示对话框", self)
        btn.move(120, 140)
        btn.clicked.connect(msg_box.open)

        # ok_btn.setDefault(True)
        cancel_btn.setDefault(True)
        print(ok_btn.isDefault())
        print(cancel_btn.isDefault())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
