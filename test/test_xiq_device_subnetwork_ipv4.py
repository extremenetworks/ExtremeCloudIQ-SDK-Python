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
from extremecloudiq.models.xiq_device_subnetwork_ipv4 import XiqDeviceSubnetworkIpv4  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceSubnetworkIpv4(unittest.TestCase):
    """XiqDeviceSubnetworkIpv4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceSubnetworkIpv4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_subnetwork_ipv4.XiqDeviceSubnetworkIpv4()  # noqa: E501
        if include_optional :
            return XiqDeviceSubnetworkIpv4(
                id = 56, 
                name = '0', 
                description = '0', 
                ip_addr_space = '0', 
                gateway_ip_type = 'FIRST', 
                vlan_profile = '0', 
                enable_dhcp = True, 
                dhcp_relay = extremecloudiq.models.xiq_device_dhcp_relay.XiqDeviceDhcpRelay(
                    id = 56, 
                    name = '0', 
                    description = '0', 
                    service_type = 'DHCP_RELAY_AGENT', 
                    platform = 'SWITCH_ENGINE_OR_FABRIC_ENGINE', 
                    primary_server = '0', 
                    secondary_server = '0', ), 
                clients_number = 56
            )
        else :
            return XiqDeviceSubnetworkIpv4(
                id = 56,
                name = '0',
                ip_addr_space = '0',
                gateway_ip_type = 'FIRST',
                vlan_profile = '0',
                enable_dhcp = True,
                clients_number = 56,
        )

    def testXiqDeviceSubnetworkIpv4(self):
        """Test XiqDeviceSubnetworkIpv4"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
