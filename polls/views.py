from django.views.generic import ListView, DetailView
from .models import *


class IndexView(ListView):
    template_name = 'index.html'
    model = Question
    context_object_name = 'questions'

class QuestionDetail(DetailView):
    template_name = 'question.html'
    model = Question
    
    