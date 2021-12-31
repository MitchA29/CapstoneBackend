from django.urls import path
from stories import views

urlpatterns = [
    path('all/',views.get_all_stories),
    path('',views.user_stories)
]