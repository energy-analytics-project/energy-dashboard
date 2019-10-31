#!/bin/bash
set -x

/home/toddg/bin/anaconda3/condabin/conda activate edc
pip install -U energy-dashboard-client

echo "command: $1, logfile: $2"
$1 2>&1 | tee $2
