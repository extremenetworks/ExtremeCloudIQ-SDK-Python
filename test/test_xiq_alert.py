# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_alert import XiqAlert  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlert(unittest.TestCase):
    """XiqAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert.XiqAlert()  # noqa: E501
        if include_optional :
            return XiqAlert(
                id = '0', 
                owner_id = 56, 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                message_metadata_id = 56, 
                message_metadata_type = '0', 
                summary = '0', 
                severity_name = '0', 
                category_name = '0', 
                severity_id = 56, 
                category_id = 56, 
                source = extremecloudiq.models.xiq_alert_source.XiqAlertSource(
                    source_type_id = 56, 
                    source_name = '0', 
                    source_type_name = '0', 
                    source_id = '0', ), 
                tags = [
                    extremecloudiq.models.xiq_alert_tag.XiqAlertTag(
                        id = 56, 
                        name = '0', 
                        value = '0', 
                        is_hidden = True, )
                    ], 
                acknowledged = True, 
                site_id = 56, 
                site_name = '0', 
                alert_policy_id = 56, 
                alert_policy_name = '0', 
                alert_rule_id = 56, 
                acknowledged_username = '0'
            )
        else :
            return XiqAlert(
                id = '0',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tags = [
                    extremecloudiq.models.xiq_alert_tag.XiqAlertTag(
                        id = 56, 
                        name = '0', 
                        value = '0', 
                        is_hidden = True, )
                    ],
        )

    def testXiqAlert(self):
        """Test XiqAlert"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
