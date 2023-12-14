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
from extremecloudiq.models.xiq_advanced_onboard_device_request import XiqAdvancedOnboardDeviceRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAdvancedOnboardDeviceRequest(unittest.TestCase):
    """XiqAdvancedOnboardDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAdvancedOnboardDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_advanced_onboard_device_request.XiqAdvancedOnboardDeviceRequest()  # noqa: E501
        if include_optional :
            return XiqAdvancedOnboardDeviceRequest(
                extreme = [
                    extremecloudiq.models.xiq_extreme_device.XiqExtremeDevice(
                        serial_number = '0', 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                exos = [
                    extremecloudiq.models.xiq_exos_device.XiqExosDevice(
                        serial_number = '0', 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                voss = [
                    extremecloudiq.models.xiq_voss_device.XiqVossDevice(
                        serial_number = '0', 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                wing = [
                    extremecloudiq.models.xiq_wing_device.XiqWingDevice(
                        serial_number = '0', 
                        mac_address = '0', 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                dell = [
                    extremecloudiq.models.xiq_dell_device.XiqDellDevice(
                        serial_number = '0', 
                        service_tag = '0', 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                dt = [
                    extremecloudiq.models.xiq_digital_twin_onboard_device.XiqDigitalTwinOnboardDevice(
                        digital_twin_device = extremecloudiq.models.xiq_digital_twin_device.XiqDigitalTwinDevice(
                            make = 'SWITCH_ENGINE', 
                            model = 'DT_5320_16P_4XE', 
                            os_type = '0', 
                            os_version = '0', 
                            vim_modules = [
                                'DT_5520_VIM_4X'
                                ], 
                            feat_licenses = [
                                'PRD_5000_PRMR'
                                ], ), 
                        location = extremecloudiq.models.xiq_device_location_assignment.XiqDeviceLocationAssignment(
                            location_id = 56, 
                            x = 1.337, 
                            y = 1.337, 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        network_policy_id = 56, 
                        hostname = '0', )
                    ], 
                unmanaged = True
            )
        else :
            return XiqAdvancedOnboardDeviceRequest(
        )

    def testXiqAdvancedOnboardDeviceRequest(self):
        """Test XiqAdvancedOnboardDeviceRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
