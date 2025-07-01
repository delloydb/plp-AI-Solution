# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BreastCancer.csv"
df = pd.read_csv(url)

# Preview data
print("Initial data shape:", df.shape)
print(df.head())

# Drop irrelevant columns
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Convert diagnosis into priority classes
# Malignant (M) = High Priority, Benign (B) = Low Priority
df['priority'] = df['diagnosis'].map({'M': 'High', 'B': 'Low'})

# Encode priority for modeling
df['priority_label'] = df['priority'].map({'High': 1, 'Low': 0})

# Drop original diagnosis column
df.drop('diagnosis', axis=1, inplace=True)

# Define features and target
X = df.drop(['priority', 'priority_label'], axis=1)
y = df['priority_label']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\nModel Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Low', 'High']))

# Feature importance plot
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=features[indices], palette="viridis")
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()
