import unittest
from mock import Mock, patch
from account.account import Account, ConnectionError


class TestAccount(unittest.TestCase):
    def test_account_returns_data_for_id_1(self):
        # Given
        account_data = {"id": "1", "name": "test"}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data

        # When
        account = Account(data_interface=mock_data_interface)

        # Then
        self.assertEqual(account_data, account.get_account(1))

    def test_account_when_connect_exception_raised(self):
        # Given
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = ConnectionError()

        # When
        account = Account(data_interface=mock_data_interface)

        # Then
        self.assertEqual("Connection error occurred. Try again.", account.get_account(1))

    @patch("account.account.requests")
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        # Given
        mock_requests.get.return_value = '500'

        # When
        account = Account(Mock())

        # Then
        self.assertEqual(account.get_current_balance(1), '500')