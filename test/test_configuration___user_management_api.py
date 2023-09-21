# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___user_management_api import ConfigurationUserManagementApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationUserManagementApi(unittest.TestCase):
    """ConfigurationUserManagementApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___user_management_api.ConfigurationUserManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_key_based_pcg_users(self):
        """Test case for add_key_based_pcg_users

        Add users to a PCG-enabled network policy  # noqa: E501
        """
        pass

    def test_assign_ports(self):
        """Test case for assign_ports

        Assign ports to devices in network policy  # noqa: E501
        """
        pass

    def test_create_end_user(self):
        """Test case for create_end_user

        Create an end user  # noqa: E501
        """
        pass

    def test_create_user_group(self):
        """Test case for create_user_group

        Create user group  # noqa: E501
        """
        pass

    def test_delete_key_based_pcg_users(self):
        """Test case for delete_key_based_pcg_users

        Delete users from a PCG-enabled network policy  # noqa: E501
        """
        pass

    def test_delete_pcg(self):
        """Test case for delete_pcg

        Delete Private Client Group from a network policy  # noqa: E501
        """
        pass

    def test_delete_ssid_user(self):
        """Test case for delete_ssid_user

        Delete end user by ID  # noqa: E501
        """
        pass

    def test_delete_user_group(self):
        """Test case for delete_user_group

        Delete user group by ID  # noqa: E501
        """
        pass

    def test_email_keys(self):
        """Test case for email_keys

        Send keys to users in network policy via Email  # noqa: E501
        """
        pass

    def test_generate_keys(self):
        """Test case for generate_keys

        Generate shared keys for users in network policy  # noqa: E501
        """
        pass

    def test_get_key_based_pcg_users(self):
        """Test case for get_key_based_pcg_users

        Get users for a PCG-enabled network policy  # noqa: E501
        """
        pass

    def test_get_port_assignments(self):
        """Test case for get_port_assignments

        Get device port assignments in network policy  # noqa: E501
        """
        pass

    def test_list_email_templates(self):
        """Test case for list_email_templates

        List Email templates  # noqa: E501
        """
        pass

    def test_list_end_users(self):
        """Test case for list_end_users

        List end users  # noqa: E501
        """
        pass

    def test_list_key_based_private_client_groups(self):
        """Test case for list_key_based_private_client_groups

        List Key-based Private Client Groups  # noqa: E501
        """
        pass

    def test_list_sms_templates(self):
        """Test case for list_sms_templates

        List SMS templates  # noqa: E501
        """
        pass

    def test_list_user_groups(self):
        """Test case for list_user_groups

        List user groups  # noqa: E501
        """
        pass

    def test_onboard_key_based_private_client_group(self):
        """Test case for onboard_key_based_private_client_group

        Create Key-based PCG in network policy  # noqa: E501
        """
        pass

    def test_regenerate_end_user_password(self):
        """Test case for regenerate_end_user_password

        Regenerate a new password for the end user  # noqa: E501
        """
        pass

    def test_setup_key_based_private_client_group_network_policy(self):
        """Test case for setup_key_based_private_client_group_network_policy

        Setup a Key-based Private Client Group  # noqa: E501
        """
        pass

    def test_update_end_user(self):
        """Test case for update_end_user

        Update an end user  # noqa: E501
        """
        pass

    def test_update_key_based_pcg_users(self):
        """Test case for update_key_based_pcg_users

        Replace all users in a PCG-enabled network policy  # noqa: E501
        """
        pass

    def test_update_user_group(self):
        """Test case for update_user_group

        Update user group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
