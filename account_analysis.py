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
nort_oil_acc = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Oil.csv", usecols=["username", "description"]).drop_duplicates(subset=['username'])
nort_industrial_acc = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Industrial.csv", usecols=["username", "description"]).drop_duplicates(subset=['username'])
nort_sewage_acc = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Sewage.csv", usecols=["username", "description"]).drop_duplicates(subset=['username'])

'''
print(nort_oil_acc.size)
print(nort_industrial_acc.size)
print(nort_sewage_acc.size)
'''

# Merging the files with the accounts on different spills
merged = pd.merge(nort_oil_acc, nort_industrial_acc, on=['username','description'], how='outer')

# drop duplicates
merged = merged.drop_duplicates(subset=['username'])

merged = pd.merge(merged, nort_sewage_acc, on=['username','description'], how='outer')

spill_merged = merged.drop_duplicates(subset=['username'])

existing_usernames = set(accounts['username'])

# getting the users that are yet to be labeled
users_to_be_labelled = spill_merged[~spill_merged['username'].isin(existing_usernames)]

print(users_to_be_labelled)

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict, train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
import re
import json
from sklearn.metrics import confusion_matrix
import pickle

tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV
tag_map['AS'] = wn.ADJ_SAT

# filepath = "finalized_8K_accounts.csv"
# filepath = "UNLABELED_accounts_emojis_replaced.csv"
filepath = "spill_data/Account/FINALIZED_Unlabeled_Data_ALL_Available_Descriptions_EMOJIS_UNCHANGED.csv"
hand_label = "hand.label"
government = "gov"
academia = "acad"
tourBiz = "tourbiz"

df = pd.read_csv(filepath)

# df = df[((df[hand_label] == 'media') | (df[hand_label] == tourBiz) |(df[hand_label] == academia) | (df[hand_label] == government) | (
#        df[hand_label] == 'other'))]

df = df[['username', 'description']]  # keep only relevant columns

lemmatizer = WordNetLemmatizer()
words_not_changed = ['media']


def preprocessing(row):
    if str(row) == "nan":
        lemma = ""
    else:
        row = str(row).lower()
        row = word_tokenize(row)  # tokenize
        lemma = [lemmatizer.lemmatize(token, tag_map[tag[0]]) if token not in words_not_changed else token for
                 token, tag in pos_tag(row)]  # lemmatization, depending on part-of-speech
        lemma = ["" if re.search(r'\b[0-9]+\b\s*', lem) else lem for lem in lemma]  # removing
    return str(lemma)


df['description_lemmatized'] = df['description'].apply(preprocessing)
