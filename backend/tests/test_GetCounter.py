import unittest

import azure.functions as func

from ...backend.GetCounter import getNewCounterValue

class TestCounter(unittest.TestCase):
    def test_counter(self):
        counter = 1
        resp = getNewCounterValue(counter)

        self.assertEqual(resp, 2)
