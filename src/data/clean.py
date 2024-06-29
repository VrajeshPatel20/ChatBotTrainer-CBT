from src.utils import BaseClass

class CleanData(BaseClass):
    def __init__(self, dataset_path, **kwargs):
        if not dataset_path:
            raise ValueError("Dataset path cannot be none")
        self.dataset_path = dataset_path
        self.remove_partial_nulls = kwargs.get("remove_partial_nulls", None)
        self.columns_to_snake_case = kwargs.get("columns_to_snake_case", None)
    
    