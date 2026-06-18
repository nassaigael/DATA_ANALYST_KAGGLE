from utils import dataframe_clean


def get_average_price_after_discount(file_to_analyze):
    data = dataframe_clean(file_to_analyze)
    return data["discounted_price"].mean().round(2)


def get_average_discount_percentage(file_to_analyze):
    data = dataframe_clean(file_to_analyze)
    return data["discount_percentage"].mean().round(2)


def get_average_rating(file_to_analyze):
    data = dataframe_clean(file_to_analyze)
    return data["rating"].mean().round(2)


def get_less_and_most_expensive_product(file_to_analyze):
    data = dataframe_clean(file_to_analyze)
    most_expensive_product = data.loc[data["discounted_price"].idxmax(), "product_id"]
    less_expensive_product = data.loc[data["discounted_price"].idxmin(), "product_id"]
    return {
        "most_expensive_product": most_expensive_product,
        "less_expensive_product": less_expensive_product
    }


file_path = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"

print(get_less_and_most_expensive_product(file_path))
