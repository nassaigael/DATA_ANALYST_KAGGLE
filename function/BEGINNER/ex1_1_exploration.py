import pandas as pd


def get_cols_and_rows_numbers(file_to_analyze):
    df = pd.read_csv(file_to_analyze)
    cols_count = 0
    for col in df:
        cols_count += 1
    return {
        'rows_count': len(df),
        'cols_count': df.columns.count(),
    }


def get_all_names_and_types_cols(file_to_analyze):
    df = pd.read_csv(file_to_analyze)
    return df.dtypes.to_dict()


def get_all_missing_values_and_columns(file_to_analyze):
    df = pd.read_csv(file_to_analyze)
    return df.isnull().sum().to_dict()


def print_five_first_row(file_to_analyze):
    df = pd.read_csv(file_to_analyze)
    return df.head(5)


# Usage example
file_path = "/data/DATA_01.csv"
