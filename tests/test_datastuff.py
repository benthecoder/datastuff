import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from datastuff import __version__, missing_vals


def test_version():
    assert __version__ == "0.1.0"


def test_missing_vals():
    df = {
        "id": [1, 2, 3, 4, 5],
        "created_at": [
            "2020-02-01",
            "2020-02-02",
            "2020-02-02",
            "2020-02-02",
            "2020-02-03",
        ],
        "color": ["red", np.NaN, "blue", "blue", "yellow"],
    }

    df = pd.DataFrame(df, columns=["id", "created_at", "color", "missing_col"])

    missing_df = missing_vals(df)
    missing_df_expected = pd.DataFrame(
        {"counts": [5, 1], "percentage": [100.0, 20.0]}
    ).set_index(pd.Index(["missing_col", "color"]))

    assert_frame_equal(missing_df, missing_df_expected)


def test_missing_vals_drop():
    df = {
        "id": [1, 2, 3, 4, 5],
        "created_at": [
            "2020-02-01",
            "2020-02-02",
            "2020-02-02",
            "2020-02-02",
            "2020-02-03",
        ],
        "color": ["red", np.NaN, "blue", "blue", "yellow"],
    }

    df = pd.DataFrame(df, columns=["id", "created_at", "color", "missing_col"])

    missing_df = missing_vals(df, drop=True)
    df_expected = df.drop("missing_col", axis=1)

    assert_frame_equal(missing_df, df_expected)
