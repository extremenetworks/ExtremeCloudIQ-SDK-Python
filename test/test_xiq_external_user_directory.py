# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_external_user_directory import XiqExternalUserDirectory  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqExternalUserDirectory(unittest.TestCase):
    """XiqExternalUserDirectory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqExternalUserDirectory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_external_user_directory.XiqExternalUserDirectory()  # noqa: E501
        if include_optional :
            return XiqExternalUserDirectory(
                ldap_retry_interval = 60, 
                local_check_interval = 30, 
                remote_check_interval = 10, 
                enable_radius_server_credential_caching = True, 
                cache_lifetime = 3600, 
                user_group_attribute = 'memberOf', 
                external_user_directory_type = 'OPEN_LDAP', 
                entries = [
                    extremecloudiq.models.xiq_external_user_directory_entry.XiqExternalUserDirectoryEntry(
                        default_server_id = 56, 
                        server_role = 'PRIMARY', )
                    ]
            )
        else :
            return XiqExternalUserDirectory(
                ldap_retry_interval = 60,
                local_check_interval = 30,
                remote_check_interval = 10,
                enable_radius_server_credential_caching = True,
                cache_lifetime = 3600,
                user_group_attribute = 'memberOf',
                external_user_directory_type = 'OPEN_LDAP',
                entries = [
                    extremecloudiq.models.xiq_external_user_directory_entry.XiqExternalUserDirectoryEntry(
                        default_server_id = 56, 
                        server_role = 'PRIMARY', )
                    ],
        )

    def testXiqExternalUserDirectory(self):
        """Test XiqExternalUserDirectory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
