# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_generate_api_token_response import XiqGenerateApiTokenResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqGenerateApiTokenResponse(unittest.TestCase):
    """XiqGenerateApiTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqGenerateApiTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_generate_api_token_response.XiqGenerateApiTokenResponse()  # noqa: E501
        if include_optional :
            return XiqGenerateApiTokenResponse(
                access_token = '0', 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expire_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                creator_id = 56, 
                customer_id = 56, 
                description = '0', 
                permissions = [
                    '0'
                    ]
            )
        else :
            return XiqGenerateApiTokenResponse(
                access_token = '0',
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator_id = 56,
                customer_id = 56,
                permissions = [
                    '0'
                    ],
        )

    def testXiqGenerateApiTokenResponse(self):
        """Test XiqGenerateApiTokenResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
