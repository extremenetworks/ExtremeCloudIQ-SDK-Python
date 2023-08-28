# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_cpu_memory_usage import XiqDeviceCpuMemoryUsage  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceCpuMemoryUsage(unittest.TestCase):
    """XiqDeviceCpuMemoryUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceCpuMemoryUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_cpu_memory_usage.XiqDeviceCpuMemoryUsage()  # noqa: E501
        if include_optional :
            return XiqDeviceCpuMemoryUsage(
                average_cpu = 56, 
                average_memory = 56, 
                timestamp = 56
            )
        else :
            return XiqDeviceCpuMemoryUsage(
        )

    def testXiqDeviceCpuMemoryUsage(self):
        """Test XiqDeviceCpuMemoryUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
