# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_device_monitor_vlan_attributes import PagedXiqDeviceMonitorVlanAttributes  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqDeviceMonitorVlanAttributes(unittest.TestCase):
    """PagedXiqDeviceMonitorVlanAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqDeviceMonitorVlanAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_device_monitor_vlan_attributes.PagedXiqDeviceMonitorVlanAttributes()  # noqa: E501
        if include_optional :
            return PagedXiqDeviceMonitorVlanAttributes(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_device_monitor_vlan_attributes.XiqDeviceMonitorVlanAttributes(
                        earliest_refresh_time = '0', 
                        latest_refresh_time = '0', 
                        latest_refresh_timestamp = 56, 
                        vlan_attributes_info = [
                            extremecloudiq.models.xiq_device_monitor_vlan_attributes_info.XiqDeviceMonitorVlanAttributesInfo(
                                vlan_id = 56, 
                                vlan_name = '0', 
                                active_ports = [
                                    '0'
                                    ], 
                                stp_instance = '0', 
                                stp_enabled = True, 
                                igmp_snooping_enabled = True, 
                                dhcp_snooping_enabled = True, 
                                vrf_name = '0', 
                                dynamic_enabled = True, 
                                member_ports = [
                                    '0'
                                    ], 
                                tagged_ports = [
                                    '0'
                                    ], 
                                untagged_ports = [
                                    '0'
                                    ], 
                                dynamic_ports = [
                                    '0'
                                    ], 
                                non_forwarding_vlan_enabled = True, )
                            ], )
                    ]
            )
        else :
            return PagedXiqDeviceMonitorVlanAttributes(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqDeviceMonitorVlanAttributes(self):
        """Test PagedXiqDeviceMonitorVlanAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()