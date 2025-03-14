# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.dashboard_wireless_client_health_export.post import ExportToCsv2
from extremecloudiq.paths.dashboard_wireless_client_health_issue_association.post import GetClientAssociationIssues
from extremecloudiq.paths.dashboard_wireless_client_health_issue_authentication.post import GetClientAuthIssues
from extremecloudiq.paths.dashboard_wireless_client_health_frequency_distribution.post import GetClientFrequencyDistribution
from extremecloudiq.paths.dashboard_wireless_client_health_connectivity_issues.post import GetClientHealthConnectivityIssues
from extremecloudiq.paths.dashboard_wireless_client_health_grid.post import GetClientHealthGrid
from extremecloudiq.paths.dashboard_wireless_client_health_filter_metadata.post import GetClientHealthGridFilterMetadata
from extremecloudiq.paths.dashboard_wireless_client_health_roaming_issues.post import GetClientHealthRoamingIssues
from extremecloudiq.paths.dashboard_wireless_client_health_issue_ipaddress.post import GetClientIpAddressIssues
from extremecloudiq.paths.dashboard_wireless_client_health_issue_roaming.post import GetClientRoamingIssues


class DashboardWirelessClientHealthApi(
    ExportToCsv2,
    GetClientAssociationIssues,
    GetClientAuthIssues,
    GetClientFrequencyDistribution,
    GetClientHealthConnectivityIssues,
    GetClientHealthGrid,
    GetClientHealthGridFilterMetadata,
    GetClientHealthRoamingIssues,
    GetClientIpAddressIssues,
    GetClientRoamingIssues,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
