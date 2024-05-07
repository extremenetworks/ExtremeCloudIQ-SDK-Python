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
from extremecloudiq.models.xiq_device_create_configure_ipv4_static_route import XiqDeviceCreateConfigureIpv4StaticRoute  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceCreateConfigureIpv4StaticRoute(unittest.TestCase):
    """XiqDeviceCreateConfigureIpv4StaticRoute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceCreateConfigureIpv4StaticRoute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_create_configure_ipv4_static_route.XiqDeviceCreateConfigureIpv4StaticRoute()  # noqa: E501
        if include_optional :
            return XiqDeviceCreateConfigureIpv4StaticRoute(
                name = '0', 
                dest_subnetwork = '0', 
                next_hop_ip = '0', 
                next_hop_ip_ping_protection = True, 
                metric = 56, 
                routing_instance = '0', 
                predefined = True
            )
        else :
            return XiqDeviceCreateConfigureIpv4StaticRoute(
                name = '0',
                dest_subnetwork = '0',
                next_hop_ip = '0',
                next_hop_ip_ping_protection = True,
                metric = 56,
                routing_instance = '0',
                predefined = True,
        )

    def testXiqDeviceCreateConfigureIpv4StaticRoute(self):
        """Test XiqDeviceCreateConfigureIpv4StaticRoute"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
