# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_floor_request import XiqCreateFloorRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateFloorRequest(unittest.TestCase):
    """XiqCreateFloorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateFloorRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_floor_request.XiqCreateFloorRequest()  # noqa: E501
        if include_optional :
            return XiqCreateFloorRequest(
                parent_id = 56, 
                name = '0', 
                environment = 'AUTO_ESTIMATE', 
                db_attenuation = 1.337, 
                measurement_unit = 'FEET', 
                installation_height = 1.337, 
                map_size_width = 1.337, 
                map_size_height = 1.337, 
                map_name = '0'
            )
        else :
            return XiqCreateFloorRequest(
                parent_id = 56,
                name = '0',
                db_attenuation = 1.337,
                measurement_unit = 'FEET',
                installation_height = 1.337,
                map_size_width = 1.337,
                map_size_height = 1.337,
        )

    def testXiqCreateFloorRequest(self):
        """Test XiqCreateFloorRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
