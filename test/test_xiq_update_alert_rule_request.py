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
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_alert_rule_request import XiqUpdateAlertRuleRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateAlertRuleRequest(unittest.TestCase):
    """XiqUpdateAlertRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateAlertRuleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_alert_rule_request.XiqUpdateAlertRuleRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateAlertRuleRequest(
                description = '0', 
                severity_id = 56, 
                trigger_type = '0', 
                duration = 56, 
                time_window = 56, 
                count = 56, 
                threshold = 1.337, 
                operator = '0'
            )
        else :
            return XiqUpdateAlertRuleRequest(
        )

    def testXiqUpdateAlertRuleRequest(self):
        """Test XiqUpdateAlertRuleRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
