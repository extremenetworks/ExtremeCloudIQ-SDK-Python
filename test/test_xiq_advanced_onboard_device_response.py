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
from extremecloudiq.models.xiq_advanced_onboard_device_response import XiqAdvancedOnboardDeviceResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAdvancedOnboardDeviceResponse(unittest.TestCase):
    """XiqAdvancedOnboardDeviceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAdvancedOnboardDeviceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_advanced_onboard_device_response.XiqAdvancedOnboardDeviceResponse()  # noqa: E501
        if include_optional :
            return XiqAdvancedOnboardDeviceResponse(
                success_devices = [
                    extremecloudiq.models.xiq_success_onboard_device.XiqSuccessOnboardDevice(
                        serial_number = '0', 
                        device_id = 56, )
                    ], 
                failure_devices = [
                    extremecloudiq.models.xiq_failure_onboard_device.XiqFailureOnboardDevice(
                        serial_number = '0', 
                        error = 'UNKNOWN', )
                    ]
            )
        else :
            return XiqAdvancedOnboardDeviceResponse(
        )

    def testXiqAdvancedOnboardDeviceResponse(self):
        """Test XiqAdvancedOnboardDeviceResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
