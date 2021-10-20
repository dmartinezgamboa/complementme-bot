from unittest import TestCase
from unittest.mock import MagicMock, patch

from client import RoastMeClient


class ClientTestCase(TestCase):

    def setUp(self):
        self.patch_run = patch.object(RoastMeClient, 'run')
        self.mock_run = self.patch_run.start()

    def tearDown(self):
        patch.stopall()

    def test_client_stores_data_property(self):
        data = MagicMock()
        roastme_instance = RoastMeClient(data=data)
        self.assertEqual(roastme_instance.data, data)

    def test_create_insult_returns_string(self):
        data = {
            "insults": [
                "You literally smell.",
            ],
            "adverbs": [
                "very",
            ],
            "adjectives": [
                "stupid.",
            ]
        }
        user = '<@DiscordUser>'
        roastme = RoastMeClient(data=data)
        result = roastme.create_insult(user)
        self.assertIsInstance(result, str)
