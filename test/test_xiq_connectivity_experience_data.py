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
from extremecloudiq.models.xiq_connectivity_experience_data import XiqConnectivityExperienceData  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqConnectivityExperienceData(unittest.TestCase):
    """XiqConnectivityExperienceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqConnectivityExperienceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_connectivity_experience_data.XiqConnectivityExperienceData()  # noqa: E501
        if include_optional :
            return XiqConnectivityExperienceData(
                id = '0', 
                info = '0', 
                name = '0', 
                quality_index = 56, 
                trend_indicator = 'UP', 
                quality_index_graph = [
                    extremecloudiq.models.xiq_data_point.XiqDataPoint(
                        timestamp = 56, 
                        value = 1.337, )
                    ]
            )
        else :
            return XiqConnectivityExperienceData(
                name = '0',
                quality_index = 56,
                trend_indicator = 'UP',
                quality_index_graph = [
                    extremecloudiq.models.xiq_data_point.XiqDataPoint(
                        timestamp = 56, 
                        value = 1.337, )
                    ],
        )

    def testXiqConnectivityExperienceData(self):
        """Test XiqConnectivityExperienceData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
