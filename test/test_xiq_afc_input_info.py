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
from extremecloudiq.models.xiq_afc_input_info import XiqAfcInputInfo  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAfcInputInfo(unittest.TestCase):
    """XiqAfcInputInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAfcInputInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_afc_input_info.XiqAfcInputInfo()  # noqa: E501
        if include_optional :
            return XiqAfcInputInfo(
                serial_number = '0', 
                coordinates = extremecloudiq.models.xiq_ap_coordinates.XiqApCoordinates(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    timestamp = 56, ), 
                elevation = extremecloudiq.models.xiq_elevation.XiqElevation(
                    height = 1.337, 
                    height_reference = 'AGL', 
                    uncertainty = 56, ), 
                ellipse = extremecloudiq.models.xiq_ellipse.XiqEllipse(
                    major_axis = 1.337, 
                    minor_axis = 1.337, 
                    orientation = 1.337, ), 
                environment = 'INDOOR'
            )
        else :
            return XiqAfcInputInfo(
        )

    def testXiqAfcInputInfo(self):
        """Test XiqAfcInputInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
