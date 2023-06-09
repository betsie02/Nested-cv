
$ Project Name: Soda Quantity Prediction

$ Description:
  This project aims to predict the quantity of soda based on historical timeseries data. It involves analyzing the data, engineering features, selecting and training regression models, and implementing nested cross-validation for robust evaluation.

$ Problem Statement
  1) We have a dataset which included data about the demand of soda, using which we can predict the quantity. The data is in the form of a timeseries.

  2) We have created a Nested Cross Validation class, which also needs to be implemented while creating the model.                                                                                                                                                                  

$ Table of Contents:

  1)Importing the dependencies

  2)Reading the csv file

  3)Data cleaning
    i)   Romving the unwanted columns in the dataset
    ii)  Handling the null/missing/na values
    iii) Converting litres to ml in the capacity column

  4)Data visualization
  
  5)Data Preprocessing

  6)Splitting the data
  
  7)Model Building

  8)Nested cv method
    i)  Splitting data using nested cv class
    ii) To check stationary
    iii)Using Nested KFold with Machine Learning Models

$ Installation:

  Install the required dependencies by running pip install -r requirements.txt.

$ Dataset:
  The dataset used in this project is publicly available. It contains timeseries data of soda quantity.

$ Data cleaning:
  The given dataset has been cleaned by removing unwanted columns, handling the missing values, and converting the litres form in soda 'capacity' column to millilitres.

$ Data Visualization:
  Various visualization techinques has been used to find the behaviour of the variables or to find the relationship between them.

$ Data Preprocessing:
  Data preprocessing is an important step in preparing your data for analysis and modeling. It involves cleaning, transforming, and organizing the data to improve its quality and suitability for machine learning algorithms.
  
$ Model Evaluation:
  Nested cross-validation is implemented to evaluate the performance of different regression models.
  Evaluation metrics such as mean squared error (MSE), root mean squared error (RMSE), and R-squared (R2) are used to assess model accuracy.

$ Results and Interpretation:
  The best-performing model is selected based on the evaluation results.
  The best-performing models are Gradiest Boosting Regressor and Decision Tree Regression.

