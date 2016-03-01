#!/usr/bin/python

from sys import argv


out_file = argv[1]
k = int(argv[2])

with open(out_file) as f:
	for line in f:
		if int(line.split()[3]) <= k:
			print(line.strip())
