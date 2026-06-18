import numpy as np
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def cleaning_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    from pandas.errors import EmptyDataError
    try :
        df = df.copy()
        df["discounted_price"] = (df["discounted_price"].str.replace(",", "")
                                  .str.replace("₹", "").astype(float))
        df["actual_price"] = (df["actual_price"].str.replace(",", "")
                              .str.replace("₹", "").astype(float))
        df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)
        df["rating"] = df["rating"].astype(float)
        df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)

        cols_types_to_verify = ["discounted_price", "actual_price", "discount_percentage", "rating", "rating_count"]
        for col in cols_types_to_verify:
            if col not in df.columns:
                print(col + " is not present in the dataframe")
                return False
            if df[col].dtype != np.float64:
                print(col + " is not numeric")
                return False
        return df
    except FileNotFoundError:
        return "This file doesn't exist on disk"
    except EmptyDataError:
        return "This file is empty on disk"
    except Exception as e:
        return e


def extract_main_category(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["main_category"] = df["category"].str.split("|").str[0]
    return df


def calculate_popularity_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["popularity_score"] = df["rating"] * np.log10(df["rating_count"] + 1)
    return df
