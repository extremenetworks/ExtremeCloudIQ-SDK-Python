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
from extremecloudiq.models.xiq_thread_net_data_service import XiqThreadNetDataService  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadNetDataService(unittest.TestCase):
    """XiqThreadNetDataService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadNetDataService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_net_data_service.XiqThreadNetDataService()  # noqa: E501
        if include_optional :
            return XiqThreadNetDataService(
                enterprise_number = 56, 
                service_data = '0', 
                server_data = '0', 
                stable = True, 
                added_by_rloc16 = '0', 
                added_by_ext_mac = '0'
            )
        else :
            return XiqThreadNetDataService(
        )

    def testXiqThreadNetDataService(self):
        """Test XiqThreadNetDataService"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()