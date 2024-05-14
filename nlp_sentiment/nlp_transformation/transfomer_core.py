from abc import ABC

import pandas as pd


class SentimentTransformer(ABC):
    def fit(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def transform(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame) -> pd.DataFrame:
        pass
