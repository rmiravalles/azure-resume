import unittest

import azure.functions as func

from ..GetCounter import getNewCounterValue


def test_counter(self):
    counter = 1
    resp = getNewCounterValue(counter)

    self.assertEqual(resp, 2)
