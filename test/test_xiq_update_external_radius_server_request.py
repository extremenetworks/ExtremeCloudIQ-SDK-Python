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
from extremecloudiq.models.xiq_update_external_radius_server_request import XiqUpdateExternalRadiusServerRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateExternalRadiusServerRequest(unittest.TestCase):
    """XiqUpdateExternalRadiusServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateExternalRadiusServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_external_radius_server_request.XiqUpdateExternalRadiusServerRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateExternalRadiusServerRequest(
                name = '0', 
                shared_secret = '0', 
                authentication_port = 1, 
                accounting_port = 1, 
                server_type = 'BOTH', 
                ip_addr = '0'
            )
        else :
            return XiqUpdateExternalRadiusServerRequest(
                name = '0',
                authentication_port = 1,
                accounting_port = 1,
                server_type = 'BOTH',
                ip_addr = '0',
        )

    def testXiqUpdateExternalRadiusServerRequest(self):
        """Test XiqUpdateExternalRadiusServerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
