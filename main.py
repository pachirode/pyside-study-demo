import os
import sys
from pathlib import Path

from PySide6.QtCore import qInstallMessageHandler
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

def custom_message_handler(mode, context, message):
    if "qml" in context.category.lower() or "js" in context.category.lower():
        print(f"[QML] {message}")
    else:
        pass

if __name__ == '__main__':
    qInstallMessageHandler(custom_message_handler)

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "layout.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
