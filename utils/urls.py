from django.urls import path
from . import views
urlpatterns = [
    path('randbg/', views.randbg, name='randbg'),
]