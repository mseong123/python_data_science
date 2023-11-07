import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load csv and return panda DataFrame"""
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Exception:{e}")
    else:
        print(f"Loading dataset of dimensions ({len(df)}, {len(df.columns)})")
        df = df.set_index('country')
        return df
