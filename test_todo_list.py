import unittest
from todo_list import add_task, view_tasks, update_task, delete_task, tasks

class TestTodoList(unittest.TestCase):

    def setUp(self):
        # Clear the tasks list before each test
        tasks.clear()

    def test_add_task(self):
        result = add_task("Read a book")
        self.assertEqual(result, "Task 'Read a book' added.")
        self.assertIn("Read a book", tasks)

    def test_view_tasks_empty(self):
        result = view_tasks()
        self.assertEqual(result, "No tasks available.")

    def test_view_tasks_with_entries(self):
        add_task("Read a book")
        add_task("Write a report")
        result = view_tasks()
        self.assertIn("1. Read a book", result)
        self.assertIn("2. Write a report", result)

    def test_update_task(self):
        add_task("Read a book")
        result = update_task(0, "Read two books")
        self.assertEqual(result, "Task 'Read a book' updated to 'Read two books'.")
        self.assertIn("Read two books", tasks)

    def test_update_task_out_of_range(self):
        result = update_task(0, "Read two books")
        self.assertEqual(result, "Error: Task index out of range.")

    def test_delete_task(self):
        add_task("Read a book")
        result = delete_task(0)
        self.assertEqual(result, "Task 'Read a book' deleted.")
        self.assertNotIn("Read a book", tasks)

    def test_delete_task_out_of_range(self):
        result = delete_task(0)
        self.assertEqual(result, "Error: Task index out of range.")

if __name__ == '__main__':
    unittest.main()
