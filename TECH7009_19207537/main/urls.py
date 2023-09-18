from django.urls import path
from . import views

urlpatterns = [
     path('display/', views.display, name='display'),
    path('home/', views.home, name="home"),
    path('commonattractions/', views.commonattractions, name="commonattractions"),
    path("itinerary_result/<str:generated_itinerary>/", views.itinerary_result, name="itinerary_result"),
]