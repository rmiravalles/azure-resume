import unittest

import pytest
import azure.functions as func

from GetCounter import getNewCounterValue

class TestCounter(unittest.TestCase):
    def test_counter(self):
        counter = 1
        resp = getNewCounterValue(counter)

        self.assertEqual(resp, 2)
