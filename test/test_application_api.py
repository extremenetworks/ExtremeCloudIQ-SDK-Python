# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.application_api import ApplicationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.application_api.ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_application_top_clients_usage(self):
        """Test case for list_application_top_clients_usage

        List the TopN clients for a application  # noqa: E501
        """
        pass

    def test_list_applications(self):
        """Test case for list_applications

        List the applications  # noqa: E501
        """
        pass

    def test_list_top_applications_usage(self):
        """Test case for list_top_applications_usage

        List the TopN applications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
