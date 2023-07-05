# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_delete_key_based_pcg_users_request import XiqDeleteKeyBasedPcgUsersRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeleteKeyBasedPcgUsersRequest(unittest.TestCase):
    """XiqDeleteKeyBasedPcgUsersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeleteKeyBasedPcgUsersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_delete_key_based_pcg_users_request.XiqDeleteKeyBasedPcgUsersRequest()  # noqa: E501
        if include_optional :
            return XiqDeleteKeyBasedPcgUsersRequest(
                user_ids = [
                    56
                    ]
            )
        else :
            return XiqDeleteKeyBasedPcgUsersRequest(
                user_ids = [
                    56
                    ],
        )

    def testXiqDeleteKeyBasedPcgUsersRequest(self):
        """Test XiqDeleteKeyBasedPcgUsersRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
