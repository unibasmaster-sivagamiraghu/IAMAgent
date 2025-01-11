import unittest
from src.tools.iam_tools import IAMTools
from src.tools.api_client import APIClient

class TestIAMAgent(unittest.TestCase):
    def setUp(self):
        self.iam_tools = IAMTools()

    def test_classify_ad_group(self):
        test_group = {
            "name": "TEST_GROUP",
            "description": "Test group for unit testing",
            "members": ["user1", "user2"]
        }
        result = self.iam_tools.classify_ad_group(test_group)
        self.assertIsNotNone(result)
        self.assertIn("classification", result)

    def test_map_to_it_role(self):
        test_classification = {
            "group_name": "TEST_GROUP",
            "classification": "ADMIN",
            "confidence": 0.95
        }
        result = self.iam_tools.map_to_it_role(test_classification)
        self.assertIsNotNone(result)