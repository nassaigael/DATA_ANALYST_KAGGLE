import os
import sys

from common_utils import cleaning_numeric_columns, load_data, extract_main_category

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

def main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df

# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(main_category(file_to_test))