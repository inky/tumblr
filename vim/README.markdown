tumblr.vim
==========

Vim syntax highlighting for Tumblr themes.

This will extend HTML syntax highlighting for files with the extension
`.tumblr.html` (e.g. `mytheme.tumblr.html`).

Installation
------------

Get the syntax file:

    cd ~/.vim/syntax/
    wget http://github.com/inky/tumblr/raw/master/vim/syntax/tumblr.vim

Add the following line to `~/.vim/filetype.vim`:

    au BufRead,BufNewFile *.tumblr.html setfiletype tumblr
