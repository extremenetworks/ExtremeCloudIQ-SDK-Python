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
from extremecloudiq.models.xiq_sites_by_wireless_entity import XiqSitesByWirelessEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqSitesByWirelessEntity(unittest.TestCase):
    """XiqSitesByWirelessEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqSitesByWirelessEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_sites_by_wireless_entity.XiqSitesByWirelessEntity()  # noqa: E501
        if include_optional :
            return XiqSitesByWirelessEntity(
                low_quality_score_count = 56, 
                medium_quality_score_count = 56, 
                high_quality_score_count = 56, 
                total_locations_count = 56
            )
        else :
            return XiqSitesByWirelessEntity(
        )

    def testXiqSitesByWirelessEntity(self):
        """Test XiqSitesByWirelessEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
