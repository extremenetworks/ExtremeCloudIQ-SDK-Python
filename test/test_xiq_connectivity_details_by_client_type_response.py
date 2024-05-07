# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_connectivity_details_by_client_type_response import XiqConnectivityDetailsByClientTypeResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqConnectivityDetailsByClientTypeResponse(unittest.TestCase):
    """XiqConnectivityDetailsByClientTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqConnectivityDetailsByClientTypeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_connectivity_details_by_client_type_response.XiqConnectivityDetailsByClientTypeResponse()  # noqa: E501
        if include_optional :
            return XiqConnectivityDetailsByClientTypeResponse(
                sites_by_wireless = extremecloudiq.models.xiq_sites_by_wireless_entity.XiqSitesByWirelessEntity(
                    low_quality_score_count = 56, 
                    medium_quality_score_count = 56, 
                    high_quality_score_count = 56, 
                    total_locations_count = 56, ), 
                sites_by_wired = extremecloudiq.models.xiq_sites_by_wired_entity.XiqSitesByWiredEntity(
                    low_quality_score_count = 56, 
                    medium_quality_score_count = 56, 
                    high_quality_score_count = 56, 
                    total_locations_count = 56, )
            )
        else :
            return XiqConnectivityDetailsByClientTypeResponse(
        )

    def testXiqConnectivityDetailsByClientTypeResponse(self):
        """Test XiqConnectivityDetailsByClientTypeResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
