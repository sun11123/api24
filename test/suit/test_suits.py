import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_login import TestUserLogin

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()