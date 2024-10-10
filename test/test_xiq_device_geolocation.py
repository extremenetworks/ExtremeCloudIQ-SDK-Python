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
from extremecloudiq.models.xiq_device_geolocation import XiqDeviceGeolocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceGeolocation(unittest.TestCase):
    """XiqDeviceGeolocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceGeolocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_geolocation.XiqDeviceGeolocation()  # noqa: E501
        if include_optional :
            return XiqDeviceGeolocation(
                latitude = 1.337, 
                longitude = 1.337, 
                height = 1.337, 
                major_axis = 1.337, 
                minor_axis = 1.337, 
                orientation = 1.337, 
                last_reported = 56
            )
        else :
            return XiqDeviceGeolocation(
                longitude = 1.337,
                height = 1.337,
                orientation = 1.337,
                last_reported = 56,
        )

    def testXiqDeviceGeolocation(self):
        """Test XiqDeviceGeolocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()