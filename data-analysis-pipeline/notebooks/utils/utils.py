import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def process_psychopy_data(path,groups=[]):
    df = pd.read_csv(path)
    
    all_trials = []

    for group in groups:
        trials = df.groupby(group).agg({
            'participant': 'first',
            'session': 'first',
            'currentTrialID': 'first',
            'startId': 'first',
            'targetId': 'first',
            'speed': 'first',
            'producedDuration': list,
            'reactionTime': list,
            'turn': 'last',
            'score': 'first',
            'visualMode': 'first',
            'targetPos': list,
            'responseBlock.keyPress.keys': 'first',
            'frameN': 'first',
            'trialStartTime': list,
            'keyPressTime': list,
            'keyReleaseTime': list,
        })

        # === Auto-expand all list columns ===
        list_columns = trials.columns[trials.applymap(type).eq(list).any()]

        for col in list_columns:
            expanded = trials[col].apply(pd.Series)

            # Rename columns: first column = original name, rest = col_attempt_2, col_attempt_3, ...
            rename_dict = {0: col}
            rename_dict.update({i: f"{col}_attempt_{i+1}" for i in range(1, expanded.shape[1])})

            expanded.rename(columns=rename_dict, inplace=True)

            # Drop original list column and insert expanded columns
            trials = pd.concat([trials.drop(columns=[col]), expanded], axis=1)

        # === Additional processing ===
        trials['interLMDistance'] = abs(trials['startId'] - trials['targetId'])
        trials['trueDuration_s'] = trials['interLMDistance'] / trials['speed'] * 10
        trials['producedDuration_s'] = trials['producedDuration']
        trials['error'] = abs(trials['producedDuration_s'] - trials['trueDuration_s'])
        trials['direction'] = trials['responseBlock.keyPress.keys'].apply(lambda x: -1 if x == 'right' else 1)
        trials['turn'] += 1
        trials['visualMode'] = trials['visualMode'].astype(int)
        trials = trials.drop(columns=['responseBlock.keyPress.keys'])

        # Reset index
        trials = trials.reset_index()

        all_trials.append(trials)

    # Concatenate all trials into one DataFrame
    final_trials = pd.concat(all_trials, ignore_index=True)
    
    return final_trials
