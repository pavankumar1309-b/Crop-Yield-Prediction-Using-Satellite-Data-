import pandas as pd

def preprocess_data(crop_data_path, weather_data_path):
    crop_df = pd.read_csv(crop_data_path)
    weather_df = pd.read_csv(weather_data_path)
    df = pd.merge(crop_df, weather_df, on='date')
    return df.dropna()
