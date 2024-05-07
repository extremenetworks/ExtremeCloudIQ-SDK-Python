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
from extremecloudiq.models.xiq_thread_border_agent_service import XiqThreadBorderAgentService  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadBorderAgentService(unittest.TestCase):
    """XiqThreadBorderAgentService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadBorderAgentService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_border_agent_service.XiqThreadBorderAgentService()  # noqa: E501
        if include_optional :
            return XiqThreadBorderAgentService(
                state = '0', 
                udp_port = 56
            )
        else :
            return XiqThreadBorderAgentService(
        )

    def testXiqThreadBorderAgentService(self):
        """Test XiqThreadBorderAgentService"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
