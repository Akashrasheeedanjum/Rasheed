
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('manager_dashbord/', views.manager_dashbord, name='manager_dashbord'),
    path('add_center/', views.add_center, name='add_center'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('purchase_milk/', views.purchase_milk, name='purchase_milk'),
    path('sale_milk/', views.sale_milk, name='sale_milk'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('recive_payment/', views.recive_payment, name='recive_payment'),
    path('center_details/', views.center_details, name='center_details'),
    path("deleteCenterMilk/<int:id>/<int:pid>",views.deleteCenterMilk,name="deleteCenterMilk"),
    path("editCenterMilk/<int:id>/<int:pid>",views.editCenterMilk,name="editCenterMilk"),
    path("deleteCenter/<int:id>/",views.deleteCenter,name="deleteCenter"),
    path("deleteCenterPayment/<int:id>/<int:pid>",views.deleteCenterPayment,name="deleteCenterPayment"),
     path("deleteCustomer/<int:id>",views.deleteCustomer,name="deleteCustomer"),
    path("deleteCustomerPayment/<int:id>/<int:pid>",views.deleteCustomerPayment,name="deleteCustomerPayment"),
    path("deleteExpence/<int:id>/<int:pid>",views.deleteExpence,name="deleteExpence"),
    path("deleteSalePayment/<int:id>/<int:pid>",views.deleteSalePayment,name="deleteSalePayment"),
    path('customer_details/', views.customer_details, name='customer_details'),
    path('view_center/<int:pid>/', views.view_center, name='view_center'),
    path('view_customer/<int:pid>/', views.view_customer, name='view_customer'),
    path('register_customer_ex', views.register_customer_ex, name='register_customer_ex'),
    path('add_customer_ex', views.add_customer_ex, name='add_customer_ex'),
    path('PNL', views.PNL, name='PNL'),
    path('BetweenPNL', views.BetweenPNL, name='BetweenPNL'),
]
