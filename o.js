$(document).ready(function() {
    $('.post-body').find('h1,h2,h3,h4,h5,h6, p,blockquote,li').each(function() {
        h = $(this).html();

        // Use nice ampersands and fix widows
        // (thanks to http://justinhileman.info/articles/more-jquery-typography)
        h = h.replace(/&amp;/g, '<span class="amp">&amp;<\/span>');
        if (!h.match(/&nbsp;/)) {
            h = h.replace(/\s([^\s>]{0,10})\s*$/, '&nbsp;$1')
        }

        $(this).html(h);
    });
});
