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
from extremecloudiq.models.xiq_alert_group_count import XiqAlertGroupCount  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAlertGroupCount(unittest.TestCase):
    """XiqAlertGroupCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAlertGroupCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_alert_group_count.XiqAlertGroupCount()  # noqa: E501
        if include_optional :
            return XiqAlertGroupCount(
                group_id = 56, 
                group_name = '0', 
                count = 56
            )
        else :
            return XiqAlertGroupCount(
                group_id = 56,
                count = 56,
        )

    def testXiqAlertGroupCount(self):
        """Test XiqAlertGroupCount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
