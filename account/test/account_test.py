import unittest
from mock import Mock
from account.account import Account


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
