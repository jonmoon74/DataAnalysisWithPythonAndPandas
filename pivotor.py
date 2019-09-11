import pandas as pd
import numpy as np


def pivot(infile="Concatenated-Merged.csv", outfile="Pivoted.csv"):
    df = pd.read_csv(infile)
    df = df.replace(-9999, np.nan)
    df["Temp"] = df["Temp"] / 10.0
    table = pd.pivot_table(df, index=["ID"], columns="Year", values="Temp")
    table.to_csv(outfile)


pivot()
