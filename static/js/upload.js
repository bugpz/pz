// 判断input是否有变化
onload = function add() {
    setInterval(Creatinput,1000)
}
function Creatinput() {
    var upi = document.createElement('input');
    upi.type = 'file';
    upi.name = 'Xfile';
    upi.id = 'upload_input';
    document.getElementById('upload_input').appendChild(upi);
}
//监听input的值变化
// $('form').on('input propertychange','upload_input',function add_input() {
//     var input = document.createElement('input');
//     input.type = 'file';
//     input.name = Xfile;
//     input.id = upload_input;
//     document.getElementById('upload_i').appendChild(input);
// })