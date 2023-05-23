# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_building_request import XiqUpdateBuildingRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateBuildingRequest(unittest.TestCase):
    """XiqUpdateBuildingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateBuildingRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_building_request.XiqUpdateBuildingRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateBuildingRequest(
                parent_id = 56, 
                name = '0', 
                address = '0'
            )
        else :
            return XiqUpdateBuildingRequest(
        )

    def testXiqUpdateBuildingRequest(self):
        """Test XiqUpdateBuildingRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
