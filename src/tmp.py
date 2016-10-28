#!/usr/bin/python

import sys


fil = sys.argv[1]

with open(fil) as f:
	for line in f:
		parts = line.strip().split()
		params = parts[0].split('_')[1:]
		print('\t'.join(params + [parts[-1]]))
