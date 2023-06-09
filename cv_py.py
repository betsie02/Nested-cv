# -*- coding: utf-8 -*-
"""cv.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QGwWcZUnKRhdpdbGZw6uZdLV3woU5hD2
"""

import pandas as pd
from types import GeneratorType

class NestedCV:
    def __init__(self, k):
        self.k = k

    def split(self, data, date_column):
        # Sort the data by the date column
        data = data.sort_values(date_column)
        
        # Calculate the number of samples in each fold
        n = len(data)
        fold_size = n // self.k

        # Generate train and validate splits
        for i in range(self.k):
            # Calculate the start and end indices of the validate split
            validate_start = i * fold_size
            validate_end = (i + 1) * fold_size if i < self.k - 1 else n
            
            # Extract the validate split
            validate = data.iloc[validate_start:validate_end].copy()
            
            # Extract the train split
            train = data.iloc[:validate_start].copy()

            yield train, validate

if __name__ == "__main__":
    # Load dataset
    data = pd.read_csv("/content/train.csv")
    data["date"] = pd.to_datetime(data["date"])

    # Nested CV
    k = 3
    cv = NestedCV(k)
    splits = cv.split(data, "date")

    # Check return type
    assert isinstance(splits, GeneratorType)

    # Check return types, shapes, and data leaks
    count = 0
    for train, validate in splits:
        # Types
        assert isinstance(train, pd.DataFrame)
        assert isinstance(validate, pd.DataFrame)

        # Shape
        assert train.shape[1] == validate.shape[1]

        # Data leak check
        train_dates = train["date"]
        validate_dates = validate["date"]
        if train_dates.max() >= validate_dates.min():
            raise AssertionError("Data leak detected. Training set and validation set have overlapping date ranges.")

        count += 1

    # Check number of splits returned
    assert count == k