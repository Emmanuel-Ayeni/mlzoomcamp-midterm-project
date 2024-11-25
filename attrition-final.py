#!/usr/bin/env python
# coding: utf-8

import os
import pickle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import roc_auc_score

# Set random seed
SEED = 42

# Initialize Kaggle API and authenticate
api = KaggleApi()
api.authenticate()

# Define the Kaggle dataset identifier and the local download path
dataset_name = "itssuru/HR-Employee-Attrition"
current_dir = os.getcwd()
project_dir = os.path.join(current_dir, "data")
os.makedirs(project_dir, exist_ok=True)

# Download and extract the dataset
api.dataset_download_files(dataset_name, path=project_dir, unzip=True)
print(f"Dataset downloaded and extracted to {project_dir}")

# Define CSV file path
csv_file_name = "HR-Employee-Attrition.csv"  # Update if necessary
csv_file_path = os.path.join(project_dir, csv_file_name)

# Check if the file exists and load the data
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"File not found: {csv_file_path}")

df = pd.read_csv(csv_file_path)
print("Dataset preview:")
print(df.head())

# Preprocess the data
df.columns = df.columns.str.lower().str.replace(' ', '_')
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for col in categorical_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')

# Drop unnecessary columns
df.drop(['employeecount', 'over18', 'standardhours'], axis=1, inplace=True)

# Split the data
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=SEED)
df_full_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=SEED)

# Define target variables
y_train = (df_full_train.attrition == 'yes').values
y_test = (df_test.attrition == 'yes').values

df_full_train.drop(columns=['attrition'], inplace=True)
df_test.drop(columns=['attrition'], inplace=True)

# Convert data to dictionary format and apply one-hot encoding
dict_train = df_full_train.fillna(0).to_dict(orient='records')
dict_test = df_test.fillna(0).to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(dict_train)
X_test = dv.transform(dict_test)

# Train the XGBoost model
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=dv.feature_names_)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=dv.feature_names_)

xgb_params = {
    'eta': 0.3,
    'max_depth': 6,
    'min_child_weight': 1,
    'objective': 'binary:logistic',
    'nthread': 8,
    'seed': SEED,
    'verbosity': 1,
}
num_trees = 100

model = xgb.train(xgb_params, dtrain, num_boost_round=num_trees)

# Evaluate the model
y_pred_xgb = model.predict(dtest)
roc_auc = roc_auc_score(y_test, y_pred_xgb)
print(f"ROC AUC Score: {roc_auc}")

# Save the model and DictVectorizer
output_file = f"model_xgb.bin"
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)
print(f"Model saved to {output_file}")
