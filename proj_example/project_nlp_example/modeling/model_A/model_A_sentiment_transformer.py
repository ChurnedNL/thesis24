from abc import ABC

import pandas as pd


class SentimentTransformer(ABC):
    def fit(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame, df_target: pd.DataFrame) -> None:
        pass

    def transform(self, df_communications: pd.DataFrame, df_dynamic: pd.DataFrame) -> pd.DataFrame:
        pass


# # Data Description
# ## `communications`
# This table contains the communications exchanged between Customer Success Managers and their clients. The table contains the following columns:
# * `from`: hashed email address of the sender.
# * `to`: hashed email address of the recipient.
# * `is_inbound`: string indicating if the email is inbound or outbound (only available for some clients).
# * `communication_type`: type of communication (email, call, meeting, etc).
# * `date`: date of the email.
# * `customer_id`: Id of the customer. Use it to join with the `dynamic_frame` table.
# * `client` : Id of the client. Use it to join with the `dynamic_frame` table.
# * `yearmonth`: year and month of the communication. Use it to join with the `dynamic_frame` table.
# * `subject_replaced`: subject of the email.
# 	* The following terms represent words that have been redacted
# 		* words that match the pattern "ENTITY_\<TYPE\>" are named entities of the type "\<TYPE\>" (example: "ENTITY_PERSON", "ENTITY_CARDINAL")
# 		* "COMPANY_\<X\>": X is the client
# 		* "PRODUCT" are references to the client's product
# 		* "RARE" are rare words, usually proper names, removed for privacy reasons.
#
# ## `dynamic_frame`
# This table contains customer features, extra-communications aggregated by yearmonth. The table contains the following columns:
# * `DynamicDate`: End date of the aggregation period.
# * `CustomerId`: Id of the customer. Use it to join with the `communications` table.
# * `MrrCorrected`: Monthly Recurring Revenue.
# * `Tenure`: Number of months the customer has been with the company.
# * `Churn`: DO NOT USE. Calculated churn label. Use MaxExpirationDate to calculate churn.
# * `CustomerValue`: DO NOT USE.
# * `MinCreationDate`: Date of the first contract start.
# * `MaxExpirationDate`: Date of the last contract expiration.
# * `yearmonth`: year and month of the communication. Use it to join with the `communications` table.
# * `client` : Id of the client. Use it to join with the `communications` table.


class MyVeryDumbSentimentTransformer(SentimentTransformer):

    def __init__(self, customer_id_col='CustomerId', yearmonth_col='yearmonth', sad_words=None):
        self.customer_id_col = customer_id_col
        self.yearmonth_col = yearmonth_col
        self.sad_words = sad_words or ['sad', 'angry', 'disappointed', 'problem']

        # To be learned during the fit
        self.avg_communications_lift = None

    def fit(self, df_communications, df_dynamic, df_target) -> None:
        # Learn something from the data

        # For example, we could learn the average number of communications per customer per month of churners
        # (DF_TARGET['Churn']=1) vs non-churners (DF_TARGET['Churn']=0)
        df_communications_w_target = pd.merge(
            df_communications, df_target, on=[self.customer_id_col, self.yearmonth_col], how='inner'
        )
        avg_communications_churners = df_communications_w_target[
            df_communications_w_target['Churn'] == 1
        ].groupby([self.customer_id_col, self.yearmonth_col]).size().mean()
        avg_communications_non_churners = df_communications_w_target[
            df_communications_w_target['Churn'] == 0
        ].groupby([self.customer_id_col, self.yearmonth_col]).size().mean()

        self.avg_communications_lift = avg_communications_churners / avg_communications_non_churners

    def transform(self, df_communications, df_dynamic) -> pd.DataFrame:
        # Count the number of sad words in the subject of the communications
        df_communications['is_sad'] = df_communications['subject_replaced'].apply(
            lambda x: sum([1 for word in x.split() if word in self.sad_words])
        )

        # Merge the communications with the dynamic frame
        df = df_communications.merge(df_dynamic, on=[self.customer_id_col, self.yearmonth_col], how='inner')

        # Calculate the sentiment score
        df['sentiment'] = df['is_sad'] * self.avg_communications_lift

        # Group by customer and yearmonth and join the sentiment score with the dynamic frame
        df_agg = df.groupby([self.customer_id_col, self.yearmonth_col])['sentiment'].sum()

        df_dyn_w_sentiment = df_dynamic.merge(df_agg, on=[self.customer_id_col, self.yearmonth_col], how='left')

        return df_dyn_w_sentiment
