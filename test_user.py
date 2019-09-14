import unittest
from app.models import User


class UserTest(unittest.TestCase):
    def SetUp(self):
        self.new_user() = User(password = '12345')

    def test_password_generator(self):
        self.assertTrue(self.new_user.password is not None)

    def test_access(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_verify_password(self):
        self.assertTrue(self.new_user.check_password('12345'))
