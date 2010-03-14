#!/usr/bin/env python
"""
Tumblr Theme Installs

Fetch the number of installs for a given Tumblr theme.

Copyright (c) 2010 Liam Cooke

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
__version__ = '2010.03.14'
__copyright__ = 'Copyright (c) 2010 Liam Cooke'
__url__ = 'http://github.com/inky/tumblr/tree/master/scripts/'

import optparse
import sys

from BeautifulSoup import BeautifulSoup

from openanything import fetch


USER_AGENT = 'ThemeInstalls/%s (Python; +%s)' % (__version__, __url__)

class HumanNumber:
    def __init__(self, string):
        self._string = str(string)
        self._int = int(string.replace(',', ''))
    def __repr__(self):
        return 'HumanNumber(%s)' % repr(self._string)
    def __str__(self):
        return self._string
    def __int__(self):
        return self._int

def theme_url(id):
    try:
        return 'http://www.tumblr.com/theme/%d' % int(id)
    except ValueError:
        return id

def theme_installs(id, full_response=False):
    """
    Return the number of installs for a given theme. id may be a numeric id
    (e.g. 1386) or a complete url (e.g. 'http://www.tumblr.com/theme/1386').
    """
    response = fetch(theme_url(id), agent=USER_AGENT)

    soup = BeautifulSoup(response['data'])
    try:
        installs = soup.find('div', id='install_count').string
        response['data'] = HumanNumber(installs)
    except AttributeError:
        response['data'] = None
    return full_response and response or response['data']


def main():
    parser = optparse.OptionParser(usage='%prog [options] theme_id')
    parser.add_option('-i', '--int', action='store_true', default=False,
                      help="machine-friendly output (e.g. 1234 instead of 1,234)")
    parser.add_option('-v', '--verbose', action='store_true', default=False,
                      help='verbose output')

    opts, args = parser.parse_args()

    if not len(args):
        parser.print_help()
        return 1

    result = theme_installs(args[0], opts.verbose)
    if opts.verbose:
        for key, val in result.items():
            if key != 'data':
                print('%s: %s' % (key, val))
        result = result['data']
    if opts.int:
        print(int(result))
    else:
        print(result)

if __name__ == '__main__':
    sys.exit(main())
