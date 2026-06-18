from utils import dataframe_clean


def get_all_products_with_rating_greater_or_equal_4(file_to_analyze):
	data = dataframe_clean(file_to_analyze)
	result = data[data["rating"] >= 4.5]
	return result["rating"]


def get_all_products_with_discount_greater_70(file_to_analyze):
	data = dataframe_clean(file_to_analyze)
	result = data[data["discount_percentage"] > 70]
	return result["discount_percentage"]


def get_all_products_with_discounted_price_less_200(file_to_analyze):
	data = dataframe_clean(file_to_analyze)
	result = data[data["discounted_price"] < 200]
	return result["discounted_price"].sort_values()


# Usage example
file_path = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(get_all_products_with_rating_greater_or_equal_4(file_path))
# print(get_all_products_with_discount_greater_70(file_path))
# print(get_all_products_with_discounted_price_less_200(file_path))
