import os
import sys

import pandas as pd

from common_utils import cleaning_numeric_columns, load_data, extract_main_category

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def analyze_categories_comprehensive(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)

	analysis = pd.DataFrame({
		'Number of Products': df.groupby('main_category').size(),
		'Average Discounted Price': df.groupby('main_category')["discounted_price"].mean().round(2),
		'Average Discount (%)': df.groupby('main_category')["discount_percentage"].mean().round(2),
		'Average Rating': df.groupby('main_category')["rating"].mean().round(2)
	})

	analysis = analysis.sort_values('Number of Products', ascending=False)

	return analysis.head()


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"

result = analyze_categories_comprehensive(file_to_test)
print(result)
