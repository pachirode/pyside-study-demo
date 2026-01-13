import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import Qt5Compat.GraphicalEffects
// import MyModule 1.0

Window {
    id: window
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    // Rectangle {
    //     id: base
    //     width: 20
    //     height: 100
    //     visible: true
    //     color: "red"
    //     property color rColor: "pink"
    // }
    //
    // Rectangle {
    //     width: 100
    //     height: 100
    //     color: base.rColor
    //     Component.onCompleted: {
    //         console.log("completed")
    //     }
    //     x: 100
    //     anchors.left: base.right
    // }
    //
    // Text {
    //     text: "Hello World"
    //     wrapMode: Text.WordWrap
    // }
    //
    // TextField {
    //     text: "Hello World"
    //     width: 100
    //     height: 100
    //     x: 200
    //     y: 200
    //     wrapMode: Text.WordWrap
    //     background: Rectangle {
    //         color: "yellow"
    //         anchors.fill: parent
    //     }
    // }

    // Image {
    //     anchors.centerIn: parent
    //     source: "imgs/carouselI1.png"
    // }

    // 鼠标事件

    // Rectangle {
    //     id: mousearea1
    //     width: 100
    //     height: 100
    //     color: "red"
    //     Drag.active: area.drag.active // 激活，拖拽区域才能识别
    //     MouseArea {
    //         id: area
    //         anchors.fill: parent
    //         onClicked: {
    //             mousearea1.color = "blue"
    //             console.log("clicked")
    //         }
    //         onDoubleClicked: {
    //             mousearea1.color = "yellow"
    //             console.log("double clicked")
    //         }
    //         drag.target: mousearea1
    //         drag.axis: Drag.XAndYAxis
    //         onReleased: {
    //             console.log("released")
    //             dropR.color = "blue"
    //         }
    //     }
    // }
    //
    // DropArea {
    //     width: 300
    //     height: 300
    //     x: 300
    //     Rectangle {
    //         id: dropR
    //         width: 200
    //         height: 200
    //         anchors.fill: parent
    //         color: "blue"
    //     }
    //     onEntered: {
    //         console.log("entered")
    //         dropR.color = "pink"
    //     }
    // }

    // 键盘事件
    // Rectangle {
    //     width: 500
    //     height: 500
    //     color: "yellow"
    //     focus: true
    //     Keys.onPressed: function(event){
    //         console.log("pressed", event.key)
    //     }
    // }

    // Button {
    //     width: 500
    //     height: 300
    //     x: 10
    //     y: 10
    //     text: "button"
    //     anchors.centerIn: parent
    //     icon.source: "imgs/carouselI1.png"
    //     icon.height: 200
    //     icon.width:300
    //     onClicked: {
    //         console.log("button clicked")
    //     }
    // }

    // DelayButton {
    //     width: 100
    //     height: 30
    //     x: 10
    //     y: 10
    //     text: "button"
    //     delay: 200
    //     onActivated: {
    //         console.log("time finished")
    //     }
    //
    //     onProgressChanged: {
    //         console.log("button process: ", progress)
    //     }
    // }

    // Switch {
    //     onPositionChanged: {
    //         console.log("position: ", position)
    //     }
    //     onVisualPositionChanged: {
    //         console.log("visual position: ", visualPosition)
    //     }
    //     onCheckedChanged: {
    //         console.log("checked: ", checked)
    //     }
    // }

    // ButtonGroup {
    //     id: gp
    //     exclusive: false // 一组选项是否互斥
    // }
    //
    // RadioButton {
    //     ButtonGroup.group: gp
    //     onCheckedChanged: {
    //         console.log("A")
    //     }
    // }
    //
    // RadioButton {
    //     y: 30
    //     ButtonGroup.group: gp
    //     onCheckedChanged: {
    //         console.log("B")
    //     }
    // }
    //
    // RadioButton {
    //     y: 60
    //     ButtonGroup.group: gp
    //     onCheckedChanged: {
    //         console.log("C")
    //     }
    // }

    // Button {
    //     width: 100
    //     height: 200
    //     onClicked:{
    //         pop.open()
    //     }
    // }

    // Popup {
    //     id: pop
    //     width: 500
    //     height: 500
    //     anchors.centerIn: parent
    // }

    // Dialog {
    //     id: pop
    //     title: "Dialog"
    //     standardButtons: Dialog.Ok | Dialog.Cancel
    // }

    // FileDialog {
    //     id: pop
    //     fileMode: FileDialog.OpenFiles
    //     onAccepted: {
    //         console.log(pop.currentFiles)
    //     }
    // }

    // Rectangle {
    //     id: re
    //     width: 500
    //     height: 500
    //     PropertyAnimation on height {
    //         duration: 3000
    //         to: 200
    //     }
    //     color: "yellow"
    //     Behavior on width {
    //         NumberAnimation {
    //             duration: 3000
    //         }
    //     }
    //     anchors.centerIn: parent
    //     states: [
    //         State {
    //             name: "state1"
    //             PropertyChanges {
    //                 target: re
    //                 color: "red"
    //             }
    //         },
    //         State {
    //             name: "state2"
    //             PropertyChanges {
    //                 target: re
    //                 color: "blue"
    //             }
    //         }
    //     ]
    //
    //     transitions: [
    //         Transition {
    //             from: "state1"
    //             to: "state2"
    //             PropertyAnimation {
    //                 target: re
    //                 property: "color"
    //                 duration: 3000
    //             }
    //         },
    //         Transition {
    //             from: "state2"
    //             to: "state1"
    //             PropertyAnimation {
    //                 target: re
    //                 property: "color"
    //                 duration: 3000
    //             }
    //         }
    //     ]
    //
    //     MouseArea {
    //         hoverEnabled: true
    //         onEntered: {
    //             re.state = "state1"
    //         }
    //         onExited: {
    //             re.state = "state2"
    //         }
    //         anchors.fill: parent
    //         onClicked: {
    //             re.width = 500
    //         }
    //     }
    // }
    //
    //
    // PropertyAnimation {
    //     id: anim
    //     target: re
    //     property: "width"
    //     from: 500
    //     to: 100
    // }
    //
    // Button {
    //     width: 100
    //     height: 30
    //     x: 10
    //     y: 10
    //     text: "button"
    //     onClicked: {
    //         anim.start ()
    //     }
    // }

    // Rectangle {
    //     id: re
    //     width: 500
    //     height: 500
    //     gradient: Gradient {
    //         GradientStop {
    //             position: 0
    //             color: "red"
    //         }
    //         GradientStop {
    //             position: 1
    //             color: "blue"
    //         }
    //         GradientStop {
    //             position: 0.5
    //             color: "yellow"
    //         }
    //     }
    // }

    // LinearGradient {
    //     anchors.fill: parent
    //     start: Qt.point(0, 0)
    //     end: Qt.point(400, 400)
    //     gradient: Gradient {
    //
    //         GradientStop {
    //             position: 0
    //             color: "red"
    //         }
    //         GradientStop {
    //             position: 0.55
    //             color: "blue"
    //         }
    //         GradientStop {
    //             position: 1
    //             color: "yellow"
    //         }
    //     }
    //
    // }

    // Image {
    //     id: img
    //     source: "imgs/carouselI1.png"
    // }
    // BrightnessContrast {
    //     id: bc
    //     source: img
    //     brightness: 0.5
    //     contrast: 0.5
    // }
    // Slider {
    //     id: slider
    //     x: 10
    //     y: 10
    //     width: 400
    //     height: 30
    //     from: 0
    //     to: 1
    //     onValueChanged: {
    //         bc.brightness = value
    //     }
    // }

    // custom_button{
    //
    // }

    // CustomButton{
    //     MouseArea{
    //         anchors.fill: parent
    //         onClicked: MySingleton.changeColor()
    //     }
    // }

    // color: MySingleton.col
    // Connections {
    //     target: MySingleton
    //     onChangeColor:{
    //         window.color = "blue"
    //     }
    // }

    color: mySingleton.col

    Rectangle {
        width: 500
        height: 500
        Text {
            anchors.centerIn: parent
            text: test.name
        }
    }
}

