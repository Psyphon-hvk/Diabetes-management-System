import pandas as pd
import joblib
from sklearn.neighbors import KNeighborsClassifier

# Load the remodeled meal dataset
file_path = "remodeled_meal_glycemic_index.xlsx"
df = pd.read_excel(file_path)

# Features (Glycemic Index) and Target (Category)
X = df[["Glycemic Index"]]
y = df["Category_Numeric"]

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)  # 3 nearest neighbors
knn.fit(X, y)

# Save the trained model
joblib.dump(knn, "knn_model.pkl")

print("✅ KNN model trained and saved successfully!")
