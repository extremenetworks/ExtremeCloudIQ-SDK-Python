# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_atp_device_stats_response import XiqAtpDeviceStatsResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAtpDeviceStatsResponse(unittest.TestCase):
    """XiqAtpDeviceStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAtpDeviceStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_atp_device_stats_response.XiqAtpDeviceStatsResponse()  # noqa: E501
        if include_optional :
            return XiqAtpDeviceStatsResponse(
                summary = '0', 
                atp_device_stats_entities = [
                    extremecloudiq.models.xiq_atp_device_stats_entity.XiqAtpDeviceStatsEntity(
                        timestamp = 56, 
                        avg_cpu = 1.337, 
                        avg_memory = 1.337, 
                        avg_client_count = 56, )
                    ]
            )
        else :
            return XiqAtpDeviceStatsResponse(
        )

    def testXiqAtpDeviceStatsResponse(self):
        """Test XiqAtpDeviceStatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
