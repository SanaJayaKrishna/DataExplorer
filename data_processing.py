import pandas as pd
from sklearn.impute import SimpleImputer

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the DataFrame by imputing missing values with the mean."""
    for col in df.columns:
        if df[col].isnull().any():
            imputer = SimpleImputer(strategy='mean')
            df[col] = imputer.fit_transform(df[[col]]).ravel()
    return df


def feature_engineering(df):
    # Example: add basic features like interaction terms or polynomials if needed
    # For demo, just return df as is
    return df
