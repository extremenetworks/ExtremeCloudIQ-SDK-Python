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
from extremecloudiq.api.user_api import UserApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create new user  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user by ID  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Get current user info  # noqa: E501
        """
        pass

    def test_get_external_user(self):
        """Test case for get_external_user

        Get external access info  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user info by ID  # noqa: E501
        """
        pass

    def test_grant_external_user(self):
        """Test case for grant_external_user

        Grant external access  # noqa: E501
        """
        pass

    def test_list_external_users(self):
        """Test case for list_external_users

        List external access users  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        List all users  # noqa: E501
        """
        pass

    def test_revoke_external_user(self):
        """Test case for revoke_external_user

        Revoke external access  # noqa: E501
        """
        pass

    def test_update_external_user(self):
        """Test case for update_external_user

        Update external access info  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
