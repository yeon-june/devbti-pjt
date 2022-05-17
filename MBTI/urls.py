from django.urls import path
from . import views

app_name = 'mbti'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:question_pk>/', views.question_page, name='question_page'),
    path('<str:mbti>/', views.result_page, name='result_page'),
    path('<str:mbti>/share/', views.share_result_page, name='share_result_page'),
]