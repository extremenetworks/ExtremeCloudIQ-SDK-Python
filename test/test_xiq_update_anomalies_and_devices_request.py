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
from extremecloudiq.models.xiq_update_anomalies_and_devices_request import XiqUpdateAnomaliesAndDevicesRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateAnomaliesAndDevicesRequest(unittest.TestCase):
    """XiqUpdateAnomaliesAndDevicesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateAnomaliesAndDevicesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_anomalies_and_devices_request.XiqUpdateAnomaliesAndDevicesRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateAnomaliesAndDevicesRequest(
                anomaly_details = [
                    extremecloudiq.models.xiq_update_action_anomaly_details.XiqUpdateActionAnomalyDetails(
                        building_id = 56, 
                        location_id = 56, 
                        anomaly_id = '0', 
                        anomaly_type = 'POE_STABILITY', )
                    ], 
                action_type = 'MUTE'
            )
        else :
            return XiqUpdateAnomaliesAndDevicesRequest(
                anomaly_details = [
                    extremecloudiq.models.xiq_update_action_anomaly_details.XiqUpdateActionAnomalyDetails(
                        building_id = 56, 
                        location_id = 56, 
                        anomaly_id = '0', 
                        anomaly_type = 'POE_STABILITY', )
                    ],
                action_type = 'MUTE',
        )

    def testXiqUpdateAnomaliesAndDevicesRequest(self):
        """Test XiqUpdateAnomaliesAndDevicesRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
