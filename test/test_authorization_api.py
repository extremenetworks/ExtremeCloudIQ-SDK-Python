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
from extremecloudiq.api.authorization_api import AuthorizationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.authorization_api.AuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_permissions(self):
        """Test case for check_permissions

        Check permissions  # noqa: E501
        """
        pass

    def test_generate_api_token(self):
        """Test case for generate_api_token

        Generate new API token  # noqa: E501
        """
        pass

    def test_get_current_api_token_info(self):
        """Test case for get_current_api_token_info

        Get current API token details  # noqa: E501
        """
        pass

    def test_list_permissions(self):
        """Test case for list_permissions

        Get permissions for current login user  # noqa: E501
        """
        pass

    def test_validate_api_token(self):
        """Test case for validate_api_token

        Validate API token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()