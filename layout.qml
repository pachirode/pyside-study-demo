import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: window
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    // Row{
    //     spacing: 10
    //     layoutDirection: Qt.LeftToRight
    //     Rectangle{
    //         color: "red"
    //         width: 100
    //         height: 100
    //     }
    //     Rectangle{
    //         color: "green"
    //         width: 100
    //         height: 100
    //     }
    //     Rectangle{
    //         color: "blue"
    //         width: 100
    //         height: 100
    //     }
    // }

    GridLayout{
        rowSpacing: 10
        columnSpacing: 20
        columns: 2
        anchors.fill: parent
        Rectangle{
            color: "red"
            width: 100
            height: 100
            Layout.alignment: Qt.AlignCenter
        }
        Rectangle{
            color: "green"
            width: 100
            height: 100
            Layout.alignment: Qt.AlignCenter
        }
        Rectangle{
            color: "blue"
            width: 100
            height: 100
            Layout.alignment: Qt.AlignCenter
        }
        Rectangle{
            color: "yellow"
            width: 100
            height: 100
            Layout.alignment: Qt.AlignCenter
        }
        CustomButton{

        }
    }
}
