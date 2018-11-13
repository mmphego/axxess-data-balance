#!/usr/bin/env python
import cookielib
import mechanize
import os
import urllib2
import time
from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

def response(url, username, password):
    br = mechanize.Browser()
    br.set_cookiejar(cookielib.CookieJar())
    try:
        br.open(url)
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        br.submit()
        response = br.response().read()
        br.cookiejar.clear()
        br.clear_history()
        _index = response.find('GBs')
        resp = float(response[_index-10:_index+10].split('>')[-1].split()[0])
        return resp
    except Exception:
        return False


if __name__ == '__main__':
    url = "https://ccp.axxess.co.za/fixed-wireless-data/view/3446425"
    data = response(url, os.getenv("USERNAME"), os.getenv("PASSWORD"))
    print ('{} GB'.format(data))
