#!/usr/bin/env python
"""
Copyright (c) 2011 Liam Cooke

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
__author__ = 'Liam Cooke'
__version__ = '2011.03.23'
__copyright__ = 'Copyright (c) 2011 Liam Cooke'
__url__ = 'http://github.com/inky/tumblr/tree/master/scripts'


import json
import optparse
import sys
from urlparse import urlparse

from openanything import fetch


USER_AGENT = 'PostInfo/%s (Python; +%s)' % (__version__, __url__)
INDENT_WIDTH = 4


indents = lambda i: ' ' * i

class TumblrURLException(Exception): pass

def tidy_json(j):
    j = j.strip()
    return j[j.index('{') : j.rindex('}') + 1]

def find_int(path):
    for p in path.split('/'):
        try:
            return int(p)
        except ValueError:
            pass
    raise TumblrURLException

def api_url(post_url):
    url = urlparse(post_url)
    post_id = find_int(url.path)
    return 'http://%s/api/read/json?id=%d' % (url.hostname, post_id)

def reblog_url(api_data):
    post = api_data['posts'][0]
    return 'http://www.tumblr.com/reblog/%s/%s' % (post['id'], post['reblog-key'])

def tumblr_post(url='', fp=None):
    if fp:
        response = {'data': fp.read()}
    else:
        response = fetch(api_url(url), agent=USER_AGENT)
    info = json.loads(tidy_json(response['data']))
    return {
        'info': info,
        'reblog-url': reblog_url(info),
    }

def pretty_print(obj, indent=0):
    if obj in (None, '', []):
        print('%s%s' % (indents(indent), '-'))
    elif hasattr(obj, 'items'):
        for k, v in obj.items():
            print('%s%s:' % (indents(indent), k))
            pretty_print(v, indent + INDENT_WIDTH)
    elif hasattr(obj, 'append'):
        for v in obj:
            pretty_print(v, indent)
    else:
        v = obj.strip() if hasattr(obj, 'strip') else obj
        print('%s%s' % (indents(indent), v))

def main():
    parser = optparse.OptionParser(usage='%prog [options] post_url')
    opts, args = parser.parse_args()
    if not args:
        parser.print_help()
        return 1

    try:
        post = tumblr_post(args[0])
    except TumblrURLException:
        sys.stderr.write('Error: URL must point to a single Tumblr post.\n')
        return 1

    pretty_print(post['info'])
    print('\nReblog URL: %s' % post['reblog-url'])

if __name__ == '__main__':
    sys.exit(main())
