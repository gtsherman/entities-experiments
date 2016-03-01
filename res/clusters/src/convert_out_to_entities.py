#!/usr/bin/python

from sys import argv
import fileinput


for line in fileinput.input():
	parts = line.split()
	doc, entity, score = parts[0], parts[2], parts[4]
	print('\t'.join([doc, entity, score]))
