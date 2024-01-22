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
from extremecloudiq.models.paged_xiq_floor import PagedXiqFloor  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqFloor(unittest.TestCase):
    """PagedXiqFloor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqFloor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_floor.PagedXiqFloor()  # noqa: E501
        if include_optional :
            return PagedXiqFloor(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_floor.XiqFloor(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        parent_id = 56, 
                        name = '0', 
                        unique_name = '0', 
                        environment = 'AUTO_ESTIMATE', 
                        db_attenuation = 1.337, 
                        measurement_unit = 'FEET', 
                        installation_height = 1.337, 
                        map_size_width = 1.337, 
                        map_size_height = 1.337, 
                        map_name = '0', )
                    ]
            )
        else :
            return PagedXiqFloor(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqFloor(self):
        """Test PagedXiqFloor"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
