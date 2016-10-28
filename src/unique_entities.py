#!/usr/bin/python

from entity_overlap import read_out_file, read_clusters_file
from sys import argv


out_file = argv[1]
clusters_file = argv[2]
topk_docs = int(argv[3])
topk_entities = int(argv[4])

returned, all_returned = read_out_file(out_file, topk_docs)
clusters = read_clusters_file(clusters_file, all_returned, topk_entities)

for query in returned:
	doc_ent_sets = []
	for doc in returned[query]:
		if doc in clusters:
			doc_ent_sets.append(clusters[doc])
	print('{}\t{}'.format(query, str(len(set.union(*doc_ent_sets)))))
