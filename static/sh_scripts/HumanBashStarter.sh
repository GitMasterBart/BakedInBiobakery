#!/bin/bash

source ~/Desktop/PipelineEnv/bin/activate

cd /Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery/biobakery/appModels/SnakePipeMultiHumaNn/

#/Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery/biobakery/appModels/SnakePipeMultiHumaNn/bbmap/reformat.sh in1=demofile_wetsus_0/kneaddata_output/demofile_wetsus_0_R1_kneaddata_paired_1.fastq in2=demofile_wetsus_0/kneaddata_output/demofile_wetsus_0_R1_kneaddata_paired_2.fastq out=demofile_wetsus_0/interleaved.fastq

#echo $2 $3 $4 $5 $6

snakemake --cores 2 --jobs 20 --config inputfiles=$1 dataset="$2" $3 $4 $5 $6 $7 $8 $9 ${11} ${12} ${13} &




