import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from datetime import datetime
from func import DTFormatOpt

        
def Input_PreProcessor(IntRate_whole_data):

    # Deleting the unuseful features like the IDs 
    IntRate_Dropped = IntRate_whole_data.drop(['X2','X3','X8','X16','X18','X19','X20'], axis=1)

    # Converting the columns with dollor and percentage sign to floats
    IntRate_Dropped[['X4','X5','X6']] = IntRate_Dropped[['X4','X5','X6']].replace('[\$,]','', regex=True).astype(float)
    IntRate_Dropped[['X1','X30']] = IntRate_Dropped[['X1','X30']].replace('[,\%]','', regex=True).astype(float)

    # Variable X9 were converted to numbers to take into account the ordinal relationship among the values
    IntRate_Dropped['X9'] = IntRate_Dropped['X9'].rank(method = 'dense')

    # Handeling the missing values by replacing them with median if continous and by mode if categorical
    IntRate_Dropped['X26'].fillna(0, inplace = True)
    IntRate_Dropped['X25'].fillna(0, inplace = True)
    IntRate_Dropped.fillna(IntRate_Dropped.median()['X4':], inplace = True)
    Ctg_Ind_Miss = ['X7','X11','X12','X14','X15','X17','X23','X32']
    IntRate_Dropped[Ctg_Ind_Miss] = IntRate_Dropped[Ctg_Ind_Miss].apply(lambda x:x.fillna(x.value_counts().index[0]))

    # Handeling categorical features by converting them to binary dummy variables
    Ctg_Ind = ['X7','X12','X14','X17','X32']
    IntRate_Dummies = pd.get_dummies(IntRate_Dropped[Ctg_Ind],drop_first = True)
    IntRate_NoMiss = IntRate_Dropped.join(IntRate_Dummies)
    IntRate_NoMiss = IntRate_NoMiss.drop(Ctg_Ind, axis=1)

    # Transforming some of the variables
        # Variable X5 were subtracted from variable X4
    IntRate_NoMiss['X5'] = IntRate_NoMiss['X4'] - IntRate_NoMiss['X5']

        # Variable X15 were categorized to 4 quearters and then binarized.
    IntRate_NoMiss['X15'] =  pd.to_datetime(IntRate_NoMiss['X15'], format='%d-%b')
    IntRate_NoMiss['X15'] = IntRate_NoMiss['X15'].dt.quarter
    IssueDate_Dummies = pd.get_dummies(IntRate_NoMiss['X15'],drop_first = True)
    IntRate_NoMiss = IntRate_NoMiss.join(IssueDate_Dummies)
    IntRate_NoMiss = IntRate_NoMiss.drop(['X15'], axis=1)

        # Variable X23 were subtracted from the most recent credit line which were opened among all the borrowers () to denote the relative duration of borrowers having credit lines.  
    Flist = ['%b-%y','%d-%b']
    IntRate_NoMiss['X23'] =  IntRate_NoMiss['X23'].apply(lambda x: DTFormatOpt(str(x),Flist))
    IntRate_NoMiss['X23'] = IntRate_NoMiss['X23'].map(lambda dt: dt.replace(year=2001) if dt.year==1900 else dt.replace(year=dt.year))
    IntRate_NoMiss['X23'] = IntRate_NoMiss['X23'].map(lambda dt: dt.replace(year=dt.year-100) if dt.year>2020 else dt.replace(year=dt.year))
    Most_Recent_Date = IntRate_NoMiss['X23'].max()
    Days_CreditLine = Most_Recent_Date - IntRate_NoMiss['X23']
    IntRate_NoMiss['X23'] = Days_CreditLine.dt.days.astype(float)
         
        # Variable X11 were converted to floats:
            # Variable X11 for Customers with work experience less than 1 year who have also missing values for their "employer or job title" were replaced with 0.
            # Variable X11 for Customers with work experience less than 1 year who have values for their "employer or job title" were replaced with 1.
            # Variable X11 for Customers with work experience more than 10 years were replaced with 15 years of experiance as an average.
    IntRate_NoMiss['X11'] = IntRate_NoMiss['X11'].replace('[,years]'or '[,year]','', regex=True ).replace( '10\+','15', regex=True)
    IntRate_NoMiss.ix[(IntRate_NoMiss['X10'].isnull())&(IntRate_NoMiss['X11'].str.contains('< 1').astype('bool')),'X11'] = '0'
    IntRate_NoMiss.ix[(IntRate_NoMiss['X10'].notnull())&(IntRate_NoMiss['X11'].str.contains('< 1').astype('bool')),'X11'] = '1'
    IntRate_NoMiss['X11'] = IntRate_NoMiss['X11'].convert_objects(convert_numeric=True)
    IntRate_Final = IntRate_NoMiss.drop(['X10'], axis=1)
    IntRate_Final.fillna(IntRate_Final.median()['X4':], inplace = True)
    IntRate_Train_Final = IntRate_Final.ix['x']
    IntRate_Test_Final = IntRate_Final.ix['y']
    # assert (IntRate_Train_Final.shape[0]-IntRate_Train_Final.dropna().shape[0]) == 0,'The training dataset still has missing values'

    return(IntRate_Train_Final, IntRate_Test_Final)
