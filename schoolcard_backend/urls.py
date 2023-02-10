from django.urls import path
from . import views

urlpatterns = [
    path('querystudent/', views.QueryStudent.as_view()),
    path('addstudent', views.AddStudent.as_view()),
    path('deletestudent', views.DeleteStudent.as_view()),
    path('pay', views.CardPay.as_view()),
    path('charge', views.CardCharge.as_view()),
]

