# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_location_tree_map import XiqLocationTreeMap  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqLocationTreeMap(unittest.TestCase):
    """XiqLocationTreeMap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqLocationTreeMap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_location_tree_map.XiqLocationTreeMap()  # noqa: E501
        if include_optional :
            return XiqLocationTreeMap(
                map_name = '0', 
                width = 1.337, 
                height = 1.337, 
                data = '0'
            )
        else :
            return XiqLocationTreeMap(
                map_name = '0',
                data = '0',
        )

    def testXiqLocationTreeMap(self):
        """Test XiqLocationTreeMap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
