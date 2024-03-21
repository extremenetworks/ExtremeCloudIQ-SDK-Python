# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomaly_device_entity import XiqAnomalyDeviceEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomalyDeviceEntity(unittest.TestCase):
    """XiqAnomalyDeviceEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomalyDeviceEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomaly_device_entity.XiqAnomalyDeviceEntity()  # noqa: E501
        if include_optional :
            return XiqAnomalyDeviceEntity(
                device_id = 56, 
                device_name = '0', 
                pinned = True, 
                wired = True, 
                anomaly_id = '0', 
                severity = 'NONE', 
                summary = '0', 
                last_detected_time = 56, 
                recommended_action = '0', 
                anomaly_subtypes = '0', 
                interface_name = '0', 
                channel_mode = '0', 
                channel = 56, 
                frequency = '0', 
                location_id = 56
            )
        else :
            return XiqAnomalyDeviceEntity(
        )

    def testXiqAnomalyDeviceEntity(self):
        """Test XiqAnomalyDeviceEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
