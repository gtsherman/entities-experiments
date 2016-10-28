#!/usr/bin/python

import string, sys


topics_file = sys.argv[1]

print('<parameters>')
with open(topics_file) as f:
	for line in f:
		if '<top>' in line:
			print('<query>')
		elif '<num>' in line:
			number = line.split()[-1]
			print('<number>{}</number>'.format(number))
		elif '<title>' in line:
			title = line.replace('<title> ', '')
			title = ''.join(c for c in title if c not in string.punctuation).lower().strip()
			print('<text>')
			print(title)
			print('</text>')
		elif '</top>' in line:
			print('</query>')
print('</parameters>')
			
