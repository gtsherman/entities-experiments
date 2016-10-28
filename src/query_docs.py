#!/usr/bin/python

import sys


have_file = sys.argv[1]
have = {}
with open(have_file) as f:
	for line in f:
		query, doc = line.strip().split()
		if query not in have:
			have[query] = []
		have[query].append(doc)

out_file = sys.argv[2]
with open(out_file) as f:
	for line in f:
		parts = line.split()
		query, doc = parts[0], parts[2]
		if doc not in have[query]:
			print('{} {}'.format(query, doc))
