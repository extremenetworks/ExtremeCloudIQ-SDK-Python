# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_update_configure_ipv4_interface import XiqDeviceUpdateConfigureIpv4Interface  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceUpdateConfigureIpv4Interface(unittest.TestCase):
    """XiqDeviceUpdateConfigureIpv4Interface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceUpdateConfigureIpv4Interface
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_update_configure_ipv4_interface.XiqDeviceUpdateConfigureIpv4Interface()  # noqa: E501
        if include_optional :
            return XiqDeviceUpdateConfigureIpv4Interface(
                ip_address = '0', 
                routing_instance = '0', 
                enable_forwarding = True, 
                enable_vlan_loopback = True, 
                use_ip_addr_as_ospf_router_id = True, 
                override_dhcp_relay = True, 
                enable_dhcp = True, 
                primary_dhcp_server = '0', 
                secondary_dhcp_server = '0', 
                predefined = True, 
                subnetwork_id = 56, 
                vlan_id = 56
            )
        else :
            return XiqDeviceUpdateConfigureIpv4Interface(
                ip_address = '0',
                routing_instance = '0',
                enable_forwarding = True,
                enable_vlan_loopback = True,
                use_ip_addr_as_ospf_router_id = True,
                override_dhcp_relay = True,
                enable_dhcp = True,
                primary_dhcp_server = '0',
                secondary_dhcp_server = '0',
                predefined = True,
        )

    def testXiqDeviceUpdateConfigureIpv4Interface(self):
        """Test XiqDeviceUpdateConfigureIpv4Interface"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
