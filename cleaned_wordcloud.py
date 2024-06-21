import pandas as pd

from wordcloud import WordCloud

import matplotlib.pyplot as plt

'''
Oil
'''
c_oil = pd.read_csv("spill_data/Cleaned_Files/C_All_Oil.csv")
c_oil['text_with_display_links'] = c_oil['text_with_display_links'].astype(str)
c_oil_tw = ' '.join(c_oil['text_with_display_links'])

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocation_threshold=100000).generate(c_oil_tw)

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

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocation_threshold=100000).generate(c_sewage_tw)

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

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocation_threshold=100000).generate(c_industrial_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Industrial Spill Word Cloud")
plt.show()