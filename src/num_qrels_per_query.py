#!/usr/bin/python

import fileinput
import pprint


q = {}
for line in fileinput.input():
	query, _, _, rel = line.split()
	if query not in q:
		q[query] = 0
	q[query] += 1 if int(rel) >= 1 else 0

pprint.pprint(q)
