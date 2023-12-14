# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_radius_proxy import PagedXiqRadiusProxy  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqRadiusProxy(unittest.TestCase):
    """PagedXiqRadiusProxy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqRadiusProxy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_radius_proxy.PagedXiqRadiusProxy()  # noqa: E501
        if include_optional :
            return PagedXiqRadiusProxy(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_radius_proxy.XiqRadiusProxy(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        description = '0', 
                        format_type = 'NAI', 
                        retry_count = 56, 
                        retry_delay = 56, 
                        dead_time = 56, 
                        enable_inject_operator_name_attribute = True, 
                        clients = [
                            extremecloudiq.models.xiq_radius_client.XiqRadiusClient(
                                id = 56, 
                                shared_secret = '0', 
                                description = '0', 
                                l3_address_profile_id = 56, )
                            ], 
                        realms = [
                            extremecloudiq.models.xiq_radius_proxy_realm.XiqRadiusProxyRealm(
                                id = 56, 
                                name = '0', 
                                enable_strip_realm_name = True, 
                                radius_client_object_id = 56, )
                            ], )
                    ]
            )
        else :
            return PagedXiqRadiusProxy(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqRadiusProxy(self):
        """Test PagedXiqRadiusProxy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
