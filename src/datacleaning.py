import pandas as pd

#checking missing value in csv file
df=pd.read_csv("data/laboratory_data_dirty.csv")

#checking how many columns and rows are there
print("\n" + "="* 60 )
print("Dataset shape")
print("\n" + "=" * 60 )
print(df.shape)
#checking missing_values
print("\n === missing values")
print(df.isnull().sum())

#checking duplicate rows
print("\n === checking duplicate rows")
print(df.duplicated().sum())


#checking gender unique values
print("\n" + "="* 60 )
print("gender  values")
print("\n" + "="* 60 )
print(df["Gender"].unique())

print("\n" + "="* 60 )
print("Department values")
print("\n" + "="* 60 )
print(df["Department"].unique())

print("\n" + "="* 60 )
print("age  values")
print("\n" + "="* 60 )
print(df["Age"] >= 120)
#checking parameter
print(df[df["Parameter_Value"].isnull()])
#check datatypes
print("\n data types")
print(df.dtypes)

print("\n" + "="* 60 )
print("Data cleaning")
print("\n" + "="* 60 )

#fix gender speling
df["Gender"]=df["Gender"].replace("malee","male")

#fix department spelling
df["Department"]=df["Department"].replace("Biochemstry",'Biochemistry')

#caluclating average  age 
avg_age=df["Age"].mean()

#filling missing agevalue 
df["Age"]=df["Age"].fillna(avg_age)

#fixing age value greterthan 120"
df.loc [df["Age"] > 120,"Age"]=avg_age

# Fill missing Unit
df["Unit"] = df["Unit"].fillna("Not Applicable")
#convering parameter value to nemric
df["Parameter_Value"] = pd.to_numeric(df["Parameter_Value"], errors="coerce")

#caluclating avg parameter value
average_parameter = df["Parameter_Value"].mean()

#filling missing parameter avlue
df["Parameter_Value"] = df["Parameter_Value"].fillna(average_parameter)
# Remove duplicate rows
df = df.drop_duplicates()


print("\n" + "="*60)
print("AFTER CLEANING")
print("="*60)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nGender Values")
print(df["Gender"].unique())

print("\nDepartment Values")
print(df["Department"].unique())


import os

print("Current Working Directory:")
print(os.getcwd())


import os

# Create the folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save the cleaned dataset
df.to_csv("data/processed/laboratory_data_cleaned.csv", index=False)

print("✅ Clean dataset saved successfully!")