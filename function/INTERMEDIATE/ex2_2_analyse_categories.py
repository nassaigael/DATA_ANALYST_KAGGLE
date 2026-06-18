from function.INTERMEDIATE.utils.ex2_1_categories import create_new_cols_category


def analyze_categories(file_to_analyze):
    data = create_new_cols_category(file_to_analyze)
    return data

# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(analyze_categories(file_to_test))
