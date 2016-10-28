#!/bin/bash
rm -rf $HOME/entities/config/clustering/tmp3
mkdir $HOME/entities/config/clustering/tmp3
python $HOME/entities/config/clustering/src/copyTemplate.py $@
