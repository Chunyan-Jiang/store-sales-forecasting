"""Load and merge all raw data tables."""
import pandas as pd
from config import DATA_RAW


def load_train() -> pd.DataFrame:
    data = pd.read_csv(DATA_RAW['train'])
    return data

def load_test() -> pd.DataFrame:
    pass


def load_stores() -> pd.DataFrame:
    pass


def load_oil() -> pd.DataFrame:
    pass


def load_holidays() -> pd.DataFrame:
    pass


def load_transactions() -> pd.DataFrame:
    pass


def build_base_table(is_train: bool = True) -> pd.DataFrame:
    """Merge train/test with all auxiliary tables into one flat DataFrame."""
    pass