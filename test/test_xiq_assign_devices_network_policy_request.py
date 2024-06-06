# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_assign_devices_network_policy_request import XiqAssignDevicesNetworkPolicyRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAssignDevicesNetworkPolicyRequest(unittest.TestCase):
    """XiqAssignDevicesNetworkPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAssignDevicesNetworkPolicyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_assign_devices_network_policy_request.XiqAssignDevicesNetworkPolicyRequest()  # noqa: E501
        if include_optional :
            return XiqAssignDevicesNetworkPolicyRequest(
                devices = extremecloudiq.models.xiq_device_filter.XiqDeviceFilter(
                    ids = [
                        56
                        ], ), 
                network_policy_id = 56
            )
        else :
            return XiqAssignDevicesNetworkPolicyRequest(
                devices = extremecloudiq.models.xiq_device_filter.XiqDeviceFilter(
                    ids = [
                        56
                        ], ),
                network_policy_id = 56,
        )

    def testXiqAssignDevicesNetworkPolicyRequest(self):
        """Test XiqAssignDevicesNetworkPolicyRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
