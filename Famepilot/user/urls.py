from django.urls import path
from user import views

urlpatterns = [
  path("",views.index,name='index'),
  path("signup",views.signup,name='signup'),
  path("login",views.handlelogin,name="handlelogin"),
  path('logout', views.handlelogout, name="handlelogout"),
]
