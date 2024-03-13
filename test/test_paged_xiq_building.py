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
from extremecloudiq.models.paged_xiq_building import PagedXiqBuilding  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqBuilding(unittest.TestCase):
    """PagedXiqBuilding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqBuilding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_building.PagedXiqBuilding()  # noqa: E501
        if include_optional :
            return PagedXiqBuilding(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_building.XiqBuilding(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        parent_id = 56, 
                        name = '0', 
                        address = extremecloudiq.models.xiq_address.XiqAddress(
                            address = '0', 
                            address2 = '0', 
                            city = '0', 
                            state = '0', 
                            postal_code = '0', ), 
                        latitude = 1.337, 
                        longitude = 1.337, )
                    ]
            )
        else :
            return PagedXiqBuilding(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqBuilding(self):
        """Test PagedXiqBuilding"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
