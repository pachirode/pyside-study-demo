import QtQuick
import QtQuick.Controls


Button {
    width: 100
    height: 50
    text: "Click me!"
    background: Rectangle {
        id: bg
        width: 100
        height: 50
        radius: 25
        color: "green"
    }
    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        onEntered: {
            bg.color = "red"
        }
        onExited: {
            bg.color = "green"
        }
    }
}
