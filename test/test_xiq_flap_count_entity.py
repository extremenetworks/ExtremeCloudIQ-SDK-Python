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
from extremecloudiq.models.xiq_flap_count_entity import XiqFlapCountEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqFlapCountEntity(unittest.TestCase):
    """XiqFlapCountEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqFlapCountEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_flap_count_entity.XiqFlapCountEntity()  # noqa: E501
        if include_optional :
            return XiqFlapCountEntity(
                timestamp = 56, 
                flap_count = 1.337, 
                sub_optimal_count = 56, 
                optimal_time_spent = 1.337
            )
        else :
            return XiqFlapCountEntity(
                timestamp = 56,
        )

    def testXiqFlapCountEntity(self):
        """Test XiqFlapCountEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()