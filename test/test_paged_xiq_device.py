# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_device import PagedXiqDevice  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqDevice(unittest.TestCase):
    """PagedXiqDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_device.PagedXiqDevice()  # noqa: E501
        if include_optional :
            return PagedXiqDevice(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_device.XiqDevice(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        serial_number = '0', 
                        service_tag = '0', 
                        mac_address = '0', 
                        device_function = 'AP', 
                        product_type = '0', 
                        hostname = '0', 
                        ip_address = '0', 
                        software_version = '0', 
                        device_admin_state = 'NEW', 
                        connected = True, 
                        last_connect_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        network_policy_name = '0', 
                        network_policy_id = 56, 
                        primary_ntp_server_address = '0', 
                        primary_dns_server_address = '0', 
                        subnet_mask = '0', 
                        default_gateway = '0', 
                        ipv6_address = '0', 
                        ipv6_netmask = 56, 
                        simulated = True, 
                        display_version = '0', 
                        active_clients = 56, 
                        location_id = 56, 
                        locations = [
                            extremecloudiq.models.xiq_location_legend.XiqLocationLegend(
                                id = 56, 
                                name = '0', )
                            ], 
                        country_code = 56, 
                        description = '0', 
                        lldp_cdp_infos = [
                            extremecloudiq.models.xiq_device_lldp_cdp_info.XiqDeviceLldpCdpInfo(
                                port_id = '0', 
                                system_id = '0', 
                                system_name = '0', 
                                interface_name = '0', )
                            ], 
                        system_up_time = 56, 
                        config_mismatch = True, 
                        managed_by = '0', )
                    ]
            )
        else :
            return PagedXiqDevice(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqDevice(self):
        """Test PagedXiqDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
