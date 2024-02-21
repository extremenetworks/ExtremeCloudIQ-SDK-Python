# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_list_alert_policies import XiqListAlertPolicies  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqListAlertPolicies(unittest.TestCase):
    """XiqListAlertPolicies unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqListAlertPolicies
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_list_alert_policies.XiqListAlertPolicies()  # noqa: E501
        if include_optional :
            return XiqListAlertPolicies(
                global_policy = extremecloudiq.models.xiq_alert_policy.XiqAlertPolicy(
                    id = 56, 
                    owner_id = 56, 
                    org_id = 56, 
                    name = '0', 
                    sites = [
                        extremecloudiq.models.xiq_alert_site.XiqAlertSite(
                            site_id = 56, 
                            site_name = '0', )
                        ], 
                    event_rules_overview = [
                        extremecloudiq.models.xiq_alert_event_rules_by_category.XiqAlertEventRulesByCategory(
                            category_id = 56, 
                            category_name = '0', 
                            rules = [
                                extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                                    id = 56, 
                                    name = '0', 
                                    enabled = True, )
                                ], )
                        ], 
                    metric_rules_overview = [
                        extremecloudiq.models.xiq_alert_metric_rules_by_metricset.XiqAlertMetricRulesByMetricset(
                            metricset_id = 56, 
                            metricset_name = '0', 
                            rules = [
                                extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                                    id = 56, 
                                    name = '0', 
                                    enabled = True, )
                                ], )
                        ], ), 
                site_policies = [
                    extremecloudiq.models.xiq_alert_policy.XiqAlertPolicy(
                        id = 56, 
                        owner_id = 56, 
                        org_id = 56, 
                        name = '0', 
                        sites = [
                            extremecloudiq.models.xiq_alert_site.XiqAlertSite(
                                site_id = 56, 
                                site_name = '0', )
                            ], 
                        event_rules_overview = [
                            extremecloudiq.models.xiq_alert_event_rules_by_category.XiqAlertEventRulesByCategory(
                                category_id = 56, 
                                category_name = '0', 
                                rules = [
                                    extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                                        id = 56, 
                                        name = '0', 
                                        enabled = True, )
                                    ], )
                            ], 
                        metric_rules_overview = [
                            extremecloudiq.models.xiq_alert_metric_rules_by_metricset.XiqAlertMetricRulesByMetricset(
                                metricset_id = 56, 
                                metricset_name = '0', 
                                rules = [
                                    extremecloudiq.models.xiq_alert_rule_overview.XiqAlertRuleOverview(
                                        id = 56, 
                                        name = '0', 
                                        enabled = True, )
                                    ], )
                            ], )
                    ]
            )
        else :
            return XiqListAlertPolicies(
        )

    def testXiqListAlertPolicies(self):
        """Test XiqListAlertPolicies"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
