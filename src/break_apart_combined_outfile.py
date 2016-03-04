#!/usr/bin/python

import fileinput


current_file = None
out = None
for line in fileinput.input():
	parts = line.split()
	l = float(parts[-1])
	l = round(l*10)/10
	l = str(l)
	if current_file != l:
		current_file = l
		out = open(l, 'a')
	out.write(' '.join(parts[:-1])+' '+l+'\n')
