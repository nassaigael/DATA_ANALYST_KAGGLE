from utils import dataframe_clean


def sort_product_by_rating_desc(file_to_sort):
	data = dataframe_clean(file_to_sort)
	result = data.sort_values(by=["rating"], ascending=False)
	return result["rating"]


def sort_product_by_discount_desc(file_to_sort):
	data = dataframe_clean(file_to_sort)
	result = data.sort_values(by=["discount_percentage"], ascending=False)
	return result["discount_percentage"]


def get_10_to_cheapest_products(file_to_sort):
	data = dataframe_clean(file_to_sort)
	result = data.sort_values(by=["actual_price"], ascending=True).head(10)
	return result[['product_name', 'rating', 'discount_percentage', 'discounted_price', ]]


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(sort_product_by_rating_desc(file_to_test))
print(sort_product_by_discount_desc(file_to_test))
print(get_10_to_cheapest_products(file_to_test))
