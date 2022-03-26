#!/bin/bash

InlogFileSSHBioInf.sh

ssh assemblix

cd ~/Desktop/Condaenv

source ~/Desktop/Condaenvbio-bakeryHumanNtoolenv/bin/activate

mkdir temp -p

export TMPDIR=/temp

humann --input $1 --output $2 --threads 14
