import os
import sys

from common_utils import cleaning_numeric_columns, load_data

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def print_stats(path):
	df = load_data(path)
	df = cleaning_numeric_columns(df)
	price_average_after_discount = df["discounted_price"].mean().__round__(2)
	average_discount_percentage = df["discount_percentage"].mean().__round__(2)
	average_rating = df["rating"].mean().__round__(2)
	cheapest_product = df.loc[df["discounted_price"].idxmax(), "discounted_price"]
	less_product = df.loc[df["discounted_price"].idxmin(), "discounted_price"]

	return price_average_after_discount, average_discount_percentage, average_rating, cheapest_product, less_product

file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
a, b, c, d, e = print_stats(file_to_test)
print(f"a = {a}$, b = {b}$, c = {c}, d = {d}$, e = {e}$")
