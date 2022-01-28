from django.urls import path
from members import views

urlpatterns = [
    path('all/',views.get_all_members),
    path('',views.user_members),
    path('delete/<str:pk>',views.delete_Member)
]