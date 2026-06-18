import os
import sys

import matplotlib.pyplot as plt

from common_utils import cleaning_numeric_columns, load_data, extract_main_category

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def main_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df


def count_news_category(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)
	return df.groupby("main_category").nunique()


def analyze_categories(filename: str):
	df = load_data(filename)
	df = cleaning_numeric_columns(df)
	df = extract_main_category(df)

	distinct_count = df["main_category"].nunique()
	print(f"\n Nombre de catégories principales distinctes: {distinct_count}\n")

	top_10 = df["main_category"].value_counts().head(10)
	print(" Top 10 des catégories par nombre de produits:")
	print(top_10)
	print()

	plt.figure(figsize=(12, 6))
	top_10.plot(kind="bar", color="steelblue", edgecolor="black")
	plt.title("Top 10 des Catégories Principales par Nombre de Produits", fontsize=14, fontweight="bold")
	plt.xlabel("Catégorie Principale", fontsize=12)
	plt.ylabel("Nombre de Produits", fontsize=12)
	plt.xticks(rotation=45, ha="right")
	plt.grid(axis="y", alpha=0.3)
	plt.tight_layout()
	plt.show()

	return df


# Usage example
file_to_test = "E:/DATA_ANALYST_KAGGLE/data/DATA_01.csv"
print(main_category(file_to_test))
print(count_news_category(file_to_test))
analyze_categories(file_to_test)
