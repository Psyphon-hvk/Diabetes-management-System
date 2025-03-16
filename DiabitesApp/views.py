from django.shortcuts import render
from .knn_recommender import recommend_meals  # Import our KNN function

# Home page view
def home_view(request):
    return render(request, "home.html")  # This loads the home page first

def meal_recommendation(request):
    recommended_meals = None

    if request.method == "POST":
        blood_sugar = float(request.POST.get("blood_sugar"))  # Get user input
        recommended_meals = recommend_meals(blood_sugar)  # Get meal recommendations

    return render(request, "recommend.html", {"meals": recommended_meals})

def predict_view(request):
    return render(request, "predict.html")

def records_view(request):
    return render(request, "records.html")
