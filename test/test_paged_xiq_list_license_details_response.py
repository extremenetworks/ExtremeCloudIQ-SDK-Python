# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_list_license_details_response import PagedXiqListLicenseDetailsResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqListLicenseDetailsResponse(unittest.TestCase):
    """PagedXiqListLicenseDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqListLicenseDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_list_license_details_response.PagedXiqListLicenseDetailsResponse()  # noqa: E501
        if include_optional :
            return PagedXiqListLicenseDetailsResponse(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_list_license_details_response.XiqListLicenseDetailsResponse(
                        id = 56, 
                        license_key = '0', 
                        status = extremecloudiq.models.xiq_license_detail_status.XiqLicenseDetailStatus(
                            license_health_color = 'GREEN', 
                            license_detail_health_state = 'EXPIRED', 
                            param1 = '0', 
                            param2 = '0', 
                            description = '0', ), 
                        devices = 56, 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return PagedXiqListLicenseDetailsResponse(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqListLicenseDetailsResponse(self):
        """Test PagedXiqListLicenseDetailsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
