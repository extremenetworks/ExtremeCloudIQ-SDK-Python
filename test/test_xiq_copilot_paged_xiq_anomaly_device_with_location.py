# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_copilot_paged_xiq_anomaly_device_with_location import XiqCopilotPagedXiqAnomalyDeviceWithLocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCopilotPagedXiqAnomalyDeviceWithLocation(unittest.TestCase):
    """XiqCopilotPagedXiqAnomalyDeviceWithLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCopilotPagedXiqAnomalyDeviceWithLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_copilot_paged_xiq_anomaly_device_with_location.XiqCopilotPagedXiqAnomalyDeviceWithLocation()  # noqa: E501
        if include_optional :
            return XiqCopilotPagedXiqAnomalyDeviceWithLocation(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_anomaly_device_with_location.XiqAnomalyDeviceWithLocation(
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
                        issue = '0', )
                    ], 
                summary = '0', 
                affected_count = extremecloudiq.models.xiq_anomaly_affected_count.XiqAnomalyAffectedCount(
                    total_anomaly_count = 56, 
                    affected_location_count = 56, 
                    affected_devices_count = 56, )
            )
        else :
            return XiqCopilotPagedXiqAnomalyDeviceWithLocation(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testXiqCopilotPagedXiqAnomalyDeviceWithLocation(self):
        """Test XiqCopilotPagedXiqAnomalyDeviceWithLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
