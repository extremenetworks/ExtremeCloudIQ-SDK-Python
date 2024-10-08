# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.alert_api import AlertApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.alert_api.AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acknowledge_alerts(self):
        """Test case for acknowledge_alerts

        Acknowledge the alerts  # noqa: E501
        """
        pass

    def test_count_alerts_by_group(self):
        """Test case for count_alerts_by_group

        Count the alerts by different grouping  # noqa: E501
        """
        pass

    def test_create_alert_email_subscription(self):
        """Test case for create_alert_email_subscription

        Create alert email subscription  # noqa: E501
        """
        pass

    def test_create_alert_policy(self):
        """Test case for create_alert_policy

        Create a site based alert policy  # noqa: E501
        """
        pass

    def test_create_alert_report(self):
        """Test case for create_alert_report

        [LRO] Create the alerts report  # noqa: E501
        """
        pass

    def test_create_alert_webhook_subscription(self):
        """Test case for create_alert_webhook_subscription

        Create alert webhook subscription  # noqa: E501
        """
        pass

    def test_delete_alert_email_subscription(self):
        """Test case for delete_alert_email_subscription

        Delete alert email subscription  # noqa: E501
        """
        pass

    def test_delete_alert_policy(self):
        """Test case for delete_alert_policy

        Delete a site-based alert policy  # noqa: E501
        """
        pass

    def test_delete_alert_webhook_subscription(self):
        """Test case for delete_alert_webhook_subscription

        Delete alert webhook subscription  # noqa: E501
        """
        pass

    def test_delete_bulk_alert_subscription_email(self):
        """Test case for delete_bulk_alert_subscription_email

        Delete alert email subscription in bulk  # noqa: E501
        """
        pass

    def test_delete_bulk_alert_subscription_webhook(self):
        """Test case for delete_bulk_alert_subscription_webhook

        Delete alert webhook subscription in bulk  # noqa: E501
        """
        pass

    def test_disable_alert_rule(self):
        """Test case for disable_alert_rule

        Disable a rule from an alert policy  # noqa: E501
        """
        pass

    def test_download_alert_report(self):
        """Test case for download_alert_report

        Download the alerts report  # noqa: E501
        """
        pass

    def test_enable_alert_rule(self):
        """Test case for enable_alert_rule

        Enable a rule from an alert policy  # noqa: E501
        """
        pass

    def test_get_alert_email_subscription(self):
        """Test case for get_alert_email_subscription

        Get alert email subscription  # noqa: E501
        """
        pass

    def test_get_alert_policy(self):
        """Test case for get_alert_policy

        Get details of an alert policy  # noqa: E501
        """
        pass

    def test_get_alert_rule(self):
        """Test case for get_alert_rule

        Get details of an alert rule  # noqa: E501
        """
        pass

    def test_get_alert_webhook_subscription(self):
        """Test case for get_alert_webhook_subscription

        Get alert webhook subscription  # noqa: E501
        """
        pass

    def test_list_alert_email_subscriptions(self):
        """Test case for list_alert_email_subscriptions

        List alert email subscriptions  # noqa: E501
        """
        pass

    def test_list_alert_policies(self):
        """Test case for list_alert_policies

        List all alert policies  # noqa: E501
        """
        pass

    def test_list_alert_webhook_subscriptions(self):
        """Test case for list_alert_webhook_subscriptions

        List alert webhook subscriptions  # noqa: E501
        """
        pass

    def test_list_alerts(self):
        """Test case for list_alerts

        List the alerts  # noqa: E501
        """
        pass

    def test_list_available_sites(self):
        """Test case for list_available_sites

        The list of current owner's available sites  # noqa: E501
        """
        pass

    def test_update_alert_email_subscription(self):
        """Test case for update_alert_email_subscription

        Update alert email subscription  # noqa: E501
        """
        pass

    def test_update_alert_policy(self):
        """Test case for update_alert_policy

        Update a site-based alert policy  # noqa: E501
        """
        pass

    def test_update_alert_rule(self):
        """Test case for update_alert_rule

        Update an alert rule  # noqa: E501
        """
        pass

    def test_update_alert_webhook_subscription(self):
        """Test case for update_alert_webhook_subscription

        Update alert webhook subscription  # noqa: E501
        """
        pass

    def test_verify_subscription_email(self):
        """Test case for verify_subscription_email

        Email Verification  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
