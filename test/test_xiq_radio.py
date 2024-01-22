# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_radio import XiqRadio  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqRadio(unittest.TestCase):
    """XiqRadio unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqRadio
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_radio.XiqRadio()  # noqa: E501
        if include_optional :
            return XiqRadio(
                name = '0', 
                channel_number = 56, 
                channel_width = '0', 
                mode = '0', 
                mac_address = '0', 
                power = 56, 
                clients = [
                    extremecloudiq.models.xiq_wireless_client.XiqWirelessClient(
                        network_policy_name = '0', 
                        ssid = '0', 
                        ssid_status = 'OPEN', 
                        ssid_security_type = 'OPEN', )
                    ]
            )
        else :
            return XiqRadio(
                name = '0',
                channel_width = '0',
                mode = '0',
        )

    def testXiqRadio(self):
        """Test XiqRadio"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
