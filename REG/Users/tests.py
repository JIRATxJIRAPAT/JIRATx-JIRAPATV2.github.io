from django.test import TestCase,Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

class userViewTestCase(TestCase):

    def setUp(self):
        password = make_password('123')
        
        User.objects.create(username = "user1" , password = password , email = "user2@example.com")


    def test_authenticate_user_page(self):
        """ user can view user page """
        user = User.objects.get(username = "user1")
        
        c = Client()
        c.force_login(user)
        response = c.get(reverse("Users:studentinfo"))
        self.assertEqual(response.status_code , 200)
    
    def test_guest_user_cannot_view_user_page(self):
        """ guest cannot view user page """
        user = User.objects.get(username = "user1")

        c = Client()
        response = c.get(reverse("Users:studentinfo"))
        self.assertEqual(response.status_code , 302)

    def test_login_view_successful(self):
        """ login successful """
        user = User.objects.get(username = "user1")
        c = Client()
        response = c.post(reverse('Users:login') , {'username': 'user1' , 'password': '123'})
        self.assertEqual(response.status_code, 302 )
    
    def test_login_view_unsuccessful(self):
        """ login unsuccessful """
        user = User.objects.get(username = "user1")
        c = Client()
        response = c.post(reverse('Users:login') , {'username': 'user1' , 'password': '069'})
        self.assertEqual(response.status_code, 200 )
        
    def test_login_view(self):
        c = Client()
        response = c.get(reverse("Users:login"))
        self.assertEqual(response.status_code , 200)

    def test_logout_view(self):
        c = Client()
        response = c.get(reverse("Users:logout"))
        self.assertEqual(response.status_code , 302)