import pandas as pd

def read_ssf_csv(fname):

    df = pd.read_csv(fname).drop('No.', axis=1)
    df.columns = [ col.strip() for col in df.columns ]

    return df
