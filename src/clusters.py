def read_clusters_file(clusters_file, k=10):
	clusters = {}
	with open(clusters_file) as f:
		cur_doc = None
		cur_ent = 0
		for line in f:
			doc, entity, score = line.split()
			if doc != cur_doc:
				cur_doc = doc
				cur_ent = 1
			elif cur_ent > k:
				continue
			cur_ent += 1
			clusters[doc] = clusters.get(doc, []) + [(entity, float(score))]
	return clusters
