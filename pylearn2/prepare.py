#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Created:  2015-05-29
#


import urllib2
import img2csv

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

if __name__ == "__main__":
    print "start"
    download("http://pics.dmm.co.jp/mono/actjpgs/asou_nozomi.jpg", "datasets/asou_nozomi.jpg")
    download("http://pics.dmm.co.jp/mono/actjpgs/uehara_ai02.jpg", "datasets/uehara_ai02.jpg")
    download("http://pics.dmm.co.jp/mono/actjpgs/sakura_mana.jpg", "datasets/sakura_mana.jpg") 
