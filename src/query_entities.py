#!/usr/bin/python

import json
import sys


out_file = sys.argv[1]
document_entities_file = sys.argv[2]
query_file = sys.argv[3]

query_docs = {}
docs = set()
with open(out_file) as f:
	for line in f:
		query, _, document, rank, _, _ = line.split()
		rank = int(rank)
		if rank > 10:
			continue
		if query not in query_docs:
			query_docs[query] = []
		query_docs[query].append(document)
		docs.add(document)

doc_entities = {}
with open(document_entities_file) as f:
	for line in f:
		document, entity, _ = line.split()
		if document not in docs:
			continue
		if document not in doc_entities:
			doc_entities[document] = []
		doc_entities[document].append(entity)

queries = {}
j = json.load(open(query_file))
for q in j['queries']:
	queries[q['title']] = q['text']

for query in query_docs:
	for doc in query_docs[query]:
		i = 0
		if doc in doc_entities:
			for entity in doc_entities[doc]:
				i += 1
				if i <= 5:
					print('\t'.join([query, '"{}"'.format(queries[query]), entity]))
