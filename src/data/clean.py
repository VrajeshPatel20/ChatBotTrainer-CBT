from src.utils import BaseClass
from src.data.read import ReadData
import pandas as pd

class CleanData(BaseClass):
    def __init__(self, **kwargs):
        self.remove_partial_nulls = kwargs.get("remove_partial_nulls", None)
        self.columns_to_snake_case = kwargs.get("columns_to_snake_case", None)
    
    def drop_null_values(self, df: pd.DataFrame , columns: list | str, **kwargs):
        """
        Drops rows with null values from a certain column
        """
        if isinstance(columns, str):
            columns = [columns]
        df = df.dropna(subset = columns, inplace = kwargs.get("inplace",True))
        return df