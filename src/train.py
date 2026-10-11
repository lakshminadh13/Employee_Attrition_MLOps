
from sklearn.tree import DecisionTreeClassifier

# Sample employee data:
# [years of experience, satisfaction score (1-5), overtime (0 or 1)]
X = [
    [1, 2, 1],
    [2, 2, 1],
    [3, 4, 0],
    [5, 5, 0],
    [1, 3, 1],
    [6, 4, 0],
    [2, 1, 1],
    [7, 5, 0],
]

# 1 = employee leaves, 0 = employee stays
y = [1, 1, 0, 0, 1, 0, 1, 0]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[2, 2, 1]])

print("Model training completed.")
print("Employee attrition prediction:", int(prediction[0]))
print("Prediction: " + ("Leaves" if prediction[0] == 1 else "Stays"))
