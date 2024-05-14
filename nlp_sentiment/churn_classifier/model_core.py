from abc import ABC

import pandas as pd


class ChurnEstimator(ABC):
    def fit(self, df_dynamic_w_sentiment: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def predict(self, df_dynamic_w_sentiment: pd.DataFrame) -> pd.DataFrame:
        pass
