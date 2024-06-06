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
from extremecloudiq.models.xiq_create_radius_client_object_request import XiqCreateRadiusClientObjectRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateRadiusClientObjectRequest(unittest.TestCase):
    """XiqCreateRadiusClientObjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateRadiusClientObjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_radius_client_object_request.XiqCreateRadiusClientObjectRequest()  # noqa: E501
        if include_optional :
            return XiqCreateRadiusClientObjectRequest(
                name = '0', 
                description = '0', 
                enable_inject_operator_name_attribute = True, 
                enable_message_authenticator_attribute = True, 
                enable_permit_dynamic_authorization_message_change = True, 
                retry_interval = 60, 
                accounting_interim_update_interval = 60, 
                entries = [
                    extremecloudiq.models.xiq_radius_client_object_entry.XiqRadiusClientObjectEntry(
                        server_role = 'PRIMARY', 
                        server_type = 'EXTERNAL_RADIUS_SERVER', 
                        radius_server_id = 56, )
                    ]
            )
        else :
            return XiqCreateRadiusClientObjectRequest(
                name = '0',
                enable_inject_operator_name_attribute = True,
                enable_message_authenticator_attribute = True,
                enable_permit_dynamic_authorization_message_change = True,
                retry_interval = 60,
                accounting_interim_update_interval = 60,
                entries = [
                    extremecloudiq.models.xiq_radius_client_object_entry.XiqRadiusClientObjectEntry(
                        server_role = 'PRIMARY', 
                        server_type = 'EXTERNAL_RADIUS_SERVER', 
                        radius_server_id = 56, )
                    ],
        )

    def testXiqCreateRadiusClientObjectRequest(self):
        """Test XiqCreateRadiusClientObjectRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
