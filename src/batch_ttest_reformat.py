#!/usr/bin/python

import fileinput


for line in fileinput.input():
	if len(line.split()) == 1:
		cur_file = line.strip()
	elif len(line.strip()) == 0:
		last_line_blank = True
	elif last_line_blank and line[0] != 'p':
		baseline = line.split()[-1].strip()
		last_line_blank = False
	elif last_line_blank:
		p = line.split()[-1].strip()
		last_line_blank = False
		#if this > baseline:
		print('\t'.join([cur_file, baseline, this, p]))
	else:
		this = line.split()[-1].strip()
		last_line_blank = False
