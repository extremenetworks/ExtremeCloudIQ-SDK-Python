# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.notification_api import NotificationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.notification_api.NotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_subscriptions(self):
        """Test case for create_subscriptions

        Create webhook subscriptions  # noqa: E501
        """
        pass

    def test_delete_subscription(self):
        """Test case for delete_subscription

        Delete webhook subscription  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List webhook subscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
