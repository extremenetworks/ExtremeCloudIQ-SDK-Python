# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_change_devices_ibeacon_request import XiqChangeDevicesIbeaconRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqChangeDevicesIbeaconRequest(unittest.TestCase):
    """XiqChangeDevicesIbeaconRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqChangeDevicesIbeaconRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_change_devices_ibeacon_request.XiqChangeDevicesIbeaconRequest()  # noqa: E501
        if include_optional :
            return XiqChangeDevicesIbeaconRequest(
                device_ids = [
                    56
                    ], 
                enabled = True, 
                major = 0, 
                minor = 0, 
                power = -127, 
                enable_monitoring = True
            )
        else :
            return XiqChangeDevicesIbeaconRequest(
                device_ids = [
                    56
                    ],
        )

    def testXiqChangeDevicesIbeaconRequest(self):
        """Test XiqChangeDevicesIbeaconRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
