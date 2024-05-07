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
from extremecloudiq.models.xiq_thread_border_router_service import XiqThreadBorderRouterService  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadBorderRouterService(unittest.TestCase):
    """XiqThreadBorderRouterService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadBorderRouterService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_border_router_service.XiqThreadBorderRouterService()  # noqa: E501
        if include_optional :
            return XiqThreadBorderRouterService(
                state = '0', 
                nat64_local_prefix = '0', 
                nat64_favored_prefix = '0', 
                nat64_favored_preference = '0', 
                nat64_omr_local_prefix = '0', 
                nat64_omr_favored_prefix = '0', 
                nat64_omr_favored_preference = '0', 
                nat64_onlink_local_prefix = '0', 
                nat64_onlink_favored_prefix = '0', 
                nat64_onlink_favored_preference = '0'
            )
        else :
            return XiqThreadBorderRouterService(
        )

    def testXiqThreadBorderRouterService(self):
        """Test XiqThreadBorderRouterService"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()