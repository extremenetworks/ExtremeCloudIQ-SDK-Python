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
from extremecloudiq.models.xiq_copilot_anomalies_by_category import XiqCopilotAnomaliesByCategory  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCopilotAnomaliesByCategory(unittest.TestCase):
    """XiqCopilotAnomaliesByCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCopilotAnomaliesByCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_copilot_anomalies_by_category.XiqCopilotAnomaliesByCategory()  # noqa: E501
        if include_optional :
            return XiqCopilotAnomaliesByCategory(
                anomalies_by_location = [
                    extremecloudiq.models.xiq_anomalies_site_entity.XiqAnomaliesSiteEntity(
                        building_id = 56, 
                        location_name = '0', 
                        anomalies_count_by_location = 56, )
                    ], 
                anomalies_by_severity = extremecloudiq.models.xiq_anomalies_severity_entity.XiqAnomaliesSeverityEntity(
                    low_severity_anomalies_count = 56, 
                    medium_severity_anomalies_count = 56, 
                    high_severity_anomalies_count = 56, 
                    anomalies_count_by_severity = 56, ), 
                anomalies_by_type = [
                    extremecloudiq.models.xiq_anomalies_type_entity.XiqAnomaliesTypeEntity(
                        anomaly_type = 'POE_STABILITY', 
                        anomalies_count_by_type = 56, )
                    ]
            )
        else :
            return XiqCopilotAnomaliesByCategory(
        )

    def testXiqCopilotAnomaliesByCategory(self):
        """Test XiqCopilotAnomaliesByCategory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
