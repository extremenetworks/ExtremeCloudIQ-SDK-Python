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
from extremecloudiq.models.xiq_wired_event_entity import XiqWiredEventEntity  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqWiredEventEntity(unittest.TestCase):
    """XiqWiredEventEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqWiredEventEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_wired_event_entity.XiqWiredEventEntity()  # noqa: E501
        if include_optional :
            return XiqWiredEventEntity(
                device_id = '0', 
                hostname = '0', 
                interface_errors = 1.337, 
                maximum_errors = 1.337, 
                mgmt_ip = '0', 
                port = '0', 
                serial_number = '0'
            )
        else :
            return XiqWiredEventEntity(
        )

    def testXiqWiredEventEntity(self):
        """Test XiqWiredEventEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
