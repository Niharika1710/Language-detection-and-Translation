# -*- coding: utf-8 -*-
"""language detection&translation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XP3SjPyQks3lyG5rwcflVND9U2GNV0Tq
"""

# -*- coding: utf-8 -*-
"""Language_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2RhJSW97DChyiRoC3JaKvATHB7zQ94V
"""

import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")
# Loading the dataset
#data = pd.read_csv("C:\Users\Niharika\OneDrive\Desktop\Language Detection1.csv")
data = pd.read_csv("Language Detection.csv")
# value count for each language
data["Language"].value_counts()
data['Text'].fillna(' ', inplace=True)
data['Language'].fillna(' ', inplace=True)
# separating the independent and dependant features
X = data["Text"]
y = data["Language"]
# converting categorical variables to numerical
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
# creating a list for appending the preprocessed text
data_list = []
# iterating through all the text
for text in X:
    # removing the symbols and numbers
    #text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    #text = re.sub(r'[[]]', ' ', text)
    # converting the text to lower case
    #text = text.lower()
    # appending to data_list
    data_list.append(text)
# creating bag of words using countvectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(data_list).toarray()
#train test splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
#model creation and prediction
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train, y_train)
# prediction
y_pred = model.predict(x_test)
# model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix
ac = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
# visualising the confusion matrix
plt.figure(figsize=(15,10))
sns.heatmap(cm, annot = True)
plt.show()
# function for predicting language
def predict(text):
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    print("The langauge is in",lang[0])

# English
predict("Analytics Vidhya provides a community based knowledge portal for Analytics and Data Science professionals")

# French
predict("Analytics Vidhya fournit un portail de connaissances basé sur la communauté pour les professionnels de l'analyse et de la science des données")

# Arabic
predict("توفر Analytics Vidhya بوابة معرفية قائمة على المجتمع لمحترفي التحليلات وعلوم البيانات")

# Spanish
predict("Analytics Vidhya proporciona un portal de conocimiento basado en la comunidad para profesionales de Analytics y Data Science.")

# Malayalam
predict("അനലിറ്റിക്സ്, ഡാറ്റാ സയൻസ് പ്രൊഫഷണലുകൾക്കായി കമ്മ്യൂണിറ്റി അധിഷ്ഠിത വിജ്ഞാന പോർട്ടൽ അനലിറ്റിക്സ് വിദ്യ നൽകുന്നു")

# Russian
predict("Analytics Vidhya - это портал знаний на базе сообщества для профессионалов в области аналитики и данных.")

predict("hi")

predict("hello world")
predict("ब्रेकिंग न्यूज़ समाचार, ताजा खबर ")
print(ac)

pip install googletrans==4.0.0-rc1

from googletrans import Translator
from requests.exceptions import Timeout

def translate_text(text, target_language='en', max_retries=5):
    translator = Translator()

    for _ in range(max_retries):
        try:
            translation = translator.translate(text, dest=target_language)
            return translation.text
        except Timeout:
            print("Timeout, retrying...")
            continue

    print("Max retries reached. Translation failed.")
    return None

# Example usage
text_to_translate = "ब्रेकिंग न्यूज़ समाचार, ताजा खबर"
translated_text = translate_text(text_to_translate, target_language='telugu')  # 'te' is the language code for Telugu

if translated_text:
    print(f'Original text: {text_to_translate}')
    print(f'Translated text: {translated_text}')



