from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('home/', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('logout/', views.logout, name = "logout"),
    path('time/', views.time, name = "time"),
    path('users/', views.panel, name = "users"),
    path('users/delete/<int:id>', views.deluser, name = "delete"),
    path('users/update/<int:id>', views.update, name = "update"),  
    path('users/adduser/', views.adduser, name = "adduser"),
    path('products/', views.products, name = "products"),
    path('products/addproduct/', views.addproduct, name = "addproduct")
]
