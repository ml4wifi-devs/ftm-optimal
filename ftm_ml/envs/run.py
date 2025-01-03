import argparse
import os
from functools import partial

import optuna


def objective(trial, ns3_path, scenario, ns3_args):
    ftm_params = {
        'ftmNumberOfBurstsExponent': trial.suggest_int('ftmNumberOfBurstsExponent', 1, 4),
        'ftmBurstDuration': trial.suggest_int('ftmBurstDuration', 2, 11),
        'ftmMinDeltaFtm': trial.suggest_int('ftmMinDeltaFtm', 1, 26),
        'ftmPartialTsfTimer': 2 ** trial.suggest_int('ftmPartialTsfTimer', 1, 16) - 1,
        'ftmPartialTsfNoPref': trial.suggest_categorical('ftmPartialTsfNoPref', [True, False]),
        'ftmAsap': trial.suggest_categorical('ftmAsap', [True, False]),
        'ftmFtmsPerBurst': trial.suggest_int('ftmFtmsPerBurst', 1, 8),
        'ftmBurstPeriod': trial.suggest_int('ftmBurstPeriod', 1, 20)
    }
    run_args = {**ns3_args, **ftm_params}

    return None


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    # global settings
    args.add_argument('--database', type=str, default='sqlite:///optuna.db')
    args.add_argument('--seed', type=int, default=100)
    args.add_argument('--ns3_path', type=str, default='')
    args.add_argument('--n_trials', type=int, default=200)
    args.add_argument('--scenario', type=str, default='scenario')

    # ns-3 args
    args.add_argument('--dataRate', type=int, default=120)
    args.add_argument('--ftmIntervalTime', type=float, default=0.1)
    args.add_argument('--fuzzTime', type=float, default=5.0)
    args.add_argument('--nWifi', type=int, default=1)
    args.add_argument('--simulationTime', type=float, default=50.0)
    args.add_argument('--warmupTime', type=float, default=10.0)

    args = args.parse_args()
    args = vars(args)

    # read the arguments
    ns3_path = args.pop('ns3_path')

    if os.environ.get('NS3_DIR'):
        ns3_path = os.environ['NS3_DIR']
    if not ns3_path:
        raise ValueError('ns-3 path not found')

    scenario = args.pop('scenario')
    seed = args.pop('seed')

    ns3_args = args
    ns3_args['RngRun'] = seed

    study = optuna.create_study(
        storage=args['database'],
        study_name='ftm-ml',
        load_if_exists=True,
        direction='maximize',
        sampler=optuna.samplers.TPESampler(seed=seed)
    )

    study.optimize(
        partial(objective, ns3_path=ns3_path, scenario=scenario, ns3_args=ns3_args),
        n_trials=args['n_trials'],
        n_jobs=-1,
        show_progress_bar=True
    )
