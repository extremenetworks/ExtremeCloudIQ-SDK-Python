# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_cloud_config_group import PagedXiqCloudConfigGroup  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqCloudConfigGroup(unittest.TestCase):
    """PagedXiqCloudConfigGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqCloudConfigGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_cloud_config_group.PagedXiqCloudConfigGroup()  # noqa: E501
        if include_optional :
            return PagedXiqCloudConfigGroup(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_cloud_config_group.XiqCloudConfigGroup(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        description = '0', 
                        predefined = True, 
                        read_only = True, 
                        zone_name = '0', 
                        zone_id = 56, 
                        zone_location_id = 56, 
                        device_ids = [
                            56
                            ], )
                    ]
            )
        else :
            return PagedXiqCloudConfigGroup(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqCloudConfigGroup(self):
        """Test PagedXiqCloudConfigGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()