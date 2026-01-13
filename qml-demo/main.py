import os
import sys
from pathlib import Path

from PySide6.QtCore import qInstallMessageHandler, QUrl, QObject, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonType, QQmlComponent


def custom_message_handler(mode, context, message):
    if "qml" in context.category.lower() or "js" in context.category.lower():
        print(f"[QML] {message}")
    else:
        pass


class Test(QObject):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self._name = name

    @Property(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == '__main__':
    qInstallMessageHandler(custom_message_handler)

    # qmlRegisterSingletonType(QUrl.fromLocalFile("MySingleton.qml"), "MyModule", 1, 0, "MySingleton")

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))

    component = QQmlComponent(engine, QUrl.fromLocalFile("MySingleton.qml"))
    com = component.create()
    engine.rootContext().setContextProperty("mySingleton", com)

    test = Test("test")
    engine.rootContext().setContextProperty("test", test)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
