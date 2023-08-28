# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_rp_radio_usage_optimization import XiqRpRadioUsageOptimization  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqRpRadioUsageOptimization(unittest.TestCase):
    """XiqRpRadioUsageOptimization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqRpRadioUsageOptimization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_rp_radio_usage_optimization.XiqRpRadioUsageOptimization()  # noqa: E501
        if include_optional :
            return XiqRpRadioUsageOptimization(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                preamble = '0', 
                beacon_period = 56, 
                enable_frame_burst = True, 
                enable_smart_antenna = True, 
                enable_backhaul_failover = True, 
                wireless_backhaul_switch_trigger_time = 56, 
                wired_backhaul_revert_hold_time = 56, 
                enable_band_steering = True, 
                band_steering_mode = '0', 
                ignore_initial_client_connection_number = 56, 
                enable_client_load_balancing = True, 
                load_balancing_mode = '0', 
                crc_error_rate_per_device = 56, 
                rf_interference_per_device = 56, 
                average_airtime_per_client = 56, 
                anchor_period = 56, 
                neighbor_query_interval = 56, 
                enable_weak_signal_probe_request_suppression = True, 
                weak_snr_threshold = 56, 
                enable_safety_net = True, 
                safety_net_period = 56, 
                enable_high_density = True, 
                management_frame_basic_data_rate = '0', 
                enable_suppress_successive_probe_request = True, 
                probe_response_reduction_option = '0', 
                suppression_limit = 56, 
                enable_radio_balance = True, 
                enable_ampdu = True, 
                enable_mu_mimo = True, 
                enable_ofdma_down_link = True, 
                enable_ofdma_up_link = True, 
                bss_coloring = 56, 
                enable_target_weak_time = True, 
                mac_ouis = [
                    extremecloudiq.models.xiq_rp_mac_oui_profile.XiqRpMacOuiProfile(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        predefined = True, 
                        value = '0', 
                        mac_type = '0', 
                        defender_defined = True, 
                        extreme_iot_defined = True, )
                    ], 
                ratio_for_5g_clients = 56
            )
        else :
            return XiqRpRadioUsageOptimization(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqRpRadioUsageOptimization(self):
        """Test XiqRpRadioUsageOptimization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
