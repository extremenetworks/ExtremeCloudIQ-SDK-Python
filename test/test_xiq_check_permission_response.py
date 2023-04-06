# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_check_permission_response import XiqCheckPermissionResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCheckPermissionResponse(unittest.TestCase):
    """XiqCheckPermissionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCheckPermissionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_check_permission_response.XiqCheckPermissionResponse()  # noqa: E501
        if include_optional :
            return XiqCheckPermissionResponse(
                permissions = [
                    extremecloudiq.models.xiq_permission.XiqPermission(
                        name = '0', 
                        description = '0', 
                        category = '0', )
                    ], 
                roles = [
                    '0'
                    ]
            )
        else :
            return XiqCheckPermissionResponse(
                permissions = [
                    extremecloudiq.models.xiq_permission.XiqPermission(
                        name = '0', 
                        description = '0', 
                        category = '0', )
                    ],
                roles = [
                    '0'
                    ],
        )

    def testXiqCheckPermissionResponse(self):
        """Test XiqCheckPermissionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()