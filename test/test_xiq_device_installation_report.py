# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_device_installation_report import XiqDeviceInstallationReport  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeviceInstallationReport(unittest.TestCase):
    """XiqDeviceInstallationReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeviceInstallationReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_device_installation_report.XiqDeviceInstallationReport()  # noqa: E501
        if include_optional :
            return XiqDeviceInstallationReport(
                onboarded = True, 
                location_name = '0', 
                network_policy_name = '0', 
                device_template_name = '0', 
                ip_address = '0', 
                default_gateway = '0', 
                ntp_server = '0', 
                dns_server = '0', 
                enable_poe = True, 
                xiq_connectivity = True, 
                installation_images = True
            )
        else :
            return XiqDeviceInstallationReport(
        )

    def testXiqDeviceInstallationReport(self):
        """Test XiqDeviceInstallationReport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
