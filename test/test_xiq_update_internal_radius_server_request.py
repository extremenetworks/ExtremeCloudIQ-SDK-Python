# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_internal_radius_server_request import XiqUpdateInternalRadiusServerRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateInternalRadiusServerRequest(unittest.TestCase):
    """XiqUpdateInternalRadiusServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateInternalRadiusServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_internal_radius_server_request.XiqUpdateInternalRadiusServerRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateInternalRadiusServerRequest(
                name = '0', 
                description = '0', 
                authentication_method_group = 'TLS_PEAP_TTLS_LEAP_MD5', 
                default_authentication_method = 'TLS', 
                enable_verify_server_cert = True, 
                server_key_password = '0', 
                enable_check_cert_common_name = True, 
                enable_check_user_for_tls_auth = True, 
                enable_check_user_for_peap_auth = True, 
                enable_check_user_for_ttls_auth = True, 
                enable_authentication_server = True, 
                enable_radius_accounting_settings = True, 
                authentication_server_port = 1, 
                active_session_limit = 0, 
                active_session_age_timeout = 30, 
                ca_certificate_id = 56, 
                server_certificate_id = 56, 
                server_key_id = 56, 
                clients = [
                    extremecloudiq.models.xiq_radius_client.XiqRadiusClient(
                        id = 56, 
                        shared_secret = '0', 
                        description = '0', 
                        l3_address_profile_id = 56, )
                    ]
            )
        else :
            return XiqUpdateInternalRadiusServerRequest(
                name = '0',
                authentication_method_group = 'TLS_PEAP_TTLS_LEAP_MD5',
                default_authentication_method = 'TLS',
                enable_verify_server_cert = True,
                enable_check_cert_common_name = True,
                enable_check_user_for_tls_auth = True,
                enable_authentication_server = True,
                enable_radius_accounting_settings = True,
                ca_certificate_id = 56,
                server_certificate_id = 56,
                server_key_id = 56,
        )

    def testXiqUpdateInternalRadiusServerRequest(self):
        """Test XiqUpdateInternalRadiusServerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
