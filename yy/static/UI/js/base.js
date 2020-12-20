function bg_color() {
    var bg_col_now = document.getElementById('nr').style.backgroundColor
    if(bg_col_now ==='rgb(240, 248, 255)'){
        bg_col_now = '#22303f'
    }
    else {
        bg_col_now = '#F0F8FF'
    }
    document.getElementById('nr').style.backgroundColor = bg_col_now;
}
  // 颜色表达式 rgb(xx, xx, xx) 为十进制  一组3个  每个范围0-255   对应#xxxxxx   x为2个一组  十六进制