# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.network_scorecard_api import NetworkScorecardApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestNetworkScorecardApi(unittest.TestCase):
    """NetworkScorecardApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.network_scorecard_api.NetworkScorecardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_client_health(self):
        """Test case for get_client_health

        Get the overall client health score  # noqa: E501
        """
        pass

    def test_get_device_health(self):
        """Test case for get_device_health

        Get the overall device health score  # noqa: E501
        """
        pass

    def test_get_network_health(self):
        """Test case for get_network_health

        Get the overall network health score  # noqa: E501
        """
        pass

    def test_get_services_health(self):
        """Test case for get_services_health

        Get the overall services health score  # noqa: E501
        """
        pass

    def test_get_wifi_health(self):
        """Test case for get_wifi_health

        Get the overall wifi health score  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
