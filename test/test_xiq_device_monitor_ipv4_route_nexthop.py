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
from extremecloudiq.models.xiq_device_monitor_ipv4_route_nexthop import XiqDeviceMonitorIpv4RouteNexthop  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceMonitorIpv4RouteNexthop(unittest.TestCase):
    """XiqDeviceMonitorIpv4RouteNexthop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceMonitorIpv4RouteNexthop
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_monitor_ipv4_route_nexthop.XiqDeviceMonitorIpv4RouteNexthop()  # noqa: E501
        if include_optional :
            return XiqDeviceMonitorIpv4RouteNexthop(
                nexthop_ipv4_address = '0', 
                nexthop_device_id = 56, 
                nexthop_host_name = '0', 
                ping_protection_enabled = True, 
                ping_protection_state = '0', 
                ping_protection_last_uptime = 56, 
                ping_protection_last_downtime = 56, 
                routing_instance = '0'
            )
        else :
            return XiqDeviceMonitorIpv4RouteNexthop(
        )

    def testXiqDeviceMonitorIpv4RouteNexthop(self):
        """Test XiqDeviceMonitorIpv4RouteNexthop"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
