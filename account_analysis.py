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
nort_oil['Label'] = 'yet'
nort_oil['Label.Type'] = 'yet'

print(nort_oil)

# saving the users that are yet to be labeled
