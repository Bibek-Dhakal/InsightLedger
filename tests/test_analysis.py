import pandas as pd
from scipy import stats


def test_pandas_loaded():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert len(df) == 2
    assert "a" in df.columns


def test_scipy_stats_available():
    # Simple sanity test for scipy
    chi2_stat, p_val = stats.chisquare([500, 500], [500, 500])
    assert p_val == 1.0
