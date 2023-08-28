# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.account_api import AccountApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_backup_viq(self):
        """Test case for backup_viq

        Backup VIQ  # noqa: E501
        """
        pass

    def test_get_default_device_password(self):
        """Test case for get_default_device_password

        Get the default device password in the account  # noqa: E501
        """
        pass

    def test_get_home_account(self):
        """Test case for get_home_account

        Get home ExtremeCloud IQ account info  # noqa: E501
        """
        pass

    def test_get_viq_info(self):
        """Test case for get_viq_info

        Get VIQ Info  # noqa: E501
        """
        pass

    def test_list_external_accounts(self):
        """Test case for list_external_accounts

        List accessible external guest accounts  # noqa: E501
        """
        pass

    def test_switch_account(self):
        """Test case for switch_account

        Switch to another ExtremeCloud IQ account  # noqa: E501
        """
        pass

    def test_update_default_device_password(self):
        """Test case for update_default_device_password

        Update the default device password in the account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
