import sys

from PySide6 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        frame = QtWidgets.QFrame(self)
        frame.setStyleSheet("background-color: rgb(0, 255, 255);")
        frame.move(10, 10)
        frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame.setLineWidth(10)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())