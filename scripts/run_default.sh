#!/bin/bash

cd $NS3_DIR

N_WIFIS=(5 10 20 50)
DATA_RATES=(0 50 100)

for nWifi in "${N_WIFIS[@]}"; do
  for dataRate in "${DATA_RATES[@]}"; do
    ./waf --run "scenario --RngRun=100 --mobilityModel=Distance --distance=5 --dataRate=$dataRate --nWifi=$nWifi --csvPath=$HOME/ftm-ml/out-n$nWifi-d$dataRate-distance-5.csv"
  done
done
