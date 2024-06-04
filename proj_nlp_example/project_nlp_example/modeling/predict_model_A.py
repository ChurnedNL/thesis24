from proj_nlp_example.project_nlp_example.dataset import load_data, get_latest_data


def main():
    # Load trained models from pickle files

    trained_transformer = load_model("transformer.pkl")
    trained_model = load_model("model.pkl")

    # Load the data to predict
    df_dynamic_frame = load_data("data.csv")
    df_communications = load_data("communications.csv")

    # Get the latest rows of the dynamic frame to predict the churn
    df_data = get_latest_data(df_dynamic_frame)

    # Transform the data
    df_data = trained_transformer.transform(df_communications, df_data)

    # Predict the churn
    df_predictions = trained_model.predict(df_data)

    return df_predictions


'''
The `prediction_script.py` script is the entry point for the prediction pipeline. It loads the prediction data, loads the trained model from a pickle file, predicts the churn using the trained model, and saves the predictions to a CSV file.

The script follows these steps:

1. Load the prediction data from a CSV file.
2. Load the trained model from a pickle file using the `load_model` function.
3. Predict the churn using the trained model by calling the `predict` method of the model.
4. Save the predictions to a CSV file named `predictions.csv`.

'''


def load_model(file_path):
    raise NotImplementedError


if __name__ == "__main__":
    main()
