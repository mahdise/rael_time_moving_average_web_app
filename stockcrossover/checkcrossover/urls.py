from django.urls import path

from . import views

app_name = 'checkcrossover'

urlpatterns = [
    path('start/', views.StartPullData.as_view()),
    path('result/', views.Result.as_view()),

]
