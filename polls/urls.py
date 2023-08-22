from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('question/<int:pk>/results/', ResultsView.as_view(), name='results'),
]