from django.test import TestCase,Client


from .models import Course
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

class CourseTestCase(TestCase):

    def setUp(self):
        Course.objects.create(course_code = "CN103" , course_name = "java lab" , semester =1 ,academic_year = 2564,limit_seat = 2,siting=0,status=True)
        

    def test_seat_available(self):
        """is_seat_available should be True"""
        subject = Course.objects.first()
        self.assertTrue(subject.is_seat_available())

    def test_seat_not_available(self):
        """is_seat_available should be False"""
        user1 = User.objects.create(username="user1",password="1234",email="user1@gmail.com")
        user2 = User.objects.create(username="user2",password="1234",email="user2@gmail.com")

        subject = Course.objects.first()
        subject.student.add(user1)
        subject.student.add(user2)

        self.assertFalse(subject.is_seat_available())
    

class RegisterViewTestCase(TestCase):

    def setUp(self):
        subject = Course.objects.create(course_code = "CN103" , course_name = "java lab" , semester =1 ,academic_year = 2564,limit_seat = 2,siting=0,status=True)
        user = User.objects.create(username="user1",password="1234",email="user1@example.com")
        subject.student.add(user)

    def test_index_view_status_code(self):
        """ index view's status code is ok"""
        c = Client()
        response = c.get(reverse('Register:index'))
        self.assertEqual(response.status_code,200)

    def test_index_view_context(self):
        """ context is correctly set """
        c = Client()
        response = c.get(reverse('Register:index'))
        self.assertEqual(response.context['Course'].count(),Course.objects.count())
    
    
    def test_valid_course_page(self):
        """valid flight page should return status code 200"""
        c = Client()
        s = Course.objects.first()
        response = c.get(reverse("Register:ShowCourse", args=(s.course_code,)))
        self.assertEqual(response.status_code,200)

    def test_invalid_course_page(self):
        """ invalid subject page should return status code 404 """

        c = Client()
        response = c.get(reverse('Register:ShowCourse', args = ("CN888",)))
        self.assertEqual(response.status_code, 404)

    def test_guest_user_cannot_apply_course(self):
        """ guest cannot apply course """
        user = User.objects.create(username = "user2" , password = "1234" , email = "user2@example.com")
        s = Course.objects.first()

        c = Client()
        response = c.get(reverse('Register:apply' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(),1)



    def test_authenticated_user_can_apply_course(self):
        """ authenticated user can apply course """
        user = User.objects.create(username="user2",password="1234",email="user2@gmail.com")
        s = Course.objects.first()
        s.limit_seat = 2
        s.save()

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Register:apply' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(),2)

    
    def test_cannot_apply_nonavailable_seat_course(self):
        """ cannot apply because seat full """
        user = User.objects.create(username="user3",password="1234",email="user3@gmail.com")
        s = Course.objects.first()
        s.limit_seat = 1
        s.save()

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Register:apply' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(), 1)

    def test_guest_user_cannot_remove_course(self):
        """ guest cannot remove course """
        user = User.objects.create(username = "user2" , password = "1234" , email = "user2@example.com")
        s = Course.objects.first()

        c = Client()
        response = c.get(reverse('Register:remove' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(),1)

    def test__authenticated_user_can_remove_course(self):
        """ authenticated user can remove course """
        user = User.objects.create(username="user2",password="1234",email="user2@gmail.com")
        s = Course.objects.first()
        s.student.add(user)

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Register:remove' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(),1)


    def test_cannot_remove_unenrollment_course(self):
        """ cannot remove unenrollment course """
        user = User.objects.create(username="user3",password="1234",email="user3@gmail.com")
        s = Course.objects.first()

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Register:remove' ,args=(s.course_code,)))
        self.assertEqual(s.student.count(), 1)

