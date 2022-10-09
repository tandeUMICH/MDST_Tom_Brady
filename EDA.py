import pandas as pd
import numpy as np
import itertools
import string

def main():
    df = pd.read_csv('../data/TB_data.csv')
    print(df.head(10))
    