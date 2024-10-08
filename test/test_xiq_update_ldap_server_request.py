# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_ldap_server_request import XiqUpdateLdapServerRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateLdapServerRequest(unittest.TestCase):
    """XiqUpdateLdapServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateLdapServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_ldap_server_request.XiqUpdateLdapServerRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateLdapServerRequest(
                name = '0', 
                description = '0', 
                enable_tls = True, 
                bind_dn = '0', 
                bind_dn_password = '0', 
                base_dn = '0', 
                l3_address_profile_id = 56, 
                protocol_type = 'LDAP', 
                enable_strip_realm_name = True, 
                destination_port = 1, 
                verification_mode = 'TRY', 
                ca_certificate_id = 56, 
                client_certificate_id = 56, 
                client_key_id = 56
            )
        else :
            return XiqUpdateLdapServerRequest(
        )

    def testXiqUpdateLdapServerRequest(self):
        """Test XiqUpdateLdapServerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
