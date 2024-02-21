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
from extremecloudiq.models.xiq_set_ssid_mode_psk_request import XiqSetSsidModePskRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqSetSsidModePskRequest(unittest.TestCase):
    """XiqSetSsidModePskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqSetSsidModePskRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_set_ssid_mode_psk_request.XiqSetSsidModePskRequest()  # noqa: E501
        if include_optional :
            return XiqSetSsidModePskRequest(
                key_management = 'WPA_PSK', 
                encryption_method = 'CCMP', 
                anti_logging_threshold = 56, 
                key_type = 'ASCII', 
                key_value = '01234567', 
                sae_group = 'ALL', 
                transition_mode = True
            )
        else :
            return XiqSetSsidModePskRequest(
                key_management = 'WPA_PSK',
                encryption_method = 'CCMP',
                key_type = 'ASCII',
                key_value = '01234567',
        )

    def testXiqSetSsidModePskRequest(self):
        """Test XiqSetSsidModePskRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
