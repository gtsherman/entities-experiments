#!/bin/bash

for i in `ls 0.*_0.0_*.*`; do echo $i; trec_eval $1 $i | grep map; done | ~/entities/src/reformat.py | compute -m max -f 3 -w
