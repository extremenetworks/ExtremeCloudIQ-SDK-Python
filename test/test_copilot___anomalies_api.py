# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.copilot___anomalies_api import CopilotAnomaliesApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestCopilotAnomaliesApi(unittest.TestCase):
    """CopilotAnomaliesApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.copilot___anomalies_api.CopilotAnomaliesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_anomalies_notifications(self):
        """Test case for get_anomalies_notifications

        """
        pass

    def test_get_anomalies_report(self):
        """Test case for get_anomalies_report

        """
        pass

    def test_get_assurance_scans_overview_data(self):
        """Test case for get_assurance_scans_overview_data

        """
        pass

    def test_get_atp_device_stats(self):
        """Test case for get_atp_device_stats

        """
        pass

    def test_get_atp_packet_counts(self):
        """Test case for get_atp_packet_counts

        """
        pass

    def test_get_copilot_anomaliesby_category(self):
        """Test case for get_copilot_anomaliesby_category

        """
        pass

    def test_get_copilot_devices_with_locations(self):
        """Test case for get_copilot_devices_with_locations

        """
        pass

    def test_get_devices_by_location(self):
        """Test case for get_devices_by_location

        """
        pass

    def test_get_dfs_recurrence_channel_stats(self):
        """Test case for get_dfs_recurrence_channel_stats

        """
        pass

    def test_get_dfs_recurrence_count_stats(self):
        """Test case for get_dfs_recurrence_count_stats

        """
        pass

    def test_get_poe_flapping_stats(self):
        """Test case for get_poe_flapping_stats

        """
        pass

    def test_get_port_efficiency_speed_duplex_stats(self):
        """Test case for get_port_efficiency_speed_duplex_stats

        """
        pass

    def test_get_port_efficiency_stats(self):
        """Test case for get_port_efficiency_stats

        """
        pass

    def test_get_wifi_capacity_client_list(self):
        """Test case for get_wifi_capacity_client_list

        """
        pass

    def test_get_wifi_capacity_stats(self):
        """Test case for get_wifi_capacity_stats

        """
        pass

    def test_get_wifi_efficiency_client_list(self):
        """Test case for get_wifi_efficiency_client_list

        """
        pass

    def test_get_wifi_efficiency_stats(self):
        """Test case for get_wifi_efficiency_stats

        """
        pass

    def test_list_anomaly_locations(self):
        """Test case for list_anomaly_locations

        """
        pass

    def test_update_anomalies_feedback(self):
        """Test case for update_anomalies_feedback

        """
        pass

    def test_update_anomaly_action(self):
        """Test case for update_anomaly_action

        """
        pass

    def test_update_anomaly_device_action(self):
        """Test case for update_anomaly_device_action

        """
        pass

    def test_update_copilot_anomalies_devices_action(self):
        """Test case for update_copilot_anomalies_devices_action

        [LRO] Update Anomalies and Devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
