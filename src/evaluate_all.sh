#!/bin/bash

for i in `find -maxdepth 1 -type f`
do
  echo $i
  trec_eval $1 $i | grep map
done | ~/entities/src/reformat.py
