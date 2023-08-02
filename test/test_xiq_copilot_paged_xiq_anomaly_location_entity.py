# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_copilot_paged_xiq_anomaly_location_entity import XiqCopilotPagedXiqAnomalyLocationEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCopilotPagedXiqAnomalyLocationEntity(unittest.TestCase):
    """XiqCopilotPagedXiqAnomalyLocationEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCopilotPagedXiqAnomalyLocationEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_copilot_paged_xiq_anomaly_location_entity.XiqCopilotPagedXiqAnomalyLocationEntity()  # noqa: E501
        if include_optional :
            return XiqCopilotPagedXiqAnomalyLocationEntity(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_anomaly_location_entity.XiqAnomalyLocationEntity(
                        location_type = 'SITE', 
                        location_ids = [
                            56
                            ], 
                        building_id = 56, 
                        location_name = '0', 
                        pinned = True, 
                        muted = True, 
                        severity = 'NONE', 
                        severity_id = 56, 
                        summary = '0', 
                        affected_device_count = 56, 
                        last_detected_time = 56, 
                        anomaly_type = 'POE_FLAPPING', )
                    ], 
                summary = '0'
            )
        else :
            return XiqCopilotPagedXiqAnomalyLocationEntity(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testXiqCopilotPagedXiqAnomalyLocationEntity(self):
        """Test XiqCopilotPagedXiqAnomalyLocationEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
