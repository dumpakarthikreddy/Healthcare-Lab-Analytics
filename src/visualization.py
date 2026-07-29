"""
import pandas as pd

import matplotlib.pyplot as plt

#read dataset
df=pd.read_csv("data\laboratory_data.csv")

#1.departmentcount
print("\n === dipartmentdistribution ===")
department_counts=df["Department"].value_counts()

plt.figure(figsize=(8,10))
plt.bar(department_counts.index,department_counts.values)

plt.title("Department-wise Test Count")
plt.xlabel("Department")
plt.ylabel("Number of Tests")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

"""
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data\laboratory_data.csv")

# -------------------------
# 1. Gender Distribution
# -------------------------
gender = df["Gender"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(gender.index, gender.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.show()

# -------------------------
# 2. Result Status Distribution
# -------------------------
result = df["Result_Status"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(result.index, result.values)
plt.title("Result Status Distribution")
plt.xlabel("Result Status")
plt.ylabel("Count")
plt.show()

# -------------------------
# 3. Age Distribution
# -------------------------
plt.figure(figsize=(7,4))
plt.hist(df["Age"], bins=6)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()