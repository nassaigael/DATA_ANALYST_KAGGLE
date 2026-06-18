import pandas as pd

from beginner_level.ex1_2_nettoyage import cleaning_numeric_columns


def print_stats(df):
	df = cleaning_numeric_columns(df)
