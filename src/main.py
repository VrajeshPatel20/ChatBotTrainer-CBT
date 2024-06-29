from src.utils import BaseClass

class TrainAndTestBot(BaseClass):
    def __init__(self, dataset_path, **kwargs):
        if not dataset_path:
            raise ValueError("Dataset path cannot be none")
        self.dataset_path = dataset_path    