# QML

# 常用控件

### Item

所有控件的基类

##### 属性

- `x`
    - 控件向右平移
- `y`
    - 控件向下平移
- `z`
    - 堆叠层级优先级
- `visual`
    - 可见性
- `scale`
    - 缩放等级
- `rotation`
- `parent`
- `opacity`
- `anchors`
    - 锚布局
    - 需要先声明控件的 `id`，使用 `id` 去定义锚布局
        - 设置水平方向锚布局，水平方向位置失效但是竖直方向不会
- `clip`
    - 区域为裁剪区域，可以组合出不同的形状

### Rectangle

### Text

- `text`
    - 文本内容
- `font`
    - 符合属性
- `warpMode`
    - 换行
- `elide`
    - 省略

### TextField

文本输入框，需要导入 `QtQuick.Controls`

- `backgroud`
    - 使用 `anchors.fill: parent` 填充一个矩形美化
- `placeholderText`
    - 提示输入信息
- `echoMode`
    - `TextInput.Password`
- `selectByMouse`
    - 设置允许鼠标拖拽

### TextArea

文本填写框

### Image

- `source`
    - 引入图片资源，如果不是使用项目中的图片需要使用 `file:///` 开头
    - 项目添加文件需要使用 `qt resource` 管理

# 事件

### 鼠标事件

需要先划分鼠标区域

### 键盘事件

需要聚焦才能使用

### 拖拽事件

可以定义在鼠标区域内或者拖拽区域

### Button 类

##### Button

##### DelayButton

演示按钮，按住动画类似进度条，主要用于按着过一定时间出发特定事件

- `delay`
    - 设置延迟时间
- `activated`
    - 时间结尾触发事件

##### Switch

##### RadioButton

##### Popup

### Dialog

##### Dialog

##### FileDialog

从 `QtQuick.Dialogs` 导入控件

##### ColorDialog

##### MessageDialog

# 状态和过渡

运行时候会涉及多种状态的切换，引入状态管理
直接变化过于突兀，使用过渡来平滑实现

### 动画

##### PropertyAnimation

##### Behavior

定义值变化的行为，可以用来替换动画效果

##### ParallelAnimation SequentialAnimation

# 图形美化

### Gradient

##### LinearGradient

##### RadialGradient

### Image

##### BrightnessContrast

##### Slider

##### Colorize

# 视图代理模型

# 布局

### Row

### RowLayout

放缩可以自动填充

### Cloumn

### Grid

# 自定义控件

自定义控件需要文件名首字母大写