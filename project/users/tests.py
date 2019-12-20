from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Doctor, Patient
# Create your tests here.
class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(email='just a test')

    def test_email_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.email}'
        self.assertEqual(expected_object_name, 'just a test')



class HomePageViewTest(TestCase):

    def setUp(self):
        User.objects.create(NID='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

    def test_view_uses_corrects_template(self):
        res = self.client.get(reverse('patient_home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'patient_home.html')


class PatientTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.paitent = Patient.objects.create(
            user=self.user,
            address='This is an address',
        )

    def test_string_representation(self):

        patient = Patient(user=self.user)
        self.assertEqual(str(patient), '')

    def test_user_content(self):

        self.assertEqual(f'{self.user.age }', 'None')
        self.assertEqual(f'{self.user.gender}', '')
        self.assertEqual(f'{self.user.email}', 'test@email.com')

    def test_user_list_view(self):

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'home.html')


    def test_get_absolute_url(self):

        self.assertEqual(self.user.get_absolute_url(), '/users/doctor/1/')

    def test_user_create_view(self):
        response = self.client.post(reverse('signup_doctor'), {
            'Name': 'Name',
            'age': 'None',
            'email': 'test@email.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'None')

class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):

        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):

        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                        [0].email, self.email)
