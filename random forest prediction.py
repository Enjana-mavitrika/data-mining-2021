# -*- coding: utf-8 -*-
"""BIG DATA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kcliXDKaJEn49YWiqqpyTrlc1tD0d8cG
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
features = pd.read_csv("/content/drive/MyDrive/bigdata/features.csv")
ids = pd.read_csv("/content/drive/MyDrive/bigdata/coded_ids.csv")
ids_labels_test = pd.read_csv("/content/drive/MyDrive/bigdata/coded_ids_labels_test.csv")
ids_labels_train = pd.read_csv("/content/drive/MyDrive/bigdata/coded_ids_labels_train.csv")

ids.head()

ids.info()

features.info()

ids_labels_train.head()

train_id=pd.merge(ids,ids_labels_train,how="right")
train_id

train_id["label"].value_counts()

"""connexion between labels train and ids"""

train=pd.merge(train_id,features,how="left")
train

train=train.drop(["coded_id","user_id"],axis=1)



train.iloc[:,1:]

train.info()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

train=train.drop(list(train.select_dtypes(object).columns),axis=1)
train["utc_offset"].fillna(train["utc_offset"].mean(),inplace=True)
#del train["spam_in_screen_name"]


train['default_profile']=train['default_profile'].replace({True :1, False: 0})

train['default_profile_image']=train['default_profile_image'].replace({True :1, False: 0})

x_train,x_test,y_train,y_test=train_test_split(train.iloc[:,1:],train.iloc[:,0],test_size=0.2)

forest=RandomForestClassifier(n_estimators=100)
forest.fit(x_train,y_train) #Training

from sklearn.metrics import accuracy_score,confusion_matrix

accuracy_score(y_test,forest.predict(x_test))

confusion_matrix(y_test,forest.predict(x_test))

accuracy_score(y_train,forest.predict(x_train))

train["label"].value_counts()


forest.feature_importances_



test.select_dtypes(object) 

test_id=pd.merge(ids,ids_labels_test,on="coded_id",how="right") 

test=pd.merge(test_id,features,on="user_id",how="left")
 
test=test.drop(list(test.select_dtypes(object).columns),axis=1)
test["utc_offset"].fillna(test["utc_offset"].mean(),inplace=True)
del test["spam_in_screen_name"]
 
 
test['default_profile']=test['default_profile'].replace({True :1, False: 0})
 
test['default_profile_image']=test['default_profile_image'].replace({True :1, False: 0})

test["label"]=forest.predict(test.iloc[:,3:])

ids_label_test=pd.merge(test[["coded_id","label"]],ids_labels_test["coded_id"],on="coded_id",how="right")

ids_label_test.to_csv("ids_label_test.csv",index=None)

