import matplotlib.pyplot as plt

from utils import dataframe_clean


def create_new_cols_category(file_to_analyse):
	data = dataframe_clean(file_to_analyse)
	data["main_category"] = data["category"].str.split("|").str[0]
	return data


def get_numbers_main_category(file_to_analyse):
	data = create_new_cols_category(file_to_analyse)
	result = data["main_category"].nunique()
	return result


def plot_top_10_categories(file_to_analyse):
	data = create_new_cols_category(file_to_analyse)
	top_10 = data["main_category"].value_counts().head(10)
	plt.figure(figsize=(10, 5))
	top_10.plot(kind="bar", color="royalblue", edgecolor="gray")
	plt.title("Top 10 categories")
	plt.xlabel("Category")
	plt.ylabel("Number of categories")
	plt.tight_layout()
	plt.show()
	return top_10


if __name__ == "__main__":
	file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"

	print("--- Affichage du DataFrame ---")
	print(create_new_cols_category(file_to_test))

	print("\n--- Nombre de catégories uniques ---")
	print(get_numbers_main_category(file_to_test))

	print("\n--- Génération du graphique ---")
	plot_top_10_categories(file_to_test)
