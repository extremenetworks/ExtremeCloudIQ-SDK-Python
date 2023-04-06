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
from extremecloudiq.models.paged_xiq_client import PagedXiqClient  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqClient(unittest.TestCase):
    """PagedXiqClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_client.PagedXiqClient()  # noqa: E501
        if include_optional :
            return PagedXiqClient(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_client.XiqClient(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        location_id = 56, 
                        device_id = 56, 
                        hostname = '0', 
                        mac_address = '0', 
                        ip_address = '0', 
                        ipv6_address = '0', 
                        os_type = '0', 
                        username = '0', 
                        user_profile_name = '0', 
                        connected = True, 
                        online_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        offline_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        vlan = 56, 
                        connection_type = 56, 
                        ssid = '0', 
                        port = '0', 
                        org_name = '0', 
                        device_function = 56, 
                        device_mac_address = '0', 
                        device_name = '0', 
                        auth = 56, 
                        channel = 56, 
                        client_health = 56, 
                        application_health = 56, 
                        radio_health = 56, 
                        network_health = 56, 
                        radio_type = 56, 
                        encryption_method = 56, 
                        interface_name = '0', 
                        bssid = '0', 
                        rssi = 56, 
                        snr = 56, 
                        description = '0', 
                        category = '0', 
                        mobility = '0', 
                        port_type_name = '0', 
                        wing_ap = True, 
                        vendor = '0', 
                        locations = [
                            extremecloudiq.models.xiq_location_legend.XiqLocationLegend(
                                id = 56, 
                                name = '0', )
                            ], )
                    ]
            )
        else :
            return PagedXiqClient(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqClient(self):
        """Test PagedXiqClient"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()