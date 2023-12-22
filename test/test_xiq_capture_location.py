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
from extremecloudiq.models.xiq_capture_location import XiqCaptureLocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCaptureLocation(unittest.TestCase):
    """XiqCaptureLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCaptureLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_capture_location.XiqCaptureLocation()  # noqa: E501
        if include_optional :
            return XiqCaptureLocation(
                direction = 'BOTH', 
                radio = 'ALL', 
                wired_interface = 'ALL', 
                wireless_band = 'ALL', 
                wired_filters = [
                    'DHCP'
                    ], 
                wireless_filters = [
                    'MANAGEMENT'
                    ]
            )
        else :
            return XiqCaptureLocation(
        )

    def testXiqCaptureLocation(self):
        """Test XiqCaptureLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
