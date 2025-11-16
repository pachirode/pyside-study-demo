import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    color: "gray"

    WorkerScript {
        id: worker
        source: "js/worker.js"
        onMessage: {
            console.log(messageObject) // 打印脚本里面发送的数据
        }
    }

    Item {
        id: item
        anchors.left: parent.left
        anchors.right: parent.right
        height: 40
        clip: true
        Row {
            Repeater {
                model: ["property1", "property2", "property3", "property4"]
                Rectangle {
                    width: item.width / 4
                    height: item.height
                    color: "white"
                    Text {
                        anchors.centerIn: parent
                        text: modelData
                    }
                }
            }
        }
    }

    Timer {
        interval: 1
        running: true
        repeat: true
        onTriggered: {
            worker.sendMessage(listModel)
        }
    }

    ListModel {
        id: listModel
        Component.onCompleted: {
            for (let i = 0; i < 100; i++) {
                listModel.append({val1: 0.1, val2: 0.2, val3: 0.3, val4: 0.4})
            }
        }
    }

    Item {
        anchors.fill: parent
        anchors.topMargin: 40
        clip: true
        ListView {
            id: listView
            model: listModel
            anchors.fill: parent
            delegate: Rectangle {
                width: item.width
                height: 40
                color: "white"
                Row {
                    Item {
                        width: listView.width / 4
                        height: 40
                        Text {
                            anchors.centerIn: parent
                            text: val1
                        }
                    }
                    Item {
                        width: listView.width / 4
                        height: 40
                        Text {
                            anchors.centerIn: parent
                            text: val2
                        }
                    }
                    Item {
                        width: listView.width / 4
                        height: 40
                        Text {
                            anchors.centerIn: parent
                            text: val3
                        }
                    }
                    Item {
                        width: listView.width / 4
                        height: 40
                        Text {
                            anchors.centerIn: parent
                            text: val4
                        }
                    }
                }
            }
        }
    }
}
