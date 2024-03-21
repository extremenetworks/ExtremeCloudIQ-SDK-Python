# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_port_efficiency_stats_response import XiqPortEfficiencyStatsResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPortEfficiencyStatsResponse(unittest.TestCase):
    """XiqPortEfficiencyStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPortEfficiencyStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_port_efficiency_stats_response.XiqPortEfficiencyStatsResponse()  # noqa: E501
        if include_optional :
            return XiqPortEfficiencyStatsResponse(
                duplex_data_rate_entities = [
                    extremecloudiq.models.xiq_duplex_data_rate_entity.XiqDuplexDataRateEntity(
                        timestamp = 56, 
                        duplex_mode = 56, 
                        datarate_mode = 56, )
                    ]
            )
        else :
            return XiqPortEfficiencyStatsResponse(
        )

    def testXiqPortEfficiencyStatsResponse(self):
        """Test XiqPortEfficiencyStatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
