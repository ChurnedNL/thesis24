from abc import ABC, abstractmethod

import pandas as pd


class SentimentTransformer(ABC):
    def fit(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def transform(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame) -> pd.DataFrame:
        pass


class ChurnEstimator(ABC):
    def fit(self, df_dynamic_w_sentiment: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def predict(self, df_dynamic_w_sentiment: pd.DataFrame) -> pd.DataFrame:
        pass

