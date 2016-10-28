#!/usr/bin/python

from sys import argv
import os


template_file = argv[1]

template = []
with open(template_file) as f:
	for line in f:
		template.append(line.strip())
		key, path = line.split(':')
		if key == 'documents-file':
			chunk_dir = '/'.join(path.strip().split('/'))


for f in os.listdir(chunk_dir):
	with open('tmp3/{}'.format(f), 'w') as out:
		for line in template:
			if line.split(':')[0] == 'documents-file':
				line = line+'/{}'.format(f)
			out.write(line+'\n')
