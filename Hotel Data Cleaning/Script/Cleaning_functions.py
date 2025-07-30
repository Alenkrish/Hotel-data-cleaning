import pandas as pd
import numpy as np

def load_dataset(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def handle_missing_values(df):
    """Handle missing values in key columns."""
    df['children'].fillna(0, inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    df['country'].fillna(df['country'].mode()[0], inplace=True)
    return df

def remove_duplicates(df):
    """Remove duplicate records from the dataset."""
    return df.drop_duplicates()

def handle_outliers(df):
    """Treat outliers using the IQR method."""
    def cap_outliers(col):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] < lower, lower, np.where(df[col] > upper, upper, df[col]))
    
    outlier_columns = ['lead_time', 'adr', 'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children', 'babies']
    for col in outlier_columns:
        cap_outliers(col)
    
    return df

def fix_inconsistencies(df):
    """Fix logical and format inconsistencies."""
    # Remove rows where there are no guests
    df = df[(df['adults'] + df['children'] + df['babies']) > 0]
    # Convert date columns if needed
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    return df

def clean_dataset(file_path):
    """Full cleaning pipeline."""
    df = load_dataset(file_path)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = handle_outliers(df)
    df = fix_inconsistencies(df)
    return df

def save_cleaned_dataset(df, output_path):
    """Save cleaned dataset to CSV."""
    df.to_csv(output_path, index=False)
