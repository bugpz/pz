function bg_color() {
    let bg_col_now = document.getElementById('nr').style.backgroundColor
    let bg_cor_now1 = bg_col_now.substring(4, bg_col_now.length - 1).replace(/\s/g, " ")
    let y = bg_cor_now1.split(",")
    let r = parseInt(y[0]).toString(16).toUpperCase()
    let g = parseInt(y[1]).toString(16).toUpperCase()
    let b = parseInt(y[2]).toString(16).toUpperCase()
    let rgb = "#" + r + g + b
    if (rgb === '#F0F8FF') {
        bg_col_now = '#22303f'
    } else {
        bg_col_now = '#F0F8FF'
    }
    document.getElementById('nr').style.backgroundColor = bg_col_now;
}

// 颜色表达式 rgb(xx, xx, xx) 为十进制  一组3个  每个范围0-255   对应#xxxxxx   x为2个一组  十六进制