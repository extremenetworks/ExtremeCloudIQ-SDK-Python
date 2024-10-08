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
from extremecloudiq.models.xiq_client_summary import XiqClientSummary  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqClientSummary(unittest.TestCase):
    """XiqClientSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqClientSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_client_summary.XiqClientSummary()  # noqa: E501
        if include_optional :
            return XiqClientSummary(
                connected_wireless_client_count = 56, 
                detected_wired_client_count = 56, 
                connected_thread_client_count = 56
            )
        else :
            return XiqClientSummary(
        )

    def testXiqClientSummary(self):
        """Test XiqClientSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
