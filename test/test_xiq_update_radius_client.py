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
from extremecloudiq.models.xiq_update_radius_client import XiqUpdateRadiusClient  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateRadiusClient(unittest.TestCase):
    """XiqUpdateRadiusClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateRadiusClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_radius_client.XiqUpdateRadiusClient()  # noqa: E501
        if include_optional :
            return XiqUpdateRadiusClient(
                id = 56, 
                shared_secret = '0', 
                description = '0', 
                l3_address_profile_id = 56
            )
        else :
            return XiqUpdateRadiusClient(
        )

    def testXiqUpdateRadiusClient(self):
        """Test XiqUpdateRadiusClient"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
