from django.test import TestCase
from .models  import User, Story, Game
# Create your tests here.

# Testing Custom User Creation cases
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='someone123@gmail.com', username='Dj', password='1234')

    def test_user_attributes(self):
        user = User.objects.get(pk=1)

        self.assertEqual(user.username, 'Dj')
        self.assertEqual(user.email, 'someone123@gmail.com')
        self.assertEqual(user.password, '1234')
        self.assertEqual(user.score, 0)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)


# Testing Story cases
class StoryTestCase(TestCase):
    def setUp(self):
        Story.objects.create(title='The great story', story_text="This is the great story's text", questions=['First Question', 'Second Question'])

    def test_user_attributes(self):
        story = Story.objects.get(pk=1)

        self.assertEqual(story.title, 'The great story')
        self.assertEqual(story.story_text, "This is the great story's text")
        self.assertEqual(story.questions, ['First Question', 'Second Question'])
        