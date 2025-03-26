#!/bin/bash

cd $NS3_DIR

N_WIFIS=(5 10 20 50)
DATA_RATES=(0 50 100)

ASAPS=("False" "True")
BURST_DURATIONS=(2 3 4 5 6 7 8 9 20 11)
BURST_PERIODS=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15)
FTMS_PER_BURSTS=(1 2 3 4 5 6 7 8 9 10)
MIN_DELTA_FTMS=(1 2 3 4 5 10 20 40 80 160)

for nWifi in "${N_WIFIS[@]}"; do
  for dataRate in "${DATA_RATES[@]}"; do
    for asap in "${ASAPS[@]}"; do
      ./waf --run "scenario --RngRun=100 --mobilityModel=RWPM --dataRate=$dataRate --nWifi=$nWifi --ftmAsap=$asap --csvPath=$HOME/ftm-optimal/out-n$nWifi-d$dataRate-rwpm-asap-$asap.csv"
    done

    for burstDuration in "${BURST_DURATIONS[@]}"; do
      ./waf --run "scenario --RngRun=100 --mobilityModel=RWPM --dataRate=$dataRate --nWifi=$nWifi --ftmBurstDuration=$burstDuration --csvPath=$HOME/ftm-optimal/out-n$nWifi-d$dataRate-rwpm-burst-duration-$burstDuration.csv"
    done

    for burstPeriod in "${BURST_PERIODS[@]}"; do
      ./waf --run "scenario --RngRun=100 --mobilityModel=RWPM --dataRate=$dataRate --nWifi=$nWifi --ftmBurstPeriod=$burstPeriod --csvPath=$HOME/ftm-optimal/out-n$nWifi-d$dataRate-rwpm-burst-period-$burstPeriod.csv"
    done

    for ftmsPerBurst in "${FTMS_PER_BURSTS[@]}"; do
      ./waf --run "scenario --RngRun=100 --mobilityModel=RWPM --dataRate=$dataRate --nWifi=$nWifi --ftmFtmsPerBurst=$ftmsPerBurst --csvPath=$HOME/ftm-optimal/out-n$nWifi-d$dataRate-rwpm-ftms-per-burst-$ftmsPerBurst.csv"
    done

    for minDeltaFtm in "${MIN_DELTA_FTMS[@]}"; do
      ./waf --run "scenario --RngRun=100 --mobilityModel=RWPM --dataRate=$dataRate --nWifi=$nWifi --ftmMinDeltaFtm=$minDeltaFtm --csvPath=$HOME/ftm-optimal/out-n$nWifi-d$dataRate-rwpm-min-delta-ftm-$minDeltaFtm.csv"
    done
  done
done
