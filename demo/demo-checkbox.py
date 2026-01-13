import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setup_ui()
        self.test_check_state()
        self.test_signal()

    def setup_ui(self):
        cb_1 = QtWidgets.QCheckBox("1", self)
        cb_2 = QtWidgets.QCheckBox("2", self)
        cb_3 = QtWidgets.QCheckBox("3", self)

        cb_1.move(200, 220)
        cb_2.move(200, 240)
        cb_3.move(200, 260)

    def test_check_state(self):
        cb = QtWidgets.QCheckBox("state", self)
        cb.setTristate(True)
        cb.setCheckState(Qt.CheckState.Checked)
        cb.clicked.connect(lambda: print(cb.isChecked()))

    def test_signal(self):
        @Slot(int)
        def test_slot(state: int):
            if state == Qt.CheckState.Checked.value:
                print("checked")
            elif state == Qt.CheckState.Unchecked.value:
                print("unchecked")
            elif state == Qt.CheckState.PartiallyChecked.value:
                print("partially checked")

        cb = QtWidgets.QCheckBox("signal", self)
        cb.setTristate(True)
        cb.setCheckState(Qt.CheckState.Checked)
        cb.stateChanged.connect(test_slot)
        cb.move(100, 200)


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(application.exec())
