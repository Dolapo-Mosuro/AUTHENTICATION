from importlib.resources import path
from django.contrib.auth import views as auth_views
from . import views
 
urlpatterns = [
    path('login_user/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.home, name='home'),
    path('register/', views.register, name='register'),

]