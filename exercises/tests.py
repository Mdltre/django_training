from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exercises.models import Book, Author, Classification, Publisher


class SearchAuthor(TestCase):
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
        
class SearchPublisher(TestCase):
    def setUpPublisher(self):
        self.client = Client()
        self.publisher1 = Publisher.objects.create(
            name='Publisher4',
            address='Address4',
            city='City4',
            state_province='Province4',
            country='Country4',
            website='website4.com'
        )
        self.publisher1 = Publisher.objects.create(
            name='Publisher5',
            address='Address5',
            city='City5',
            state_province='Province5',
            country='Country5',
            website='website5.com'
        )
        
    def testPublisher_Search(self):
        user=User.objects.create_superuser(username='hello', password='world')
        self.client.force_login(user)
        query = "Publisher5"
        response = self.client.get(reverse("publisher-results"),{"q": query})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["publisher"],
            [r for r in Author.objects.filter(first_name__icontains=query)]
        )

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='user2', email='user2@email.com', password='password')

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
        
class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="user2", email="user2@gmail.com", password="password")
        self.client.force_login(self.user)

    def test_successful_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logout_view'))
        
class ClassificationInfoTest(TestCase):
    def setUp(self):
        user=User.objects.create_superuser(username='hello', password='world')
        self.client.force_login(user)
        self.classification = Classification.objects.create(code="100", name="Test", description="Thriller generally keeps its audience on the edge of their seats as the plot builds towards a climax.")

    def test_classification_detail_view(self):
        response = self.client.get(reverse("classification", args=[self.classification.id]))
        self.assertEqual(response.status_code, 200)
        
class AddAuthorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='user2', password='password')
        self.client.force_login(self.user)
        self.url = reverse('create-author')
        self.data = {
            'first_name': 'Newbie',
            'last_name': 'Audie',
            'email': 'newdie@email.com',
        }
        
    def test_update_author(self):
        # create an author
        self.client.force_login(self.user)
        data = {
            "first_name": "Tester",
            "last_name": "Tests",
            "email": "test@gmail.com"
        }
        response = self.client.post(reverse("update-author", args=[1]), data=data, follow=True)
        self.assertContains(response,"Tester")
        author = Author.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.count(), 1)
        
    def test_delete_author(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("delete-author", args=[1]), follow=True)
        self.assertNotContains(response,"Newbie")
        self.assertEqual(Author.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
    
    def test_anonymous_cannot_access_page(self):
        response = self.client.get(reverse("create-author"))
        self.assertRedirects(response, "/accounts/login/?next=/create-author/")
