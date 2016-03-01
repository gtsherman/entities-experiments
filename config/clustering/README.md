Cluster Configuration
=====================

Generally, you want the same cluster configuration but split up for N different chunks of needed files. Set the template to the correct settings, then run:

`./src/copyTemplate template N`

where `N` is the number of copies you need. These copies will be written to `tmp/`. You can then use these copies as follows:

`cd tmp/`
`~/entities/run/parallelClustering /path/to/output/directory/`
