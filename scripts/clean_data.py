import math
import numpy as np
import pandas as pd


def clean_data(data_path, out_path):
    df = pd.read_csv(data_path)
    df.columns = map(str.lower, df.columns)
    df = df.loc[df['ozone'].notnull()]
    df.to_csv(out_path, index=False)


clean_data(snakemake.input[0], snakemake.output[0])
