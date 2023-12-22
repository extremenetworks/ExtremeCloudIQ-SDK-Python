# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_alert_event_rules_by_category import XiqAlertEventRulesByCategory  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlertEventRulesByCategory(unittest.TestCase):
    """XiqAlertEventRulesByCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlertEventRulesByCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert_event_rules_by_category.XiqAlertEventRulesByCategory()  # noqa: E501
        if include_optional :
            return XiqAlertEventRulesByCategory(
                category_id = 56, 
                category_name = '0', 
                rules = [
                    extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                        id = 56, 
                        name = '0', 
                        enabled = True, )
                    ]
            )
        else :
            return XiqAlertEventRulesByCategory(
                category_id = 56,
                category_name = '0',
                rules = [
                    extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                        id = 56, 
                        name = '0', 
                        enabled = True, )
                    ],
        )

    def testXiqAlertEventRulesByCategory(self):
        """Test XiqAlertEventRulesByCategory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
