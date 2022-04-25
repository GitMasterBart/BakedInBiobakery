#!/bin/bash

# shellcheck disable=SC1090
source ~/Desktop/StageWetsus2022/BakedInBiobakery/Bio-bakeryHumaNtoolenv/bin/activate Bio-bakeryHumaNtoolenv

# shellcheck disable=SC2164
#cd ~/Desktop/StageWetsus2022/TranscriptoomAnalysis
#./HumanBashScriptSSH

#mkdir temp -p
#export TMPDIR=/temp

#humann --input $1 --output $2 --threads $3
#humann -i /Users/bengels/Desktop/Uploaded_files/demofile_wetsusR1.fastq.gz -o ~/Desktop/output_data/ --threads 12 --bypass-nucleotide-search --input-format fastq.gz --protein-database ~/Desktop/Uploaded_files/humann_dbs/uniref
# shellcheck disable=SC1073
# shellcheck disable=SC2034

kneaddata --input /Users/bengels/Desktop/Uploaded_files/demofile_wetsusR1.fastq.gz --reference-db ~/Desktop/kneaddataMap --output ~/Desktop/kneaddataMap/kneaddataOutputSingleEnd --trimmomatic ~/Desktop/kneaddataMap/Trimmomatic-0.36/

#humann -i $1 -o $2 --threads 12 --bypass-nucleotide-search --input-format $3 --protein-database $4 &

