
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Register,name='register'),
    path('login',views.Login,name="login"),
    path('logout/',views.Logout,name='logout'),
    path('show',views.Show,name='show')
]
