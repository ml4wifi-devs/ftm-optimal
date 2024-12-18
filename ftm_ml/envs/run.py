import os
os.environ['JAX_ENABLE_X64'] = 'True'

import argparse

from py_interface import *

from ftm_ml.envs.ns3_ai_structures import *


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    # global settings
    args.add_argument('--seed', type=int, default=100)
    args.add_argument('--mempoolKey', type=int, default=1234)
    args.add_argument('--ns3Path', type=str, default='')
    args.add_argument('--scenario', type=str, default='scenario')

    # ns-3 args
    args.add_argument('--agentIntervalTime', type=float, default=5.0)
    args.add_argument('--csvPath', type=str, default='results.csv')
    args.add_argument('--dataRate', type=int, default=120)
    args.add_argument('--ftmIntervalTime', type=float, default=0.1)
    args.add_argument('--fuzzTime', type=float, default=5.0)
    args.add_argument('--nWifi', type=int, default=1)
    args.add_argument('--simulationTime', type=float, default=50.0)
    args.add_argument('--warmupTime', type=float, default=10.0)

    args = args.parse_args()
    args = vars(args)

    # read the arguments
    ns3_path = args.pop('ns3Path')

    if os.environ.get('NS3_DIR'):
        ns3_path = os.environ['NS3_DIR']
    if not ns3_path:
        raise ValueError('ns-3 path not found')

    mempool_key = args.pop('mempoolKey')
    scenario = args.pop('scenario')
    seed = args.pop('seed')

    ns3_args = args
    ns3_args['RngRun'] = seed
    ns3_args['useMlAgent'] = True

    # set up the environment
    exp = Experiment(mempool_key, MEM_SIZE, scenario, ns3_path)
    var = Ns3AIRL(MEMBLOCK_KEY, Env, Act)

    try:
        # run the experiment
        ns3_process = exp.run(setting=ns3_args, show_output=True)
        action = None

        while not var.isFinish():
            with var as data:
                if data is None:
                    break

                data.act.numberOfBurstExponent = 1
                data.act.burstDuration = 6
                data.act.minDeltaFtm = 4
                data.act.partialTsfTimer = 0
                data.act.partialTsfNoPref = True
                data.act.asap = True
                data.act.ftmsPerBurst = 2
                data.act.burstPeriod = 2

        ns3_process.wait()
    finally:
        del exp
