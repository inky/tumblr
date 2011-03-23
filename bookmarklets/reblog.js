// 1. Minify with http://jscompress.com/
// 2: s/ /%20/g
// 3. s/^/javascript:/

(function() {

    var w = window,
        d = document,
        l = d.location,
        t = d.title,
        u = /\/([0-9]+)($|\/)/.exec(l.pathname),
        c = 'inkyrblg',
        p, r, s;

    inkyrblg = function(o) {
        p = o.posts[0];
        w.location = 'http://www.tumblr.com/reblog/' + p.id + '/' + p['reblog-key'];
    };

    if (u && u[1]) {
        d.title = '(Loading...)%20' + t;
        w[c] = eval(c);
        s = d.createElement('SCRIPT');
        s.src = 'http://' + l.host + '/api/read/json?callback=' + c + '&id=' + u[1];
        d.getElementsByTagName('HEAD')[0].appendChild(s);
    } else {
        alert('This will only work on a Tumblr post page.');
    }

}())
