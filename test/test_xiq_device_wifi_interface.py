# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_wifi_interface import XiqDeviceWifiInterface  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceWifiInterface(unittest.TestCase):
    """XiqDeviceWifiInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceWifiInterface
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_wifi_interface.XiqDeviceWifiInterface()  # noqa: E501
        if include_optional :
            return XiqDeviceWifiInterface(
                frequency = '0', 
                ssid_count = 56, 
                client_count = 56, 
                neighbor_clients = 56, 
                channel_util = 56, 
                channel = 56, 
                channel_width = 56, 
                tx_utilization = 56, 
                rx_utilization = 56, 
                tx_byte_count = 56, 
                rx_byte_count = 56, 
                noise_floor = 56, 
                crc_error_frame = 56, 
                tx_retry_frame = 56, 
                rx_retry_frame = 56, 
                unicast_tx_packet_count = 56, 
                unicast_rx_packet_count = 56, 
                broadcast_tx_packet_count = 56, 
                broadcast_rx_packet_count = 56, 
                tx_air_time = 56, 
                rx_air_time = 56, 
                total_utilization = 56, 
                scan_avg_interference = 56, 
                mac_address = '0', 
                power = 56, 
                rx_errors = 56, 
                tx_errors = 56, 
                interface_name = '0', 
                radio_profile_name = '0'
            )
        else :
            return XiqDeviceWifiInterface(
        )

    def testXiqDeviceWifiInterface(self):
        """Test XiqDeviceWifiInterface"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
