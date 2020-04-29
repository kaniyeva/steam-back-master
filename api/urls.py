from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('', views.CategoryListView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:id>/', views.category_detailed),
    path('games/', views.GamesView.as_view()),
    path('games/<int:id>/', views.game_details),
    path('games/review/', views.ReviewView.as_view()),
    path('login/', obtain_jwt_token)
]