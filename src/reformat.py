#!/usr/bin/python

import fileinput


cur_doc = None
l = 0
for line in fileinput.input():
	parts = line.strip().split()
	if l % 2 == 0:
		cur_doc = parts[0]
	else:
		#parts = [parts[0], parts[-1]]
		print('\t'.join([cur_doc, parts[-1]]))
	l += 1
