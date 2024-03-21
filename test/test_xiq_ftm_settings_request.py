# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_ftm_settings_request import XiqFtmSettingsRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqFtmSettingsRequest(unittest.TestCase):
    """XiqFtmSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqFtmSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_ftm_settings_request.XiqFtmSettingsRequest()  # noqa: E501
        if include_optional :
            return XiqFtmSettingsRequest(
                wgs84_override = True, 
                wgs84 = extremecloudiq.models.xiq_wgs84.XiqWgs84(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    altitude = 1.337, ), 
                zsubelement_override = True, 
                zsubelement = extremecloudiq.models.xiq_zsubelement.XiqZsubelement(
                    expected_to_move = True, 
                    floor_number = 56, 
                    above_floor = extremecloudiq.models.xiq_zsubelement_above_floor.XiqZsubelementAboveFloor(
                        height = 1.337, 
                        height_uncertainty = 1.337, ), ), 
                civic_address_override = True, 
                civic_address = '0'
            )
        else :
            return XiqFtmSettingsRequest(
                wgs84_override = True,
                zsubelement_override = True,
                civic_address_override = True,
        )

    def testXiqFtmSettingsRequest(self):
        """Test XiqFtmSettingsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()