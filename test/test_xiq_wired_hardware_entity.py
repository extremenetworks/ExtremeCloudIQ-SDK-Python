# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_wired_hardware_entity import XiqWiredHardwareEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqWiredHardwareEntity(unittest.TestCase):
    """XiqWiredHardwareEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqWiredHardwareEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_wired_hardware_entity.XiqWiredHardwareEntity()  # noqa: E501
        if include_optional :
            return XiqWiredHardwareEntity(
                quality_index = 56, 
                timestamp = 56, 
                total_switches = 56, 
                affected_ratio = 56, 
                affected = 1.337
            )
        else :
            return XiqWiredHardwareEntity(
                timestamp = 56,
        )

    def testXiqWiredHardwareEntity(self):
        """Test XiqWiredHardwareEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
