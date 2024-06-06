# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_mac_object_request import XiqCreateMacObjectRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateMacObjectRequest(unittest.TestCase):
    """XiqCreateMacObjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateMacObjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_mac_object_request.XiqCreateMacObjectRequest()  # noqa: E501
        if include_optional :
            return XiqCreateMacObjectRequest(
                name = '0', 
                description = '0', 
                value = '0', 
                mac_type = 'MAC_OUI', 
                mac_address_end = '0'
            )
        else :
            return XiqCreateMacObjectRequest(
                name = '0',
                value = '0',
                mac_type = 'MAC_OUI',
        )

    def testXiqCreateMacObjectRequest(self):
        """Test XiqCreateMacObjectRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
