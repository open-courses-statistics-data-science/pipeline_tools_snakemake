import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump


def fit_linear_model(data_path, out_path):
    df = pd.read_csv(data_path)
    ozone = df['ozone'].values
    temp = df['temp'].values
    ozone = ozone.reshape(len(ozone), 1)
    temp = temp.reshape(len(temp), 1)
    reg = LinearRegression().fit(temp, ozone)
    dump(reg, out_path)


fit_linear_model(snakemake.input[0], snakemake.output[0])
