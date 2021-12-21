from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# vote action
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))