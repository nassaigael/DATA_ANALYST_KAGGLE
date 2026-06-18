import pandas as pd

from common import cleaning_numeric_columns


def print_stats(filename):
	df = pd.read_csv(filename)
	# df = cleaning_numeric_columns(df)
	price_average_after_discount = df["discounted_price"].mean().round(2)
	return price_average_after_discount

file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(print_stats(file_to_test))