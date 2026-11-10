#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Student: Dandan Zhang, u1601232

# Explanation: After downloading the data from the internet, 
# I carried out preprocessing operations such as data reading and cleaning, 
# and then proceeded with the five practice exercises.


# In[2]:


## Dataset Introduction 

# This notebook uses the breast cancer dataset from the UCI Machine Learning Repository. 
# This dataset consists of 286 records, 9 features related to health, and a target variable indicating whether the breast cancer has recurred.

## Data Loading and Initial Data Inspection.

import pandas as pd
column_names = [
    "Class",
    "age",
    "menopause",
    "tumor-size",
    "inv-nodes",
    "node-caps",
    "deg-malig",
    "breast",
    "breast-quad",
    "irradiat"
]

# Load the local dataset and convert '?' into missing values.
df = pd.read_csv(
    "breast-cancer.data",
    header=None,
    names=column_names,
    na_values="?"
)

print(df.head())

print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())


# In[3]:


## Brief data preprocessing

# Create a copy for data preparation.
df_clean = df.copy()

# Standardize column names.
df_clean.columns = (
    df_clean.columns
    .str.lower()
    .str.replace("-", "_", regex=False)
)

df_clean = df_clean.rename(
    columns={"class": "recurrence_status"}   # The meaning is clearer and avoids the syntax issues of class python.
)

# Preserve records by labeling missing categories as Unknown.

# Select categorical text columns.
categorical_columns = df_clean.select_dtypes(
    include=["object", "string"]
).columns

# Replace missing categorical values with "Unknown".
df_clean[categorical_columns] = (
    df_clean[categorical_columns].fillna("Unknown")
)

# Add a generated row ID for the melt and pivot demonstrations.
df_clean.insert(
    0,                             # New column placed in the first position
    "patient_id",                  # Name of the New column
    range(1, len(df_clean) + 1)    # Value of the new column
)

print(df_clean.head())


# In[4]:


# Melt, pivot, aggregation, and groupby use all 286 records.
# Iteration is demonstrated using the first ten records.


# In[5]:


# 1. The melt() 
# The melt() function converts wide-format data into long-format data. 

# Select the columns used in the melt demonstration.
melt_source = df_clean[
    [
        "patient_id",
        "recurrence_status",
        "age",
        "menopause",
        "tumor_size",
        "deg_malig",
        "breast"
    ]
]

# Display the original wide-format data.
print("Original wide-format data:")
print(melt_source.head())

# Convert the selected health features from wide format to long format.
melt_result = melt_source.melt(
    id_vars=["patient_id", "recurrence_status"],  # Keep the patient identification information unchanged.
    value_vars=["age", "menopause", "tumor_size", "deg_malig", "breast"],  # Convert multiple columns into multiple rows
    var_name="health_feature",  #The new column retains the original column name.
    value_name="feature_value"  #The new column stores the corresponding data values.
)

# Diaplay part of the long-format result.
print("Long-format data after melt:")
print(melt_result.head(10))

# The five health_features of each patient were transformed into five rows.
print("Original shape:", melt_source.shape)
print("Melted shape:", melt_result.shape)

# View the five elements of patient 1 separately
print(
    melt_result[
        melt_result["patient_id"] == 1
    ]
)


# In[6]:


# 2.Pivot
# The function of pivot() is the opposite of melt(). 
# It converts the long-format data back to the wide format.

# Convert the long-format data back into wide format.
pivot_result = melt_result.pivot(
    index=["patient_id","recurrence_status"], # patient_id and recurrence_status determine each row.
    columns="health_feature", # Change the five "health feature" items back into columns.
    values="feature_value" # Fill the corresponding positions with the data from feature_value.
).reset_index() # Restore the patient_id and recurrence_status columns from the index to their normal positions as regular columns.

# Display the restored wide-format data.
print(pivot_result.head())

print("Pivoted shape:", pivot_result.shape)


# In[7]:


# 3. Aggregation
# The Aggregate() function aggregates multiple pieces of data into statistical results.

# Statistically analyze the degree of malignancy (deg_malig) for all patients.
aggregation_result = df_clean["deg_malig"].agg(
    ["count", "mean", "median", "min", "max"]
)

print(aggregation_result)


# Here, the tumor_size of all patients is statistically analyzed as an example.
# Since the tumor size is an interval-type categorical data, the main statistics include the number of records, the number of categories and the mode.
# Aggregation： summarize the tumor size variable.
tumor_size_summary = df_clean["tumor_size"].agg(
    total_patients="count",  # count: count the number of tumor size records.
    number_categories="nunique",  # nunique: count the number of different size intervals.
    most_common_size=lambda values: values.mode().iloc[0]  # mode(): count the size interval with the highest frequency. # .iloc[0]: extract the first mode.
)  

print(tumor_size_summary)



# In[8]:


# 4. Iteration
# It indicates processing the DataFrame row by row.

# Create an empty list to store the iteration results.
iteration_result = []

# Iterate through the first ten patient records.
for index, row in df_clean.head(10).iterrows():  #index: the index of the current row; row: the data of the current row; iterrows(): Returns one row at a time.

    #Save selected information from the current patient.
    patient_information = {"patient_id": row["patient_id"],
                           "recurrence_status": row["recurrence_status"],
                           "age": row["age"],
                           "menopause": row["menopause"],
                           "malignancy_degree": row["deg_malig"],
                           "breast": row["breast"]

    }

    # Add the current patient's information to the list
    iteration_result.append(patient_information)

# Convert the list of dictionaries into a DataFrame for clearer display.
iteration_df = pd.DataFrame(iteration_result)

print(iteration_df)


# In[9]:


# 5.Groupby

# Group patients by menopause and calculate.
# The malignancy degree statistics for each group.

groupby_result = (
    df_clean
    .groupby("menopause")["deg_malig"] # First, group the patients according to their menopausal status, and then calculate the statistical values of malignancy for each group.
    .agg(["count", "mean", "min", "max"]) # Calculate multiple statistical results.
    .round(2) # Round the values in the result to two decimal places.
)

print(groupby_result)


# In[ ]:




