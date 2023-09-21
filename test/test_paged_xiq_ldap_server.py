# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_ldap_server import PagedXiqLdapServer  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqLdapServer(unittest.TestCase):
    """PagedXiqLdapServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqLdapServer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_ldap_server.PagedXiqLdapServer()  # noqa: E501
        if include_optional :
            return PagedXiqLdapServer(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_ldap_server.XiqLdapServer(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        enable_tls = True, 
                        bind_dn = '0', 
                        bind_dn_password = '0', 
                        base_dn = '0', 
                        l3_address_profile_id = 56, 
                        protocol_type = 'LDAP', 
                        enable_strip_realm_name = True, 
                        destination_port = 56, 
                        verification_mode = 'TRY', 
                        ca_certificate_id = 56, 
                        client_certificate_id = 56, 
                        client_key_id = 56, 
                        client_key_password = '0', )
                    ]
            )
        else :
            return PagedXiqLdapServer(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqLdapServer(self):
        """Test PagedXiqLdapServer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
