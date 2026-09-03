"""Unit tests for CronCraft."""

import unittest
from croncraft.translator import natural_to_cron
from croncraft.explainer import explain_cron


class TestCronCraft(unittest.TestCase):

    def test_natural_to_cron_mapping(self):
        res = natural_to_cron("every 15 minutes")
        self.assertEqual(res["cron"], "*/15 * * * *")

        res_daily = natural_to_cron("every day at midnight")
        self.assertEqual(res_daily["cron"], "0 0 * * *")

    def test_explain_cron_format(self):
        res = explain_cron("0 0 1 * *")
        self.assertTrue(res["valid"])
        self.assertIn("At 00:00 on day 1 of the month", res["description"])


if __name__ == "__main__":
    unittest.main()
