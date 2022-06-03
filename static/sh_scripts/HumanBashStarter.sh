#!/bin/bash

source ~/Desktop/PipelineEnv/bin/activate

cd /Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery/biobakery/appModels/SnakePipeMultiHumaNn/

snakemake --cores 2 --jobs 20 --config inputfiles=$1 name=$2 user_index=$3 research_index=$4 dataset=$5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} ${15} ${16}  &

#snakemake --cores 2 --jobs 20 --config inputfiles=$1 dataset="$2" $3 $4 $5 $6 $7 $8 $9 ${11} ${12} ${13} --unlock &




