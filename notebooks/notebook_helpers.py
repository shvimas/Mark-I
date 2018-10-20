import os
import sys

import pandas as pd


def add_src_to_pythonpath():
    sys.path.append(os.path.abspath(os.path.join(__file__, '../../src')))


def df_to_dicts(df: pd.DataFrame) -> list:
    return list(map(lambda index_row: {col: val for col, val in zip(df.columns, index_row[1])}, df.iterrows()))
