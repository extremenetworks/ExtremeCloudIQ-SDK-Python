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
from extremecloudiq.models.xiq_auth_log import XiqAuthLog  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAuthLog(unittest.TestCase):
    """XiqAuthLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAuthLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_auth_log.XiqAuthLog()  # noqa: E501
        if include_optional :
            return XiqAuthLog(
                id = '0', 
                auth_type = '0', 
                sn = '0', 
                vhm_id = '0', 
                username = '0', 
                reply = '0', 
                called_station_id = '0', 
                calling_station_id = '0', 
                auth_date = 56, 
                ssid = '0', 
                identity = '0', 
                nas_port_type = '0', 
                reject_reason = '0', 
                nas_identifier = '0', 
                mgmt_mac_address = '0', 
                org_id = 56, 
                timestamp = 56
            )
        else :
            return XiqAuthLog(
                id = '0',
        )

    def testXiqAuthLog(self):
        """Test XiqAuthLog"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
