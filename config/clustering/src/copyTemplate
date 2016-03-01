#!/usr/bin/python

from sys import argv


template_file = argv[1]
num_chunks = int(argv[2])

template = []
with open(template_file) as f:
	for line in f:
		template.append(line.strip())

for i in range(1, num_chunks+1):
	with open('tmp/{}'.format(i), 'w') as out:
		for line in template:
			if line.split(':')[0] == 'documents-file':
				line = line.split('/')
				line[-1] = str(i)
				line = '/'.join(line)
			out.write(line+'\n')
