"""classproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from classapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.homefun,name='index'),
    path('index/userdetails/',views.userfunc,name='userdetail'),
    path('index/Fooddetails/',views.foodfunc,name='fooddetail'),
    path('index/uplodUser/',views.upload_User,name='user'),
    path('index/uplodfood/',views.upload_Food,name='food'),
    path('index/uplodreview/',views.upload_review,name='review'),
    path('index/updatereview/<int:rev_id>',views.update_review),
    path('index/deletereview/<int:rev_id>',views.delete_review),
    path('index/Fooddetails/updatefood/<int:food_id>',views.update_food),
    path('index/Fooddetails/deletefood/<int:food_id>',views.delete_food),
    path('index/userdetails/updateuser/<str:user_id>',views.update_user),
    path('index/userdetails/deleteuser/<str:uname>',views.delete_user,name='dt'),
    path("register/", views.register_request, name="register"),
    path("", views.login_request, name="login"),
]
