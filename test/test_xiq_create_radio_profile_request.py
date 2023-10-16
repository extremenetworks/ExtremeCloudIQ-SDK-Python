# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_radio_profile_request import XiqCreateRadioProfileRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateRadioProfileRequest(unittest.TestCase):
    """XiqCreateRadioProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateRadioProfileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_radio_profile_request.XiqCreateRadioProfileRequest()  # noqa: E501
        if include_optional :
            return XiqCreateRadioProfileRequest(
                name = '0', 
                description = '0', 
                transmission_power = 1, 
                max_transmit_power = 10, 
                transmission_power_floor = 2, 
                transmission_power_max_drop = 0, 
                max_clients = 1, 
                enable_client_transmission_power = True, 
                client_transmission_power = 1, 
                radio_mode = 'B_G', 
                enable_ofdma = True
            )
        else :
            return XiqCreateRadioProfileRequest(
                name = '0',
        )

    def testXiqCreateRadioProfileRequest(self):
        """Test XiqCreateRadioProfileRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
