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
from extremecloudiq.models.client_health import ClientHealth  # noqa: E501
from extremecloudiq.rest import ApiException

class TestClientHealth(unittest.TestCase):
    """ClientHealth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClientHealth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.client_health.ClientHealth()  # noqa: E501
        if include_optional :
            return ClientHealth(
                overall_score = 56, 
                wifi_health_score = 56, 
                network_health_score = 56, 
                application_health_score = 56
            )
        else :
            return ClientHealth(
        )

    def testClientHealth(self):
        """Test ClientHealth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
