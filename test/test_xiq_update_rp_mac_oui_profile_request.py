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
from extremecloudiq.models.xiq_update_rp_mac_oui_profile_request import XiqUpdateRpMacOuiProfileRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateRpMacOuiProfileRequest(unittest.TestCase):
    """XiqUpdateRpMacOuiProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateRpMacOuiProfileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_rp_mac_oui_profile_request.XiqUpdateRpMacOuiProfileRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateRpMacOuiProfileRequest(
                name = '0', 
                value = '0', 
                description = '0', 
                mac_type = '0', 
                defender_defined = True
            )
        else :
            return XiqUpdateRpMacOuiProfileRequest(
        )

    def testXiqUpdateRpMacOuiProfileRequest(self):
        """Test XiqUpdateRpMacOuiProfileRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
