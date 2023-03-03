# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_external_radius_server_request import XiqCreateExternalRadiusServerRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateExternalRadiusServerRequest(unittest.TestCase):
    """XiqCreateExternalRadiusServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateExternalRadiusServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_external_radius_server_request.XiqCreateExternalRadiusServerRequest()  # noqa: E501
        if include_optional :
            return XiqCreateExternalRadiusServerRequest(
                name = '0', 
                shared_secret = '0', 
                authentication_port = 1, 
                accounting_port = 1, 
                server_type = 'BOTH', 
                ip_addr = '0', 
                enable_a3 = True
            )
        else :
            return XiqCreateExternalRadiusServerRequest(
                name = '0',
                authentication_port = 1,
                accounting_port = 1,
                server_type = 'BOTH',
                ip_addr = '0',
                enable_a3 = True,
        )

    def testXiqCreateExternalRadiusServerRequest(self):
        """Test XiqCreateExternalRadiusServerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
