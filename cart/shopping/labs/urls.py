from django.urls import path
from . import views


urlpatterns=[
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
    path('labs/', views.addlabs, name='addlabs'),
    path('services/', views.addservices, name='addservices'),
    path('shop/', views.shop, name='shop'),
]