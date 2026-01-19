import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Qt


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        self.test_spin_box()

    def test_spin_box(self):
        spin_box = QtWidgets.QSpinBox()
        spin_box.setRange(0, 1000)
        spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        spin_box.setKeyboardTracking(False)
        spin_box.setAccelerated(True)

        info_label = QtWidgets.QLabel('等待用户输入值')

        @Slot()
        def show_value():
            info_label.setText(f"用户输入的数值为{spin_box.value()}")
            info_label.adjustSize()

        spin_box.editingFinished.connect(show_value)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(spin_box)
        layout.addWidget(info_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
