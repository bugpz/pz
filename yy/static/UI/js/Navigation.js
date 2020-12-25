
onload = function navigation() {
    let d = document.getElementById('Navigation')
    let body = {
        'https://github.com/': 'github',
        'https://www.v2ex.com/': 'V2EX',
        'https://www.aliyun.com/': 'aliyun',
        'https://cloud.tencent.com/': 'cloudqq',
        'https://cloud.baidu.com/': 'baiduyun',
        'https://sso.qiniu.com/': 'qiniu',
        'https://v.qq.com/': 'vqq',
        'https://www.iqiyi.com/': 'iqiyi',
        'https://www.youku.com/': 'youku',
        'https://www.douyu.com/': 'douyu',
        'https://www.huya.com/': 'huya',
        'https://www.bilibili.com/': 'bilibili',
        'https://www.jianshu.com/"': 'jianshu',
        'https://www.oschina.net/': 'oschina',
        'http://www.myzaker.com/': 'zaker',
        'https://www.jd.com/': 'jd',
        'http://ifkdy.com/': 'ifkdy',
        'https://www.dytt8.net/': 'dytt8',
        'https://imgurl.org/': 'imgurl',
        'https://www.processon.com/': 'processon',
        'http://www.xiachufang.com/': 'xiachufang'
    };
    for(let i in body){
        $(d).append('<div style="width: 25%; float: left;"><a href='+i +' '+' target="_blank">\n' +
        '        <img style="width: 32px; height: 32px;" src="/static/UI/icon/'+body[i]+'.png\  ">\n' +
        '        <span data-v-ed292c2c="">'+body[i]+'</span>\n' +
        '    </a></div>')
    }

}