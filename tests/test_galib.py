# -*- coding: utf-8 -*-

import unittest

from xoxzo.galib.ganalytics import HitClient

class TestHitClient(unittest.TestCase):

    # Set your Google Analytics Tracking Id here 
    #GA_ID = "UA-XXXXXXXX-1"

    def setUp(self):
        self.hc = HitClient(self.GA_ID)

    def test_not_implemented_hit_type(self):
        self.assertRaises(NotImplementedError, self.hc.send_hit, "newtype")

    def test_event_hit(self):

        # Test with required params only
        self.hc.send_hit(
                "event",
                event_category="Users",
                event_action="New Registration",
                )

        # Test with optional params included
        self.hc.send_hit(
                "event",
                event_category="Users",
                event_action="New Registration w Value",
                user_id="uy6rafdye7",
                event_label="JP",
                event_value="7",
                )

    def test_transaction_hit(self):

        # Test with required params only
        trans_id_01 = self.hc.send_hit(
                "transaction",
                revenue="999",
                currency="MYR",
                )
        self.assertTrue(trans_id_01, msg="Missing transaction id")

        # Test with optional params included
        trans_id_02 = self.hc.send_hit(
                "transaction",
                revenue="10000",
                currency="JPY",
                user_id="uy6rafdye7",
                shipping="1000",
                tax="800",
                affiliation="Test Category",
                transaction_id="testtransactionid01",
                )
        self.assertTrue(trans_id_02, msg="Missing transaction id")

        self.assertNotEqual(trans_id_01, trans_id_02, msg="Transaction id not unique")

if __name__ == "__main__":
    unittest.main()
