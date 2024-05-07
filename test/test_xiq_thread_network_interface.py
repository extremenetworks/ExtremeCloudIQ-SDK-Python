# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_thread_network_interface import XiqThreadNetworkInterface  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadNetworkInterface(unittest.TestCase):
    """XiqThreadNetworkInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadNetworkInterface
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_network_interface.XiqThreadNetworkInterface()  # noqa: E501
        if include_optional :
            return XiqThreadNetworkInterface(
                interface_name = '0', 
                is_active = True, 
                is_broadcast = True, 
                is_loopback = True, 
                is_point_to_point = True, 
                is_running = True, 
                is_arp = True, 
                is_promisc = True, 
                is_all_multi = True, 
                is_multicast = True, 
                is_dynamic = True, 
                mtu = 56, 
                hw_mac_address = '0', 
                ipv4 = '0', 
                ipv4_mask = '0', 
                ipv4_broadcast = '0', 
                ipv6_settings = [
                    extremecloudiq.models.xiq_thread_ipv6_setting.XiqThreadIpv6Setting(
                        address = '0', 
                        scope = '0', 
                        cast = '0', 
                        type = '0', )
                    ]
            )
        else :
            return XiqThreadNetworkInterface(
        )

    def testXiqThreadNetworkInterface(self):
        """Test XiqThreadNetworkInterface"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
