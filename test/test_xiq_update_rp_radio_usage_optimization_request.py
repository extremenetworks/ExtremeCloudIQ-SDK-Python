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
from extremecloudiq.models.xiq_update_rp_radio_usage_optimization_request import XiqUpdateRpRadioUsageOptimizationRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateRpRadioUsageOptimizationRequest(unittest.TestCase):
    """XiqUpdateRpRadioUsageOptimizationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateRpRadioUsageOptimizationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_rp_radio_usage_optimization_request.XiqUpdateRpRadioUsageOptimizationRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateRpRadioUsageOptimizationRequest(
                preamble = '0', 
                beacon_period = 40, 
                enable_frame_burst = True, 
                enable_smart_antenna = True, 
                enable_backhaul_failover = True, 
                wireless_backhaul_switch_trigger_time = 1, 
                wired_backhaul_revert_hold_time = 1, 
                enable_band_steering = True, 
                band_steering_mode = '0', 
                ratio_for5g_clients = 1, 
                ignore_initial_client_connection_number = 1, 
                enable_client_load_balancing = True, 
                load_balancing_mode = '0', 
                crc_error_rate_per_device = 1, 
                rf_interference_per_device = 1, 
                average_airtime_per_client = 1, 
                anchor_period = 10, 
                neighbor_query_interval = 1, 
                enable_weak_signal_probe_request_suppression = True, 
                weak_snr_threshold = 1, 
                enable_safety_net = True, 
                safety_net_period = 5, 
                enable_high_density = True, 
                management_frame_basic_data_rate = '0', 
                enable_suppress_successive_probe_request = True, 
                probe_response_reduction_option = '0', 
                suppression_limit = 1, 
                enable_radio_balance = True, 
                mac_oui_ids = [
                    56
                    ], 
                enable_ampdu = True, 
                enable_mu_mimo = True, 
                enable_ofdma_down_link = True, 
                enable_ofdma_up_link = True, 
                bss_coloring = 1, 
                enable_target_weak_time = True
            )
        else :
            return XiqUpdateRpRadioUsageOptimizationRequest(
        )

    def testXiqUpdateRpRadioUsageOptimizationRequest(self):
        """Test XiqUpdateRpRadioUsageOptimizationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
