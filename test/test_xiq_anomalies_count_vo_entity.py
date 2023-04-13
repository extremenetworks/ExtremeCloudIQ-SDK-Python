# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomalies_count_vo_entity import XiqAnomaliesCountVoEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomaliesCountVoEntity(unittest.TestCase):
    """XiqAnomaliesCountVoEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomaliesCountVoEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomalies_count_vo_entity.XiqAnomaliesCountVoEntity()  # noqa: E501
        if include_optional :
            return XiqAnomaliesCountVoEntity(
                timestamp = 56, 
                total_anomalies_count = 56, 
                wifi_efficiency_count = 56, 
                wifi_capacity_count = 56, 
                poe_count = 56, 
                pe_count = 56, 
                dfs_count = 56, 
                mb_cast_count = 56
            )
        else :
            return XiqAnomaliesCountVoEntity(
                timestamp = 56,
        )

    def testXiqAnomaliesCountVoEntity(self):
        """Test XiqAnomaliesCountVoEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
