# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_location import XiqDeviceLocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceLocation(unittest.TestCase):
    """XiqDeviceLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_location.XiqDeviceLocation()  # noqa: E501
        if include_optional :
            return XiqDeviceLocation(
                location_id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                parent_id = 56, 
                location_name = '0', 
                location_unique_name = '0', 
                location_type = '0', 
                location_address = '0', 
                x = 1.337, 
                y = 1.337, 
                latitude = 1.337, 
                longitude = 1.337
            )
        else :
            return XiqDeviceLocation(
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                location_name = '0',
                location_unique_name = '0',
                location_type = '0',
        )

    def testXiqDeviceLocation(self):
        """Test XiqDeviceLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
