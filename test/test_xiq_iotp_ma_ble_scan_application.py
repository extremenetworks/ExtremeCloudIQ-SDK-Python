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
from extremecloudiq.models.xiq_iotp_ma_ble_scan_application import XiqIotpMaBleScanApplication  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqIotpMaBleScanApplication(unittest.TestCase):
    """XiqIotpMaBleScanApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqIotpMaBleScanApplication
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_iotp_ma_ble_scan_application.XiqIotpMaBleScanApplication()  # noqa: E501
        if include_optional :
            return XiqIotpMaBleScanApplication(
                min_rss = -120, 
                uuid = 'a', 
                vendors = [
                    extremecloudiq.models.xiq_iotp_ma_ble_scan_vendor.XiqIotpMaBleScanVendor(
                        vendor_type = 'ANY', 
                        vendor_name = '0', 
                        company_id = -1, )
                    ], 
                app_type = 'IBEACON'
            )
        else :
            return XiqIotpMaBleScanApplication(
                app_type = 'IBEACON',
        )

    def testXiqIotpMaBleScanApplication(self):
        """Test XiqIotpMaBleScanApplication"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
