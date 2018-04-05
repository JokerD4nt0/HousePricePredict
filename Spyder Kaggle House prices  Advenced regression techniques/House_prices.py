# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:50:50 2018
7 mars 2018
@author: Adrien Morla
Adrien Morla
"""
import pandas as pd
import seaborn as sb

df_train = pd.read_csv("../Kaggle Houses prices  Advenced regression techniques/train.csv")
#df_prix = df_train["SalePrice"]
#df_train = df_train.drop(["SalePrice"], axis = 1)


df_train = df_train.drop(["MSSubClass","MSZoning","LotFrontage","LotArea","Street","Alley","LotShape","LandContour",
                          "Utilities","LotConfig","LandSlope","Neighborhood","Condition2","BldgType","OverallQual",
                         "OverallCond","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","ExterQual",
                         "ExterCond","Foundation","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2",
                         "BsmtFinSF2","BsmtUnfSF","HeatingQC","LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath",
                         "FullBath","HalfBath","KitchenQual","Functional","Fireplaces","FireplaceQu","GarageYrBlt",
                         "GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PoolQC","MiscFeature",
                         "MiscVal","MoSold","SaleType","SaleCondition"], axis = 1)

sb.heatmap(df_train.corr(), annot=True)
