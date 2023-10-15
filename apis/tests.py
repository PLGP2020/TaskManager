from django.test import TestCase, Client
from django.contrib.auth.models import User

from tasks.models import Task

class TestTaskModel(TestCase):

    def setUp(self):
        self.t = Task(id=1,
                      name='Reading a book',
                      description='Read a 20 pages from chatper 3 from your favorite book',
                      status='New')
        

    def test_create_task(self):
            self.assertIsInstance(self.t, Task)

    def test_str_representation(self):
         self.assertEquals(str(self.t), "Reading a book")


class TestTaskListView(TestCase):
     
     def setUp(self):
          test_user = User.objects.create_user(username='testuser',
                                               password='test@#953password')
          test_user.save()
          self.client = Client()
    
     def test_task_list_view_nonauthenticated(self):
          response = self.client.get('/api/')
          self.assertEquals(response.status_code, 403)

     def test_task_list_view_authenticated(self):
          login = self.client.login(username='testuser',
                                    password='test@#953password')
          response = self.client.get('/api/')
          self.assertEquals(response.status_code, 200)

class TestTaskAddTaskView(TestCase):
     
     def setUp(self):
          test_user = User.objects.create_user(username='testuser',
                                               password='test@#953password')
          test_user.save()
          self.client = Client()

     def test_task_add_view_nonauthenticated(self):
          response = self.client.get('/api/new_task/')
          self.assertEquals(response.status_code, 403)

     def test_task_add_view_authenticated(self):     
          login = self.client.login(username='testuser',
                                    password='test@#953password')
          response = self.client.get('/api/new_task/')
          self.assertEquals(response.status_code, 200)
           
          
           





