import sys

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, Slot, QPoint


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)
        # self.setup_ui()
        # self.test_echo_mode()
        # self.test_limit_length()
        # self.test_readonly()
        # self.test_align()
        # self.test_slot()
        # self.test_cursor_move()
        # self.test_validator()
        # self.test_completer()
        # self.test_self_action()

    def setup_ui(self):
        line_edit = QtWidgets.QLineEdit(self)
        # line_edit.move(100, 100)

    def test_echo_mode(self):
        line1 = QtWidgets.QLineEdit(self)
        line2 = QtWidgets.QLineEdit(self)
        line3 = QtWidgets.QLineEdit(self)
        line4 = QtWidgets.QLineEdit(self)

        line1.move(200, 10)
        line2.move(200, 40)
        line3.move(200, 70)
        line4.move(200, 100)

        line1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        line2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        line3.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)  # 编辑时可见密码
        line4.setEchoMode(QtWidgets.QLineEdit.EchoMode.NoEcho)  # 长度也不可见

    def test_limit_length(self):
        line_limit = QtWidgets.QLineEdit(self)
        line_limit.setMaxLength(5)
        line_limit.setPlaceholderText("请输入用户名，限制长度5")
        line_limit.move(200, 150)

    def test_readonly(self):
        line_readonly = QtWidgets.QLineEdit(self)
        line_readonly.setReadOnly(True)
        line_readonly.setText("只读")
        line_readonly.move(200, 180)

    def test_align(self):
        line_align = QtWidgets.QLineEdit(self)
        line_align.move(200, 220)
        line_align.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        line_align.setTextMargins(50, 0, 0, 0)
        line_align.setText("测试对齐")

    def test_slot(self):
        clear_btn = QtWidgets.QPushButton("清空")
        select_btn = QtWidgets.QPushButton("全选")
        copy_btn = QtWidgets.QPushButton("复制")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(clear_btn)
        layout.addWidget(select_btn)
        layout.addWidget(copy_btn)

        line1 = QtWidgets.QLineEdit(self)
        line2 = QtWidgets.QLineEdit(self)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(line1)
        main_layout.addWidget(line2)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)

        @Slot()
        def test_clear():
            line1.clear()
            line2.clear()

        clear_btn.clicked.connect(test_clear)

        @Slot()
        def test_select():
            line1.selectAll()
            line2.selectAll()

        select_btn.clicked.connect(test_select)

    def test_cursor_move(self):

        line = QtWidgets.QLineEdit()

        # 移动光标
        move_group = QtWidgets.QGroupBox("move cursor")
        move_step_length = QtWidgets.QCheckBox("word")
        move_select = QtWidgets.QCheckBox("move and select")
        cursor_forward_btn = QtWidgets.QPushButton("forward")
        cursor_backward_btn = QtWidgets.QPushButton("backward")

        move_layout = QtWidgets.QVBoxLayout()
        move_layout.addWidget(move_step_length)
        move_layout.addWidget(move_select)
        move_layout.addWidget(cursor_forward_btn)
        move_layout.addWidget(cursor_backward_btn)
        move_group.setLayout(move_layout)

        # 光标位置
        pos_group = QtWidgets.QGroupBox("cursor position")
        pos_line_edit = QtWidgets.QLineEdit()
        pos_line_edit.setReadOnly(True)
        set_pos_spinbox = QtWidgets.QSpinBox()
        set_pos_spinbox.setRange(0, 100)
        pos_at_label = QtWidgets.QLabel("at")

        point = QPoint(80, 20)

        pos_layout = QtWidgets.QFormLayout()
        pos_layout.addRow(QtWidgets.QLabel("光标当前位置："), pos_line_edit)
        pos_layout.addRow(QtWidgets.QLabel("将光标位置设置到："), set_pos_spinbox)
        pos_layout.addRow(QtWidgets.QLabel(f"{point.toTuple()}处的光标位于"), pos_at_label)
        pos_group.setLayout(pos_layout)

        # 光标移动
        move_style_group = QtWidgets.QGroupBox("move style")
        toward_switch = QtWidgets.QPushButton("switch text toward")
        logical_move = QtWidgets.QPushButton("logical move style")
        visual_move = QtWidgets.QPushButton("visual move style")

        move_style_layout = QtWidgets.QVBoxLayout()
        move_style_layout.addWidget(toward_switch)
        move_style_layout.addWidget(logical_move)
        move_style_layout.addWidget(visual_move)
        move_style_group.setLayout(move_style_layout)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(line)
        main_layout.addWidget(move_group)
        main_layout.addWidget(pos_group)
        main_layout.addWidget(move_style_group)

        self.setLayout(main_layout)

        # slot

        @Slot()
        def cursor_move_forward():
            mark = move_select.isChecked()
            if move_step_length.isChecked():
                line.cursorWordForward(mark)
            else:
                line.cursorForward(mark)
            line.setFocus()

        cursor_forward_btn.clicked.connect(cursor_move_forward)

        @Slot()
        def cursor_backward_forward():
            mark = move_select.isChecked()
            if move_step_length.isChecked():
                line.cursorWordBackward(mark)
            else:
                line.cursorBackward(mark)
            line.setFocus()

        cursor_backward_btn.clicked.connect(cursor_backward_forward)

        @Slot()
        def show_cursor_pos():
            pos_line_edit.setText(str(line.cursorPosition()))

        line.cursorPositionChanged.connect(show_cursor_pos)

        @Slot(int)
        def move_cursor_pos(pos):
            line.setCursorPosition(pos)
            line.setFocus()

        set_pos_spinbox.valueChanged[int].connect(move_cursor_pos)

        @Slot()
        def update_pos_at_label():
            pos_at_label.setText(f"{line.cursorPositionAt(point)}")

        line.cursorPositionChanged.connect(update_pos_at_label)

        @Slot(bool)
        def change_toward(yes):
            if yes:
                line.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            else:
                line.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            line.setFocus()

        toward_switch.toggled[bool].connect(change_toward)

        @Slot()
        def set_logical_move():
            line.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
            line.setFocus()

        logical_move.clicked.connect(set_logical_move)

        @Slot()
        def set_visual_move():
            line.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
            line.setFocus()

        visual_move.clicked.connect(set_visual_move)

    def test_validator(self):
        line = QtWidgets.QLineEdit()
        ip = QtWidgets.QLineEdit()

        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel("两位数："), line)
        layout.addRow(QtWidgets.QLabel("IPv4："), ip)
        self.setLayout(layout)

        validator = QtGui.QIntValidator(10, 99, line)
        line.setValidator(validator)

        ip_mask = "000.000.000.000;_"
        ip.setInputMask(ip_mask)

    def test_completer(self):
        line = QtWidgets.QLineEdit()
        line.setPlaceholderText("测试自动补全")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(line)
        self.setLayout(layout)

        completer = QtWidgets.QCompleter(["test1", "test2", "test3"], line)
        line.setCompleter(completer)

    def test_self_action(self):
        line = QtWidgets.QLineEdit()
        line.setPlaceholderText("测试自定义行为")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(line)
        self.setLayout(layout)

        action = QtGui.QAction(line)
        eye_icon = QtGui.QIcon("eye.png")
        eye_slash = QtGui.QIcon("eye_slash.png")
        action.setIcon(eye_icon)

        @Slot()
        def switch():
            if line.echoMode() == QtWidgets.QLineEdit.EchoMode.Password:
                line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                action.setIcon(eye_icon)
            else:
                line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                action.setIcon(eye_slash)

        action.triggered.connect(switch)
        line.addAction(action, QtWidgets.QLineEdit.ActionPosition.TrailingPosition)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
