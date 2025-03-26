#!/bin/bash

cd $NS3_DIR

./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=0 --nWifi=5 --logPath=$HOME/ftm-optimal/log-dynamic-n5-d0.csv --ftmAsap=False --ftmBurstDuration=6 --ftmBurstPeriod=5 --ftmFtmsPerBurst=4 --ftmMinDeltaFtm=4"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=50 --nWifi=5 --logPath=$HOME/ftm-optimal/log-dynamic-n5-d50.csv --ftmAsap=True --ftmBurstDuration=8 --ftmBurstPeriod=10 --ftmFtmsPerBurst=7 --ftmMinDeltaFtm=4"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=100 --nWifi=5 --logPath=$HOME/ftm-optimal/log-dynamic-n5-d100.csv --ftmAsap=False --ftmBurstDuration=8 --ftmBurstPeriod=5 --ftmFtmsPerBurst=7 --ftmMinDeltaFtm=3"

./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=0 --nWifi=10 --logPath=$HOME/ftm-optimal/log-dynamic-n10-d0.csv --ftmAsap=True --ftmBurstDuration=11 --ftmBurstPeriod=10 --ftmFtmsPerBurst=6 --ftmMinDeltaFtm=40"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=50 --nWifi=10 --logPath=$HOME/ftm-optimal/log-dynamic-n10-d50.csv --ftmAsap=False --ftmBurstDuration=10 --ftmBurstPeriod=5 --ftmFtmsPerBurst=6 --ftmMinDeltaFtm=10"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=100 --nWifi=10 --logPath=$HOME/ftm-optimal/log-dynamic-n10-d100.csv --ftmAsap=False --ftmBurstDuration=10 --ftmBurstPeriod=5 --ftmFtmsPerBurst=4 --ftmMinDeltaFtm=80"

./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=0 --nWifi=20 --logPath=$HOME/ftm-optimal/log-dynamic-n20-d0.csv --ftmAsap=False --ftmBurstDuration=9 --ftmBurstPeriod=5 --ftmFtmsPerBurst=3 --ftmMinDeltaFtm=5"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=50 --nWifi=20 --logPath=$HOME/ftm-optimal/log-dynamic-n20-d50.csv --ftmAsap=False --ftmBurstDuration=10 --ftmBurstPeriod=5 --ftmFtmsPerBurst=10 --ftmMinDeltaFtm=2"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=100 --nWifi=20 --logPath=$HOME/ftm-optimal/log-dynamic-n20-d100.csv --ftmAsap=True --ftmBurstDuration=11 --ftmBurstPeriod=1 --ftmFtmsPerBurst=1 --ftmMinDeltaFtm=1"

./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=0 --nWifi=50 --logPath=$HOME/ftm-optimal/log-dynamic-n50-d0.csv --ftmAsap=False --ftmBurstDuration=11 --ftmBurstPeriod=5 --ftmFtmsPerBurst=6 --ftmMinDeltaFtm=5"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=50 --nWifi=50 --logPath=$HOME/ftm-optimal/log-dynamic-n50-d50.csv --ftmAsap=True --ftmBurstDuration=11 --ftmBurstPeriod=12 --ftmFtmsPerBurst=1 --ftmMinDeltaFtm=4"
./waf --run "scenario --RngRun=100 --simulationTime=100 --ftmParamsSwitch=50 --logInterval=1 --mobilityModel=Distance --distance=5 --dataRate=100 --nWifi=50 --logPath=$HOME/ftm-optimal/log-dynamic-n50-d100.csv --ftmAsap=True --ftmBurstDuration=11 --ftmBurstPeriod=11 --ftmFtmsPerBurst=1 --ftmMinDeltaFtm=2"
