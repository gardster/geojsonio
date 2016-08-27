#!/usr/bin/env python

import urllib
import sys
import webbrowser

url = "http://geojson.io/#data=data:application/json,{}"

geojson = sys.stdin.read()
geojson = geojson.replace(" ","")
paramstr = urllib.quote(geojson)
webbrowser.open_new_tab(url.format(paramstr))
