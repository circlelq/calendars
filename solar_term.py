#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import urllib.request

# 开始和结束年份
begin = 2018
end = 2050

url = 'https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T%dc.txt'

JieQi_j = ('小雪', '大雪', '小寒', '大寒', '立春', '雨水', '惊蛰', '谷雨', '立夏', '小满', '芒种', '小暑', '大暑', '立秋', '处暑', '白露', '寒露', '霜降', '立冬', '小雪', '大雪')

JieQi_f = ('小雪', '大雪', '小寒', '大寒', '立春', '雨水', '驚蟄', '穀雨', '立夏', '小滿', '芒種', '小暑', '大暑', '立秋', '處暑', '白露', '寒露', '霜降', '立冬', '小雪', '大雪')

ics_head = (
	'BEGIN:VCALENDAR\n'
	'METHOD:PUBLISH\n'
	'VERSION:2.0\n'
	'X-WR-CALNAME:二十四节气\n'
	'PRODID:circle and Hong Kong Observatory\n'
	'X-WR-TIMEZONE:Asia/Shanghai\n'
	'CALSCALE:GREGORIAN\n'
)

ics_event = (
	'BEGIN:VEVENT\n'
	'DTSTART;VALUE=DATE:%s\n'
	'DTEND;VALUE=DATE:%s\n'
	'UID:%s-circle\n'
	'DTSTAMP:20200722T071539Z\n'
	# 'DESCRIPTION:%s\n'
	# 'URL;VALUE=URI:%s\n'
	'SUMMARY:%s\n'
	'END:VEVENT\n'
)

ics_end = 'END:VCALENDAR'

solar_term = [ics_head]

def AddToICS(solar):
	'''整理格式'''
	# 读取年份
	year = solar[:4]
	solar = solar[5:]
	month = solar[:2]
	# 读取月份
	if month[1] == '月':
		month = '0' + month[0]
		solar = solar[2:]
	else:
		solar = solar[3:]
	day = solar[:2]
	# 读取日
	if day[1] == '日':
		day = '0' + day[0]
	# 节气名
	solar = solar.replace(' ','')
	name = JieQi_j[JieQi_f.index(solar[-3:-1])]
	date = year + month + day
	line = ics_event % (date, date, date, name)
	solar_term.append(line)


def main():
	for i in range(begin,end):
		# with open('%04d.txt'%i,'wb') as file:
			with urllib.request.urlopen(url % i) as f:
				html = f.read()
				lines = html.decode('big5').split('\n')
				for line in lines:
				    # print('下载完成:%04d' % i )
				    for j in JieQi_f:
					    if j in line:
					    	AddToICS(line)
					    	break
					    	# print(line)
					    	# file.write(line.encode('utf-8'))
					    	# print('下载完成:%02d' % i )
	# file.close()
	solar_term.append(ics_end)
	# print(type(solar_term))
	with open('solar_term.ics','wb') as file:
		for line in solar_term:
			file.write(line.encode('utf-8'))
		file.close()


if __name__ == "__main__":
    main()

