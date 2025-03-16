import pandas as pd
import joblib
import numpy as np

# Load the trained KNN model
knn = joblib.load("knn_model.pkl")

# Load the meal dataset
df = pd.read_excel("remodeled_meal_glycemic_index.xlsx")

# Function to recommend meals based on blood sugar level
def recommend_meals(blood_sugar):
    # Convert blood sugar to a Glycemic Index category
    if blood_sugar < 70:
        category = 2  # High-GI meals for low blood sugar
    elif 70 <= blood_sugar <= 140:
        category = 1  # Medium-GI meals for normal levels
    else:
        category = 0  # Low-GI meals for high blood sugar

    # Find meals similar to the given category
    glycemic_index = np.array([[blood_sugar]])
    neighbors = knn.kneighbors(glycemic_index, n_neighbors=5, return_distance=False)
    
    recommended_meals = df.iloc[neighbors[0]]["Meal Combination"].tolist()
    
    return recommended_meals

# Test the function
if __name__ == "__main__":
    test_sugar = 85  # Example blood sugar level
    print(f"Recommended meals for blood sugar {test_sugar}:")
    print(recommend_meals(test_sugar))
