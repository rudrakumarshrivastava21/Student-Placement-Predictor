import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
student_data = pd.read_csv('placement_data.csv')

# Select inputs and output
features = student_data[['cgpa', 'iq']]
target = student_data['placement']

# Split the dataset into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Check how well the model performs
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2%}")

# Try a sample prediction
test_student = [[9.9, 115]]
result = model.predict(test_student)

print("\nPrediction result:")
if result[0] == 1:
    print("This student will probably get placed")
else:
    print("This student might need some improvement before placement")