#!/bin/python3

from urllib.parse import urlparse
import sys, getopt
import ximalaya
import netease
import ifeng

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:')
    except getopt.GetoptError:
        print(sys.argv[0], ' -u <the URL of album on ximalaya')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: ', sys.argv[0], ' -u http://www.ximalaya.com/14043986/album/2807703')
            sys.exit(0)
        elif opt == '-u':
            print('Processing the album: ', arg)
            url = arg

    if (url.find('http://') == -1) and (url.find('https://') == -1):
        url = 'http://' + url

    site = urlparse(url).netloc

    if site == 'www.ximalaya.com':
        ximalaya.proc_album(url)
    elif site == 'music.163.com':
        netease.proc_album(url)
    elif site == 'diantai.ifeng.com':
        ifeng.proc_album(url)


if __name__ == "__main__":
    main()
