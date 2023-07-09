from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalize(df, range=(-1,1)):
    scaler = MinMaxScaler(feature_range=range)
    df_normalized = pd.DataFrame(scaler.fit_transform(df.values.T).T, columns=df.columns)
    return df_normalized 