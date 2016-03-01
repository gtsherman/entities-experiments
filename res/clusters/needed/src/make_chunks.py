#!/usr/bin/python

from sys import argv
from math import ceil


file_to_slice = argv[1]
number_of_chunks = int(argv[2])

lines = []
with open(file_to_slice) as f:
	for line in f:
		lines.append(line)

num_per_chunk = int(ceil(len(lines) / float(number_of_chunks)))

chunk = 1
n = 0
while n <= len(lines):
	with open(str(chunk), 'w') as out:
		for l in lines[n:n+num_per_chunk]:
			out.write(l)
	chunk += 1
	n += num_per_chunk
