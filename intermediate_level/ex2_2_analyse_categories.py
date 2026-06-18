import os
import sys


from common_utils import cleaning_numeric_columns, load_data, extract_main_category

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

def products_totals_by_main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)

	return df.groupby('main_category').sum()

def average_discounted_price_by_main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df.groupby('main_category')["discounted_price"].mean().round(2)

def average_discount_by_main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df.groupby('main_category')["discount_percentage"].mean().round(2)

def average_rating_by_main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df.groupby('main_category')["rating"].mean().round(2)

# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(products_totals_by_main_category(file_to_test))
print(average_discounted_price_by_main_category(file_to_test))
print(average_discount_by_main_category(file_to_test))
print(average_rating_by_main_category(file_to_test))