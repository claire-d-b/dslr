import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

# Step 1: Load the datasets (replace these with your actual file paths)
data1 = pd.read_csv('dataset_train.csv')  # Training data
data2 = pd.read_csv('dataset_test.csv')  # Testing data

# Step 2: Preprocess the Data
# Assuming that the target variable is the last column in the datasets

# Extract features and target for both datasets
X_train = data1.iloc[:, 6:]  # Features (all columns except last)
y_train = data1.iloc[:, 1]   # Target (last column)

X_test = data2.iloc[:, 6:]   # Features (all columns except last)
y_test = data2.iloc[:, 1]    # Target (last column)

# Create an imputer to fill missing values with the mean of each column
imputer = SimpleImputer(strategy='mean')

# Apply the imputer to both the training and test sets
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Initialize the imputer to use the most frequent value for imputation
imputer = SimpleImputer(strategy='most_frequent')

# Impute missing values in the target variable
y_train_imputed = imputer.fit_transform(y_train.values.reshape(-1, 1)).ravel()

# Step 3: Feature Scaling
# It's often a good idea to scale features for logistic regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

# Step 4: Train Logistic Regression Model
model = LogisticRegression(max_iter=200)  # You can adjust max_iter if needed
model.fit(X_train_scaled, y_train_imputed)

# Load the true values using the same format as your predictions
houses_data = pd.read_csv('houses.csv')

# Assuming 'houses.csv' contains the ground truth labels
# in the same order as test data
# You may need to adjust this depending on your actual
# data structure
# Assuming the target is in the first column
y_true = houses_data.iloc[:, 1].to_numpy()

# Step 5: Make Predictions on the test set
y_pred = model.predict(X_test_scaled)

# Make sure y_true and y_pred have the same length
if len(y_true) != len(y_pred):
    print(f"Warning: Length mismatch between y_true\
          ({len(y_true)}) and y_pred ({len(y_pred)})")
    # Adjust to use only the first matching rows
    min_len = min(len(y_true), len(y_pred))
    y_true = y_true[:min_len]
    y_pred = y_pred[:min_len]

# Step 6: Evaluate the Model
# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)
print(y_true)
print(y_pred)
print(f"Accuracy: {accuracy:.4f}")

y_pred = pd.DataFrame(y_pred).reset_index()
y_pred.columns = ['Index', 'Hogwarts House']

# Save the predictions to a CSV file
y_pred.to_csv('predictions.csv', header=True, index=False)
