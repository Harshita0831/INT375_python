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