from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('contractor', views.profile, name='profile'),
    path('contractor/profile/<str:username>/', views.profile, name='profile'),
    path('contractor/form/', views.contractorform, name='contractorform'),
    path('contractor/addemployee/', views.addemployee, name='addemployee'),
    path('contractor/employee/', views.employee, name='employee'),
    path('contractor/pdf', views.GeneratePdf, name='GeneratePdf')
]
