# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.client_api import ClientApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestClientApi(unittest.TestCase):
    """ClientApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.client_api.ClientApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disconnect_client(self):
        """Test case for disconnect_client

        Disconnect the client  # noqa: E501
        """
        pass

    def test_get_active_clients_count(self):
        """Test case for get_active_clients_count

        Get active clients count  # noqa: E501
        """
        pass

    def test_get_client(self):
        """Test case for get_client

        Get client info  # noqa: E501
        """
        pass

    def test_get_client_summary(self):
        """Test case for get_client_summary

        Get client summary metrics  # noqa: E501
        """
        pass

    def test_get_client_usage(self):
        """Test case for get_client_usage

        Get usage per client  # noqa: E501
        """
        pass

    def test_list_active_clients(self):
        """Test case for list_active_clients

        List active clients  # noqa: E501
        """
        pass

    def test_set_clients_aliases(self):
        """Test case for set_clients_aliases

        Set the aliases for multiple clients  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
