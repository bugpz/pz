// 判断input是否有变化

onload = function Creatinput() {
    $('form').append('<input type="file" name="xFile" id="fileupload" multiple>' +
        '<input type="submit" value="上传" id="test">')
}
function add() {
    $('form').append('<input type="file" name="xFile" id="upload_input">')
}

