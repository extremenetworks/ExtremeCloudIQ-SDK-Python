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
from extremecloudiq.models.xiq_thread_ipv6_setting import XiqThreadIpv6Setting  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadIpv6Setting(unittest.TestCase):
    """XiqThreadIpv6Setting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadIpv6Setting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_ipv6_setting.XiqThreadIpv6Setting()  # noqa: E501
        if include_optional :
            return XiqThreadIpv6Setting(
                address = '0', 
                scope = '0', 
                cast = '0', 
                type = '0'
            )
        else :
            return XiqThreadIpv6Setting(
        )

    def testXiqThreadIpv6Setting(self):
        """Test XiqThreadIpv6Setting"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
