from django import forms


class DataForm(forms.Form):
   
    Pregnancies = forms.FloatField()
    Glucose = forms.FloatField()
    BloodPressure =  forms.FloatField()
    SkinThickness = forms.FloatField()
    Insulin = forms.FloatField()
    bmi = forms.FloatField()
    DiabetesPedigreeFunction = forms.FloatField()
    Age  = forms.FloatField()