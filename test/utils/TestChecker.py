import unittest
from utils import Checker

class TestChecker(unittest.TestCase):


    def test_ready(self):
        Checker.phone_ready()
        rs = Checker.get_phone_status()
        self.assertTrue("ready" in rs)