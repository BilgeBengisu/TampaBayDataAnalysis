import pandas as pd

from wordcloud import WordCloud

import matplotlib.pyplot as plt

'''
Oil
'''
c_oil = pd.read_csv("spill_data/Cleaned_Files/C_All_Oil.csv")
c_oil['text_with_display_links'] = c_oil['text_with_display_links'].astype(str)
c_oil_tw = ' '.join(c_oil['text_with_display_links'])
oil_stop_words = ["oil", "crude", "petroleum", "tar ball", "tar balls","leak","leaks","leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords=oil_stop_words).generate(c_oil_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Oil Spill Word Cloud")
plt.show()

'''
Sewage
'''

c_sewage = pd.read_csv("spill_data/Cleaned_Files/C_All_Sewage.csv")
c_sewage['text_with_display_links'] = c_sewage['text_with_display_links'].astype(str)
c_sewage_tw = ' '.join(c_sewage['text_with_display_links'])
sewage_stop_words=["sewer", "sewers", "sewage", "septic", "stormwater", "storm water", "reclaimed water", "reclaim water", "untreated", "raw", "overflow", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "dump", "dumps", "dumped", "dumping","ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords=sewage_stop_words).generate(c_sewage_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Sewage Spill Word Cloud")
plt.show()

'''
Industrial
'''

c_industrial = pd.read_csv("spill_data/Cleaned_Files/C_All_Industrial.csv")
c_industrial['text_with_display_links'] = c_industrial['text_with_display_links'].astype(str)
c_industrial_tw = ' '.join(c_industrial['text_with_display_links'])
industrial_stop_words = ["wastewater","contaminants", "contamination", "contaminating", "chemical", "chemicals", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage","dump", "dumps", "dumped","dumping", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords=industrial_stop_words).generate(c_industrial_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Industrial Spill Word Cloud")
plt.show()