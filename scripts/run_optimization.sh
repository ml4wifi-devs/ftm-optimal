#!/bin/bash

N_WIFIS=(5 10 20 50)
DATA_RATES=(0 50 100)
DISTANCES=(5 50)

for nWifi in "${N_WIFIS[@]}"; do
  for dataRate in "${DATA_RATES[@]}"; do
    for distance in "${DISTANCES[@]}"; do
      python main.py --nWifi=$nWifi --dataRate=$dataRate --distance=$distance --mobility="Distance"
      python main.py --n_trials=200 --nWifi=$nWifi --dataRate=$dataRate --distance=$distance --mobility="Distance" --constrained
    done
    python main.py --nWifi=$nWifi --dataRate=$dataRate --mobility="RWPM"
    python main.py --n_trials=200 --nWifi=$nWifi --dataRate=$dataRate --mobility="RWPM" --constrained
  done
done
