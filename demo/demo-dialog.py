import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QDir


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        # self.test()
        # self.test_modal()
        self.test_file_open()
        # self.test_file_save()

    def test(self):
        dialog = QtWidgets.QDialog(self)
        dialog.resize(400, 300)
        QtWidgets.QLabel("模态对话框仍然存在并在运行，主窗口的关闭事件通常无法正常完成", dialog)

        btn = QtWidgets.QPushButton("弹出对话框", self)
        btn.move(200, 200)
        btn.clicked.connect(lambda: dialog.exec())

    def test_modal(self):
        line_edit = QtWidgets.QLineEdit(self)
        line_edit.move(200, 200)
        line_edit.setPlaceholderText("测试交互状态")

        dialog = QtWidgets.QMessageBox(self)
        dialog.setWindowTitle("模态/非模态")
        dialog.setText("模态窗口将阻塞")
        dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)

        btn_modal = QtWidgets.QPushButton("打开模态窗口")
        btn_modal.clicked.connect(lambda: dialog.exec())

        btn = QtWidgets.QPushButton("打开非模态窗口")

        def show():
            dialog.setModal(False)
            dialog.show()

        btn.clicked.connect(show)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(btn_modal)
        layout.addWidget(btn)

        self.setLayout(layout)

    def test_file_open(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)  # 设置模式，打开或者保存两种
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)  # 只能选择单个现有文件
        dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)
        dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Accept, "选择")
        dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Reject, "取消")

        # 设置过滤
        dialog.setFilter(QDir.Filter.NoDotAndDotDot)
        dialog.setNameFilters(
            ("Python (*.py)", "Init (*.ini)")
        )

        btn = QtWidgets.QPushButton("选择文件", self)
        btn.move(150, 200)
        btn.clicked.connect(lambda: dialog.exec())

        info_le = QtWidgets.QLineEdit(self)
        info_le.move(150, 250)
        info_le.setMinimumWidth(600)
        dialog.fileSelected.connect(lambda path: info_le.setText(path))

    def test_file_save(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)  # 设置模式，打开或者保存两种
        dialog.setDefaultSuffix("txt")
        dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Accept, "保存")
        dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Reject, "取消")

        info_le = QtWidgets.QLineEdit(self)
        info_le.setMinimumWidth(600)
        btn = QtWidgets.QPushButton("保存文件", self)
        info_label = QtWidgets.QLabel(self)

        btn.clicked.connect(lambda: dialog.exec())
        dialog.fileSelected.connect(lambda path: info_le.setText(path))
        dialog.currentChanged.connect(lambda: info_label.setText(dialog.directory().path()))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(info_le)
        layout.addWidget(btn)
        layout.addWidget(info_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
