# Importing necessary packages
import numpy as np
import pandas as pd
import datetime
import time

from Input_PreProcessor import Input_PreProcessor
from Models import First_Model_SVR
from Models import SVR_Predictor
from Models import Second_Model_KRR
from Models import KRR_Predictor
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from func import DTFormatOpt

# Reading the data
Address_train = 'C:/Users/nekooeimehr/AppData/Local/Programs/Python/Python35-32/ImanNekooeimehrStateFarmSampleCode/State Farm Data Science WORK SAMPLE/Data for Cleaning & Modeling.csv'
Address_test = 'C:/Users/nekooeimehr/AppData/Local/Programs/Python/Python35-32/ImanNekooeimehrStateFarmSampleCode/State Farm Data Science WORK SAMPLE/Holdout for Testing Method 2.csv'
Address_test_SVR = 'C:/Users/nekooeimehr/AppData/Local/Programs/Python/Python35-32/ImanNekooeimehrStateFarmSampleCode/State Farm Data Science WORK SAMPLE/Results Method 1.csv'
Address_test_KRR = 'C:/Users/nekooeimehr/AppData/Local/Programs/Python/Python35-32/ImanNekooeimehrStateFarmSampleCode/State Farm Data Science WORK SAMPLE/Results Method 2.csv'

IntRate_train_data = pd.read_csv(Address_train, low_memory=False)
IntRate_train_data = IntRate_train_data.drop(IntRate_train_data.index[399999])
IntRate_train_data = IntRate_train_data.dropna(subset = ['X1'])
IntRate_test_data = pd.read_csv(Address_test, low_memory=False)
IntRate_whole_data = pd.concat([IntRate_train_data, IntRate_test_data], keys=['x', 'y'])

(Processed_Train_data2, Processed_Test_data) = Input_PreProcessor(IntRate_whole_data)

Processed_Train_data = Processed_Train_data2.sample(n = 2000, replace=False)

# Seperating the input variables(Predictors) and the output variable and scaling the input variables
Input_train_Data = Processed_Train_data.iloc[:,1:]
Scaled_train_Data = scale(Input_train_Data)
Output_Data = Processed_Train_data['X1']
Input_test_Data = Processed_Test_data.iloc[:,1:]
Scaled_test_Data = scale(Input_test_Data)

#######################################First Model: Support Vector Regression######################################################
# Building the model
(MeanMSE_SVR, svr_Tuned) = First_Model_SVR(Scaled_train_Data, Output_Data)

# Predicting the test set using the built model
#SVR_Results = SVR_Predictor(svr_Tuned, Scaled_test_Data, Address_test_SVR)

#######################################Second Model: Kernel Ridge Regression######################################################
# Building the model
(MeanMSE_KRR, krr_Tuned) = Second_Model_KRR(Scaled_train_Data, Output_Data)

# Predicting the test set using the built model
#KRR_Results = KRR_Predictor(krr_Tuned, Scaled_test_Data, Address_test_KRR)

