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
from extremecloudiq.models.xiq_atp_packet_counts_entity import XiqAtpPacketCountsEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAtpPacketCountsEntity(unittest.TestCase):
    """XiqAtpPacketCountsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAtpPacketCountsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_atp_packet_counts_entity.XiqAtpPacketCountsEntity()  # noqa: E501
        if include_optional :
            return XiqAtpPacketCountsEntity(
                timestamp = 56, 
                unicast_tx = 1.337, 
                unicast_rx = 1.337, 
                multicast_tx = 1.337, 
                multicast_rx = 1.337, 
                broadcast_tx = 1.337, 
                broadcast_rx = 1.337
            )
        else :
            return XiqAtpPacketCountsEntity(
                timestamp = 56,
        )

    def testXiqAtpPacketCountsEntity(self):
        """Test XiqAtpPacketCountsEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
