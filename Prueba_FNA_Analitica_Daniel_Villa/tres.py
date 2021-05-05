#!/usr/bin/python3
"""Clowd word"""

from wordcloud import ImageColorGenerator, WordCloud
import pandas as pd
import unicodedata
import matplotlib
import matplotlib.pyplot as plt

chats_df = pd.read_excel('chats.xlsx')
chats_df[' Conversación'] = chats_df[' Conversación'].str.lower().str.split()
words = chats_df[' Conversación'].dropna()
words = words.map(lambda w: [p.strip().lower() for p in w])
words = words.explode()
from nltk.corpus import stopwords
# Eliminar palabras usadas comunmente como a, la, lo...
stop = stopwords.words('Spanish')

words.apply(lambda x: [item for item in x if item not in stop])
words.head()
words = words.to_frame()
words = words.reset_index()
from wordcloud import ImageColorGenerator, WordCloud

# Mostrar grafica en forma de diccionario
words_dic = {key: value for key, value in zip(words["index"], words[" Conversación"])}

# Castear  string a float y generar la word cloud
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(words_dic)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()