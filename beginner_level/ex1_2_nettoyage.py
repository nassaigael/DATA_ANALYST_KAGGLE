import numpy as np
import pandas as pd


def cleaning_numeric_columns(filename):
	df = pd.read_csv(filename)
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
	for col in cols_types_to_verify:
		print(df[col].describe())

	return True


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(cleaning_numeric_columns(file_to_test))
