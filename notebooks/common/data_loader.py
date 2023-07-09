import pandas as pd


def get_ucr_label(df):
    return df[0].to_numpy()


def get_ucr_feature(df):
    return df.drop(columns=[0])


def get_ucr_training_data():
    df = pd.read_table("../data/UCRArchive_2018/Wafer/Wafer_TRAIN.tsv", header=None)
    return get_ucr_feature(df), get_ucr_label(df)


def get_ucr_test_data():
    df = pd.read_table("../data/UCRArchive_2018/Wafer/Wafer_TEST.tsv", header=None)
    return get_ucr_feature(df), get_ucr_label(df)