from django.test import TestCase
from ..models import Board, Task, User

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            user=self.user
        )
        self.board = Board.objects.create(
            name="Test Board",
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertEqual(self.task.status, "in_progress")
        self.assertEqual(self.task.user, self.user)


    def test_board_creation(self):
        self.assertEqual(self.board.name, "Test Board")
        self.assertEqual(self.board.user, self.user)
        self.assertIsNone(self.board.tasks)

