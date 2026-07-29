import pandas as pd

df=pd.read_csv("data/processed/laboratory_data_cleaned.csv")
print(df.head())

#adding age column to dataset
def age_group(age):
    if age < 18:
        return "child"
    elif age < 40:
        return "adult"
    elif age < 60:
        return "midddle age"
    else:
        return "senior citzen"
df["Age_group"]=df["Age"].apply(age_group)


print(df[["Patient_Name","Age","Age_group"]])


print("\n===== Age Group Distribution =====")
print(df["Age_group"].value_counts())

#creating singledatetime column
df["Test_DateTime"]=pd.to_datetime(df["Test_Date"] + " " + df["Test_Time"])

print(df[["Test_Date","Test_Time","Test_DateTime"]].head())

#counting hours
df["Test_Hours"]=df["Test_DateTime"].dt.hour

print(df[["Test_Hours","Test_DateTime"]])

#extracting dayname
df["Day_Name"]=df["Test_DateTime"].dt.day_name()
print(df[["Test_DateTime","Day_Name"]])

#number of tests per hour
test_count=df["Test_Hours"].value_counts().sort_index()
print(test_count)

#creating pyplots

import matplotlib.pyplot as plt

plt.figure(figsize=(8,10))
plt.bar(test_count.index,test_count.values)
plt.title("test count per hour")
plt.xlabel("Hour")
plt.ylabel("number of tests")
plt.show()


df.to_csv(
    "data/processed/laboratory_feature_engineered.csv",
    index=False
)

print("✅ Feature Engineering Completed")