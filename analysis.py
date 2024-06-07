
import pandas as pd
import matplotlib.pyplot as plt

'''
tf_path = "spill_data/OilSpill_Manatee_all_SIMPLE_columns.csv"
df = pd.read_csv(tf_path)

#print(df["created_at.x"])

# stripping the time mark and keeping only the date
df["created_at.x"] = df["created_at.x"].str.split().str[0]

#print(df["created_at.x"])

df["created_at.x"].value_counts().plot.bar()
plt.title("Oil Spill Mention Frequency in Manatee")
plt.xlabel("date")
plt.show()
'''


tf_path = "spill_data/IndustrialSpill_Manatee_all_SIMPLE_columns.csv"
df = pd.read_csv(tf_path)
'''
# stripping the time mark and keeping only the date
df["created_at.x"] = df["created_at.x"].str.split().str[0]
date = df["created_at.x"]

date.value_counts().plot.bar()
plt.title("Industrial Spill Mention Frequency in Manatee")
plt.xlabel("date")
plt.show()
'''

from datetime import datetime
import matplotlib.dates as mdates

df["created_at.x"] = df["created_at.x"].str.slice(0,10)

df['count'] = df.groupby('created_at.x')['created_at.x'].transform('count')

df['created_at.x'] = pd.to_datetime(df['created_at.x'])

date = df["created_at.x"]

count = df["count"]

# Plottin the basic time series

# Format x-axis as dates
fig, ax = plt.subplots()
ax.plot(date, count)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b, %d %Y'))
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Count of created_at.x by Date')
plt.tight_layout()
plt.show()

# filling in the days where there were no tweets

# Generate a date range covering the entire period
date_range = pd.date_range(start=date.min(), end=date.max())

# Create a DataFrame with the date range
date_df = pd.DataFrame(date_range, columns=['created_at.x'])

# Merge the original DataFrame with the date DataFrame, filling missing values with 0
merged_df = pd.merge(date_df, df.groupby('created_at.x').size().reset_index(name='count'), on='created_at.x', how='left').fillna(0)

# Plot
fig, ax = plt.subplots()
ax.plot(merged_df['created_at.x'], merged_df['count'])

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Count of created_at.x by Date')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


"""
So we got time series on an individual dataset and filled in the dates when there was no data recorded.
Let's turn it into functions to be able to run it on anything more easily
"""
def get_date_count(df):
    df["created_at.x"] = df["created_at.x"].str.slice(0,10)

    df['count'] = df.groupby('created_at.x')['created_at.x'].transform('count')

    df['created_at.x'] = pd.to_datetime(df['created_at.x'])

    return df

def fill_in_dates(df):
    # Extract the columns other than 'created_at.x'
    other_columns = df.drop(columns=['created_at.x', 'count'])
    # Generate a date range covering the entire period
    date_range = pd.date_range(start=df["created_at.x"].min(), end=df["created_at.x"].max())

    # Create a DataFrame with the date range
    date_df = pd.DataFrame(date_range, columns=['created_at.x'])

    # Merge the original DataFrame with the date DataFrame, filling missing values with 0
    merged_df = pd.merge(date_df, df.groupby('created_at.x').size().reset_index(name='count'), on='created_at.x', how='left').fillna(0)

    # Merge the modified DataFrame back with the original columns
    merged_df = pd.concat([other_columns, merged_df], axis=1)

    return merged_df

def plot_time_series(df, title=None):
    fig, ax = plt.subplots()
    ax.plot(df['created_at.x'], df['count'])

    # Format x-axis as dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xlabel('Date')
    plt.ylabel('Count')
    if title:
        plt.title(title)
    else:
        plt.title('Time Series')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


tf_path = "spill_data/IndustrialSpill_Sarasota_all_SIMPLE_columns.csv"
df = pd.read_csv(tf_path)

df = get_date_count(df)

df = fill_in_dates(df)

plot_time_series(df, 'Sarasota Industrial Spill')

# Now let's combine all datasets of a spill type
import os
# Getting all the files in the spill data
all_files = os.listdir("spill_data")

# Filter files that start with "oil"
oil_files = [file for file in all_files if file.startswith('IndustrialSpill')]

dfs = []

# Read each file and append its DataFrame to the list
for file in oil_files:
    file_path = os.path.join("spill_data", file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# removing duplicates
combined_df = combined_df.drop_duplicates()

# Save the combined DataFrame to a CSV file
#combined_df.to_csv('spill_data/All_IndustrialSpill.csv', index=False)

'''
Great, now let's plot all three types of spill and label them 
'''

# Load the first CSV file
Industrial = pd.read_csv('spill_data/All_IndustrialSpill.csv')
Industrial = get_date_count(Industrial)
Industrial = fill_in_dates(Industrial)

# Load the second CSV file
Oil = pd.read_csv('spill_data/All_OilSpill.csv')
Oil = get_date_count(Oil)
Oil = fill_in_dates(Oil)

# Load the third CSV file
Sewage = pd.read_csv('spill_data/All_SewageSpill.csv')
Sewage = get_date_count(Sewage)
Sewage = fill_in_dates(Sewage)

# Extract columns to plot from the first and second CSV files
x1 = Industrial['created_at.x']
y1 = Industrial['count']

x2 = Oil['created_at.x']
y2 = Oil['count']

x3 = Sewage['created_at.x']
y3 = Sewage['count']

# Plot the first and second columns
plt.plot(x1, y1, label='Industrial')
plt.plot(x2, y2, label='Oil')
plt.plot(x3, y3, label='Sewage')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Tweet Count on Different Types of Spill')

# Add legend
plt.legend()

# Show plot
plt.show()

"""
Now Let's plot the same thing but only have original tweets
"""

# Removing RT data

def remove_RT(df, file_name):
    # Filter out rows where the text column starts with 'RT @'
    df = df[~df['text'].astype(str).str.startswith('RT @')]
    # Save the filtered DataFrame back to the CSV file
    df.to_csv(f"spill_data/NORT_{file_name}.csv", index=False)
    return df

# Load the first CSV file
Industrial = pd.read_csv('spill_data/All_IndustrialSpill.csv')
Industrial = get_date_count(Industrial)
Industrial = fill_in_dates(Industrial)
Industrial = remove_RT(Industrial, 'Industrial')

# Load the second CSV file
Oil = pd.read_csv('spill_data/All_OilSpill.csv')
Oil = get_date_count(Oil)
Oil = fill_in_dates(Oil)
Oil = remove_RT(Oil, 'Oil')

# Load the third CSV file
Sewage = pd.read_csv('spill_data/All_SewageSpill.csv')
Sewage = get_date_count(Sewage)
Sewage = fill_in_dates(Sewage)
Sewage = remove_RT(Sewage, 'Sewage')

# Extract columns to plot from the first and second CSV files
x1 = Industrial['created_at.x']
y1 = Industrial['count']

x2 = Oil['created_at.x']
y2 = Oil['count']

x3 = Sewage['created_at.x']
y3 = Sewage['count']

# Plot the first and second columns
plt.plot(x1, y1, label='Industrial')
plt.plot(x2, y2, label='Oil')
plt.plot(x3, y3, label='Sewage')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Tweet Count on Different Types of Spill')

# Add legend
plt.legend()

# Show plot
plt.show()