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
        parts_data = MagicMock()
        full_data = MagicMock()
        roastme_instance = RoastMeClient(
            roasts_parts=parts_data,
            roasts_full=full_data)
        self.assertEqual(roastme_instance.roasts_parts, parts_data)
        self.assertEqual(roastme_instance.roasts_full, full_data)

    def test_find_tagged_user_finds_user(self):
        roasts_parts = MagicMock()
        roasts_full = MagicMock()

        roastme_instance = RoastMeClient(
            roasts_parts=roasts_parts, 
            roasts_full=roasts_full
        )

        message_author = "<@discord_user_1>"

        message_mentions = [
            roastme_instance.user,
            "<@discord_user_2>",
            "<@discord_user_3>"
            ]

        result = roastme_instance.find_tagged_user(message_author, message_mentions)
        self.assertEqual(result, "<@discord_user_2>")
