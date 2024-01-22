# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_anomalies_severity_entity import XiqAnomaliesSeverityEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAnomaliesSeverityEntity(unittest.TestCase):
    """XiqAnomaliesSeverityEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAnomaliesSeverityEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_anomalies_severity_entity.XiqAnomaliesSeverityEntity()  # noqa: E501
        if include_optional :
            return XiqAnomaliesSeverityEntity(
                low_severity_anomalies_count = 56, 
                medium_severity_anomalies_count = 56, 
                high_severity_anomalies_count = 56, 
                anomalies_count_by_severity = 56
            )
        else :
            return XiqAnomaliesSeverityEntity(
        )

    def testXiqAnomaliesSeverityEntity(self):
        """Test XiqAnomaliesSeverityEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
