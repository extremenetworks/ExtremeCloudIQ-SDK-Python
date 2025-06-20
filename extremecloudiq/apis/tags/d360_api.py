# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.d360_client_graph.post import GetClientGraph
from extremecloudiq.paths.d360_client_grid_metadata.get import GetClientGridMetadata
from extremecloudiq.paths.d360_client_stats.get import GetClientStats
from extremecloudiq.paths.d360_client_grid.post import GetClientStatsGrid
from extremecloudiq.paths.d360_device_issues.get import GetDeviceIssues
from extremecloudiq.paths.d360_device_metadata.get import GetDeviceMetaData
from extremecloudiq.paths.d360_device_stats.get import GetDeviceStats1
from extremecloudiq.paths.d360_overview_devices_summary.get import GetDeviceSummary1
from extremecloudiq.paths.d360_ssid_metadata.get import GetSsidMetadata
from extremecloudiq.paths.d360_wireless_surrounding_aps.post import GetSurroundingAps
from extremecloudiq.paths.d360_device_interfaces.get import GetWifiInterfacePerDevice
from extremecloudiq.paths.d360_wireless_interfaces_graph.get import GetWirelessInterfaceGraph
from extremecloudiq.paths.d360_wireless_interfaces_stats.get import GetWirelessWifi


class D360Api(
    GetClientGraph,
    GetClientGridMetadata,
    GetClientStats,
    GetClientStatsGrid,
    GetDeviceIssues,
    GetDeviceMetaData,
    GetDeviceStats1,
    GetDeviceSummary1,
    GetSsidMetadata,
    GetSurroundingAps,
    GetWifiInterfacePerDevice,
    GetWirelessInterfaceGraph,
    GetWirelessWifi,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
