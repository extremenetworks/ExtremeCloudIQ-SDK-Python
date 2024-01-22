# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_extreme_devices import XiqExtremeDevices  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqExtremeDevices(unittest.TestCase):
    """XiqExtremeDevices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqExtremeDevices
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_extreme_devices.XiqExtremeDevices()  # noqa: E501
        if include_optional :
            return XiqExtremeDevices(
                sns = [
                    '0'
                    ]
            )
        else :
            return XiqExtremeDevices(
                sns = [
                    '0'
                    ],
        )

    def testXiqExtremeDevices(self):
        """Test XiqExtremeDevices"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
