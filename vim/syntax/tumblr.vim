" Vim syntax file
" Language:     Tumblr HTML Theme
" Maintainer:   Liam Cooke <liamcooke@gmail.com>
" URL:          http://github.com/inky/tumblr/blob/master/vim/syntax/tumblr.vim
" Last Change:  2010 Mar 10

runtime! syntax/html.vim
unlet b:current_syntax

syntax match tumblrBlock '{/\?block:[A-Za-z0-9-]\+}' oneline containedin=ALL
syntax match tumblrTag '{[A-Za-z0-9-:]\+}' oneline containedin=ALL

hi def link tumblrBlock Label
hi def link tumblrTag Identifier

let b:current_syntax = "tumblr"
