import QtQuick
import QtQuick.Controls

Window {
    id: window
    visible: true
    width: 640
    height: 480
    title: qsTr("ListView")
    color: "white"

    // ListView {
    //     id: listView
    //     anchors.fill: parent
    //     model: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    //     spacing: 5
    //     delegate: Rectangle {
    //         width: listView.width
    //         height: 50
    //         color: "lightgray"
    //         border.width: 1
    //         border.color: "black"
    //         Text {
    //             text: modelData
    //             anchors.centerIn: parent
    //         }
    //     }
    // }

    ListModel {
        id: listModel
        ListElement {
            name: "Mike"
            age: 18
            city: "New York"
        }
        ListElement {
            name: "James"
            age: 19
            city: "New York"
        }
        ListElement {
            name: "Jim"
            age: 20
            city: "New York"
        }
    }

    Column {
        spacing: 5
        anchors.right: parent.right
        width: 200
        Button {
            width: parent.width
            text: "添加"
            onClicked: {
                // listModel.append({
                //     name: "Mike",
                //     age: 18,
                //     city: "New York"
                // })
                listModel.insert(0, {
                    name: "Mike",
                    age: 18,
                    city: "New York"
                })
            }
        }
        Button {
            width: parent.width
            text: "删除"
            onClicked: {
                listModel.remove(listModel.count - 1)
            }
        }
    }

    ListView {
        id: listView
        anchors.fill: parent
        model: listModel
        spacing: 5
        anchors.rightMargin: 200
        add: Transition {
            NumberAnimation {
                properties: "y";
                duration: 300
            }
        }

        section {
            property: "name"
            criteria: ViewSection.FullSection
            delegate:
                Rectangle {
                    height: 50
                    width: 50
                    radius: 25
                    color: "lightgray"
                    Text {
                        text: section
                        anchors.centerIn: parent
                    }
                }
        }

        header: Item {
            width: listView.width
            height: 50
            Rectangle {
                id: leftRect
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                color: "lightgray"
                border.width: 1
                border.color: "black"
                Text {
                    text: "姓名"
                    anchors.centerIn: parent
                }
            }

            Rectangle {
                id: rightRect
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                color: "lightgray"
                border.width: 1
                border.color: "black"
                Text {
                    text: "年龄"
                    anchors.centerIn: parent
                }
            }
        }

        highlight: Item {
            width: listView.width
            height: 50
            z: 100

            function setText(name, age) {
                hightTextName.text = name
                hightTextAge.text = age
            }

            Rectangle {
                id: leftRect
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                border.color: "red"
                Text {
                    id: hightTextName
                    anchors.centerIn: parent
                }
            }

            Rectangle {
                id: rightRect
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                border.color: "red"
                Text {
                    id: hightTextAge
                    anchors.centerIn: parent
                }
            }
        }

        delegate: Item {
            width: listView.width
            height: 50

            Rectangle {
                id: leftRect
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                color: "lightgray"
                border.width: 1
                border.color: "black"
                Text {
                    text: listModel.get(index).name
                    anchors.centerIn: parent
                }
            }

            Rectangle {
                id: rightRect
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                width: parent.width / 2 - 5
                color: "lightgray"
                border.width: 1
                border.color: "black"
                Text {
                    text: listModel.get(index).age
                    anchors.centerIn: parent
                }
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true
                onEntered: {
                    listView.currentIndex = index
                    listView.highlightItem.setText(listModel.get(index).name, listModel.get(index).age)
                }
            }
        }

        footer: Item {
            width: listView.width
            height: 50
            Rectangle {
                id: leftRect
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                color: "lightgray"
                width: parent.width
                border.width: 1
                border.color: "black"
                Text {
                    text: "结束"
                    anchors.centerIn: parent
                }
            }
        }
    }

}