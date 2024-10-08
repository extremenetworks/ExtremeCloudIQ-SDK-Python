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
from extremecloudiq.models.xiq_thread_networks import XiqThreadNetworks  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqThreadNetworks(unittest.TestCase):
    """XiqThreadNetworks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqThreadNetworks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_thread_networks.XiqThreadNetworks()  # noqa: E501
        if include_optional :
            return XiqThreadNetworks(
                networks = [
                    extremecloudiq.models.xiq_thread_network_config.XiqThreadNetworkConfig(
                        id = 56, 
                        channel = 56, 
                        channel_mask = '0', 
                        ext_pan_id = '0', 
                        mesh_local_prefix = '0', 
                        network_key = '0', 
                        network_name = '0', 
                        pan_id = '0', 
                        pskc = '0', 
                        obtain_network_key_enabled = True, 
                        native_commissioning_enabled = True, 
                        routers_enabled = True, 
                        external_commissioning_enabled = True, 
                        beacons_enabled = True, 
                        commercial_commissioning_enabled = True, 
                        autonomous_enrollment_enabled = True, 
                        network_key_provisioning_enabled = True, 
                        non_ccm_routers_enabled = True, 
                        active_timestamp = 56, )
                    ]
            )
        else :
            return XiqThreadNetworks(
        )

    def testXiqThreadNetworks(self):
        """Test XiqThreadNetworks"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
