from src.utils import BaseClass
import pandas as pd


class ReadData(BaseClass):
    def __init__(self, dataset_path, **kwargs):
        self.dataset_path = dataset_path
        self.file_type = os
        self.extra_args = kwargs.get("extra_args", None) if isinstance(kwargs.get("extra_args", None), dict) else None
    
    def get_pandas_df(self):
        try:
            if self.extra_args:
                data = pd.read_csv(self.dataset_path, **self.extra_args)
            else:
                data = pd.read_csv(self.dataset_path)
        except Exception as e:
            print(f"Unable to read file due to {e}")
            return -1
        return data