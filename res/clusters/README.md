Clusters
========

Precomputed document clusters of the form:

> doc	relatedDoc	confidence

This directory is structured as `target/clustered/clusters.tsv` where `target` refers to the target collection (the documents being retrieved) and `clustered` refers to the collection being clustered (either the target collection or some external collection).

Note that due to Github file limits, some `clusters.tsv` files may be compressed. Similarly, the files in the `needed` directory are preserved where possible, but limits have prevented uploading of several important files. These files can be recreated, however. See the README in `~/entities/config/clustering` for instructions on creating clusters.
