import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        # self.test()
        # self.test_signal()
        self.test_country()

    def test(self):
        cbb = QtWidgets.QComboBox(self)
        cbb.move(300, 100)
        cbb.addItem("1")
        cbb.addItem("2")
        cbb.addItem("3")
        cbb.insertSeparator(1)
        cbb.addItem("4")

        cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        cbb.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        cbb.setMinimumContentsLength(3)
        cbb.setMaxCount(12)

    def test_signal(self):
        cbb = QtWidgets.QComboBox(self)
        cbb.move(200, 200)
        cbb.resize(400, 60)
        cbb.addItems([str(i) for i in range(100, 110)])
        cbb.addItem("100", {"key": "value"})

        cbb.currentIndexChanged.connect(lambda: print(f"当前文本为：{cbb.currentText()}"))

        print(cbb.findText("102"))

        cbb.setEditable(True)
        cbb.setFrame(False)

        info_label = QtWidgets.QLabel(self)
        info_label.move(100, 100)

        @Slot()
        def test_popup():
            cbb.showPopup()

        btn = QtWidgets.QPushButton("展开", self)
        btn.move(100, 50)
        btn.clicked.connect(test_popup)

        cbb.setCompleter(QtWidgets.QCompleter(["102", "104"]))

        @Slot(int)
        def test_index(index):
            info = f"传入的索引为{index}，该项对应的文本为{cbb.itemText(index)}"
            info_label.setText(info)
            info_label.adjustSize()

        cbb.activated.connect(test_index)

    def test_country(self):
        self.country_dic = {
            "中国": {
                "CN": "北京"
            },
            "美国": {
                "US": "华盛顿"
            },
            "日本": {
                "JP": "东京"
            },
            "英国": {
                "GB": "伦敦"
            },
            "法国": {
                "FR": "巴黎"
            },
            "德国": {
                "DE": "柏林"
            },
            "俄罗斯": {
                "RU": "莫斯科"
            },
            "韩国": {
                "KR": "首尔"
            },
            "加拿大": {
                "CA": "渥太华"
            },
            "澳大利亚": {
                "AU": "堪培拉"
            }
        }

        self.country_cbb = QtWidgets.QComboBox()
        self.city_cbb = QtWidgets.QComboBox()
        self.code_cbb = QtWidgets.QComboBox()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.country_cbb)
        layout.addWidget(self.code_cbb)
        # layout.addWidget(self.city_cbb)
        self.setLayout(layout)

        self.country_cbb.addItems(self.country_dic.keys())

        self.country_cbb.currentIndexChanged.connect(self.test_country_s)

    def test_country_s(self):
        self.city_cbb.clear()
        name = self.country_cbb.currentText()
        cities = self.country_dic[name]
        for code, city in cities.items():
            self.code_cbb.addItem(code, city)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
