#!/usr/bin/python

import fileinput


max_run = None
max_value = 0.0

cur_run = None
for line in fileinput.input():
	parts = line.split()
	if len(parts) > 1:
		cur_value = float(parts[-1])
		if cur_value > max_value:
			max_run = cur_run
			max_value = cur_value
	else:
		cur_run = line.strip()

print('Maximum run: {}, {}'.format(max_run, max_value))
