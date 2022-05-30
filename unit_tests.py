import unittest
import linux


class TestLinux(unittest.TestCase):
    def testmsg(self):  # Test case to check whether msg has exact has contents or not.
        result = linux.hotd
        self.assertGreater(len(result), 0)
        self.assertLess(len(result), 2)  # Checking whether ftn returns only 1 msg or more. if more test fails
