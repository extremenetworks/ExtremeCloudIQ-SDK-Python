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
from extremecloudiq.models.xiq_api_token_info import XiqApiTokenInfo  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqApiTokenInfo(unittest.TestCase):
    """XiqApiTokenInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqApiTokenInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_api_token_info.XiqApiTokenInfo()  # noqa: E501
        if include_optional :
            return XiqApiTokenInfo(
                user_name = '0', 
                user_id = 56, 
                role = '0', 
                owner_id = 56, 
                data_center = '0', 
                scopes = [
                    '0'
                    ], 
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expiration_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expires_in = 56
            )
        else :
            return XiqApiTokenInfo(
                user_name = '0',
                user_id = 56,
                role = '0',
                owner_id = 56,
                data_center = '0',
                scopes = [
                    '0'
                    ],
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqApiTokenInfo(self):
        """Test XiqApiTokenInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
