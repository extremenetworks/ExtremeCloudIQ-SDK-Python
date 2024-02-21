# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_lldp_cdp_info import XiqDeviceLldpCdpInfo  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceLldpCdpInfo(unittest.TestCase):
    """XiqDeviceLldpCdpInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceLldpCdpInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_lldp_cdp_info.XiqDeviceLldpCdpInfo()  # noqa: E501
        if include_optional :
            return XiqDeviceLldpCdpInfo(
                port_id = '0', 
                system_id = '0', 
                system_name = '0', 
                interface_name = '0'
            )
        else :
            return XiqDeviceLldpCdpInfo(
        )

    def testXiqDeviceLldpCdpInfo(self):
        """Test XiqDeviceLldpCdpInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
