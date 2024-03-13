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
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_alert_webhook_subscription import XiqAlertWebhookSubscription  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlertWebhookSubscription(unittest.TestCase):
    """XiqAlertWebhookSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlertWebhookSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert_webhook_subscription.XiqAlertWebhookSubscription()  # noqa: E501
        if include_optional :
            return XiqAlertWebhookSubscription(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                url = '0', 
                secret = '0', 
                is_enabled = True, 
                is_subscribe_all = True, 
                alert_policy_ids = [
                    56
                    ]
            )
        else :
            return XiqAlertWebhookSubscription(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '0',
                secret = '0',
                is_enabled = True,
                is_subscribe_all = True,
        )

    def testXiqAlertWebhookSubscription(self):
        """Test XiqAlertWebhookSubscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
