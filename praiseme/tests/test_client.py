from unittest import TestCase
from unittest.mock import MagicMock, patch

from client import PraiseMeClient


class ClientTestCase(TestCase):

    def setUp(self):
        self.patch_run = patch.object(PraiseMeClient, 'run')
        self.mock_run = self.patch_run.start()

    def tearDown(self):
        patch.stopall()

    def test_client_stores_data_property(self):
        parts_data = MagicMock()
        full_data = MagicMock()
        praiseme_instance = PraiseMeClient(
            praises_parts=parts_data,
            praises_full=full_data)
        self.assertEqual(praiseme_instance.praises_parts, parts_data)
        self.assertEqual(praiseme_instance.praises_full, full_data)

    def test_find_tagged_user_finds_user(self):
        praises_parts = MagicMock()
        praises_full = MagicMock()

        praiseme_instance = PraiseMeClient(
            praises_parts=praises_parts, 
            praises_full=praises_full
        )

        message_author = "<@discord_user_1>"

        message_mentions = [
            praiseme_instance.user,
            "<@discord_user_2>",
            "<@discord_user_3>"
            ]

        result = praiseme_instance.find_tagged_user(
            message_author, 
            message_mentions
            )
        self.assertEqual(result, "<@discord_user_2>")
