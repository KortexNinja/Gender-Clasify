import pandas as pd
import numpy as np
# Machine Learning Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer


# Load data
df = pd.read_excel('nombres.xlsx')

df_names = df
f=0
m=1
df_names.sex.replace({'F':0,'M':1},inplace=True)
print(df_names.sex.unique())

Xfeatures =df_names['name']
cv = CountVectorizer()
X = cv.fit_transform(Xfeatures)
cv.get_feature_names()
from sklearn.model_selection import train_test_split
# Features 
X
# Labels
y = df_names.sex

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.00001, random_state=42)
# Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
# Accuracy of our Model
print("Accuracy of Model",clf.score(X_test,y_test)*100,"%")
# Accuracy of our Model
print("Accuracy of Model",clf.score(X_train,y_train)*100,"%")

print('------------BIENVENIDO------------')
print('escribe el nombre del archivo')
filename = input()
df2predict = pd.read_excel(filename+'.xlsx')

nombres =df2predict['Nombres']

vector = cv.transform(nombres).toarray()
res = clf.predict(vector)

final_data = pd.DataFrame({'Nombres': nombres, 'Sexo': res })
#Back to M and F
final_data.Sexo.replace({0:'F',1:'M'},inplace=True)



writer = pd.ExcelWriter('Clasificados.xlsx')
final_data.to_excel(writer,'sheet1')
print(final_data)
writer.save()
