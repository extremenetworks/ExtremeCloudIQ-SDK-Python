# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_device_monitor_vlan_ipv4_interfaces import PagedXiqDeviceMonitorVlanIpv4Interfaces  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqDeviceMonitorVlanIpv4Interfaces(unittest.TestCase):
    """PagedXiqDeviceMonitorVlanIpv4Interfaces unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqDeviceMonitorVlanIpv4Interfaces
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_device_monitor_vlan_ipv4_interfaces.PagedXiqDeviceMonitorVlanIpv4Interfaces()  # noqa: E501
        if include_optional :
            return PagedXiqDeviceMonitorVlanIpv4Interfaces(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_device_monitor_vlan_ipv4_interfaces.XiqDeviceMonitorVlanIpv4Interfaces(
                        earliest_refresh_time = '0', 
                        latest_refresh_time = '0', 
                        latest_refresh_timestamp = 56, 
                        vlan_ipv4_interfaces_details = [
                            extremecloudiq.models.xiq_device_monitor_vlan_ipv4_interfaces_details.XiqDeviceMonitorVlanIpv4InterfacesDetails(
                                vlan_id = 56, 
                                vlan_name = '0', 
                                ipv4_forwarding_enabled = True, 
                                routing_instance = '0', 
                                ipv4_address = '0', 
                                ipv4_subnet = '0', 
                                member_ports = [
                                    '0'
                                    ], 
                                tagged_ports = [
                                    '0'
                                    ], 
                                untagged_ports = [
                                    '0'
                                    ], 
                                non_forwarding_vlan_enabled = True, )
                            ], )
                    ]
            )
        else :
            return PagedXiqDeviceMonitorVlanIpv4Interfaces(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqDeviceMonitorVlanIpv4Interfaces(self):
        """Test PagedXiqDeviceMonitorVlanIpv4Interfaces"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
