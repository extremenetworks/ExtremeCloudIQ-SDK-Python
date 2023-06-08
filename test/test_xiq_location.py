# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_location import XiqLocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqLocation(unittest.TestCase):
    """XiqLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_location.XiqLocation()  # noqa: E501
        if include_optional :
            return XiqLocation(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                parent_id = 56, 
                name = '0', 
                unique_name = '0', 
                type = '0', 
                address = '0', 
                children = [
                    extremecloudiq.models.xiq_location.XiqLocation(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        parent_id = 56, 
                        name = '0', 
                        unique_name = '0', 
                        type = '0', 
                        address = '0', 
                        children = [
                            extremecloudiq.models.xiq_location.XiqLocation(
                                id = 56, 
                                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                org_id = 56, 
                                parent_id = 56, 
                                name = '0', 
                                unique_name = '0', 
                                type = '0', 
                                address = '0', )
                            ], )
                    ]
            )
        else :
            return XiqLocation(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
                unique_name = '0',
                type = '0',
        )

    def testXiqLocation(self):
        """Test XiqLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
