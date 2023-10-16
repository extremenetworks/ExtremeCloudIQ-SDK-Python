# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomaly_device_with_location import XiqAnomalyDeviceWithLocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomalyDeviceWithLocation(unittest.TestCase):
    """XiqAnomalyDeviceWithLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomalyDeviceWithLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomaly_device_with_location.XiqAnomalyDeviceWithLocation()  # noqa: E501
        if include_optional :
            return XiqAnomalyDeviceWithLocation(
                building_id = 56, 
                location_name = '0', 
                muted = True, 
                severity = 'NONE', 
                anomaly_type = 'POE_STABILITY', 
                last_detected_time = 56, 
                device_id = 56, 
                device_name = '0', 
                device_model = '0', 
                device_make = '0', 
                switch_stack = True, 
                category = 'WIRED', 
                interface_name = '0', 
                location_id = 56, 
                anomaly_id = '0', 
                frequency = '0', 
                channel_number = 56, 
                channel_mode = '0', 
                recommended_action = '0', 
                issue = '0'
            )
        else :
            return XiqAnomalyDeviceWithLocation(
                building_id = 56,
                location_name = '0',
                muted = True,
                severity = 'NONE',
                anomaly_type = 'POE_STABILITY',
                last_detected_time = 56,
                device_id = 56,
                device_name = '0',
                device_model = '0',
                device_make = '0',
                switch_stack = True,
                category = 'WIRED',
                interface_name = '0',
        )

    def testXiqAnomalyDeviceWithLocation(self):
        """Test XiqAnomalyDeviceWithLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
