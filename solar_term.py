#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T%dc.txt'

JieQi = [ '小雪', '大雪',
                 '小寒', '大寒',
                 '立春', '雨水', '惊蛰',
                 '谷雨',
                 '立夏', '小满', '芒种',
                 '小暑', '大暑',
                 '立秋', '处暑', '白露',
                 '寒露', '霜降',
                 '立冬', '小雪', '大雪', '冬至']

ics_head = [
	'BEGIN:VCALENDAR\n'
	'METHOD:PUBLISH\n'
	'VERSION:2.0\n'
	'X-WR-CALNAME:二十四节气'
	'PRODID:circle and Hong Kong Observatory\n'
	'X-WR-TIMEZONE:Asia/Shanghai\n'
	'CALSCALE:GREGORIAN\n'
]

ics_event = [
	'BEGIN:VEVENT\n'
	'TRANSP:TRANSPARENT\n'
	'DTEND;VALUE=DATE:%s\n'
	'UID:693F0393-circle\n'
	'DTSTAMP:20200722T071539Z\n'
	# 'DESCRIPTION:%s\n'
	# 'URL;VALUE=URI:%s\n'
	'SUMMARY:%s\n'
	'LAST-MODIFIED:20200722T071620Z\n'
	'DTSTART;VALUE=DATE:%s\n'
	'END:VEVENT\n'
]

ics_end = 'END:VCALENDAR'

def AddToICS(solar):
	'''整理格式'''
	year = solar[:4]
	solar = solar[5:]
	print(solar)
	month = solar[:2]
	if month[1] == '月':
		month = '0' + month[0]
	else month ==
	pass


def main():
	for i in range(2020,2021):
		# with open('%04d.txt'%i,'wb') as file:
			with urllib.request.urlopen(url % i) as f:
				html = f.read()
				lines = html.decode('big5').split('\n')
				for line in lines:
				    # print('下载完成:%04d' % i )
				    for j in JieQi:
					    if j in line:
					    	AddToICS(line)
					    	break
					    	# print(line)
					    	# file.write(line.encode('utf-8'))
					    	# print('下载完成:%02d' % i )
	# file.close()


if __name__ == "__main__":
    main()

# for i in JieQi:
# 	print(i)