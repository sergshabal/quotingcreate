#!/usr/bin/env python


it_host = 'http://it.troika.ru/dic/firm_quote/quotations_xml.wbp'

import urllib2
import codecs

b = urllib2.urlopen(it_host)
s = b.read()

data = codecs.open('quotation_xml', encoding='utf-8',mode='w+')
data.writelines(s)

f = codecs.open('it_troika.csv', encoding='utf-8',mode='w+')
#f = codecs.open('it_troika.csv', mode='w+')

if len(s):
	ss = []
	ss = s.split('\n')
	for l in ss[5:23]:
		#f.write(l + '\n')
		f.write(l.decode('utf-8') + u'\n')

f.close()

