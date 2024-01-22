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
from extremecloudiq.models.xiq_wifi_efficiency_client_list_response import XiqWifiEfficiencyClientListResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqWifiEfficiencyClientListResponse(unittest.TestCase):
    """XiqWifiEfficiencyClientListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqWifiEfficiencyClientListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_wifi_efficiency_client_list_response.XiqWifiEfficiencyClientListResponse()  # noqa: E501
        if include_optional :
            return XiqWifiEfficiencyClientListResponse(
                client_stats_entities = [
                    extremecloudiq.models.xiq_client_stats_entity.XiqClientStatsEntity(
                        client_mac = '0', 
                        client_name = '0', 
                        client_host_os = '0', 
                        avg_snr = 56, 
                        avg_tx_rate = 56, 
                        avg_rx_rate = 56, 
                        client_id = 56, 
                        avg_rssi = 56, 
                        health_score = 'NONE', )
                    ]
            )
        else :
            return XiqWifiEfficiencyClientListResponse(
        )

    def testXiqWifiEfficiencyClientListResponse(self):
        """Test XiqWifiEfficiencyClientListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
