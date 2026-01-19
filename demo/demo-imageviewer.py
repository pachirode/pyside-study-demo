import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication, QImage, QPalette, QKeySequence, QImageReader, QColorSpace, QPixmap, QImageWriter
from PySide6.QtCore import QDir, QStandardPaths, QMimeData, QFileInfo, QSettings, QCoreApplication
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication, QSizePolicy, QScrollArea, QScrollBar, QMessageBox, QFileDialog, QDialog

app_dir = Path(QCoreApplication.applicationDirPath())
config_path = app_dir / "config.ini"

settings = QSettings(
    str(config_path),
    QSettings.Format.IniFormat,
)


class ImageViewer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ImageViewer')
        # 按主屏幕百分比设置，如果多显示器环境，也只取主屏幕
        self.resize(QGuiApplication.primaryScreen().availableSize() * 3 / 5)
        # 当前选中屏幕
        # screen = self.windowHandle().screen()
        # self.resize(screen.availableSize() * 3 / 5)

        self.image = QImage()
        self.scale_factor = 1.0
        self.image_label = QLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.image_label.setScaledContents(True)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setBackgroundRole(QPalette.ColorRole.Dark)
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setVisible(False)

        self.setCentralWidget(self.scroll_area)

        self.create_actions()

    def create_actions(self):
        file_menu = self.menuBar().addMenu('&File')
        open_act = file_menu.addAction('&Open...', self.open)
        save_as_act = file_menu.addAction("&Save As...", self.save_as)
        file_menu.addSeparator()
        exit_act = file_menu.addAction('&Exit', self.close)
        exit_act.setShortcut("Ctrl+Q")

        edit_menu = self.menuBar().addMenu('&Edit')
        copy_act = edit_menu.addAction("&Copy", self.copy)
        copy_act.setShortcut(QKeySequence.StandardKey.Copy)
        paste = edit_menu.addAction("&Paste", self.paste)
        paste.setShortcut(QKeySequence.StandardKey.Paste)
        edit_menu.addSeparator()

        view_menu = self.menuBar().addMenu('&View')
        zoom_in_act = view_menu.addAction("Zoom &In", self.zoom_in)
        zoom_in_act.setShortcut(QKeySequence.StandardKey.ZoomIn)
        zoom_out_act = view_menu.addAction("Zoom &Out", self.zoom_out)
        zoom_out_act.setShortcut(QKeySequence.StandardKey.ZoomOut)
        normal_act = view_menu.addAction("&Normal", self.normal)
        normal_act.setShortcut("Ctrl+Shift+N")
        view_menu.addSeparator()
        fit_act = view_menu.addAction("&Fit to window", self.fit_to_window)
        fit_act.setShortcut("Ctrl+Shift+F")

    def scale_image(self, factor):
        self.scale_factor *= factor
        self.image_label.resize(self.scale_factor * self.image_label.pixmap().size())
        self.adjust_scroll_bar(self.scroll_area.horizontalScrollBar(), factor)
        self.adjust_scroll_bar(self.scroll_area.verticalScrollBar(), factor)

    def adjust_scroll_bar(self, scroll_bar: QScrollBar, factor):
        scroll_bar.setValue(int(factor * scroll_bar.value() + ((factor - 1) * scroll_bar.pageStep() / 2)))

    def load_file(self, file_name):
        reader = QImageReader(file_name)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot load {QDir.toNativeSeparators(file_name)}: {reader.errorString()}",
            )
            return False

        self.set_image(new_image)
        self.setWindowFilePath(file_name)

        message = (
            f"Opened '{QDir.toNativeSeparators(file_name)}'"
            f"{self.image.width()}x{self.image.height()}, Depth: {self.image.depth()}"
        )
        self.statusBar().showMessage(message)
        return True

    def set_image(self, new_image):
        self.image = new_image
        if self.image.colorSpace().isValid():
            self.image.convertedToColorSpace(QColorSpace.ColorModel.Rgb)
        self.image_label.setPixmap(QPixmap.fromImage(self.image))
        self.scale_factor = 1.0
        self.scroll_area.setVisible(True)
        self.image_label.adjustSize()

    def save_file(self, file_name):
        writer = QImageWriter(file_name)

        if not writer.write(self.image):
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot write {QDir.toNativeSeparators(file_name)}: {writer.errorString()}",
            )
            return False
        message = f"Wrote '{QDir.toNativeSeparators(file_name)}'"
        self.statusBar().showMessage(message)
        return True

    def initialize_image_file_dialog(self, dialog: QFileDialog, accept_mode: QFileDialog.AcceptMode):
        last_dir = settings.value("lastDir", None)
        if last_dir and QDir(last_dir).exists():
            dialog.setDirectory(last_dir)
        else:
            pictures_locations = QStandardPaths.standardLocations(QStandardPaths.StandardLocation.PicturesLocation)
            if not pictures_locations:
                dialog_dir = QDir.currentPath()
            else:
                dialog_dir = pictures_locations[-1]
            dialog.setDirectory(dialog_dir)

        mime_type_filters = []
        if accept_mode == QFileDialog.AcceptMode.AcceptOpen:
            supported_mime_types = QImageReader.supportedMimeTypes()
        else:
            supported_mime_types = QImageWriter.supportedMimeTypes()

        for mime_type_name in supported_mime_types:
            mime_type_filters.append(str(mime_type_name))
        mime_type_filters.sort()

        dialog.setMimeTypeFilters(mime_type_filters)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(accept_mode)
        if accept_mode == QFileDialog.AcceptMode.AcceptSave:
            dialog.setDefaultSuffix("jpg")

    def open(self):
        dialog = QFileDialog(self, "Open File")
        self.initialize_image_file_dialog(dialog, QFileDialog.AcceptMode.AcceptOpen)

        while dialog.exec() == QDialog.DialogCode.Accepted:
            file_name = dialog.selectedFiles()[0]

            if self.load_file(file_name):
                # 成功打开图片，记录其所在目录
                settings.setValue("lastDir", QFileInfo(file_name).absolutePath())
                break

    def save_as(self):
        dialog = QFileDialog(self, "Save File As")
        self.initialize_image_file_dialog(dialog, QFileDialog.AcceptMode.AcceptSave)
        while dialog.exec() == QDialog.DialogCode.Accepted:
            file_name = dialog.selectedFiles()[0]

            if self.save_file(file_name):
                # 成功打开图片，记录其所在目录
                settings.setValue("lastDir", QFileInfo(file_name).absolutePath())
                break

    def close(self):
        self.image = QImage()
        self.image_label.clear()
        self.scale_factor = 1.0
        self.scroll_area.close()
        self.setWindowFilePath("")
        self.statusBar().clearMessage()

    def copy(self):
        QGuiApplication.clipboard().setImage(self.image)

    def paste(self):
        mime_data = QGuiApplication.clipboard().mimeData()
        if mime_data and mime_data.hasImage():
            image = QGuiApplication.clipboard().image()
            self.set_image(image)

    def zoom_in(self):
        self.scale_image(1.25)

    def zoom_out(self):
        self.scale_image(0.8)

    def normal(self):
        self.image_label.adjustSize()
        self.scale_factor = 1.0

    def fit_to_window(self):
        self.scroll_area.setWidgetResizable(True)
        self.normal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())
