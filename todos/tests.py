from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta
from .models import TODO

# Create your tests here.

class TODOModelTest(TestCase):
    """Test cases for the TODO model"""

    def setUp(self):
        """Set up test data"""
        self.todo = TODO.objects.create(
            title="Test TODO",
            description="This is a test TODO",
            due_date=date.today() + timedelta(days=7)
        )

    def test_todo_creation(self):
        """Test that a TODO can be created"""
        self.assertEqual(self.todo.title, "Test TODO")
        self.assertEqual(self.todo.description, "This is a test TODO")
        self.assertFalse(self.todo.resolved)

    def test_todo_str(self):
        """Test the string representation of TODO"""
        self.assertEqual(str(self.todo), "Test TODO")

    def test_todo_default_resolved(self):
        """Test that resolved defaults to False"""
        new_todo = TODO.objects.create(title="Another TODO")
        self.assertFalse(new_todo.resolved)


class TODOViewsTest(TestCase):
    """Test cases for TODO views"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = Client()
        self.todo = TODO.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7)
        )

    def test_home_view(self):
        """Test that home page loads and displays TODOs"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO")
        self.assertTemplateUsed(response, 'todos/home.html')

    def test_home_view_empty(self):
        """Test home page with no TODOs"""
        TODO.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No TODOs yet")

    def test_create_todo_get(self):
        """Test GET request to create TODO page"""
        response = self.client.get(reverse('create_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/create.html')

    def test_create_todo_post(self):
        """Test POST request to create a new TODO"""
        response = self.client.post(reverse('create_todo'), {
            'title': 'New TODO',
            'description': 'New description',
            'due_date': (date.today() + timedelta(days=5)).strftime('%Y-%m-%d')
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(TODO.objects.filter(title='New TODO').exists())

    def test_edit_todo_get(self):
        """Test GET request to edit TODO page"""
        response = self.client.get(reverse('edit_todo', args=[self.todo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/edit.html')
        self.assertContains(response, "Test TODO")

    def test_edit_todo_post(self):
        """Test POST request to edit a TODO"""
        response = self.client.post(reverse('edit_todo', args=[self.todo.id]), {
            'title': 'Updated TODO',
            'description': 'Updated description',
            'due_date': (date.today() + timedelta(days=10)).strftime('%Y-%m-%d')
        })
        self.assertEqual(response.status_code, 302)  # Redirect after edit
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated TODO')
        self.assertEqual(self.todo.description, 'Updated description')

    def test_delete_todo_get(self):
        """Test GET request to delete TODO page"""
        response = self.client.get(reverse('delete_todo', args=[self.todo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/delete.html')
        self.assertContains(response, "Test TODO")

    def test_delete_todo_post(self):
        """Test POST request to delete a TODO"""
        todo_id = self.todo.id
        response = self.client.post(reverse('delete_todo', args=[todo_id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(TODO.objects.filter(id=todo_id).exists())

    def test_toggle_resolved(self):
        """Test toggling the resolved status of a TODO"""
        self.assertFalse(self.todo.resolved)

        # Toggle to resolved
        response = self.client.post(reverse('toggle_resolved', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)

        # Toggle back to pending
        response = self.client.post(reverse('toggle_resolved', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.resolved)

    def test_edit_nonexistent_todo(self):
        """Test editing a TODO that doesn't exist"""
        response = self.client.get(reverse('edit_todo', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_todo(self):
        """Test deleting a TODO that doesn't exist"""
        response = self.client.get(reverse('delete_todo', args=[9999]))
        self.assertEqual(response.status_code, 404)
