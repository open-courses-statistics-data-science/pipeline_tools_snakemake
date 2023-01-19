import numpy as np
import pandas as pd
from joblib import load
import matplotlib.pyplot as plt


def plot_regression(model_path, data_path, out_path):
    reg = load(model_path)
    df = pd.read_csv(data_path)
    ozone = df['ozone'].values
    temp = df['temp'].values
    ozone = ozone.reshape(len(ozone), 1)
    temp = temp.reshape(len(temp), 1)
    plt.scatter(temp, ozone, color='black')
    plt.plot(temp, reg.predict(temp), color='blue', linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(out_path)


plot_regression(snakemake.input[0], snakemake.input[1], snakemake.output[0])
