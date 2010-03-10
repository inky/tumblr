if exists("did_load_filetypes")
    finish
endif

runtime! ftdetect/*.vim

au! BufRead,BufNewFile *.tumblr.html setfiletype tumblr
