if exists("did_load_filetypes")
    finish
endif

augroup tumblr
    au! BufRead,BufNewFile *.tumblr.html setfiletype tumblr
augroup END
