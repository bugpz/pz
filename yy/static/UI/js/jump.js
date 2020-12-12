var s1;
var s2;
var x = 4;
var y = 3;
var out_time = document.getElementById("out_time")
var out_time_w = document.getElementById("wait_out_time")

onload = function jump() {
     s1 = setInterval(upload_out_time, 1000);
     s2 = setInterval(wait_out_time, 1000)
};


function upload_out_time() {
    if (!out_time) {
        clearInterval(s1)
    } else if (out_time && x >= 0) {
        out_time.innerText = x;
    } else {
        location.href = '/index/';
    }
    x--;
}

function wait_out_time() {
    if (!out_time_w) {
        clearInterval(s2)
    } else if (out_time_w && y >= 0) {
        out_time_w.innerText = y;
    } else {
        location.href = "/login/"
    }
    y--;
}
