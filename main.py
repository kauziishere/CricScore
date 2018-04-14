import requests
import re
import urllib2
import os
import cookielib
import json
from bs4 import BeautifulSoup
import subprocess as sp
import time

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def function():
	url = "http://www.cricbuzz.com/live-cricket-scores/"
	DIR="Pictures" 
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
	}
	bs = get_soup(url, header)
	data = bs.find_all("div", class_ = "cb-lv-scrs-col text-black")
	
	all_vals = []
	for i in data:
		flag = 1
		val = ''
		for j in str(i):
			if j == "<":
				flag = 0
			elif j == '>':
				flag = 1
			elif flag == 1:
				val += j
		val += '\n'
		all_vals.append(val)
	cmd = 'notify-send ' + '"Cricket Score" ' +'"' + '\n'.join(all_vals) + '"'
	sp.call(cmd, shell = True)

if __name__ == "__main__":
	cnt = 0
	while(True):
		function()
		time.sleep(60)
