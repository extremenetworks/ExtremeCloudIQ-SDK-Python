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
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_alert_email_subscription import XiqAlertEmailSubscription  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlertEmailSubscription(unittest.TestCase):
    """XiqAlertEmailSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlertEmailSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert_email_subscription.XiqAlertEmailSubscription()  # noqa: E501
        if include_optional :
            return XiqAlertEmailSubscription(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email = '0', 
                is_enabled = True, 
                is_email_verified = True, 
                is_subscribe_all = True, 
                alert_policy_ids = [
                    56
                    ]
            )
        else :
            return XiqAlertEmailSubscription(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '0',
                is_enabled = True,
                is_email_verified = True,
                is_subscribe_all = True,
        )

    def testXiqAlertEmailSubscription(self):
        """Test XiqAlertEmailSubscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
