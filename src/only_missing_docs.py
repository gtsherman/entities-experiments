#!/usr/bin/python

import sys


queries_tsv_file = sys.argv[1]
missing_file = sys.argv[2]

missing = set()
with open(missing_file) as f:
	for line in f:
		missing.add(line.strip())

with open(queries_tsv_file) as f:
	for line in f:
		if line.split('\t')[0] in missing:
			print(line.strip())
