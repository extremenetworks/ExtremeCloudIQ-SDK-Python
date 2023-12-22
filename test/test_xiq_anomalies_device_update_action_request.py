# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomalies_device_update_action_request import XiqAnomaliesDeviceUpdateActionRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomaliesDeviceUpdateActionRequest(unittest.TestCase):
    """XiqAnomaliesDeviceUpdateActionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomaliesDeviceUpdateActionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomalies_device_update_action_request.XiqAnomaliesDeviceUpdateActionRequest()  # noqa: E501
        if include_optional :
            return XiqAnomaliesDeviceUpdateActionRequest(
                anomaly_type = 'POE_STABILITY', 
                action_type = 'MUTE', 
                location_id = 56, 
                anomaly_id = '0'
            )
        else :
            return XiqAnomaliesDeviceUpdateActionRequest(
        )

    def testXiqAnomaliesDeviceUpdateActionRequest(self):
        """Test XiqAnomaliesDeviceUpdateActionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
