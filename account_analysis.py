import pandas as pd

# This program's purpose to identify the account types. The types are:
# - media
# - government
# - academia
# - tourism & business
# - other (public)

# the labeled accounts from the red tide research is being utilized
accounts = pd.read_csv("Final_Account_Labels_for_Dashboard.csv")
# and the new accounts will be labeled with ML algorithm from red tide research

#starting to practice with a small dataset before running on all spills combined
nort_oil = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Oil.csv", usecols=["username", "description"])
print(nort_oil)

existing_usernames = set(accounts['username'])
new_usernames = nort_oil[~nort_oil['username'].isin(existing_usernames)]


print(new_usernames)

new_usernames["Label"] = "yet to be set"
new_usernames["Label.Type"] = "yet to be set"

print(new_usernames)
# saving the users that are yet to be labeled
