# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___policy_api import ConfigurationPolicyApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationPolicyApi(unittest.TestCase):
    """ConfigurationPolicyApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___policy_api.ConfigurationPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_cwp_to_ssid(self):
        """Test case for attach_cwp_to_ssid

        Attach CWP to an SSID  # noqa: E501
        """
        pass

    def test_attach_radius_server_group_to_ssid(self):
        """Test case for attach_radius_server_group_to_ssid

        Attach radius server group to an SSID  # noqa: E501
        """
        pass

    def test_attach_user_profile_to_ssid(self):
        """Test case for attach_user_profile_to_ssid

        Attach user profile to an SSID  # noqa: E501
        """
        pass

    def test_change_psk_password(self):
        """Test case for change_psk_password

        Change the SSID PSK password  # noqa: E501
        """
        pass

    def test_create_classification_rule(self):
        """Test case for create_classification_rule

        Create classification rule  # noqa: E501
        """
        pass

    def test_create_cloud_config_group(self):
        """Test case for create_cloud_config_group

        Create new cloud config group  # noqa: E501
        """
        pass

    def test_create_mac_oui_profile(self):
        """Test case for create_mac_oui_profile

        Create a MAC OUI profile  # noqa: E501
        """
        pass

    def test_create_radio_profile(self):
        """Test case for create_radio_profile

        Create a radio profile  # noqa: E501
        """
        pass

    def test_create_user_profile(self):
        """Test case for create_user_profile

        Create a user profile  # noqa: E501
        """
        pass

    def test_delete_classification_rule(self):
        """Test case for delete_classification_rule

        Delete classification rule by ID  # noqa: E501
        """
        pass

    def test_delete_cloud_config_group(self):
        """Test case for delete_cloud_config_group

        Delete a cloud config group  # noqa: E501
        """
        pass

    def test_delete_co_user_profile(self):
        """Test case for delete_co_user_profile

        Delete an user profile by ID  # noqa: E501
        """
        pass

    def test_delete_radio_profile(self):
        """Test case for delete_radio_profile

        Delete radio profile by ID  # noqa: E501
        """
        pass

    def test_delete_rp_mac_oui_profile(self):
        """Test case for delete_rp_mac_oui_profile

        Delete MAC OUI profile  # noqa: E501
        """
        pass

    def test_disable_ssid_cwp(self):
        """Test case for disable_ssid_cwp

        Disable the CWP on the SSID  # noqa: E501
        """
        pass

    def test_enable_ssid_cwp(self):
        """Test case for enable_ssid_cwp

        Enable and attach the CWP on the SSID  # noqa: E501
        """
        pass

    def test_get_classification_rule(self):
        """Test case for get_classification_rule

        Get a classification rule by ID  # noqa: E501
        """
        pass

    def test_get_cloud_config_group(self):
        """Test case for get_cloud_config_group

        Get a cloud config group  # noqa: E501
        """
        pass

    def test_get_neighborhood_analysis(self):
        """Test case for get_neighborhood_analysis

        Get neighborhood analysis settings  # noqa: E501
        """
        pass

    def test_get_radio_profile(self):
        """Test case for get_radio_profile

        Get radio profile by ID  # noqa: E501
        """
        pass

    def test_get_rp_channel_selection(self):
        """Test case for get_rp_channel_selection

        Get channel selection settings  # noqa: E501
        """
        pass

    def test_get_rp_mac_oui_profile(self):
        """Test case for get_rp_mac_oui_profile

        Get MAC OUI profile  # noqa: E501
        """
        pass

    def test_get_rp_miscellaneous_settings(self):
        """Test case for get_rp_miscellaneous_settings

        Get radio miscellaneous settings  # noqa: E501
        """
        pass

    def test_get_rp_radio_usage_optimization(self):
        """Test case for get_rp_radio_usage_optimization

        Get radio usage optimization settings  # noqa: E501
        """
        pass

    def test_get_rp_sensor_scan_settings(self):
        """Test case for get_rp_sensor_scan_settings

        Get sensor scan settings  # noqa: E501
        """
        pass

    def test_get_rp_wmm_qos_settings(self):
        """Test case for get_rp_wmm_qos_settings

        Get Wmm QoS settings  # noqa: E501
        """
        pass

    def test_get_user_profile(self):
        """Test case for get_user_profile

        Get user profile by ID  # noqa: E501
        """
        pass

    def test_list_classification_rules(self):
        """Test case for list_classification_rules

        List classification rules  # noqa: E501
        """
        pass

    def test_list_cloud_config_groups(self):
        """Test case for list_cloud_config_groups

        List clould config groups  # noqa: E501
        """
        pass

    def test_list_l3_address_profiles(self):
        """Test case for list_l3_address_profiles

        List L3 address profiles  # noqa: E501
        """
        pass

    def test_list_radio_profiles(self):
        """Test case for list_radio_profiles

        List radio profiles  # noqa: E501
        """
        pass

    def test_list_rp_mac_oui_profiles(self):
        """Test case for list_rp_mac_oui_profiles

        List MAC OUI profiles  # noqa: E501
        """
        pass

    def test_list_ssids(self):
        """Test case for list_ssids

        List SSIDs  # noqa: E501
        """
        pass

    def test_list_user_profiles(self):
        """Test case for list_user_profiles

        List user profiles  # noqa: E501
        """
        pass

    def test_rename_ssid(self):
        """Test case for rename_ssid

        Rename SSID (Wireless name)  # noqa: E501
        """
        pass

    def test_set_ssid_mode_dot1x(self):
        """Test case for set_ssid_mode_dot1x

        Change the SSID mode to 802.1x  # noqa: E501
        """
        pass

    def test_set_ssid_mode_open(self):
        """Test case for set_ssid_mode_open

        Change the SSID mode to open access  # noqa: E501
        """
        pass

    def test_set_ssid_mode_ppsk(self):
        """Test case for set_ssid_mode_ppsk

        Change the SSID mode to PPSK  # noqa: E501
        """
        pass

    def test_set_ssid_mode_psk(self):
        """Test case for set_ssid_mode_psk

        Change the SSID mode to PSK  # noqa: E501
        """
        pass

    def test_set_ssid_mode_wep(self):
        """Test case for set_ssid_mode_wep

        Change the SSID mode to WEP  # noqa: E501
        """
        pass

    def test_update_classification_rule(self):
        """Test case for update_classification_rule

        Update classification rule  # noqa: E501
        """
        pass

    def test_update_cloud_config_group(self):
        """Test case for update_cloud_config_group

        Update cloud config group information  # noqa: E501
        """
        pass

    def test_update_co_user_profile(self):
        """Test case for update_co_user_profile

        Update user profile  # noqa: E501
        """
        pass

    def test_update_neighborhood_analysis(self):
        """Test case for update_neighborhood_analysis

        Update neighborhood analysis settings  # noqa: E501
        """
        pass

    def test_update_radio_profile(self):
        """Test case for update_radio_profile

        Update radio profile by ID  # noqa: E501
        """
        pass

    def test_update_rp_channel_selection(self):
        """Test case for update_rp_channel_selection

        Update channel selection settings  # noqa: E501
        """
        pass

    def test_update_rp_mac_oui_profile(self):
        """Test case for update_rp_mac_oui_profile

        Update MAC OUI profile  # noqa: E501
        """
        pass

    def test_update_rp_miscellaneous_settings(self):
        """Test case for update_rp_miscellaneous_settings

        Update radio miscellaneous settings  # noqa: E501
        """
        pass

    def test_update_rp_radio_usage_optimization(self):
        """Test case for update_rp_radio_usage_optimization

        Update radio usage optimization settings  # noqa: E501
        """
        pass

    def test_update_rp_sensor_scan_settings(self):
        """Test case for update_rp_sensor_scan_settings

        Update sensor scan settings  # noqa: E501
        """
        pass

    def test_update_rp_wmm_qos_settings(self):
        """Test case for update_rp_wmm_qos_settings

        Update Wmm QoS settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
