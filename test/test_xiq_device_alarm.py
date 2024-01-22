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
from extremecloudiq.models.xiq_device_alarm import XiqDeviceAlarm  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceAlarm(unittest.TestCase):
    """XiqDeviceAlarm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceAlarm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_alarm.XiqDeviceAlarm()  # noqa: E501
        if include_optional :
            return XiqDeviceAlarm(
                entity_id = 56, 
                timestamp = 56, 
                severity = '0', 
                category = '0', 
                device_mac = '0', 
                client_mac = '0', 
                description = '0'
            )
        else :
            return XiqDeviceAlarm(
        )

    def testXiqDeviceAlarm(self):
        """Test XiqDeviceAlarm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
