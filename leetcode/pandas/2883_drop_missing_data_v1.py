"""
 * 2883. Drop Missing Data (Answer v1)
 * Problem Link: https://leetcode.com/problems/drop-missing-data/
 * Solution Link (Personal):
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])