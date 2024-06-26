from project_nlp_example.modeling.model_A.model_A_sentiment_transformer import MyVeryDumbSentimentTransformer
from project_nlp_example.modeling.model_A.model_A_churn_estimator import MySimpleEstimator

from project_nlp_example.dataset import get_communications, get_dynamic_frame


def main():
    # Load data
    df_dynamic_frame_raw = get_dynamic_frame()
    df_communications = get_communications()

    df_target = df_dynamic_frame_raw[['CustomerId', 'yearmonth', 'Churn']]
    df_dynamic_frame = df_dynamic_frame_raw.drop('Churn', axis=1)

    # Set hyperparameters search space
    hyperparameters = {
        'sad_words': [
            ['sad', 'bad', 'unhappy'],
            ['sad', 'bad', 'unhappy', 'terrible'],
            ['sad', 'bad', 'unhappy', 'terrible', 'disappointed'],
        ],
        'alpha': [0.1, 0.5, 1.0, 2.0, 5.0]
    }

    best_hyperparameters = None
    best_score = None
    best_model = None

    # Iterate over the hyperparameters search space
    best_model, best_transformer, best_hyperparameters, best_score = do_hyperparameter_search(
        hyperparameters, df_communications, df_dynamic_frame, df_target
    )

    # Save the best model
    save_model(best_model, "model.pkl")
    save_model(best_transformer, "transformer.pkl")
    save_model(best_hyperparameters, "hyperparameters.pkl")


""" 
The `train_model_A.py` script is the entry point for the regularization pipeline. It loads the data, sets the 
hyperparameters search space, iterates over the hyperparameters search space, creates the model, fits the model, 
predicts the churn, evaluates the model, and saves the best model to a pickle file.
"""


def do_hyperparameter_search(hyperparameters, df_communications, df_dynamic_frame, df_target):
    # Implement your own hyperparameter search logic here
    best_hyperparameters = None
    best_score = None
    best_model = None
    best_transformer = None

    # There are smarter ways to do this, but this is just an example.
    for sad_words in hyperparameters['sad_words']:
        for alpha in hyperparameters['alpha']:
            # Create the model
            transformer = MyVeryDumbSentimentTransformer(sad_words=sad_words)
            classifier = MySimpleEstimator(alpha=alpha)

            # Transform the data
            transformer.fit(df_communications, df_dynamic_frame, df_target)
            df_data = transformer.transform(df_communications, df_dynamic_frame)

            # Fit the model
            classifier.fit(df_data, df_target)

            # Predict the churn
            df_predictions = classifier.predict(df_data)

            # Evaluate the model
            score = evaluate(df_predictions, df_target)

            # Save the best model
            if best_score is None or score > best_score:
                best_score = score
                best_hyperparameters = {'sad_words': sad_words, 'alpha': alpha}
                best_transformer = transformer
                best_model = classifier

    return best_model, best_transformer, best_hyperparameters, best_score


def evaluate(df_predictions, df_target):
    # Implement your own evaluation logic here
    raise NotImplementedError


def save_model(model, file_path):
    # Implement your own save model logic here
    raise NotImplementedError


if __name__ == "__main__":
    main()
