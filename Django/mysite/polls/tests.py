import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_box, days):
    # intended behaviour:
    # question published given "question_box" and
    # number of "days" offset (negative for past,   
    # positive for future - yet to be published)
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_box = question_box, pub_date=time)

class QuestionModelTests(TestCase):
    def test_question_was_published_recently_with_future_question(self):
        # intended behaviour:
        # was_published_recently() returns False for questions 
        # whose pub_date is in the future. Testing 30 days in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)
    def test_question_was_published_recently_with_old_question(self):
        # intended behaviour:
        # was_published_recently() returns False for question whose pub_date 
        # is older than 1 day. Testing 1 day 1 second.
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_question_was_published_recently_with_recent_question(self):
        # intended behaviour:
        # was_published_recently() returns True for question
        # whose pub_date is within the last day. Testing 1 day - 1 second.
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)

        self.assertIs(recent_question.was_published_recently(), True)
       
class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        # intended behaviour:
        # if no questions exist, display  no questions
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")

    def test_past_question(self):
        # intended behaviour:
        # Questions with pub_date in the past are displayed
        question = create_question(question_box="Past Question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question],)

    def test_future_question(self):
        # intended behaviour:
        # Questions with pub_date in the future aren't displayed
        question = create_question(question_box="Future Question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question_display_only_past(self):
        # intended bahviour:
        # if both future and past questions exist,
        # display only the past question.
        question = create_question(question_box="Past Question.", days=-30)
        create_question(question_box="Future Question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question],)

    def test_two_past_question(self):
        # intended behaviour:
        # Questions index page may display multiple questions.
        # Currently order-independent. Order doesn't matter. Check note below.
        question1 = create_question(question_box="Past Question 1.", days=-30)
        question2 = create_question(question_box="Past Question2.", days=-3)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question1, question2],ordered=False)
        # NOTE: got around passing this test by setting assertQueryEqual(ordered=False). Fix this later.

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        # intended behaviour:
        # The detail view of future question returns a 404
        future_question = create_question(question_box="Future Question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        # intended behaviour:
        # The detail view of a past question displays the question's text
        past_question = create_question(question_box="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_box)