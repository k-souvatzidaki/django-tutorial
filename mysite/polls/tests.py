from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    # test was_published_recently() with a future question
    def test_was_published_recently_future_q(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    # test was_published_recently() with an older question 
    def test_was_published_recently_old_q(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # test was_published_recently() with a recent question
    def test_was_published_recently_recent_q(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)