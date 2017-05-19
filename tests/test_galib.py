# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal
import json

from xoxzo.galib.ganalytics import HitClient

class TestHitClient(unittest.TestCase):

    # Set your Google Analytics Tracking Id here 
    #GA_ID = "UA-XXXXXXXX-1"

    def setUp(self):
        self.hc = HitClient(self.GA_ID, debug=True)

    def test_not_implemented_hit_type(self):
        self.assertRaises(NotImplementedError, self.hc.send_hit, "newtype")

    def test_event_hit(self):

        # Test with required params only
        r = self.hc.send_hit(
                "event",
                event_category="Users",
                event_action="New Registration",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))

        # Test with optional params included
        r = self.hc.send_hit(
                "event",
                event_category="Users",
                event_action="New Registration w Value",
                user_id="uy6rafdye7",
                event_label="JP",
                event_value="7",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))

    def test_transaction_hit(self):

        # Test with optional params included
        r = self.hc.send_hit(
                "transaction",
                revenue="2160",
                currency="JPY",
                user_id="uy6Rafdye7",
                shipping="500",
                tax="160",
                affiliation="Test Category",
                transaction_id="XXXtesttransid01",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))

        # Test with required params only
        r = self.hc.send_hit(
                "transaction",
                revenue="999",
                currency="MYR",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))

        # Test with only some of the optional params included
        r = self.hc.send_hit(
                "transaction",
                revenue="2160",
                currency="JPY",
                user_id="uy6rTfdye7",
                tax="160",
                transaction_id="XXXtesttransid011",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))

        # Test with Decimal data since most monetary data is in Decimals
        r = self.hc.send_hit(
                "transaction",
                revenue=Decimal("2160"),
                currency="JPY",
                user_id="uy6rTfdye8",
                tax=Decimal("160"),
                transaction_id="XXXtesttransid012",
                )
        self.assertTrue(r['hitParsingResult'][0]['valid'], 
                        msg="FAILED %s" % (r)
                       )
        self.assertNotEqual(r['parserMessage'][0]['messageType'],
                        "ERROR", msg="FAILED %s" % (r))


if __name__ == "__main__":
    unittest.main()
