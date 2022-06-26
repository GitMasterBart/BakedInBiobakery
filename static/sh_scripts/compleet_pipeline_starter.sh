#!/bin/bash

source venv/bin/activate

cd /Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery/biobakery/appModels/SnakePipeMultiHumaNn/

rm -r -f $1/.snakemake

snakemake --cores 6 --jobs 200 --config inputfiles=$1 name=$2 user_index=$3 research_index=$4 dataset=$5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15} ${16}   &


#snakemake --dag --cores 2 --jobs 200 --config inputfiles=$1 name=$2 user_index=$3 research_index=$4 dataset=$5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15} ${16} | dot -Tsvg > dag.svg  &




