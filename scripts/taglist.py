#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import simplejson
import sys

from tumblr import Api


def taglist(username):
    api = Api(username)
    posts = api.read()
    alltags = {}
    for post in posts:
        tags = post.get('tags', [])
        for tag in tags:
            try:
                alltags[tag][0] += 1
            except KeyError:
                alltags[tag] = [1, post.get('date-gmt', '')]

    taglist = [tuple(val+[tag]) for tag,val in alltags.items()]
    return sorted(taglist, reverse=True)

def main():
    prog, args = sys.argv[0], sys.argv[1:]
    if not args:
        print 'usage: %s username' % prog
        return
    tags = taglist(args[0])
    print simplejson.dumps(tags)

if __name__ == '__main__':
    main()
