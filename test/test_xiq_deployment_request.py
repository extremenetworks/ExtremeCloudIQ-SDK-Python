# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_deployment_request import XiqDeploymentRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeploymentRequest(unittest.TestCase):
    """XiqDeploymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeploymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_deployment_request.XiqDeploymentRequest()  # noqa: E501
        if include_optional :
            return XiqDeploymentRequest(
                devices = extremecloudiq.models.xiq_device_filter.XiqDeviceFilter(
                    ids = [
                        56
                        ], ), 
                policy = extremecloudiq.models.xiq_deployment_policy.XiqDeploymentPolicy(
                    enable_complete_configuration_update = True, 
                    firmware_upgrade_policy = extremecloudiq.models.xiq_firmware_upgrade_policy.XiqFirmwareUpgradePolicy(
                        enable_enforce_upgrade = True, 
                        enable_distributed_upgrade = True, ), 
                    firmware_activate_option = extremecloudiq.models.xiq_firmware_activate_option.XiqFirmwareActivateOption(
                        enable_activate_at_next_reboot = True, 
                        activation_delay_seconds = 56, 
                        activation_time = 56, ), )
            )
        else :
            return XiqDeploymentRequest(
                devices = extremecloudiq.models.xiq_device_filter.XiqDeviceFilter(
                    ids = [
                        56
                        ], ),
                policy = extremecloudiq.models.xiq_deployment_policy.XiqDeploymentPolicy(
                    enable_complete_configuration_update = True, 
                    firmware_upgrade_policy = extremecloudiq.models.xiq_firmware_upgrade_policy.XiqFirmwareUpgradePolicy(
                        enable_enforce_upgrade = True, 
                        enable_distributed_upgrade = True, ), 
                    firmware_activate_option = extremecloudiq.models.xiq_firmware_activate_option.XiqFirmwareActivateOption(
                        enable_activate_at_next_reboot = True, 
                        activation_delay_seconds = 56, 
                        activation_time = 56, ), ),
        )

    def testXiqDeploymentRequest(self):
        """Test XiqDeploymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
