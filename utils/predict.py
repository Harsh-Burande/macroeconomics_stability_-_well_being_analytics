import pandas as pd
import pickle


# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)


def predict_risk(input_dict):
    """
    Predict risk level from user input
    """

    # Convert input to DataFrame
    df = pd.DataFrame([input_dict])

    # KEEP ONLY TRAINED FEATURES
    df = df[[
        "Headline Consumer Price Inflation",
        "Freedom to make life choices",
        "Perceptions of corruption"
    ]]

    # Ensure numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.fillna(0)

    # Predict
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    # Feature importance
    importances = model.feature_importances_
    features = df.columns

    feature_importance = dict(zip(features, importances))

    return prediction[0], max(proba[0]), feature_importance