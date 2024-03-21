# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___network_api import ConfigurationNetworkApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationNetworkApi(unittest.TestCase):
    """ConfigurationNetworkApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___network_api.ConfigurationNetworkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tunnel_concentrator(self):
        """Test case for create_tunnel_concentrator

        Create a Tunnel Concentrator  # noqa: E501
        """
        pass

    def test_delete_tunnel_concentrator(self):
        """Test case for delete_tunnel_concentrator

        Delete TunnelConcentrator by ID  # noqa: E501
        """
        pass

    def test_get_tunnel_concentrator(self):
        """Test case for get_tunnel_concentrator

        Get Tunnel Concentrator by ID  # noqa: E501
        """
        pass

    def test_list_tunnel_concentrators(self):
        """Test case for list_tunnel_concentrators

        List Tunnel Concentrators  # noqa: E501
        """
        pass

    def test_update_tunnel_concentrator(self):
        """Test case for update_tunnel_concentrator

        Update TunnelConcentrator by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
