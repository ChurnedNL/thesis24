from abc import ABC

import pandas as pd


class ChurnEstimator(ABC):
    def fit(self, df_dynamic_w_sentiment: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def predict(self, df_dynamic_w_sentiment: pd.DataFrame) -> pd.DataFrame:
        pass


class MySimpleEstimator(ChurnEstimator):

    def __init__(self, customer_id_col='CustomerId', yearmonth_col='yearmonth', sentiment_col='sentiment', alpha=1.0, target_col='Churn'):
        self.customer_id_col = customer_id_col
        self.yearmonth_col = yearmonth_col
        self.sentiment_col = sentiment_col
        self.target_col = target_col
        self.alpha = alpha
        self.threshold = None  # To be learned during the fit
        self.sentiment_threshold = None  # To be learned during the fit

    def fit(self, df_dynamic_w_sentiment, df_target) -> None:
        # Learn the churn threshold
        self.threshold = df_target[self.target_col].mean()
        # Learn the sentiment threshold
        self.sentiment_threshold = df_dynamic_w_sentiment[self.sentiment_col].mean()
        # Make sure the sentiment threshold is less than alpha
        self.sentiment_threshold = min(self.sentiment_threshold, self.alpha)

    def predict(self, df_dynamic_w_sentiment) -> pd.DataFrame:
        if self.threshold is None:
            raise Exception("You should call the fit method first")
        # Predict the churn based on the sentiment score
        df = df_dynamic_w_sentiment.copy()
        df['ChurnPrediction'] = (df[self.sentiment_col] > self.sentiment_threshold).astype(int)

        return df[[self.customer_id_col, self.yearmonth_col, 'ChurnPrediction']]
