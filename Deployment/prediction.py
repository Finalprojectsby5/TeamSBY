import pandas as pd
import pickle
import numpy as np

# Load the trained AdaBoost model
with open('adaboost_logreg_best.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler and encoder
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

def buat_prediksi(data):
    df = pd.DataFrame(data)

    # Ensure all features are in the correct order
    feature_order = ['gender', 'annual_income', 'type_income', 'education', 'marital_status', 'housing_type', 'type_occupation', 'family_members', 'customer_age_years']
    df = df[feature_order]

    # Separate numerical and categorical features
    df_num = df.select_dtypes(include=[np.number])
    df_cat = df.select_dtypes(include=['object'])

    # Ensure the input categories are known to the encoder
    for col in df_cat.columns:
        df_cat[col] = pd.Categorical(df_cat[col], categories=encoder.categories_[df_cat.columns.get_loc(col)])

    # Apply the scaler and encoder
    df_num_scaled = scaler.transform(df_num)
    df_cat_encoded = encoder.transform(df_cat).toarray()

    # Concatenate scaled numerical features and encoded categorical features
    X = np.concatenate([df_num_scaled, df_cat_encoded], axis=1)

    # Make prediction using AdaBoost model
    prediction = model.predict(X)
    return prediction
