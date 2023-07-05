# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_wireless_performance_entity import XiqWirelessPerformanceEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqWirelessPerformanceEntity(unittest.TestCase):
    """XiqWirelessPerformanceEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqWirelessPerformanceEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_wireless_performance_entity.XiqWirelessPerformanceEntity()  # noqa: E501
        if include_optional :
            return XiqWirelessPerformanceEntity(
                timestamp = 56, 
                quality_index = 56, 
                total_clients = 56, 
                time_to_connect_score = 56, 
                performance_score = 56, 
                snr = 56, 
                retries_data = extremecloudiq.models.xiq_wireless_performance_retries_entity.XiqWirelessPerformanceRetriesEntity(
                    rx_retry = 1.337, 
                    tx_retry = 1.337, 
                    above_retry_threshold = 1.337, )
            )
        else :
            return XiqWirelessPerformanceEntity(
                timestamp = 56,
        )

    def testXiqWirelessPerformanceEntity(self):
        """Test XiqWirelessPerformanceEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
