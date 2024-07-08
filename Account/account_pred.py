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
filepath = "Account/FINALIZED_Unlabeled_Data_ALL_Available_Descriptions_EMOJIS_UNCHANGED.csv"
hand_label = "hand.label"
government = "gov"
academia = "acad"
tourBiz = "tourbiz"

df = pd.read_csv(filepath)

print(df)

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

print(df['description_lemmatized'])


# Removing all the empty descriptions!!!
print(df.shape)
print(df[df['description_lemmatized'] != ""].shape) 
df = df[df['description_lemmatized'] != ""]

# Re-indexing the remaining observations
df = df.reset_index(drop=True)

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# is used for X_test
embeddings = model.encode(df['description'].tolist())

filename = 'Account/SVM_BERT_unweighted_enhanced_model_full(1, 2).pickle'
loaded_model = pickle.load(open(filename, 'rb'))

X_test = embeddings

bag_of_words_y_pred_test = loaded_model.predict(X_test)

bag_of_words_y_pred_test

pred_prob = loaded_model.predict_proba(X_test)

pred_prob
bag_of_words_y_pred_test
pd.concat([pd.DataFrame(bag_of_words_y_pred_test), pd.DataFrame(pred_prob)], axis=1)

pred_prob.shape

pred_prob_df = pd.DataFrame(pred_prob, columns = ['acad_prob','gov_prob','media_prob','other_prob', 'tourbiz_prob'])

bag_of_words_y_pred_test.size

df['label_simplified'] = bag_of_words_y_pred_test

#df = df.drop(columns=['description_lemmatized'])

df1 = pd.concat([df, pred_prob_df], axis=1)

df1.to_csv('Account/SVM_BERT_unweighted_UNLABELED_PREDICTED_SPILL_accounts_W_PROBABILITIES_emojis_unchanged.csv', index=False)