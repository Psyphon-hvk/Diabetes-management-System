from django.urls import path
from .views import home_view, meal_recommendation, predict_view, records_view

urlpatterns = [
    path("", home_view, name="home"),  # Home page
    path("recommend/", meal_recommendation, name="meal_recommendation"),
    path("predict/", predict_view, name="predict_view"),
    path("records/", records_view, name="records_view"),
]
