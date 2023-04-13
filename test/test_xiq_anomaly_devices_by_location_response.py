# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomaly_devices_by_location_response import XiqAnomalyDevicesByLocationResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomalyDevicesByLocationResponse(unittest.TestCase):
    """XiqAnomalyDevicesByLocationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomalyDevicesByLocationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomaly_devices_by_location_response.XiqAnomalyDevicesByLocationResponse()  # noqa: E501
        if include_optional :
            return XiqAnomalyDevicesByLocationResponse(
                location_entity = extremecloudiq.models.xiq_anomaly_location_entity.XiqAnomalyLocationEntity(
                    location_type = 'SITE', 
                    location_id = 56, 
                    location_name = '0', 
                    pinned = True, 
                    muted = True, 
                    severity = 'NONE', 
                    severity_id = 56, 
                    summary = '0', 
                    affected_device_count = 56, 
                    last_detected_time = 56, 
                    anomaly_type = 'POE_FLAPPING', ), 
                devices = [
                    extremecloudiq.models.xiq_anomaly_device_entity.XiqAnomalyDeviceEntity(
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
                        interface_name = '0', )
                    ]
            )
        else :
            return XiqAnomalyDevicesByLocationResponse(
        )

    def testXiqAnomalyDevicesByLocationResponse(self):
        """Test XiqAnomalyDevicesByLocationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
