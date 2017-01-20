#!/usr/bin/python

import sys

in_file = sys.argv[1]
stoplist_file = sys.argv[2]

stopwords = set()

with open(stoplist_file) as f:
	for line in f:
		stopwords.add(line.strip())

with open(in_file) as f:
	for line in f:
		word = line.split()[-1].strip()
		if word not in stopwords:
			print(line.strip())
