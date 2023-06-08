# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.authentication_api import AuthenticationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        User login with username and password  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        User logout (Revoke the current access token)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
