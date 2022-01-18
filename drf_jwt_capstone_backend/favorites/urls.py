from django.urls import path
from favorites import views

urlpatterns = [
    path('all/',views.get_all_favorites),
    path('',views.user_favorites),
    path('delete/<str:pk>',views.delete_favorite)
]