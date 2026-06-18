import pandas as pd

def data_type_exploration(file_to_analyze):
	df = pd.read_csv(file_to_analyze)
	lines_count = len(df.index)
	cols_count = len(df.columns)
	cols_names_with_types = df.dtypes
	missing_values_with_columns = df.isnull().sum(),
	show = df.head(5)
	return {
		"lines_count": lines_count,
		"cols_count": cols_count,
		"cols_names_with_types": cols_names_with_types,
		"missing_values_with_columns": missing_values_with_columns,
		"show": show
	}


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(data_type_exploration(file_to_test))