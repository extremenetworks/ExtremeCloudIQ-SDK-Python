# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_set_ssid_mode_wep_request import XiqSetSsidModeWepRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqSetSsidModeWepRequest(unittest.TestCase):
    """XiqSetSsidModeWepRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqSetSsidModeWepRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_set_ssid_mode_wep_request.XiqSetSsidModeWepRequest()  # noqa: E501
        if include_optional :
            return XiqSetSsidModeWepRequest(
                key_management = 'WEP_8021X', 
                encryption_method = 'WEP104', 
                authentication_method = 'OPEN', 
                default_key = 'FIRST', 
                key_type = 'ASCII', 
                key_value = 'abcd123456789', 
                key_value2 = '01234', 
                key_value3 = '01234', 
                key_value4 = '01234', 
                radius_server_group_id = 56
            )
        else :
            return XiqSetSsidModeWepRequest(
                key_management = 'WEP_8021X',
                encryption_method = 'WEP104',
        )

    def testXiqSetSsidModeWepRequest(self):
        """Test XiqSetSsidModeWepRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
