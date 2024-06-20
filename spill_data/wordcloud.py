import pandas as pd

from wordcloud import WordCloud

import matplotlib.pyplot as plt

cleaned_text = pd.read_csv("spill_data/Clean_Oil/Clean10_OilSpill.csv")

print(cleaned_text)

text = ' '.join(cleaned_text['text'])

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocation_threshold=100000).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()