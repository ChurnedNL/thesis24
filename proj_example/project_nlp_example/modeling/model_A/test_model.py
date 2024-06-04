import pandas as pd

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

from project_nlp_example.modeling.model_A.model_A_churn_estimator import MySimpleEstimator
from project_nlp_example.modeling.model_A.model_A_sentiment_transformer import MyVeryDumbSentimentTransformer

DF_COMMUNICATIONS = pd.DataFrame(
    {
        "customer_id": [1, 1, 1],
        "yearmonth": ["2021-01-01", "2021-04-01", "2021-07-01"],
        "from": ["a", "a", "a"],
        "to": ["b", "b", "b"],
        "is_inbound": ["yes", "yes", "yes"],
        "communication_type": ["email", "email", "email"],
        "date": ["2021-01-01", "2021-04-02", "2021-07-03"],
        "client": ["A", "A", "A"],
        "subject_replaced": ["Re: welcome", "Product is awesome", "Problems during onboarding: RARE comments"],
    }
)

DF_DYNAMIC = pd.DataFrame(
    {
        "DynamicDate": ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-01", "2021-06-01", "2021-07-01"],
        "CustomerId": [1, 1, 1, 1, 1, 1, 1],
        "MrrCorrected": [100, 100, 100, 100, 100, 100, 100],
        "Tenure": [1, 2, 3, 4, 5, 6, 7],
        "CustomerValue": [100, 100, 100, 100, 100, 100, 100],
        "yearmonth": ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-01", "2021-06-01", "2021-07-01"],
        "client": ["A", "A", "A", "A", "A", "A", "A"],
    }
)

DF_TARGET = pd.DataFrame(
    {
        "CustomerId": [1, 1, 1, 1, 1, 1, 1],
        "yearmonth": ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-01", "2021-06-01", "2021-07-01"],
        "Churn": [0, 0, 0, 0, 1, 1, 1],
    }
)


DF_DYNAMIC_W_SENTIMENT = pd.DataFrame(
    {
        "DynamicDate": ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-01", "2021-06-01", "2021-07-01"],
        "CustomerId": [1, 1, 1, 1, 1, 1, 1],
        "MrrCorrected": [100, 100, 100, 100, 100, 100, 100],
        "Tenure": [1, 2, 3, 4, 5, 6, 7],
        "CustomerValue": [100, 100, 100, 100, 100, 100, 100],
        "yearmonth": ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-01", "2021-06-01", "2021-07-01"],
        "client": ["A", "A", "A", "A", "A", "A", "A"],
        "sentiment": [0, 0, 1, 0, 0, 0, 1],
    }
)


def test_transformer():
    df_communications = DF_COMMUNICATIONS.rename(columns={'customer_id': 'CustomerId'})
    transformer = MyVeryDumbSentimentTransformer()

    transformer.fit(df_communications, DF_DYNAMIC, DF_TARGET)
    res = transformer.transform(df_communications, DF_DYNAMIC)


def test_estimator():
    estimator = MySimpleEstimator()
    estimator.fit(DF_DYNAMIC_W_SENTIMENT, DF_TARGET)
    y_pred = estimator.predict(DF_DYNAMIC_W_SENTIMENT)

