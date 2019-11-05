#Use Logistic Regression
import numpy as np
import pandas as pd
import sklearn as sk
import datetime
import os
import seaborn as sns#数据可视化
from datetime import date
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
import pickle #用于存储模型
import seaborn as sns
from sklearn.metrics import *
from sklearn.model_selection import *
from sklearn.linear_model import LogisticRegression
import matplotlib
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC,Ridge
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVR
from sklearn.preprocessing import RobustScaler
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
# import xgboost as xgb
# import lightgbm as lgb
# from catboost import Pool, CatBoostRegressor

train_data = pd.read_csv('case2_training.csv')
test_data =pd.read_csv('case2_testing.csv')
y_train = train_data['Price']
combine_data = pd.concat((train_data,test_data)).reset_index(drop=True)
combine_data.drop(['Price','ID'],axis=1,inplace=True)


print("数据共有",combine_data.shape[1],"列,",combine_data.shape[0],"行\n")
print("训练集有",train_data.shape[0],'行',"测试集有",test_data.shape[0],"行\n")
print("object数据共有",combine_data.dtypes[combine_data.dtypes=='object'].value_counts().sum(),"列\n")
print("非object数据共有",combine_data.dtypes[combine_data.dtypes!='object'].value_counts().sum(),"列\n")
#print('the columns name of test dataset:\n',test.columns)
#print(train.info())
#10个特征，50000行数据
#print(train.date_account_created.value_counts().head())
#print(train.date_account_created.value_counts().tail())
#print(train.isnull().sum())

"""
数据共有 8 列, 70000 行

训练集有 50000 行 测试集有 20000 行

object数据共有 0 列

非object数据共有 8 列,8列字符串

"""
train_data = combine_data[:train_data.shape[0]]
train_data = pd.concat((train_data,y_train),axis=1)
#左边两图，SalePrice的分布以及QQ图
#右边两图，log(SalePrice)的分布及QQ图
#取对数后更趋向正态分布
fig = plt.figure(figsize=(14,8))
plt.subplot2grid((2,2),(0,0))
sns.distplot((train_data['Price']))
plt.subplot2grid((2,2),(0,1))
sns.distplot(np.log((train_data['Price'])),fit=norm)
plt.subplot2grid((2,2),(1,0))
res = stats.probplot(train_data['Price'], plot=plt)
plt.subplot2grid((2,2),(1,1))
res = stats.probplot(np.log(train_data['Price']), plot=plt)


corrmat = abs(train_data.corr())
plt.subplots(figsize=(12,9))
sns.heatmap(corrmat, vmax=0.9, square=True)


fig = plt.figure(figsize=(14,8))
abs(train_data.corr()['Price']).sort_values(ascending=True).plot.bar()
plt.xticks(fontsize=20)

#how beds affect price
fig = plt.figure(figsize=(14,8))
plt.scatter(x=train_data['Beds'],y=train_data['Price'])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("Beds",fontsize=20)
plt.ylabel("Price",fontsize=20)

fig = plt.figure(figsize=(14,8))
plt.scatter(x=train_data['Review'],y=train_data['Price'])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("Review",fontsize=20)
plt.ylabel("Price",fontsize=20)

fig = plt.figure(figsize=(14,8))
plt.scatter(x=train_data['Accept'],y=train_data['Price'])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("Accept",fontsize=20)
plt.ylabel("Price",fontsize=20)

fig = plt.figure(figsize=(10,6))
plt.scatter(x=train_data['Beds'],y=train_data['Price'])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("Pic Quality",fontsize=20)
plt.ylabel("Price",fontsize=20)
plt.show()

n_folds = 5
def rmsle_cv(model):
    kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(train_data.values)
    rmse= np.sqrt(-cross_val_score(model, train_data.values, y_train.values, scoring="neg_mean_squared_error", cv = kf))
    return(rmse)

lasso = make_pipeline(RobustScaler(), Lasso(alpha =0.2, random_state=3))
ridge = make_pipeline(RobustScaler(), Ridge(alpha =0.2, random_state=6))

score = rmsle_cv(lasso)
print("Lasso Score: ",score.mean())
score = rmsle_cv(ridge)
print("ridge Score: ",score.mean())
KRR = KernelRidge()
score = rmsle_cv(KRR)
print("KRR Score: ",score.mean())
"""
KernelRidge(alpha=1, coef0=1, degree=3, gamma=None, kernel='linear',kernel_params=None)
"""
