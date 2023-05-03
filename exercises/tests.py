from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exercises.models import Book, Author, Classification, Publisher


class AuthorMethodTests(TestCase):
    def setUpAuthor(self):
        self.client = Client()
        self.author1 = Author.objects.create(
            first_name='Autho', 
            last_name='Tres', 
            email='atres@email.com'
            )
        self.author2 = Author.objects.create(
            first_name='Au', 
            last_name='Quatro', 
            email='auquatro@email.com'
            )
        self.publisher1 = Publisher.objects.create(
            name='Publisher4',
            address='Address4',
            city='City4',
            state_province='Province4',
            country='Country4',
            website='website4.com'
        )
        self.book1 = Book.objects.create(
            title='Book4',
            publisher=self.publisher1
        )
        self.book1.authors.add(self.author1, self.author2)
        
    def testAuthor_Search(self):
        user=User.objects.create_superuser(username='hello', password='world')
        self.client.force_login(user)
        query = "A"
        response = self.client.get(reverse("author-results"),{"q": query})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["authors"],
            [r for r in Author.objects.filter(first_name__icontains=query)]
        )

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user2', email='user2@email.com', password='password')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'user2', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_wrong_pass_login(self):
        response = self.client.post(reverse('login'), {'username': 'user2', 'password': 'helloworld'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
        
    def test_wrong_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'user3', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')