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
from extremecloudiq.models.xiq_onboard_device_request import XiqOnboardDeviceRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqOnboardDeviceRequest(unittest.TestCase):
    """XiqOnboardDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqOnboardDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_onboard_device_request.XiqOnboardDeviceRequest()  # noqa: E501
        if include_optional :
            return XiqOnboardDeviceRequest(
                extreme = extremecloudiq.models.xiq_extreme_devices.XiqExtremeDevices(
                    sns = [
                        '0'
                        ], ), 
                exos = extremecloudiq.models.xiq_exos_devices.XiqExosDevices(
                    sns = [
                        '0'
                        ], ), 
                voss = extremecloudiq.models.xiq_voss_devices.XiqVossDevices(
                    sns = [
                        '0'
                        ], ), 
                wing = extremecloudiq.models.xiq_wing_devices.XiqWingDevices(
                    sn_to_mac = {
                        'key' : '0'
                        }, ), 
                dell = extremecloudiq.models.xiq_dell_devices.XiqDellDevices(
                    sn_to_st = {
                        'key' : '0'
                        }, ), 
                dt = extremecloudiq.models.xiq_digital_twin_devices.XiqDigitalTwinDevices(
                    dts = [
                        extremecloudiq.models.xiq_digital_twin_device.XiqDigitalTwinDevice(
                            make = 'SWITCH_ENGINE', 
                            model = 'DT_5320_16P_4XE', 
                            os_type = '0', 
                            os_version = '0', 
                            vim_modules = [
                                'DT_5520_VIM_4X'
                                ], 
                            feat_licenses = [
                                'PRD_5000_PRMR'
                                ], )
                        ], )
            )
        else :
            return XiqOnboardDeviceRequest(
        )

    def testXiqOnboardDeviceRequest(self):
        """Test XiqOnboardDeviceRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
