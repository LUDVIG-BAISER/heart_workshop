import pandas as pd
def prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].map({
            '1': 1,
            'Male': 1,
            '0': 0,
            'Female': 0
        }).astype(float)
    return df