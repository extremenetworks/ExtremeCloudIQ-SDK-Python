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
from extremecloudiq.models.paged_xiq_tunnel_concentrator import PagedXiqTunnelConcentrator  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqTunnelConcentrator(unittest.TestCase):
    """PagedXiqTunnelConcentrator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqTunnelConcentrator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_tunnel_concentrator.PagedXiqTunnelConcentrator()  # noqa: E501
        if include_optional :
            return PagedXiqTunnelConcentrator(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_tunnel_concentrator.XiqTunnelConcentrator(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        redundant = True, 
                        primary_tc = 56, 
                        backup_tc = 56, 
                        primary_listening_interface = 1, 
                        backup_listening_interface = 1, 
                        primary_bridging_interface = 1, 
                        backup_bridging_interface = 1, 
                        primary_ip = '0', 
                        backup_ip = '0', 
                        primary_vlan = 1, 
                        backup_vlan = 1, 
                        primary_tagged = True, 
                        backup_tagged = True, 
                        tunnel_address = 'a', 
                        router_id = 56, 
                        gateway = '0', 
                        native_vlan = 1, )
                    ]
            )
        else :
            return PagedXiqTunnelConcentrator(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqTunnelConcentrator(self):
        """Test PagedXiqTunnelConcentrator"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
