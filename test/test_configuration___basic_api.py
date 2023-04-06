# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___basic_api import ConfigurationBasicApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationBasicApi(unittest.TestCase):
    """ConfigurationBasicApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___basic_api.ConfigurationBasicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_vlan_profile(self):
        """Test case for create_vlan_profile

        Create VLAN profile  # noqa: E501
        """
        pass

    def test_delete_vlan_profile(self):
        """Test case for delete_vlan_profile

        Delete a VLAN profile  # noqa: E501
        """
        pass

    def test_delete_vlan_profiles(self):
        """Test case for delete_vlan_profiles

        [LRO] Delete VLAN profiles  # noqa: E501
        """
        pass

    def test_get_vlan_profile(self):
        """Test case for get_vlan_profile

        Get a VLAN profile  # noqa: E501
        """
        pass

    def test_list_vlan_profiles(self):
        """Test case for list_vlan_profiles

        List VLAN profiles  # noqa: E501
        """
        pass

    def test_update_vlan_profile(self):
        """Test case for update_vlan_profile

        Update a VLAN profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
