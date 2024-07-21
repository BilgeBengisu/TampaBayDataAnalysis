# Tampa Bay Environmental Twitter Data Analysis
This repository manipulates and visualizes environmental Twitter data regarding the Tampa Bay, FL. Libraries used are pandas, matplotlib, re, sklearn, and wordcloud. The motivation is to highlight the relationship between environmental issues and online interaction.

### Analysis.ipynb
This file contains step-by-step the cleaning process of the tweets in the "text_with_display_links" column. The cleaned files of 3 spill types are stored in spill_data folder: Cleaned_Files & Cleaned_NORT_Files (RTs removed)

### Analysis.py
This python file contains functions to plot time series. When the file is run, it plots time series of all 3 spill types with and without RTs. Empty dates are filled na rows to appear in the time series.

### cleaned_wordcloud.py
This file visualizes the cleaned tweets via wordcloud. The respective query words to get the twitter data are filtered from the word pool.

### cleaned_nongeo_wordcloud.py
This file visualizes the cleaned tweets via wordcloud. **The locations and** the respective query words to get the twitter data are filtered from the word pool.

## Account Folder
This folder contains any analysis done regarding the user accounts. **ALL_Labeled_Accounts_Spill&RedTide.csv** is the file with all accounts - the most updated labeling.
 
### account_selection.py
This file saves the accounts that havent been labeled yet from Red Tide Research to **Spill_Accounts_To_Be_Labeled.csv** 

### account_pred.py
This file runs the SVM model(pickle file in the folder) from Red Tide research on **Spill_Accounts_To_Be_Labeled.csv** and saves the predictions to **SVM_BERT_unweighted_UNLABELED_PREDICTED_SPILL_accounts_W_PROBABILITIES_emojis_unchanged.csv**

### SVM_Predicting_Remaining_22K_BERT.ipynb
This jupyter notebook modified from Red Tide Research has two extra sections: **Relabeling "other" rows** & **TF-IDF**
#### Relabeling "other" rows
The users to be relabeled were stored in **Accounts_To_Relabel.csv** by extracting the "other" labeled rows if they had a different prediction column where the probability is higher than 0.3. Relabeling was done manually by Prof. Skripnikov and is stored in **Final_Account_Relabeling.csv**
#### TF-IDF
In this section, the file is processed to get the first 3 columns in the photo below for every account type in each spill type. Later, these files are merged together in their respective spill types to be fed to tf-idf. The merged file is in the **merged_tf_idf** folder. Individual files in the merged result are stored in **not_merged_tf_idf** and result from the tf_idf_preprocessing() function in the jupyter notebook. TF-IDF wordcloud was attempted but didn't result in outcome.
![tf-idf](Account/tf_idf/tf-idf.png)
