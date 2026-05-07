import pandas as pd
import numpy as np


def create_features(df):
    """
    Apply feature engineering to the dataset.
    This function must be used BOTH during training and prediction.
    """

    # 1. Sort data (VERY IMPORTANT)
    df = df.sort_values(['Country', 'Year']).copy()

    # 2. Previous Year Inflation
    df['previous_year_inflation'] = df.groupby('Country')['Headline Consumer Price Inflation'].shift(1)
    df['previous_year_inflation'] = df['previous_year_inflation'].fillna(0)

    # 3. Inflation Change
    df['Inflation_change'] = df['Headline Consumer Price Inflation'] - df['previous_year_inflation']

    # 4. Inflation Volatility (std of change per country)
    df['Inflation_volatility'] = df.groupby('Country')['Inflation_change'].transform(lambda x: x.std())
    df['Inflation_volatility'] = df['Inflation_volatility'].fillna(0)

    # 5. Rolling Average (3-year trend)
    df['inflation_rolling_average'] = df.groupby('Country')['Headline Consumer Price Inflation'] \
                                        .transform(lambda x: x.rolling(window=3).mean())

    # Fill initial NaNs using backfill
    df['inflation_rolling_average'] = df['inflation_rolling_average'].bfill()

    return df
