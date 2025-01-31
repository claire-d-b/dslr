import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer

# Step 1: Load the datasets (replace these with your actual file paths)
data1 = pd.read_csv('dataset_train.csv')  # Training data
data2 = pd.read_csv('dataset_test.csv')  # Testing data

# Step 2: Preprocess the Data
# Assuming that the target variable is the last column in the datasets

# Extract features and target for both datasets
X_train = data1.iloc[:, 6:]  # Features (all columns except last)
y_train = data1.iloc[:, 1]   # Target (last column)

print("xtrain", X_train)
print("ytrain", y_train)
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
y_test_imputed = imputer.transform(y_test.values.reshape(-1, 1)).ravel()

# Step 3: Feature Scaling
# It's often a good idea to scale features for logistic regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

# Step 4: Train Logistic Regression Model
model = LogisticRegression(max_iter=200)  # You can adjust max_iter if needed
model.fit(X_train_scaled, y_train_imputed)

# Step 5: Make Predictions on the test set
y_pred = model.predict(X_test_scaled)

# Save the predictions to a CSV file
pd.DataFrame(y_pred).to_csv('predictions.csv', index=False)

# # Step 6: Evaluate the Model
# accuracy = accuracy_score(y_test_imputed, y_pred)
# print(f"Accuracy: {accuracy:.4f}")

# # Confusion Matrix
# cm = confusion_matrix(y_test_imputed, y_pred)
# print("Confusion Matrix:")
# print(cm)

# # Optionally, print classification report for more details
# (precision, recall, f1-score)
# print("Classification Report:")
# print(classification_report(y_test_imputed, y_pred))
