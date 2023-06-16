# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.device_api import DeviceApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.device_api.DeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_device_location(self):
        """Test case for assign_device_location

        Assign location to a device  # noqa: E501
        """
        pass

    def test_assign_device_network_policy(self):
        """Test case for assign_device_network_policy

        Assign network policy to a device  # noqa: E501
        """
        pass

    def test_assign_devices_country_code(self):
        """Test case for assign_devices_country_code

        Assign a country code to devices  # noqa: E501
        """
        pass

    def test_assign_devices_location(self):
        """Test case for assign_devices_location

        Assign location to multiple devices  # noqa: E501
        """
        pass

    def test_assign_devices_network_policy(self):
        """Test case for assign_devices_network_policy

        Assign network policy to multiple devices  # noqa: E501
        """
        pass

    def test_assign_devices_radius_proxy(self):
        """Test case for assign_devices_radius_proxy

        Assign RADIUS proxy to devices  # noqa: E501
        """
        pass

    def test_bounce_device_port(self):
        """Test case for bounce_device_port

        Bounce port of a device (EXOS, VOSS and SR Switches  # noqa: E501
        """
        pass

    def test_change_device_description(self):
        """Test case for change_device_description

        Change description for a device  # noqa: E501
        """
        pass

    def test_change_device_level_ssid_status(self):
        """Test case for change_device_level_ssid_status

        Enable or disable SSID for a device  # noqa: E501
        """
        pass

    def test_change_device_status_to_manage(self):
        """Test case for change_device_status_to_manage

        Change admin state to 'Managed' for a device  # noqa: E501
        """
        pass

    def test_change_device_status_to_unmanage(self):
        """Test case for change_device_status_to_unmanage

        Change admin state to 'Unmanaged' for a device  # noqa: E501
        """
        pass

    def test_change_devices_ibeacon(self):
        """Test case for change_devices_ibeacon

        Change iBeacon settings for devices  # noqa: E501
        """
        pass

    def test_change_devices_os_mode(self):
        """Test case for change_devices_os_mode

        Change device OS mode  # noqa: E501
        """
        pass

    def test_change_hostname(self):
        """Test case for change_hostname

        Change hostname for a device  # noqa: E501
        """
        pass

    def test_change_status_to_manage(self):
        """Test case for change_status_to_manage

        Change status to Managed  # noqa: E501
        """
        pass

    def test_change_status_to_unmanage(self):
        """Test case for change_status_to_unmanage

        Change status to Unmanaged  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete a device  # noqa: E501
        """
        pass

    def test_delete_devices(self):
        """Test case for delete_devices

        Delete devices  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Get device info for a specific device  # noqa: E501
        """
        pass

    def test_get_device_cpu_memory_history(self):
        """Test case for get_device_cpu_memory_history

        Get device CPU/memory usage history  # noqa: E501
        """
        pass

    def test_get_device_ibeacon(self):
        """Test case for get_device_ibeacon

        Get the device iBeacon setting  # noqa: E501
        """
        pass

    def test_get_device_level_ssid_status(self):
        """Test case for get_device_level_ssid_status

        Get SSID status for a device  # noqa: E501
        """
        pass

    def test_get_device_location(self):
        """Test case for get_device_location

        Get location for a device  # noqa: E501
        """
        pass

    def test_get_device_network_policy(self):
        """Test case for get_device_network_policy

        Get network policy for a device  # noqa: E501
        """
        pass

    def test_get_device_stats(self):
        """Test case for get_device_stats

        Get device stats  # noqa: E501
        """
        pass

    def test_get_device_wifi_interface(self):
        """Test case for get_device_wifi_interface

        Get the device WiFi interfaces stats  # noqa: E501
        """
        pass

    def test_get_xiq_device_installation_report(self):
        """Test case for get_xiq_device_installation_report

        Get device installation report  # noqa: E501
        """
        pass

    def test_list_device_alarm(self):
        """Test case for list_device_alarm

        List alarms for a device  # noqa: E501
        """
        pass

    def test_list_devices(self):
        """Test case for list_devices

        [LRO] List devices  # noqa: E501
        """
        pass

    def test_list_devices_by_network_policy(self):
        """Test case for list_devices_by_network_policy

        List assigned devices for network policy  # noqa: E501
        """
        pass

    def test_list_digital_twin_products(self):
        """Test case for list_digital_twin_products

        List Digital Twin product information.  # noqa: E501
        """
        pass

    def test_onboard_devices(self):
        """Test case for onboard_devices

        Onboard Devices  # noqa: E501
        """
        pass

    def test_override_device_level_ssid(self):
        """Test case for override_device_level_ssid

        Override SSID for a device  # noqa: E501
        """
        pass

    def test_query_devices_location(self):
        """Test case for query_devices_location

        Query location for multiple devices  # noqa: E501
        """
        pass

    def test_query_devices_network_policy(self):
        """Test case for query_devices_network_policy

        Query network policy for multiple devices  # noqa: E501
        """
        pass

    def test_reboot_device(self):
        """Test case for reboot_device

        Reboot a device  # noqa: E501
        """
        pass

    def test_reboot_devices(self):
        """Test case for reboot_devices

        Reboot devices  # noqa: E501
        """
        pass

    def test_reset_device(self):
        """Test case for reset_device

        [LRO] Reset a device to factory default  # noqa: E501
        """
        pass

    def test_revoke_device_location(self):
        """Test case for revoke_device_location

        Revoke location for a device  # noqa: E501
        """
        pass

    def test_revoke_device_network_policy(self):
        """Test case for revoke_device_network_policy

        Revoke network policy for a device  # noqa: E501
        """
        pass

    def test_revoke_devices_location(self):
        """Test case for revoke_devices_location

        Revoke location for multiple devices  # noqa: E501
        """
        pass

    def test_revoke_devices_network_policy(self):
        """Test case for revoke_devices_network_policy

        Revoke network policy for multiple devices  # noqa: E501
        """
        pass

    def test_revoke_devices_radius_proxy(self):
        """Test case for revoke_devices_radius_proxy

        Revoke RADIUS proxy from multiple devices  # noqa: E501
        """
        pass

    def test_send_cli_to_device(self):
        """Test case for send_cli_to_device

        Send CLI to a device  # noqa: E501
        """
        pass

    def test_send_cli_to_devices(self):
        """Test case for send_cli_to_devices

        [LRO] Send CLI to devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
