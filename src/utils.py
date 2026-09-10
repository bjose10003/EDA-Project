"""Utility functions for the EDA project."""

import pandas as pd


def data_overview(df: pd.DataFrame) -> None:
    """Print a quick overview of a DataFrame."""
    print("Shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
