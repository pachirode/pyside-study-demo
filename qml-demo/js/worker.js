WorkerScript.onMessage = function run(listModel) {
    for (let i = 0; i < listModel.count; i++) {
        let data = listModel.get(i);
        listModel.set(i, {val1: data.val1 + 1, val2: data.val2 + 1, val3: data.val3 + 1, val4: data.val4 + 1})
    }

    WorkerScript.sendMessage(listModel)
    listModel.sync()
}