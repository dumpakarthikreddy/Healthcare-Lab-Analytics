import pandas as pd

#read the datset
df = pd.read_csv("data\laboratory_data.csv")

# Display the first 5 rows
print("===== First 5 Records =====")
print(df.head())

print("\n ==== datshape====")
print(df.shape)


print("\n === columns names===")
print(df.columns)

print("\n === dataframe information ===")
print(df.info)

print("\n ==== average age ===")
print(df["Age"].mean())

print("\n ==== maximum age ===")
print(df["Age"].max())

print("\n ==== minimum age ===")
print(df["Age"].min())

print("\n ==== total patient count ===")
print(df["Patient_ID"].count())

print("\n ==== gender distribution ===")
print(df["Gender"].value_counts())

print("\n ==== test distribution ===")
print(df["Test_Name"].value_counts())

print("\n ==== department distribution ===")
print(df["Department"].value_counts())

print("\n ==== machine distribution ===")
print(df["Machine_Name"].value_counts())

print("\n ==== test result distribution ===")
print(df["Sample_Status"].value_counts())