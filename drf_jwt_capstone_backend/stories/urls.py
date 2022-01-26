from django.urls import path
from stories import views

urlpatterns = [
    path('all/',views.get_all_stories),
    path('',views.user_stories),
    path('delete/<int:pk>',views.stories_delete),
    path('read/<int:pk>',views.read_story)
]