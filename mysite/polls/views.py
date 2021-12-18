from django.template import loader
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# homepage
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5] # returns 5 most recent questions
    # template = loader.get_template('polls/index.html') # load template
    context = {
        'latest_question_list': question_list, # pass argument to template : the questions list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

# a question page
def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    
    # BETTER ALTERNATIVE to maintain loose coupling : get_object_or_404
    question = get_object_or_404(Question, pk=question_id) # calls get() function of the model’s manager, raises Http404 if the object doesn’t exist.
    return render(request, 'polls/detail.html', {'question': question})

# results of question page
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# vote action
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)