import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(len(obj_id) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"create User email=\"test@example.com\" \
                            password=\"test123\"")
            obj_id = f.getvalue().strip()
            self.assertTrue(len(obj_id) > 0)

    def test_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create ")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_invalid_attr(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel invalid_attr=1")
            output = f.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
