import pandas as pd


def clean_data(file_to_analyze):
    df = pd.read_csv(file_to_analyze)
    cols = ["discounted_price", "actual_price", "discount_percentage", "rating_count", "rating"]

    for col in cols:
        df[col] = df[col].replace({
            '%': '',
            ',': '',
            '₹': ''
        }, regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce', downcast='float')
        if df[col].dtypes != "float32":
            print(f"[ERROR] {col} is not numeric this is {df[col].dtypes}")
    return df
