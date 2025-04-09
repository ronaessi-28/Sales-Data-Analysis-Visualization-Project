
import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Convert to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

    # Drop unused columns
    if 'Row ID' in df.columns:
        df.drop(['Row ID', 'Postal Code'], axis=1, inplace=True)

    # Feature engineering
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Day'] = df['Order Date'].dt.day

    return df
