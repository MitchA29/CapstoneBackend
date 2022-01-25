from django.urls import path
from clubs import views

urlpatterns = [
    path('all/',views.get_all_clubs),
    path('',views.user_clubs),
    path('delete/<int:pk>',views.clubs_delete)
]