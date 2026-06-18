import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

def print_stats(filename):
	from common_utils import cleaning_numeric_columns
	df = cleaning_numeric_columns(filename)
	price_average_after_discount = df["discounted_price"].mean().round(2)
	return price_average_after_discount

file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(print_stats(file_to_test))