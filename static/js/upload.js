// 判断input是否有变化

onload = function Creatinput() {
    $('form').append('<input type="file" name="xFile" id="upload_input">' +
        '<input type="submit" value="上传" id="test">')
}
function add() {
    $('form').append('<input type="file" name="xFile" id="upload_input">')
}
//监听input的值变化
// $('form').on('input propertychange','upload_input',function add_input() {
//     var input = document.createElement('input');
//     input.type = 'file';
//     input.name = Xfile;
//     input.id = upload_input;
//     document.getElementById('upload_i').appendChild(input);
// })