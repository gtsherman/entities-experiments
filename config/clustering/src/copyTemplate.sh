#!/bin/bash
rm -rf $HOME/entities/config/clustering/tmp
mkdir $HOME/entities/config/clustering/tmp
python $HOME/entities/config/clustering/src/copyTemplate.py $@
