from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import *


class IndexView(ListView):
    template_name = 'index.html'
    model = Question
    context_object_name = 'questions'

class QuestionDetail(DetailView):
    template_name = 'question.html'
    model = Question    
    
class ResultsView(DetailView):
    template_name = 'results.html'
    model = Question 
    
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "question.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))