import unittest
from unittest.mock import patch, MagicMock
from services import check_calendar_availability, draft_gmail_reply, create_task

class TestServices(unittest.TestCase):

    @patch('services.get_credentials')
    @patch('services.build')
    def test_check_calendar_availability(self, mock_build, mock_get_credentials):
        mock_creds = MagicMock()
        mock_get_credentials.return_value = mock_creds

        mock_service = MagicMock()
        mock_build.return_value = mock_service

        mock_events = MagicMock()
        mock_service.events.return_value = mock_events

        mock_list = MagicMock()
        mock_events.list.return_value = mock_list

        # Mock no returning events (availability is True)
        mock_list.execute.return_value = {'items': []}

        is_free = check_calendar_availability("2023-11-20T10:00:00", "2023-11-20T11:00:00")
        self.assertTrue(is_free)

    @patch('services.get_credentials')
    @patch('services.build')
    def test_draft_gmail_reply(self, mock_build, mock_get_credentials):
        mock_creds = MagicMock()
        mock_get_credentials.return_value = mock_creds

        mock_service = MagicMock()
        mock_build.return_value = mock_service

        mock_users = MagicMock()
        mock_service.users.return_value = mock_users

        mock_drafts = MagicMock()
        mock_users.drafts.return_value = mock_drafts

        mock_create = MagicMock()
        mock_drafts.create.return_value = mock_create
        mock_create.execute.return_value = {'id': '12345'}

        draft = draft_gmail_reply("test@example.com", "Support", "Body")
        self.assertEqual(draft, {'id': '12345'})

if __name__ == '__main__':
    unittest.main()
