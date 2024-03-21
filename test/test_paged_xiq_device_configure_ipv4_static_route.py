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
from extremecloudiq.models.paged_xiq_device_configure_ipv4_static_route import PagedXiqDeviceConfigureIpv4StaticRoute  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqDeviceConfigureIpv4StaticRoute(unittest.TestCase):
    """PagedXiqDeviceConfigureIpv4StaticRoute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqDeviceConfigureIpv4StaticRoute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_device_configure_ipv4_static_route.PagedXiqDeviceConfigureIpv4StaticRoute()  # noqa: E501
        if include_optional :
            return PagedXiqDeviceConfigureIpv4StaticRoute(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_device_configure_ipv4_static_route.XiqDeviceConfigureIpv4StaticRoute(
                        name = '0', 
                        dest_subnetwork = '0', 
                        next_hop_ip = '0', 
                        next_hop_ip_ping_protection = True, 
                        metric = 56, 
                        routing_instance = '0', 
                        predefined = True, 
                        ipv4_static_route_id = 56, )
                    ]
            )
        else :
            return PagedXiqDeviceConfigureIpv4StaticRoute(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqDeviceConfigureIpv4StaticRoute(self):
        """Test PagedXiqDeviceConfigureIpv4StaticRoute"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()