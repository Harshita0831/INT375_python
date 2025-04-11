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
plt.bar(avg_pollutants.index, avg_pollutants.values, color="blue")
plt.xlabel("Pollutants")
plt.ylabel("Average Pollutants level")
plt.title("Average Pollutant Levels comparison")
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()