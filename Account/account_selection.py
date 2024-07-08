import pandas as pd

# This program's purpose to identify the account types. The types are:
# - media (media)
# - government (gov)
# - academia (acad)
# - tourism & business (tourbiz)
# - public & others (other)

# the labeled accounts from the red tide research is being utilized
accounts = pd.read_csv("Final_Account_Labels_for_Dashboard.csv")
# and the new accounts will be labeled with ML algorithm from red tide research

'''
#starting to practice with a small dataset before running on all spills combined
nort_oil = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Oil.csv", usecols=["username", "description"])
print(nort_oil)

existing_usernames = set(accounts['username'])

# saving the users that are yet to be labeled
new_usernames = nort_oil[~nort_oil['username'].isin(existing_usernames)]


print(new_usernames)

new_usernames["Label"] = "yet to be set"
new_usernames["Label.Type"] = "yet to be set"

print(new_usernames)
'''

# getting unique accounts on each spill
oil_acc = pd.read_csv("spill_data/All_OilSpill.csv", usecols=["username", "description", "verified"]).drop_duplicates(subset=['username'])
industrial_acc = pd.read_csv("spill_data/All_IndustrialSpill.csv", usecols=["username", "description", "verified"]).drop_duplicates(subset=['username'])
sewage_acc = pd.read_csv("spill_data/All_SewageSpill.csv", usecols=["username", "description", "verified"]).drop_duplicates(subset=['username'])

print(oil_acc.size)
print(industrial_acc.size)
print(sewage_acc.size)


# Merging the files with the accounts on different spills
merged = pd.merge(oil_acc, industrial_acc, on=['username','description', 'verified'], how='outer')

# drop duplicates
merged = merged.drop_duplicates(subset=['username'])

merged = pd.merge(merged, sewage_acc, on=['username','description', 'verified'], how='outer')

spill_merged = merged.drop_duplicates(subset=['username'])

existing_usernames = set(accounts['username'])

print(spill_merged.size)

# getting the users that are yet to be labeled
users_to_be_labelled = spill_merged[~spill_merged['username'].isin(existing_usernames)]

users_to_be_labelled.to_csv("Account/Spill_Accounts_To_Be_Labeled.csv")

print(users_to_be_labelled)
