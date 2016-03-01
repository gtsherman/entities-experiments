#!/bin/bash
# $1 = n, as in "top n entities"
cat 1/*/stdout > combined
$HOME/entities/res/clusters/src/get_top_k_entities.py combined $1 | $HOME/entities/res/clusters/src/convert_out_to_entities.py > clusters_$1.tsv
rm combined
