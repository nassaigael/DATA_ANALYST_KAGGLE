import os
import sys

from common_utils import cleaning_numeric_columns, load_data

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def sort_by_rating_desc(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	return df.sort_values(by=['rating'], ascending=False)


def sort_by_discount(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	return df.sort_values(by=['discount_percentage'], ascending=False)


def print_top_10_cheapest_products(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	columns_to_show = ["product_name", "rating", "discounted_price", "discount_percentage"]
	df = df.sort_values(by=["discounted_price"], ascending=False).head(10)[columns_to_show]
	return df


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(sort_by_rating_desc(file_to_test)["rating"].to_string())
print(sort_by_discount(file_to_test)["discount_percentage"].to_string())
print(print_top_10_cheapest_products(file_to_test))
