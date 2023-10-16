# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_poe_flapping_stats_response import XiqPoeFlappingStatsResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPoeFlappingStatsResponse(unittest.TestCase):
    """XiqPoeFlappingStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPoeFlappingStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_poe_flapping_stats_response.XiqPoeFlappingStatsResponse()  # noqa: E501
        if include_optional :
            return XiqPoeFlappingStatsResponse(
                summary = '0', 
                flap_count_entities = [
                    extremecloudiq.models.xiq_flap_count_entity.XiqFlapCountEntity(
                        timestamp = 56, 
                        flap_count = 1.337, 
                        sub_optimal_count = 56, 
                        optimal_time_spent = 1.337, )
                    ]
            )
        else :
            return XiqPoeFlappingStatsResponse(
        )

    def testXiqPoeFlappingStatsResponse(self):
        """Test XiqPoeFlappingStatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
