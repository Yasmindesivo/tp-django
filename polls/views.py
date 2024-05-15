from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from polls.models import Question


# Create your views here.

#view: lógica

def index(request):
    questions = Question.objects.order_by("-date") #Ordena del mas nuevo a más viejo

    context = {
        "questions":questions
    }

    return render(request, "index.html", context)
    
def detail(request, question_id):
    return HttpResponse("This is question number: " + str(question_id))