# Python-Data-Analysis-Sample-Project
I did this project in Python for a private insurance company as work sample. The dataset contains the data for almost half million borrowers with 32 features. The purpose was to make a model to predict the interest rate. 

Before starting analyzing the data, I spent a good amount of time understanding all the variables by checking them on internet and looking their values and their statistics. Based on my opinion understanding the problem and in particular the definition of the variables will give a very good insight on how to model the data. I also spend most of my time cleaning the data. I think it is very true in data mining that “garbage in, garbage out”. Therefore, it is very important to clean and preprocess the data as much as possible. I have done the following steps to preprocess and model the dataset.

  1.	Deleting useless variables.
Some of the variables were removed from the dataset 
    •	The IDs: IDs are unique for each example in the dataset, hence they do not provide any additional information to the model.
    •	Employer or job title: It may have effects on the model, however since competitors are not allowed to use any external data and also the answers are so different for each borrower as it is self-filled, it was removed from the set of variables.
    •	Reason for loan provided by borrower: Similar to the last variable that was removed. Also, this variable is empty in the testing set for all the borrowers.
    •	First 3 numbers of zip code and state of borrower: Could be a very important variable. However, since it is not allowed to use external data, it was removed from the set of variables . 

  2.	Converting the columns with dollar and percentage sign to floats
As an important step in cleaning the data, the variables which could be mistakenly considered as strings were converted to numerical variables by removing their string part.

  3.	Handling missing values
Missing values were replaced with median if they’re continuous and by mode if they’re categorical. Median was used instead of mean, because it is more robust to non-normal data and it is computationally less expensive.

  4.	Handling categorical variables by converting them to binary dummy variables
The categorical variables were converted to binary dummy variables. For the variable “loan subgrade”, by surfing on internet, it was noticed that this variable could be considered as an ordinal variable, hence it was converted to numbers.

  5.	Transforming some of the variables 
Some of the variables were transformed to better help the model. These transformation include:
    •	Variable X5 were subtracted from variable X4: Variable X5 and X4 were highly correlated and in most of the examples, they have equal values. The new variable “X5-X4” is not correlated to “X4” anymore.
    •	Variable X15 were categorized to 4 quarters and then converted to binary dummy variables: This variable represent the time of the year the loans were issued. Depending on the periods of the year, the interest rate could be different. For instance, normally the interest rates are higher when issued closer to the end of the year. 
    •	Variable X23 were subtracted from the most recent credit line which was opened among all the borrowers: The new variable represents the relative duration of borrowers having credit lines or in other words, the relative age of each borrower’s credit line.
    •	Variable X11 were converted to floats: Variable “X11” for borrowers with work experience less than 1 year who have also missing values for their "employer or job title" were replaced with 0 years of being employed. Variable “X11” for borrowers with work experience less than 1 year who have values for their "employer or job title" were replaced with 1. Finally, variable X11 for borrowers with work experience more than 10 years were replaced with 15 years of experience.

After preparing the dataset, two models were developed to predict the interest rates. First model is Support Vector Regression (SVR) and the second model is Kernel Ridge Regression (KRR). For tuning the parameters of the model, random permutation cross validation was used in which in each iteration 0.01% of the dataset was used for training and 0.05% of the dataset was used for validation. The process repeats 10 times and find the parameters which denote the lowest MSE. The best parameters were selected among C = [0.1, 1, 10, 100] and gamma = [0.01, 0.1, 1, 10]. 

Both of these methods are taking advantage of the kernel trick in which the original space is transformed to a non-linear space. Both have a penalty term (L1 norm) in their objective functions which help the generality of the model. The parameter of the penalty term in both models can trade-off between the model complexity and generality. In general, the difference between the two methods is their loss function. For ridge regression it is the ridge and for SVR is the epsilon-insensitive loss. In terms of complexity, both are time consuming for such a large dataset and that’s why a smaller portion of the dataset was used for training and validation. However, KRR is faster for training, while SVR is faster for predicting, because SVR just uses a small portion of the training examples called support vectors. In terms of MSE, using 10-fold CV on a sample dataset of 2000 borrowers, SVR outperforms KRR. The MSE for SVR was 3.77748, while for KRR it was 4.37456.          
Finally, the test set were predicted using the built models and the results were written in the .CSV file. 

