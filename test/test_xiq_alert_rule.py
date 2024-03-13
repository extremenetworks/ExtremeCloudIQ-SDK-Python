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
from extremecloudiq.models.xiq_alert_rule import XiqAlertRule  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlertRule(unittest.TestCase):
    """XiqAlertRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlertRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert_rule.XiqAlertRule()  # noqa: E501
        if include_optional :
            return XiqAlertRule(
                id = 56, 
                message_metadata_id = 56, 
                message_metadata_name = '0', 
                message_metadata_type = '0', 
                description = '0', 
                severity_id = 56, 
                severity_name = '0', 
                is_enabled = True, 
                trigger_type = '0', 
                duration = 56, 
                time_window = 56, 
                count = 56, 
                threshold = 1.337, 
                unit = '0', 
                operator = '0'
            )
        else :
            return XiqAlertRule(
                id = 56,
                message_metadata_id = 56,
                severity_id = 56,
                is_enabled = True,
                trigger_type = '0',
        )

    def testXiqAlertRule(self):
        """Test XiqAlertRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
