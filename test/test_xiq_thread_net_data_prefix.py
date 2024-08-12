# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_thread_net_data_prefix import XiqThreadNetDataPrefix  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadNetDataPrefix(unittest.TestCase):
    """XiqThreadNetDataPrefix unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadNetDataPrefix
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_net_data_prefix.XiqThreadNetDataPrefix()  # noqa: E501
        if include_optional :
            return XiqThreadNetDataPrefix(
                prefix = '0', 
                route_preference = '0', 
                added_by_rloc16 = '0', 
                added_by_ext_mac = '0', 
                preferred = True, 
                slaac = True, 
                dhcp = True, 
                configure = True, 
                default_route = True, 
                on_mesh = '0', 
                stable = True, 
                nd_dns = True, 
                dp = True
            )
        else :
            return XiqThreadNetDataPrefix(
        )

    def testXiqThreadNetDataPrefix(self):
        """Test XiqThreadNetDataPrefix"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
