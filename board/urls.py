from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='board_main'),
    path('t/<str:thread_id>/', views.thread, name='board_thread'),
    path('add_thread/', views.add_thread, name='board_add_thread'),
    path('add_reply', views.add_reply, name='board_add_reply'),
]