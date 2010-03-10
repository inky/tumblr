function rgbToHex(rgbString) {
    var parts = rgbString.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    for (var i = 1; i <= 3; i++) {
        parts[i] = parseInt(parts[i]).toString(16);
        if (parts[i].length == 1) parts[i] = '0' + parts[i];
    }
    delete (parts[0]);
    return parts.join('');
}

$(document).ready(function() {
    var darkTheme = $(document.body).is('.dark');
    var bgColor = rgbToHex($('body').css('background-color'));

    // Use nice ampersands.
    // http://patrickhaney.com/thinktank/2008/08/19/automatic-awesompersands
    var tags = ['h1','h2','h3','h4','h5','h6','p','blockquote','li'];
    var amp_tags = jQuery.map(tags, function(t) { return t + ":contains('&')"; }).join(',');
    $('.post-body').find(amp_tags).contents().each(function() {
        if (this.nodeType == 3) {  // text
            $(this).replaceWith(this.nodeValue.replace(/&/g, '<span class="amp">&amp;</span>'));
        }
    });

    $('.post-body object').each(function() {
        // Make YouTube players match the theme's background colour, and enable HD playback.
        // http://matthewbuchanan.name/post/261951286/improving-the-youtube-player
        if (!darkTheme) {
            if ($(this).find("param[value^='http://www.youtube.com']").length) {
                var parent = $(this).parent();
                var youtubeCode = parent.html();
                var params = "";
                if (youtubeCode.toLowerCase().indexOf("<param") == -1) {
                    $("param", this).each(function() {
                        params += $(this).get(0).outerHTML;
                    });
                }
                var oldOpts = /rel=0/g;
                var newOpts = "rel=0&amp;hd=1&amp;color1=0x" + bgColor + "&amp;color2=0x" + bgColor;
                youtubeCode = youtubeCode.replace(oldOpts, newOpts);
                if (params != "") {
                    params = params.replace(oldOpts, newOpts);
                    youtubeCode = youtubeCode.replace(/<embed/i, params + "<embed");
                }
                parent.html(youtubeCode);
            }
        }
    });
});
