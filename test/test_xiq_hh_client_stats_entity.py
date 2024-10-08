# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_hh_client_stats_entity import XiqHhClientStatsEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqHhClientStatsEntity(unittest.TestCase):
    """XiqHhClientStatsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqHhClientStatsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_hh_client_stats_entity.XiqHhClientStatsEntity()  # noqa: E501
        if include_optional :
            return XiqHhClientStatsEntity(
                client_mac = '0', 
                client_name = '0', 
                client_host_os = '0', 
                avg_snr = 56, 
                client_id = 56, 
                health_score = 'NONE'
            )
        else :
            return XiqHhClientStatsEntity(
        )

    def testXiqHhClientStatsEntity(self):
        """Test XiqHhClientStatsEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
