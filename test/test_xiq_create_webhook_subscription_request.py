# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_webhook_subscription_request import XiqCreateWebhookSubscriptionRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateWebhookSubscriptionRequest(unittest.TestCase):
    """XiqCreateWebhookSubscriptionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateWebhookSubscriptionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_webhook_subscription_request.XiqCreateWebhookSubscriptionRequest()  # noqa: E501
        if include_optional :
            return XiqCreateWebhookSubscriptionRequest(
                application = 'example-app', 
                url = 'https://webhook_endpoint-example-123', 
                secret = 'erw3245cq3dasbjtyj', 
                message_type = 'LOCATION_AP_CENTRIC'
            )
        else :
            return XiqCreateWebhookSubscriptionRequest(
                application = 'example-app',
                url = 'https://webhook_endpoint-example-123',
                message_type = 'LOCATION_AP_CENTRIC',
        )

    def testXiqCreateWebhookSubscriptionRequest(self):
        """Test XiqCreateWebhookSubscriptionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
