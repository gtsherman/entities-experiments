#!/bin/bash

for i in `ls 0.*_*.*_0.0`; do echo $i; trec_eval $1 $i | grep map; done | ~/entities/src/reformat.py | compute -m max -f 3 -w
