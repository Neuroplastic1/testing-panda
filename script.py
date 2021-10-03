# Cleaning and visualizing with Pandas, matplotlib and seaborn
import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# to understand if a user’s location is correlated to their age by using a histogram to visualize the distribution of all of the ages in the dataset
#histogram code:

age = new_df["age"]
sns.displot(age)
 
plt.show() 

# now that we have a sense of the age distribution of our user base, let’s see if there is a relationship between a user’s age and their location.
# mean age location code:
location_mean_age = new_df.groupby("location").age.mean() 
 
print(location_mean_age)

# visualize the means using a barplot:
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
    y= "age"
)
plt.show()

#Other visualizations provide other information about the relationship between age and location. For example, a violin plot shows distributions of age like a histogram, but creates separate distributions for each category.
# violinplot code:
plt.close()
sns.violinplot(x="location", y="age", data=new_df)
 
plt.show()
