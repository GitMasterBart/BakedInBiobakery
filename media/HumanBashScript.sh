#!/bin/bash

cd ~/Desktop/StageWetsus2022/TranscriptoomAnalysis

#./HumanBashScriptSSH

source /usr/local/Caskroom/miniconda/base/bin/activate HumanNEnv

mkdir temp -p

export TMPDIR=/temp

humann --input $1 --output $2 --threads $3
