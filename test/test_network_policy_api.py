# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.network_policy_api import NetworkPolicyApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestNetworkPolicyApi(unittest.TestCase):
    """NetworkPolicyApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.network_policy_api.NetworkPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_ssids_to_network_policy(self):
        """Test case for add_ssids_to_network_policy

        Add SSIDs to a network policy  # noqa: E501
        """
        pass

    def test_create_network_policy(self):
        """Test case for create_network_policy

        Create network policy  # noqa: E501
        """
        pass

    def test_delete_network_policy(self):
        """Test case for delete_network_policy

        Delete the network policy  # noqa: E501
        """
        pass

    def test_delete_ssids_from_network_policy(self):
        """Test case for delete_ssids_from_network_policy

        Removes SSIDs from the network policy  # noqa: E501
        """
        pass

    def test_get_network_policy(self):
        """Test case for get_network_policy

        Get the network policy  # noqa: E501
        """
        pass

    def test_list_network_polices(self):
        """Test case for list_network_polices

        List network policies  # noqa: E501
        """
        pass

    def test_list_ssids_by_network_policy(self):
        """Test case for list_ssids_by_network_policy

        List SSIDs for a network policy  # noqa: E501
        """
        pass

    def test_update_network_policy(self):
        """Test case for update_network_policy

        Update the network policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
