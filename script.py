import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# print code:
print(user_data.head(17))

# merge code:
new_df = pd.merge(user_data, pop_data)

# Paste location code here:
print(new_df.head(15))

# create and populate a new location column, based on how a user’s location is classified
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# print code:
print(new_df.head(15))
