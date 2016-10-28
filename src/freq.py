#!/usr/bin/python

from collections import Counter
import fileinput


to_count_file = fileinput.input()

query_entities = {}
query_text = {}
for line in to_count_file:
	query, qtext, entity = line.strip().split('\t')
	query_text[query] = qtext
	if query not in query_entities:
		query_entities[query] = []
	query_entities[query].append(entity)

for query in query_entities:
	count = Counter(query_entities[query]).most_common()
	for tup in count:
		print('\t'.join([query, query_text[query], tup[0], str(tup[1])]))
