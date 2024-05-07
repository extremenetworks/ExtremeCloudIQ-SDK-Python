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
from extremecloudiq.models.xiq_internal_radius_device import XiqInternalRadiusDevice  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqInternalRadiusDevice(unittest.TestCase):
    """XiqInternalRadiusDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqInternalRadiusDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_internal_radius_device.XiqInternalRadiusDevice()  # noqa: E501
        if include_optional :
            return XiqInternalRadiusDevice(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                radius_server_id = 56, 
                radius_server_name = '0', 
                host_name = '0'
            )
        else :
            return XiqInternalRadiusDevice(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                radius_server_id = 56,
                radius_server_name = '0',
                host_name = '0',
        )

    def testXiqInternalRadiusDevice(self):
        """Test XiqInternalRadiusDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
