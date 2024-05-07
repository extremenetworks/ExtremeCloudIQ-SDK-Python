# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
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

    def test_attach_client_monitor_profile_to_ssid(self):
        """Test case for attach_client_monitor_profile_to_ssid

        Attach client monitor profile to an SSID  # noqa: E501
        """
        pass

    def test_attach_cwp_to_ssid(self):
        """Test case for attach_cwp_to_ssid

        Attach CWP to an SSID  # noqa: E501
        """
        pass

    def test_attach_ip_firewall_policy_to_user_profile(self):
        """Test case for attach_ip_firewall_policy_to_user_profile

        Attach IP Firewall Policy to an User Profile  # noqa: E501
        """
        pass

    def test_attach_mac_firewall_policy_to_user_profile(self):
        """Test case for attach_mac_firewall_policy_to_user_profile

        Attach MAC Firewall Policy to an User Profile  # noqa: E501
        """
        pass

    def test_attach_radius_client_profile_to_ssid(self):
        """Test case for attach_radius_client_profile_to_ssid

        Attach RADIUS client profile to an SSID  # noqa: E501
        """
        pass

    def test_attach_radius_server_group_to_ssid(self):
        """Test case for attach_radius_server_group_to_ssid

        Attach radius server group to an SSID  # noqa: E501
        """
        pass

    def test_attach_service_to_ip_firewall_policy(self):
        """Test case for attach_service_to_ip_firewall_policy

        Attach IP Firewall Rule to IP Firewall policy  # noqa: E501
        """
        pass

    def test_attach_service_to_mac_firewall_policy(self):
        """Test case for attach_service_to_mac_firewall_policy

        Attach MAC Firewall Rule to MAC Firewall policy  # noqa: E501
        """
        pass

    def test_attach_user_profile_assignment_to_ssid(self):
        """Test case for attach_user_profile_assignment_to_ssid

        Attach user profile assignment to an SSID  # noqa: E501
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

    def test_create_client_monitor_profile(self):
        """Test case for create_client_monitor_profile

        Create a client monitor profile  # noqa: E501
        """
        pass

    def test_create_cloud_config_group(self):
        """Test case for create_cloud_config_group

        Create new cloud config group  # noqa: E501
        """
        pass

    def test_create_iot_profile(self):
        """Test case for create_iot_profile

        Create a IoT profile  # noqa: E501
        """
        pass

    def test_create_ip_firewall_policy(self):
        """Test case for create_ip_firewall_policy

        Create IP Firewall policy  # noqa: E501
        """
        pass

    def test_create_l3_address_profile(self):
        """Test case for create_l3_address_profile

        Create a L3 address profile  # noqa: E501
        """
        pass

    def test_create_mac_firewall_policy(self):
        """Test case for create_mac_firewall_policy

        Create MAC Firewall policy  # noqa: E501
        """
        pass

    def test_create_mac_object(self):
        """Test case for create_mac_object

        Create a mac object  # noqa: E501
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

    def test_create_user_profile_assignment(self):
        """Test case for create_user_profile_assignment

        Create a user profile assignment  # noqa: E501
        """
        pass

    def test_delete_classification_rule(self):
        """Test case for delete_classification_rule

        Delete classification rule by ID  # noqa: E501
        """
        pass

    def test_delete_client_monitor_profile(self):
        """Test case for delete_client_monitor_profile

        Delete an client monitor profile by ID  # noqa: E501
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

    def test_delete_iot_profile(self):
        """Test case for delete_iot_profile

        Delete IoT profile by ID  # noqa: E501
        """
        pass

    def test_delete_ip_firewall_policy(self):
        """Test case for delete_ip_firewall_policy

        Delete IP Firewall policy by ID  # noqa: E501
        """
        pass

    def test_delete_l3_address_profile(self):
        """Test case for delete_l3_address_profile

        Delete a L3 address profile by ID  # noqa: E501
        """
        pass

    def test_delete_mac_firewall_policy(self):
        """Test case for delete_mac_firewall_policy

        Delete MAC Firewall policy by ID  # noqa: E501
        """
        pass

    def test_delete_mac_object_profiles(self):
        """Test case for delete_mac_object_profiles

        Delete a MAC object by ID  # noqa: E501
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

    def test_delete_user_profile_assignment(self):
        """Test case for delete_user_profile_assignment

        Delete an user profile assignment by ID  # noqa: E501
        """
        pass

    def test_detach_ip_firewall_policy_from_user_profile(self):
        """Test case for detach_ip_firewall_policy_from_user_profile

        Detach IP Firewall Policy from an User Profile  # noqa: E501
        """
        pass

    def test_detach_mac_firewall_policy_from_user_profile(self):
        """Test case for detach_mac_firewall_policy_from_user_profile

        Detach MAC Firewall Policy from an User Profile  # noqa: E501
        """
        pass

    def test_detach_service_to_ip_firewall_policy(self):
        """Test case for detach_service_to_ip_firewall_policy

        Detach IP Firewall Rule from IP Firewall policy  # noqa: E501
        """
        pass

    def test_detach_service_to_mac_firewall_policy(self):
        """Test case for detach_service_to_mac_firewall_policy

        Detach MAC Firewall Rule from MAC Firewall policy  # noqa: E501
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

    def test_get_client_monitor_profile(self):
        """Test case for get_client_monitor_profile

        Get client monitor profile by ID  # noqa: E501
        """
        pass

    def test_get_cloud_config_group(self):
        """Test case for get_cloud_config_group

        Get a cloud config group  # noqa: E501
        """
        pass

    def test_get_iot_profile(self):
        """Test case for get_iot_profile

        Get IoT profile by ID  # noqa: E501
        """
        pass

    def test_get_ip_firewall_policy(self):
        """Test case for get_ip_firewall_policy

        Get IP Firewall Policy by ID  # noqa: E501
        """
        pass

    def test_get_l3_address_profile(self):
        """Test case for get_l3_address_profile

        Get a L3 address profile by ID  # noqa: E501
        """
        pass

    def test_get_mac_firewall_policy(self):
        """Test case for get_mac_firewall_policy

        Get MAC Firewall Policy by ID  # noqa: E501
        """
        pass

    def test_get_mac_object(self):
        """Test case for get_mac_object

        Get MAC Object by ID  # noqa: E501
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

    def test_get_ssid_advanced_settings(self):
        """Test case for get_ssid_advanced_settings

        Get SSID advanced settings  # noqa: E501
        """
        pass

    def test_get_user_profile(self):
        """Test case for get_user_profile

        Get user profile by ID  # noqa: E501
        """
        pass

    def test_get_user_profile_assignment(self):
        """Test case for get_user_profile_assignment

        Get user profile assignment by ID  # noqa: E501
        """
        pass

    def test_list_classification_rules(self):
        """Test case for list_classification_rules

        List classification rules  # noqa: E501
        """
        pass

    def test_list_client_monitor_profiles(self):
        """Test case for list_client_monitor_profiles

        List client monitor profiles  # noqa: E501
        """
        pass

    def test_list_cloud_config_groups(self):
        """Test case for list_cloud_config_groups

        List clould config groups  # noqa: E501
        """
        pass

    def test_list_iot_profiles(self):
        """Test case for list_iot_profiles

        List IoT profiles  # noqa: E501
        """
        pass

    def test_list_ip_firewall_policies(self):
        """Test case for list_ip_firewall_policies

        List IP Firewall policies  # noqa: E501
        """
        pass

    def test_list_l3_address_profiles(self):
        """Test case for list_l3_address_profiles

        List L3 address profiles  # noqa: E501
        """
        pass

    def test_list_mac_firewall_policies(self):
        """Test case for list_mac_firewall_policies

        List MAC Firewall policies  # noqa: E501
        """
        pass

    def test_list_mac_object_profiles(self):
        """Test case for list_mac_object_profiles

        List mac object profiles  # noqa: E501
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

    def test_list_user_profile_assignments(self):
        """Test case for list_user_profile_assignments

        List user profile assignments  # noqa: E501
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

    def test_update_client_monitor_profile(self):
        """Test case for update_client_monitor_profile

        Update client monitor profile  # noqa: E501
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

    def test_update_iot_profile(self):
        """Test case for update_iot_profile

        Update IoT profile by ID  # noqa: E501
        """
        pass

    def test_update_ip_policy_request(self):
        """Test case for update_ip_policy_request

        Update IP Firewall policy by ID  # noqa: E501
        """
        pass

    def test_update_l3_address_profile(self):
        """Test case for update_l3_address_profile

        Update a L3 address profile  # noqa: E501
        """
        pass

    def test_update_mac_firewall_policy(self):
        """Test case for update_mac_firewall_policy

        Update MAC Firewall policy by ID  # noqa: E501
        """
        pass

    def test_update_mac_object(self):
        """Test case for update_mac_object

        Update MAC Object by ID  # noqa: E501
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

    def test_update_ssid_advanced_settings(self):
        """Test case for update_ssid_advanced_settings

        Update SSID advanced settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
