from mysite.polls.models import Choice,Question
from django.utils import timezone

print(Question.objects.all()) #show all items 
q = Question(question_text="What's new?", pub_date=timezone.now()) #new question
q.save()
print(q.id) #1
print(q.question_text) #"What's new?"
print(q.pub_date) #datetime.datetime(2021, 12, 18, 22, 36, 36, 705994, tzinfo=datetime.timezone.utc)
#change text 
q.question_text = "What's up?"
q.save()
print(Question.objects.all()) #<QuerySet [<Question: Question object (1)>]>

#after adding __str__ method in Question (models.py): 
from django.utils import timezone
current_year = timezone.now().year
print(Question.objects.get(pub_date__year=current_year)) # <Question: What's up?>
q = Question.objects.get(pk=1)
print (q) # same
print(q.was_published_recently()) # True

# give some choices to question 
print(q.choice_set.all()) # <QuerySet []>
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
print(q.choice_set.all()) # <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
print(c.question) # What's up?
print(q.choice_set.count()) # 3

print(Choice.objects.filter(question__pub_date__year=current_year)) # <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

c = q.choice_set.filter(choice_text__startswith='Just hacking') # delete a choice 
c.delete() #(1, {'polls.Choice': 1})