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
plt.bar(avg_pollutants.index, avg_pollutants.values, color=sns.color_palette("Blues", 7), edgecolor = "black")
plt.xlabel("Pollutants")
plt.ylabel("Average Pollutants level")
plt.title("Average Pollutant Levels comparison")
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()

#using histogram to see maximum pollutant
plt.figure(figsize=(10,5))
plt.hist(df["pollutant_max"].dropna(), bins = 30, color = "green", edgecolor = "black", linestyle = ":")
plt.xlabel("Maximum Pollutant Level")
plt.ylabel("Frequency")
plt.title("Distribution of Maximum Pollutant Levels")
plt.show()

#Comparison between Maximum and minimum pollutant using scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="pollutant_min", y="pollutant_max", hue="pollutant_id", palette="viridis", alpha=0.7)
plt.xlabel("MinimumPollutant Level")
plt.ylabel("Maximum Pollutant Level")
plt.title("Scatter plot for Minimum vs Maximum Pollutant Levels")
plt.show()


#Using Line graph to see CO(Carbon monoxide) over a period of time
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

#State wise pollution monitoring using pie chart
state_station_counts = df.groupby("state")["station"].nunique().sort_values(ascending=False)

#Keep top 5, group the rest as "Others"
top = 5
top_states = state_station_counts.head(top)
others = pd.Series([state_station_counts.iloc[top:].sum()], index=["Others"])
final_counts = pd.concat([top_states, others])


plt.figure(figsize=(8,8))
colors = sns.color_palette("Blues", 6)
plt.pie(final_counts, labels=final_counts.index, autopct="%1.1f%%", colors=colors)

plt.title("State wise Distribution of Monitoring Stations")
plt.show()



#Using boxplot to detect outliers in pollutant_avg 
sns.boxplot(x=df["pollutant_avg"])
plt.title('The boxplot of average pollutant')
plt.show()

#outliers boundaries of pollutant_avg
q1 = df["pollutant_avg"].quantile(0.25)
q3 = df["pollutant_avg"].quantile(0.75)
IQR = q3 - q1

lower_bound = q1 - 1.5*IQR
upper_bound = q3 + 1.5*IQR

print(lower_bound)    #-80.5
print(upper_bound)    #171.5

#detect outliers using boxplot of average pollutant
outliers = df[(df["pollutant_avg"] < lower_bound) | (df["pollutant_avg"] > upper_bound)]
print("Outliers in Pollutant Average", outliers["pollutant_avg"])



#using Heatmap to show patterns between pollutant average and state
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))

sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="Blues", linewidths=0.5, cbar=True, square=True)
plt.title("Correlation Matrix", fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
#plt.tight_layout()
plt.show()