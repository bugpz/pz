onload = function jump() {
    setInterval(go,1000)
};
var x = 4;
function go() {
    if(x >= 0){
        document.getElementById('out_time').innerText=x;
    }else {
        location.href='/index/';
    }
    x--;
}
