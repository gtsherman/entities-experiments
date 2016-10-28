#!/usr/bin/python

import sys


out_file = sys.argv[1]

docs = set()
with open(out_file) as f:
	for line in f:
		doc = line.split()[2]
		if doc not in docs:
			docs.add(doc)
			print(doc)
