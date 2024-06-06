# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_active_directory_server import XiqActiveDirectoryServer  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqActiveDirectoryServer(unittest.TestCase):
    """XiqActiveDirectoryServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqActiveDirectoryServer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_active_directory_server.XiqActiveDirectoryServer()  # noqa: E501
        if include_optional :
            return XiqActiveDirectoryServer(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                name = '0', 
                description = '0', 
                base_dn = '0', 
                enable_tls = True, 
                bind_dn = '0', 
                bind_dn_password = '0', 
                domain = '0', 
                computer_ou = '0', 
                domain_admin = '0', 
                domain_admin_password = '0', 
                enable_save_domain_admin_credentials = True, 
                short_domain = '0', 
                realm = '0', 
                base_dn_fetch_mode = 'AUTO', 
                connection_setup_device_id = 56, 
                l3_address_profile_id = 56
            )
        else :
            return XiqActiveDirectoryServer(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqActiveDirectoryServer(self):
        """Test XiqActiveDirectoryServer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
