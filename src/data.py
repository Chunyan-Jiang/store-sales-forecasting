"""Load and merge all raw data tables."""
import pandas as pd
from config import DATA_RAW


def load_train() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "train.csv")
    return data

def load_test() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "test.csv")
    return data


def load_stores() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "stores.csv")
    return data


def load_oil() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "oil.csv")
    return data


def load_holidays() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "holidays_events.csv")
    return data


def load_transactions() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW / "transactions.csv")
    return data


def build_base_table(is_train: bool = True) -> pd.DataFrame:
    """Merge train/test with all auxiliary tables into one flat DataFrame."""
    pass