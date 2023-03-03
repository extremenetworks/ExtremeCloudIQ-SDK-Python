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
from extremecloudiq.models.xiq_update_key_based_pcg_users_request import XiqUpdateKeyBasedPcgUsersRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateKeyBasedPcgUsersRequest(unittest.TestCase):
    """XiqUpdateKeyBasedPcgUsersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateKeyBasedPcgUsersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_key_based_pcg_users_request.XiqUpdateKeyBasedPcgUsersRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateKeyBasedPcgUsersRequest(
                users = [
                    extremecloudiq.models.xiq_key_based_pcg_user_base_info.XiqKeyBasedPcgUserBaseInfo(
                        name = '0', 
                        email = '0', 
                        user_group_name = '0', )
                    ]
            )
        else :
            return XiqUpdateKeyBasedPcgUsersRequest(
                users = [
                    extremecloudiq.models.xiq_key_based_pcg_user_base_info.XiqKeyBasedPcgUserBaseInfo(
                        name = '0', 
                        email = '0', 
                        user_group_name = '0', )
                    ],
        )

    def testXiqUpdateKeyBasedPcgUsersRequest(self):
        """Test XiqUpdateKeyBasedPcgUsersRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
