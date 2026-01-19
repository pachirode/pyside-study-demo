import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        self.test_slider()

    def test_slider(self):
        slider = QtWidgets.QSlider(self)
        slider.move(200, 200)
        slider.setMaximum(200)
        slider.setMinimum(20)
        slider.setSingleStep(10)

        dial = QtWidgets.QDial(self)
        dial.move(360, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(240, 200)

        slider_label = QtWidgets.QLabel(self)
        slider_label.move(100, 200)

        @Slot(int)
        def test_dial(value: int):
            info_label.setText(f"滑块值变为{value}")
            info_label.adjustSize()

        dial.valueChanged.connect(test_dial)

        @Slot(int)
        def test_slider(value: int):
            slider_label.setText(f"滑块值{value}")
            slider_label.adjustSize()
        slider.valueChanged.connect(test_slider)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
