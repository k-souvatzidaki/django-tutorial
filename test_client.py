from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

setup_test_environment()
client = Client()

response = client.get('/') # Not Found: /
print(response.status_code) # 404

response = client.get(reverse('polls:index'))
print(response.status_code) # 200
print(response.content) # b'\n    <ul>\n    \n        <!-- <li><a href="/polls/1/">What&#x27;s up?</a></li> -->\n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n'
print(response.context['latest_question_list']) # <QuerySet [<Question: What's up?>]>