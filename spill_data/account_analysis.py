import pandas as pd

# This program's purpose to identify the account types. The types are:
# - media
# - government
# - academia
# - other (public)

# the labeled accounts from the red tide research is being utilized and 
# the missing accounts are identified with the ML algorithm implemented previously for the red tide research. 

nort_oil = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Oil.csv")



