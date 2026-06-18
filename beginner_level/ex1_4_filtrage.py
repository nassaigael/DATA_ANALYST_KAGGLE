import os
import sys

from common_utils import cleaning_numeric_columns, load_data

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def filter_by_rating_and_discount_percentage_and_price(path: str):
	df = load_data(path)
	df = cleaning_numeric_columns(df)
	product_with_rate_less_4 = df[df["rating"] >= 4.5]
	product_with_discount_greater_70 = df[df["discount_percentage"] > 70]
	product_with_discounted_price_less_200 = df[df["discounted_price"] < 200]
	return {
		"length rating >= 4.5": len(product_with_rate_less_4),
		"length discount > 70": len(product_with_discount_greater_70),
		"length discounted price > 200": len(product_with_discounted_price_less_200),
	}


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(filter_by_rating_and_discount_percentage_and_price(file_to_test))
