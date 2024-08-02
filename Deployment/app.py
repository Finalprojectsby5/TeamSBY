import streamlit as st
import pandas as pd
from prediction import buat_prediksi
from eda import run as run_eda
import pickle
import numpy as np
from kmodes.kprototypes import KPrototypes

# Load the scaler and encoder
with open('scaler_cluster.pkl', 'rb') as file:
    scaler_cluster = pickle.load(file)
with open('model_pca.pkl', 'rb') as file:
    pca = pickle.load(file)
with open('cluster_model.pkl', 'rb') as file:
    kp = pickle.load(file)

def main():
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Select Page", ["Prediction", "EDA"])

    if menu == "Prediction":
        st.title("Credit Card Application Status Prediction")

        # Manual Input Form
        example_data = [{
            'gender': st.selectbox('Gender', ['M', 'F']),  # Ensure the categories match the encoder's
            'annual_income': st.number_input('Annual Income', value=50000),
            'type_income': st.selectbox('Type of Income', ['Working', 'Commercial associate', 'State servant', 'Pensioner', 'Student']),
            'education': st.selectbox('Education', ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary']),
            'marital_status': st.selectbox('Marital Status', ['Single / not married', 'Married', 'Civil marriage', 'Widow / Widower', 'Separated']),
            'housing_type': st.selectbox('Housing Type', ['House / apartment', 'Rented apartment', 'With parents', 'Municipal apartment', 'Office apartment', 'Co-op apartment']),
            'type_occupation': st.selectbox('Occupation', ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff', 'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff', 'Waiters/barmen staff', 'Low-skill Laborers', 'Realty agents', 'Secretaries']),
            'family_members': st.number_input('Family Members', value=1),
            'customer_age_years': st.number_input('Customer Age', value=35)
        }]

        if st.button('Predict'):
            df = pd.DataFrame(example_data)
            prediksi = buat_prediksi(df)
            
            # Replace 0 with "Yes" and 1 with "No"
            prediksi = ["Yes" if pred == 0 else "No" for pred in prediksi]
            st.write(prediksi[0])
            st.write(f'## Prediction Result:')
            df['label'] = prediksi[0]
            st.dataframe(df)
            num_columns =  ['annual_income', 'family_members', 'customer_age_years']
            cat_columns =  ['type_income', 'education', 'marital_status', 'housing_type', 'type_occupation', 'label']
            
            # Displaying approval message
            if prediksi[0] == "Yes":
                st.write("### Credit Card Application Status: Approved")
            else:
                st.write("## Credit Card Application Status: Rejected")
                customers_df_num = df[num_columns]
                customers_df_cat = df[cat_columns]
                num_scaled_df = scaler_cluster.transform(customers_df_num)
                customers_df_num_scaled_pca = pca.transform(num_scaled_df)
                customers_df_final = np.concatenate([customers_df_num_scaled_pca, customers_df_cat], axis=1)
                customers_df_final = pd.DataFrame(customers_df_final, columns=[['PCA1', 'PCA2','PCA3'] + cat_columns])
                customers_df_final = customers_df_final.infer_objects()
                index_cat_columns = [0, 1, 2, 3]
                pred = kp.predict(customers_df_final, categorical=index_cat_columns)
                st.write("### ini cluster no", str(pred[0]))

    elif menu == "EDA":
        st.title("Exploratory Data Analysis (EDA)")
        run_eda()

if __name__ == '__main__':
    main()
