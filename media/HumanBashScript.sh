#!/bin/bash

# shellcheck disable=SC1090
source ~/Desktop/StageWetsus2022/BakedInBiobakery/Bio-bakeryHumaNtoolenv/bin/activate Bio-bakeryHumaNtoolenv

# shellcheck disable=SC2164
#cd ~/Desktop/StageWetsus2022/TranscriptoomAnalysis

#./HumanBashScriptSSH

mkdir temp -p

export TMPDIR=/temp

humann --input $1 --output $2 --threads $3
