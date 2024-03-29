# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_update_vlan_attributes import XiqDeviceUpdateVlanAttributes  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceUpdateVlanAttributes(unittest.TestCase):
    """XiqDeviceUpdateVlanAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceUpdateVlanAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_update_vlan_attributes.XiqDeviceUpdateVlanAttributes()  # noqa: E501
        if include_optional :
            return XiqDeviceUpdateVlanAttributes(
                name = '0', 
                dhcp_snooping_enabled = True, 
                dhcp_snooping_action = 'NONE', 
                igmp_snooping_enabled = True, 
                immediate_leave = True, 
                always_create = True
            )
        else :
            return XiqDeviceUpdateVlanAttributes(
        )

    def testXiqDeviceUpdateVlanAttributes(self):
        """Test XiqDeviceUpdateVlanAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
