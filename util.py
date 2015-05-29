#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Created:  2015-05-29
#
import urllib2

def download(url, dest):
    """
    downlaod file from internet
    @param url target url to download
    @dest destination to store file 

    example
        download("http://xxx.co.jp/test.jpg", "img/test.jpg")
    """
    response = urllib2.urlopen(url)
    output = open(dest, 'wb')
    output.write(response.read())
    output.close()
