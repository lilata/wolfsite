from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.accounts_login, name='login'),
    path('signup/', views.accounts_signup, name='signup'),
    path('logout/', views.accounts_logout, name='logout'),
    path('github_callback/', views.github_callback, name='github_callback'),
    path('github_login/', views.github_login, name='github_login')
]