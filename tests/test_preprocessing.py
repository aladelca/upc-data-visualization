import pandas as pd

from notebooks.preprocessing import add_lag_features


def test_add_lag_features_calculates_global_lags_using_date_order():
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(["2024-01-03", "2024-01-01", "2024-01-02"]),
            "sales": [30, 10, 20],
        }
    )

    result = add_lag_features(
        df,
        date_column="date",
        value_columns="sales",
        lags=[1, 2],
    )

    pd.testing.assert_series_equal(
        result["sales_lag_1"],
        pd.Series([20.0, None, 10.0], name="sales_lag_1"),
    )
    pd.testing.assert_series_equal(
        result["sales_lag_2"],
        pd.Series([10.0, None, None], name="sales_lag_2"),
    )


def test_add_lag_features_calculates_grouped_lags_per_series():
    df = pd.DataFrame(
        {
            "store": ["A", "A", "B", "B"],
            "date": pd.to_datetime(["2024-01-02", "2024-01-01", "2024-01-02", "2024-01-01"]),
            "sales": [110, 100, 210, 200],
        }
    )

    result = add_lag_features(
        df,
        date_column="date",
        value_columns="sales",
        lags=1,
        group_columns="store",
    )

    pd.testing.assert_series_equal(
        result["sales_lag_1"],
        pd.Series([100.0, None, 200.0, None], name="sales_lag_1"),
    )
