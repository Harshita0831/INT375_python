import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt   
import seaborn as sns  

#LOADING DATASET
df = pd.read_csv(r'C:\Users\Harshita\Downloads\air_qual.csv')
print(df) #printing dataset

#Exploring Dataset
print("Information of the Dataset: \n",df.info())
print("Illustration of Dataset: \n",df.describe())

#Handling missing values
print("Missing values in dataset: \n",df.isnull().sum())

df["pollutant_min"] = df["pollutant_min"].fillna(df["pollutant_min"].mean())
df["pollutant_max"] = df["pollutant_max"].fillna(df["pollutant_max"].median())
df["pollutant_avg"] = df["pollutant_avg"].fillna(df["pollutant_avg"].mode())

#Removing empty rows
df.dropna(inplace = True)

print("Missing values after cleaning: \n",df.isnull().sum())

#Printing the dataset after cleaning
print(df)

#Some operations on dataset
print("First 15 rows of Dataset: ",df.head(15))
print("Last 15 rows of Dataset: ",df.tail(15))
print("Datatype of Dataset: ",df.dtypes)
print("Shape of Dataset: ",df.shape)

#Handling Duplicates
print(f"Duplicate Rows: ",df.duplicated().sum())
df.drop_duplicates(inplace = True)    #removing duplicates

# Finding Unique value
print("Unique State: ",df["state"].unique())   #checking unique values
df["state"] = df["state"].str.strip().str.title()


#import pandas as pd
df.to_csv("air_qual.csv", index = False)

#Visualization of data
#bar plot
avg_pollutants = df.groupby("pollutant_id")["pollutant_avg"].mean().sort_values(ascending=False)
plt.figure(figsize = (10,5))
plt.bar(avg_pollutants.index, avg_pollutants.values, color=["blue","green", "indigo", "orange","yellow", "red", "grey" ])
plt.xlabel("Pollutants")
plt.ylabel("Average Pollutants level")
plt.title("Average Pollutant Levels comparison")
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()

#using histogram to see maximum pollutant
plt.figure(figsize=(10,5))
plt.hist(df["pollutant_max"].dropna(), bins = 50, color = "green", edgecolor = "black", linestyle = ":")
plt.xlabel("Maximum Pollutant Level")
plt.ylabel("Frequency")
plt.title("Distribution of Maximum Pollutant Levels")
plt.show()

#Comparison between Maximum and minimum pollutant using 
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="pollutant_min", y="pollutant_max", hue="pollutant_id", palette="viridis", alpha=0.7)
plt.xlabel("MinimumPollutant Level")
plt.ylabel("Maximum Pollutant Level")
plt.title("Scatter plot for Minimum vs Maximum Pollutant Levels")
plt.show()


#Using Line graph to see CO(Carbon monxide) over a period of time
df["last_update"] = pd.to_datetime(df["last_update"], format="%d-%m-%Y %H:%M")
co_df = df[df["pollutant_id"] == "CO"]
daily_co = co_df.groupby(co_df["last_update"].dt.date)["pollutant_avg"].mean()
plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_co.index, y=daily_co.values, color = "blue", marker="^")
plt.xlabel("Date")
plt.ylabel("Average Carbon Monoxide level")
plt.title("Daily Average of Carbon Monoxide over time")
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()