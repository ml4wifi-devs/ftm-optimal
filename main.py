import argparse
import subprocess
import os
from functools import partial

import optuna


def run_until_success(ns3_path, scenario, ns3_args, base_seed=100):
    dict_to_args = lambda d: ' '.join([f'--{k}={v}' for k, v in d.items()])
    seed = base_seed

    while True:
        try:
            ns3_args['RngRun'] = seed
            cmd = f'./waf --run "{scenario} {dict_to_args(ns3_args)}"'
            result = subprocess.run(cmd, cwd=ns3_path, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            seed += 1
            if seed > base_seed + 10:
                return None


def objective(trial, ns3_path, scenario, constrained, ns3_args):
    if constrained:
        ftm_params = {
            'ftmBurstDuration': trial.suggest_int('ftmBurstDuration', 2, 6),
            'ftmBurstPeriod': trial.suggest_int('ftmBurstPeriod', 2, 15),
            'ftmMinDeltaFtm': trial.suggest_categorical('ftmMinDeltaFtm', [4, 5, 10, 20]),
        }
    else:
        ftm_params = {
            'ftmAsap': trial.suggest_categorical('ftmAsap', [True, False]),
            'ftmBurstDuration': trial.suggest_int('ftmBurstDuration', 2, 11),
            'ftmBurstPeriod': trial.suggest_int('ftmBurstPeriod', 1, 15),
            'ftmFtmsPerBurst': trial.suggest_int('ftmFtmsPerBurst', 1, 10),
            'ftmMinDeltaFtm': trial.suggest_categorical('ftmMinDeltaFtm', [1, 2, 3, 4, 5, 10, 20, 40, 80, 160]),
        }

    run_args = {**ns3_args, **ftm_params}
    result = run_until_success(ns3_path, scenario, run_args)

    try:
        result = result.split('\n')[-6].split(',')[-1]
        return float(result)
    except (ValueError, AttributeError) as e:
        return None


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    # global settings
    args.add_argument('--constrained', default=False, action='store_true')
    args.add_argument('--database', type=str, default=None)
    args.add_argument('--seed', type=int, default=100)
    args.add_argument('--ns3_path', type=str, default='')
    args.add_argument('--n_trials', type=int, default=500)
    args.add_argument('--scenario', type=str, default='scenario')

    # ns-3 args
    args.add_argument('--area', type=float, default=40.0)
    args.add_argument('--dataRate', type=float, default=10.0)
    args.add_argument('--distance', type=float, default=0.0)
    args.add_argument('--ftmIntervalTime', type=float, default=1.0)
    args.add_argument('--fuzzTime', type=float, default=5.0)
    args.add_argument('--mobilityModel', type=str, default='Distance')
    args.add_argument('--nWifi', type=int, default=1)
    args.add_argument('--simulationTime', type=float, default=50.0)
    args.add_argument('--warmupTime', type=float, default=10.0)

    args = args.parse_args()
    args = vars(args)

    # read the arguments
    if args['database']:
        database = args['database']
    elif not args['constrained']:
        database = 'sqlite:///ftm.db'
    elif args['constrained']:
        database = 'sqlite:///ftm-constrained.db'

    args.pop('database')
    constrained = args.pop('constrained')
    seed = args.pop('seed')
    ns3_path = args.pop('ns3_path')
    n_trials = args.pop('n_trials')
    scenario = args.pop('scenario')

    if os.environ.get('NS3_DIR'):
        ns3_path = os.environ['NS3_DIR']
    if not ns3_path:
        raise ValueError('ns-3 path not found')

    # create the optuna study
    study = optuna.create_study(
        storage=database,
        study_name=f'ftm-ml-n{args["nWifi"]}-d{args["dataRate"]}-mob-{args["mobilityModel"]}-dis{args["distance"]}',
        load_if_exists=True,
        direction='maximize',
        sampler=optuna.samplers.TPESampler(seed=seed)
    )

    study.optimize(
        partial(objective, ns3_path=ns3_path, scenario=scenario, ns3_args=args, constrained=constrained),
        n_trials=n_trials,
        n_jobs=24,
        show_progress_bar=True
    )
