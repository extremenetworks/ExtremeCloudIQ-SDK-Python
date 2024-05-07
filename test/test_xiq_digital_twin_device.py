# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_digital_twin_device import XiqDigitalTwinDevice  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDigitalTwinDevice(unittest.TestCase):
    """XiqDigitalTwinDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDigitalTwinDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_digital_twin_device.XiqDigitalTwinDevice()  # noqa: E501
        if include_optional :
            return XiqDigitalTwinDevice(
                make = 'SWITCH_ENGINE', 
                model = 'DT_5320_16P_4XE', 
                os_type = '0', 
                os_version = '0', 
                vim_modules = [
                    'DT_5520_VIM_4X'
                    ], 
                feat_licenses = [
                    'PRD_5000_PRMR'
                    ]
            )
        else :
            return XiqDigitalTwinDevice(
                make = 'SWITCH_ENGINE',
                model = 'DT_5320_16P_4XE',
                os_version = '0',
        )

    def testXiqDigitalTwinDevice(self):
        """Test XiqDigitalTwinDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
