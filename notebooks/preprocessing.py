from __future__ import annotations

from collections.abc import Sequence

import numpy as np
import pandas as pd


def final_merge(
    products: pd.DataFrame,
    product_subcategory: pd.DataFrame,
    product_category: pd.DataFrame,
) -> pd.DataFrame:
    df_final = products.merge(
        product_subcategory.rename(columns={"Name": "subcategory_name"}).drop(
            columns=["ModifiedDate", "rowguid"]
        ),
        on="ProductSubcategoryID",
        how="left",
    ).merge(
        product_category.rename(columns={"Name": "category_name"}).drop(
            columns=["ModifiedDate", "rowguid"]
        ),
        on="ProductCategoryID",
        how="left",
    )
    return df_final


def add_lag_features(
    df: pd.DataFrame,
    *,
    date_column: str,
    value_columns: str | Sequence[str],
    lags: int | Sequence[int],
    group_columns: str | Sequence[str] | None = None,
) -> pd.DataFrame:
    if date_column not in df.columns:
        raise KeyError(f"Column '{date_column}' was not found in the dataframe.")

    normalized_value_columns = [value_columns] if isinstance(value_columns, str) else list(value_columns)
    normalized_group_columns = (
        []
        if group_columns is None
        else [group_columns] if isinstance(group_columns, str) else list(group_columns)
    )
    normalized_lags = [lags] if isinstance(lags, int) else list(lags)

    if not normalized_value_columns:
        raise ValueError("At least one value column is required.")
    if not normalized_lags:
        raise ValueError("At least one lag value is required.")
    if any(lag <= 0 for lag in normalized_lags):
        raise ValueError("Lag values must be positive integers.")

    required_columns = {date_column, *normalized_value_columns, *normalized_group_columns}
    missing_columns = sorted(required_columns.difference(df.columns))
    if missing_columns:
        missing_as_text = ", ".join(missing_columns)
        raise KeyError(f"Missing required columns: {missing_as_text}.")

    working_df = df.copy()
    working_df["_original_order"] = np.arange(len(working_df))
    working_df = working_df.sort_values([*normalized_group_columns, date_column], kind="mergesort")

    for lag in sorted(set(normalized_lags)):
        for value_column in normalized_value_columns:
            lag_column = f"{value_column}_lag_{lag}"
            if normalized_group_columns:
                working_df[lag_column] = working_df.groupby(
                    normalized_group_columns,
                    sort=False,
                )[value_column].shift(lag)
            else:
                working_df[lag_column] = working_df[value_column].shift(lag)

    working_df = working_df.sort_values("_original_order", kind="mergesort")
    return working_df.drop(columns="_original_order")
