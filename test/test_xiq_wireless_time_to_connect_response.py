# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_wireless_time_to_connect_response import XiqWirelessTimeToConnectResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqWirelessTimeToConnectResponse(unittest.TestCase):
    """XiqWirelessTimeToConnectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqWirelessTimeToConnectResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_wireless_time_to_connect_response.XiqWirelessTimeToConnectResponse()  # noqa: E501
        if include_optional :
            return XiqWirelessTimeToConnectResponse(
                quality_index_graph = [
                    extremecloudiq.models.xiq_wireless_time_to_connect_entity.XiqWirelessTimeToConnectEntity(
                        timestamp = 56, 
                        quality_index = 56, 
                        total_clients = 56, 
                        time_to_connect_score = 56, 
                        above_assoc_threshold = 56, 
                        above_auth_threshold = 56, 
                        above_dhcp_threshold = 56, 
                        time_to_assoc = 56, 
                        time_to_auth = 56, 
                        time_to_dhcp = 56, 
                        performance_score = 56, )
                    ]
            )
        else :
            return XiqWirelessTimeToConnectResponse(
        )

    def testXiqWirelessTimeToConnectResponse(self):
        """Test XiqWirelessTimeToConnectResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
