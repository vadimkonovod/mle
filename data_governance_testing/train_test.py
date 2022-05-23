import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import json
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold, cross_val_predict

train = pd.read_csv('train.csv')

###########################
### DATA CLEANING
###########################
train.replace({'Sex': {'male': 0, 'female': 1}}, inplace=True)
train['Age'].fillna(1000, inplace=True)

###########################
### MODELLING
###########################
y = train['Survived']
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = train[features]

model = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=1)
cv = KFold(n_splits=5, shuffle=True)
yhat = cross_val_predict(estimator= model, X=X, y=y, cv=cv)

acc = np.mean(yhat==y)
tn, fp, fn, tp = confusion_matrix(y, yhat).ravel()
specificity = tn / (tn + fp)
sensitivity = tp / (tp + fn)

with open("metrics.json", 'w') as outfile:
    json.dump({ "accuracy": acc, "specificity": specificity, "sensitivity": sensitivity}, outfile)

###########################
### PLOT FEATURE IMPORTANCE
###########################
model.fit(X, y)
importances = model.feature_importances_
labels = X.columns
feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature", "importance"])
feature_df = feature_df.sort_values(by='importance', ascending=False,)

axis_fs = 18 #fontsize
title_fs = 22 #fontsize
sns.set(style="whitegrid")

ax = sns.barplot(x="importance", y="feature", data=feature_df)
ax.set_xlabel('Importance', fontsize = axis_fs) 
ax.set_ylabel('Feature', fontsize = axis_fs)
ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

plt.tight_layout()
plt.savefig("feature_importance.png",dpi=120) 
plt.close()
