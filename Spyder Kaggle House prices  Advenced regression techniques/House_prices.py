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

#Supression arbitraire des colonnes "inutiles"
df_train = df_train.drop(["MSSubClass","MSZoning","LotFrontage","LotArea","Street","Alley","LotShape","LandContour",
                          "Utilities","LotConfig","LandSlope","Neighborhood","Condition2","BldgType","OverallQual",
                         "OverallCond","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","ExterQual",
                         "ExterCond","Foundation","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2",
                         "BsmtFinSF2","BedroomAbvGr","KitchenAbvGr","BsmtUnfSF","HeatingQC","LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath",
                         "FullBath","HalfBath","KitchenQual","Functional","Fireplaces","FireplaceQu","GarageYrBlt",
                         "GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PoolQC","MiscFeature",
                         "MiscVal","MoSold","SaleType","SaleCondition"], axis = 1)

#On renomme les variable de manière à les rendre intélligible...
df_train = df_train.rename(index=str, columns={"Condition1" : "TypeAcces", 
                                 "HouseStyle" : "StyleStructure",
                                 "YearBuilt" : "AnneeConstruction",
                                 "YearRemodAdd" : "AnneeRenovattion",
                                "MasVnrArea" : "SurfaceBrique",
                                "BsmtQual" : "HauteurMaison",
                                "TotalBsmtSF" : "SurfaceMaison",
                                "Heating" : "TypeChauffage",
                                "CentralAir" : "Climatiseur",
                                "Electrica l" : "SystemeElectrique",
                                "1stFlrSF" : "Surface1E",
                                "2ndFlrSF" : "Surface2E",
                                "Bedroom" : "NbChambres",
                                "Kitchen" : "NbCuisines",
                                "TotRmsAbvGrd" : "NbTotChambres",
                                "GarageType" : "EmplacementGarage",
                                "PavedDrive" : "RoutePavee",
                                "WoodDeckSF" : "SurfaceCoureBois",
                                "OpenPorchSF" : "SurfacePorcheExt",
                                "EnclosedPorch" : "SurfacePorcheInt",
                                "3SsnPorch" : "SurfacePorche3saisons",
                                "ScreenPorch" : "SurfaceVerenda",
                                "PoolArea" : "SurfacePiscine",
                                "Fence" : "QualiteCloture",
                                "YrSold" : "AnneeVente",
                                "SalePrice" : "PrixVente"})

#Remplacement des valeurs nan des colonnes concernées par un string "NA".
df_train['EmplacementGarage'] = df_train['EmplacementGarage'].fillna("NA")
df_train['QualiteCloture'] = df_train['QualiteCloture'].fillna("NA")
df_train['Electrical'] = df_train['Electrical'].fillna("NA")
df_train['HauteurMaison'] = df_train['HauteurMaison'].fillna("NA")

#On remplace les valeurs nan de la colonne SurfaceBrique par des 0

df_train['SurfaceBrique'] = df_train['SurfaceBrique'].fillna(0)


df_train.info()

sb.heatmap(df_train.corr(), annot=True)
