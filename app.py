import streamlit as st
import pandas as pd
from eda import run_eda
from data_processing import clean_data, feature_engineering
from ml import train_model, evaluate_model
from utils import load_data, save_report

def main():
    st.title("DataExplorer: Automated EDA & ML Workflow")

    # File uploader for CSV or Excel
    data_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx", "xls"])
    if data_file:
        df = load_data(data_file)
        st.write("### Raw Data Preview", df.head())

        # Run automated cleaning
        if st.sidebar.checkbox("Auto Clean Data", value=True):
            df = clean_data(df)
            st.write("### Cleaned Data Preview", df.head())

        # Feature engineering
        if st.sidebar.checkbox("Feature Engineering"):
            df = feature_engineering(df)
            st.write("### After Feature Engineering", df.head())

        # Run EDA
        if st.sidebar.button("Run EDA"):
            run_eda(df)

        # ML Model Selection
        st.sidebar.header("Model Training & Evaluation")
        target = st.sidebar.selectbox("Select Target Column", options=df.columns)
        features = st.sidebar.multiselect("Select Feature Columns", options=[c for c in df.columns if c != target])
        model_name = st.sidebar.selectbox("Choose ML Model", ["Logistic Regression", "Decision Tree", "Random Forest", "KNN"])
        test_size = st.sidebar.slider("Test Set Size (%)", min_value=10, max_value=50, value=20)
        run_ml = st.sidebar.button("Train & Evaluate Model")

        if run_ml:
            if not features:
                st.error("Please select at least one feature column")
            else:
                X = df[features]
                y = df[target]
                metrics, model = train_model(X, y, model_name, test_size/100)
                evaluate_model(metrics)

                # Optionally save report
                if st.sidebar.checkbox("Download Report"):
                    save_report(df, metrics, model_name)

if __name__ == "__main__":
    main()
