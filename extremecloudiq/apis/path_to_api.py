import typing_extensions

from extremecloudiq.paths import PathValues
from extremecloudiq.apis.paths.usergroups_id import UsergroupsId
from extremecloudiq.apis.paths.user_profiles_id import UserProfilesId
from extremecloudiq.apis.paths.tunnel_concentrators_id import TunnelConcentratorsId
from extremecloudiq.apis.paths.ssids_id_psk_password import SsidsIdPskPassword
from extremecloudiq.apis.paths.ssids_id_mode_wep import SsidsIdModeWep
from extremecloudiq.apis.paths.ssids_id_mode_psk import SsidsIdModePsk
from extremecloudiq.apis.paths.ssids_id_mode_ppsk import SsidsIdModePpsk
from extremecloudiq.apis.paths.ssids_id_mode_open import SsidsIdModeOpen
from extremecloudiq.apis.paths.ssids_id_mode_dot1x import SsidsIdModeDot1x
from extremecloudiq.apis.paths.ssids_advanced_settings_id import SsidsAdvancedSettingsId
from extremecloudiq.apis.paths.site_afc_schedule import SiteAfcSchedule
from extremecloudiq.apis.paths.radius_servers_internal_id import RadiusServersInternalId
from extremecloudiq.apis.paths.radius_servers_external_id import RadiusServersExternalId
from extremecloudiq.apis.paths.radius_proxies_id import RadiusProxiesId
from extremecloudiq.apis.paths.radius_client_objects_id import RadiusClientObjectsId
from extremecloudiq.apis.paths.radio_profiles_id import RadioProfilesId
from extremecloudiq.apis.paths.radio_profiles_wmm_qos_id import RadioProfilesWmmQosId
from extremecloudiq.apis.paths.radio_profiles_sensor_scan_id import RadioProfilesSensorScanId
from extremecloudiq.apis.paths.radio_profiles_radio_usage_opt_id import RadioProfilesRadioUsageOptId
from extremecloudiq.apis.paths.radio_profiles_neighborhood_analysis_id import RadioProfilesNeighborhoodAnalysisId
from extremecloudiq.apis.paths.radio_profiles_miscellaneous_id import RadioProfilesMiscellaneousId
from extremecloudiq.apis.paths.radio_profiles_mac_ouis_id import RadioProfilesMacOuisId
from extremecloudiq.apis.paths.radio_profiles_channel_selection_id import RadioProfilesChannelSelectionId
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id_users import PcgsKeyBasedNetworkPolicyPolicyIdUsers
from extremecloudiq.apis.paths.network_policies_id import NetworkPoliciesId
from extremecloudiq.apis.paths.mac_object_profiles_id import MacObjectProfilesId
from extremecloudiq.apis.paths.mac_firewall_policies_id import MacFirewallPoliciesId
from extremecloudiq.apis.paths.locations_id import LocationsId
from extremecloudiq.apis.paths.locations_site_id import LocationsSiteId
from extremecloudiq.apis.paths.locations_floor_id import LocationsFloorId
from extremecloudiq.apis.paths.locations_building_id import LocationsBuildingId
from extremecloudiq.apis.paths.ldap_servers_id import LdapServersId
from extremecloudiq.apis.paths.l3_address_profiles_id import L3AddressProfilesId
from extremecloudiq.apis.paths.ip_firewall_policies_id import IpFirewallPoliciesId
from extremecloudiq.apis.paths.iot_profiles_id import IotProfilesId
from extremecloudiq.apis.paths.hotspot_service_provider_profiles_id import HotspotServiceProviderProfilesId
from extremecloudiq.apis.paths.hotspot_profiles_id import HotspotProfilesId
from extremecloudiq.apis.paths.hiq_context import HiqContext
from extremecloudiq.apis.paths.hiq_context_reading import HiqContextReading
from extremecloudiq.apis.paths.hiq_context_creating import HiqContextCreating
from extremecloudiq.apis.paths.endusers_id import EndusersId
from extremecloudiq.apis.paths.devices_id_radio_operating_mode import DevicesIdRadioOperatingMode
from extremecloudiq.apis.paths.devices_id_network_policy import DevicesIdNetworkPolicy
from extremecloudiq.apis.paths.devices_id_location import DevicesIdLocation
from extremecloudiq.apis.paths.devices_id_hostname import DevicesIdHostname
from extremecloudiq.apis.paths.devices_id_ftm_settings import DevicesIdFtmSettings
from extremecloudiq.apis.paths.devices_id_description import DevicesIdDescription
from extremecloudiq.apis.paths.devices_id_client_monitor import DevicesIdClientMonitor
from extremecloudiq.apis.paths.devices_radius_proxy_assign import DevicesRadiusProxyAssign
from extremecloudiq.apis.paths.devices_ibeacon import DevicesIbeacon
from extremecloudiq.apis.paths.deployments_deployment_id import DeploymentsDeploymentId
from extremecloudiq.apis.paths.copilot_anomalies_update_device_action import CopilotAnomaliesUpdateDeviceAction
from extremecloudiq.apis.paths.copilot_anomalies_update_action import CopilotAnomaliesUpdateAction
from extremecloudiq.apis.paths.copilot_anomalies_devices_update_action import CopilotAnomaliesDevicesUpdateAction
from extremecloudiq.apis.paths.copilot_anomalies_devices_feedback import CopilotAnomaliesDevicesFeedback
from extremecloudiq.apis.paths.clients_alias import ClientsAlias
from extremecloudiq.apis.paths.client_monitor_profiles_id import ClientMonitorProfilesId
from extremecloudiq.apis.paths.classification_rules_id import ClassificationRulesId
from extremecloudiq.apis.paths.ccgs_id import CcgsId
from extremecloudiq.apis.paths.alert_subscriptions_webhooks_id import AlertSubscriptionsWebhooksId
from extremecloudiq.apis.paths.alert_subscriptions_emails_id import AlertSubscriptionsEmailsId
from extremecloudiq.apis.paths.alert_policies_policy_id_rules_rule_id import AlertPoliciesPolicyIdRulesRuleId
from extremecloudiq.apis.paths.alert_policies_id import AlertPoliciesId
from extremecloudiq.apis.paths.account_viq_default_device_password import AccountViqDefaultDevicePassword
from extremecloudiq.apis.paths.vlan_profiles import VlanProfiles
from extremecloudiq.apis.paths.vlan_profiles_delete import VlanProfilesDelete
from extremecloudiq.apis.paths.users import Users
from extremecloudiq.apis.paths.users_external import UsersExternal
from extremecloudiq.apis.paths.usergroups import Usergroups
from extremecloudiq.apis.paths.user_profiles import UserProfiles
from extremecloudiq.apis.paths.user_profiles_id_mac_firewall_policies_detach import UserProfilesIdMacFirewallPoliciesDetach
from extremecloudiq.apis.paths.user_profiles_id_mac_firewall_policies_attach import UserProfilesIdMacFirewallPoliciesAttach
from extremecloudiq.apis.paths.user_profiles_id_ip_firewall_policies_detach import UserProfilesIdIpFirewallPoliciesDetach
from extremecloudiq.apis.paths.user_profiles_id_ip_firewall_policies_attach import UserProfilesIdIpFirewallPoliciesAttach
from extremecloudiq.apis.paths.user_profile_assignments import UserProfileAssignments
from extremecloudiq.apis.paths.tunnel_concentrators import TunnelConcentrators
from extremecloudiq.apis.paths.subscriptions_webhook import SubscriptionsWebhook
from extremecloudiq.apis.paths.ssids_id_user_profile_attach import SsidsIdUserProfileAttach
from extremecloudiq.apis.paths.ssids_id_user_profile_assignment_attach import SsidsIdUserProfileAssignmentAttach
from extremecloudiq.apis.paths.ssids_id_radius_server_group_attach import SsidsIdRadiusServerGroupAttach
from extremecloudiq.apis.paths.ssids_id_radius_client_profile_attach import SsidsIdRadiusClientProfileAttach
from extremecloudiq.apis.paths.ssids_id_cwp_enable import SsidsIdCwpEnable
from extremecloudiq.apis.paths.ssids_id_cwp_disable import SsidsIdCwpDisable
from extremecloudiq.apis.paths.ssids_id_cwp_attach import SsidsIdCwpAttach
from extremecloudiq.apis.paths.ssids_id_client_monitor_profile_attach import SsidsIdClientMonitorProfileAttach
from extremecloudiq.apis.paths.ssids_id_rename import SsidsIdRename
from extremecloudiq.apis.paths.site_spectrum_ import SiteSpectrum
from extremecloudiq.apis.paths.rtts import Rtts
from extremecloudiq.apis.paths.radius_servers_internal import RadiusServersInternal
from extremecloudiq.apis.paths.radius_servers_external import RadiusServersExternal
from extremecloudiq.apis.paths.radius_proxies import RadiusProxies
from extremecloudiq.apis.paths.radius_client_objects import RadiusClientObjects
from extremecloudiq.apis.paths.radio_profiles import RadioProfiles
from extremecloudiq.apis.paths.radio_profiles_mac_ouis import RadioProfilesMacOuis
from extremecloudiq.apis.paths.pcgs_key_based import PcgsKeyBased
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id_port_assignments import PcgsKeyBasedNetworkPolicyPolicyIdPortAssignments
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id_keys_generate import PcgsKeyBasedNetworkPolicyPolicyIdKeysGenerate
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id_keys_email import PcgsKeyBasedNetworkPolicyPolicyIdKeysEmail
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id_onboard import PcgsKeyBasedNetworkPolicyPolicyIdOnboard
from extremecloudiq.apis.paths.packetcaptures import Packetcaptures
from extremecloudiq.apis.paths.packetcaptures_id_upload import PacketcapturesIdUpload
from extremecloudiq.apis.paths.packetcaptures_id_stop import PacketcapturesIdStop
from extremecloudiq.apis.paths.operations_operation_id_cancel import OperationsOperationIdCancel
from extremecloudiq.apis.paths.nos_device_device_id_nos_api import NosDeviceDeviceIdNosApi
from extremecloudiq.apis.paths.network_services import NetworkServices
from extremecloudiq.apis.paths.network_policies import NetworkPolicies
from extremecloudiq.apis.paths.network_policies_id_ssids_remove import NetworkPoliciesIdSsidsRemove
from extremecloudiq.apis.paths.network_policies_id_ssids_add import NetworkPoliciesIdSsidsAdd
from extremecloudiq.apis.paths.mac_object_profiles import MacObjectProfiles
from extremecloudiq.apis.paths.mac_firewall_policies import MacFirewallPolicies
from extremecloudiq.apis.paths.mac_firewall_policies_id_mac_firewall_rule_detach import MacFirewallPoliciesIdMacFirewallRuleDetach
from extremecloudiq.apis.paths.mac_firewall_policies_id_mac_firewall_rule_attach import MacFirewallPoliciesIdMacFirewallRuleAttach
from extremecloudiq.apis.paths.logs_audit_reports import LogsAuditReports
from extremecloudiq.apis.paths.logout import Logout
from extremecloudiq.apis.paths.login import Login
from extremecloudiq.apis.paths.locations import Locations
from extremecloudiq.apis.paths.locations_site import LocationsSite
from extremecloudiq.apis.paths.locations_import_ekahau import LocationsImportEkahau
from extremecloudiq.apis.paths.locations_floorplan import LocationsFloorplan
from extremecloudiq.apis.paths.locations_floor import LocationsFloor
from extremecloudiq.apis.paths.locations_building import LocationsBuilding
from extremecloudiq.apis.paths.locations_init import LocationsInit
from extremecloudiq.apis.paths.ldap_servers import LdapServers
from extremecloudiq.apis.paths.l3_address_profiles import L3AddressProfiles
from extremecloudiq.apis.paths.ip_firewall_policies import IpFirewallPolicies
from extremecloudiq.apis.paths.ip_firewall_policies_id_ip_firewall_rule_detach import IpFirewallPoliciesIdIpFirewallRuleDetach
from extremecloudiq.apis.paths.ip_firewall_policies_id_ip_firewall_rule_attach import IpFirewallPoliciesIdIpFirewallRuleAttach
from extremecloudiq.apis.paths.iot_profiles import IotProfiles
from extremecloudiq.apis.paths.hotspot_service_provider_profiles import HotspotServiceProviderProfiles
from extremecloudiq.apis.paths.hotspot_profiles import HotspotProfiles
from extremecloudiq.apis.paths.hiq_organizations import HiqOrganizations
from extremecloudiq.apis.paths.hiq_organizations_id_rename import HiqOrganizationsIdRename
from extremecloudiq.apis.paths.endusers import Endusers
from extremecloudiq.apis.paths.endusers_id_regenerate_password import EndusersIdRegeneratePassword
from extremecloudiq.apis.paths.devices_id_thread_commissioner_stop import DevicesIdThreadCommissionerStop
from extremecloudiq.apis.paths.devices_id_thread_commissioner_start import DevicesIdThreadCommissionerStart
from extremecloudiq.apis.paths.devices_id_ssid_status_change import DevicesIdSsidStatusChange
from extremecloudiq.apis.paths.devices_id_ssid_override import DevicesIdSsidOverride
from extremecloudiq.apis.paths.devices_id_monitor_refresh import DevicesIdMonitorRefresh
from extremecloudiq.apis.paths.devices_id_iot_enable import DevicesIdIotEnable
from extremecloudiq.apis.paths.devices_id_iot_disable import DevicesIdIotDisable
from extremecloudiq.apis.paths.devices_id_bounce_port import DevicesIdBouncePort
from extremecloudiq.apis.paths.devices_id_unmanage import DevicesIdUnmanage
from extremecloudiq.apis.paths.devices_id_reset import DevicesIdReset
from extremecloudiq.apis.paths.devices_id_reboot import DevicesIdReboot
from extremecloudiq.apis.paths.devices_id_manage import DevicesIdManage
from extremecloudiq.apis.paths.devices_id_cli import DevicesIdCli
from extremecloudiq.apis.paths.devices_os_change import DevicesOsChange
from extremecloudiq.apis.paths.devices_network_policy_revoke import DevicesNetworkPolicyRevoke
from extremecloudiq.apis.paths.devices_network_policy_query import DevicesNetworkPolicyQuery
from extremecloudiq.apis.paths.devices_network_policy_assign import DevicesNetworkPolicyAssign
from extremecloudiq.apis.paths.devices_location_revoke import DevicesLocationRevoke
from extremecloudiq.apis.paths.devices_location_query import DevicesLocationQuery
from extremecloudiq.apis.paths.devices_location_assign import DevicesLocationAssign
from extremecloudiq.apis.paths.devices_country_code_assign import DevicesCountryCodeAssign
from extremecloudiq.apis.paths.devices_client_monitor_revoke import DevicesClientMonitorRevoke
from extremecloudiq.apis.paths.devices_client_monitor_query import DevicesClientMonitorQuery
from extremecloudiq.apis.paths.devices_client_monitor_assign import DevicesClientMonitorAssign
from extremecloudiq.apis.paths.devices_unmanage import DevicesUnmanage
from extremecloudiq.apis.paths.devices_reboot import DevicesReboot
from extremecloudiq.apis.paths.devices_onboard import DevicesOnboard
from extremecloudiq.apis.paths.devices_manage import DevicesManage
from extremecloudiq.apis.paths.devices_delete import DevicesDelete
from extremecloudiq.apis.paths.devices_cli import DevicesCli
from extremecloudiq.apis.paths.devices_check_ownership import DevicesCheckOwnership
from extremecloudiq.apis.paths.devices_advanced_onboard import DevicesAdvancedOnboard
from extremecloudiq.apis.paths.deployments import Deployments
from extremecloudiq.apis.paths.deployments_firmware_metadatas import DeploymentsFirmwareMetadatas
from extremecloudiq.apis.paths.copilot_anomalies_exclude_vlans import CopilotAnomaliesExcludeVlans
from extremecloudiq.apis.paths.copilot_anomalies_exclude_vlans_csv import CopilotAnomaliesExcludeVlansCsv
from extremecloudiq.apis.paths.client_monitor_profiles import ClientMonitorProfiles
from extremecloudiq.apis.paths.classification_rules import ClassificationRules
from extremecloudiq.apis.paths.ccgs import Ccgs
from extremecloudiq.apis.paths.auth_permissions_check import AuthPermissionsCheck
from extremecloudiq.apis.paths.auth_apitoken import AuthApitoken
from extremecloudiq.apis.paths.auth_apitoken_validate import AuthApitokenValidate
from extremecloudiq.apis.paths.aps_afc_update import ApsAfcUpdate
from extremecloudiq.apis.paths.ap_spectrum_ import ApSpectrum
from extremecloudiq.apis.paths.alerts_reports import AlertsReports
from extremecloudiq.apis.paths.alerts_acknowledge import AlertsAcknowledge
from extremecloudiq.apis.paths.alert_subscriptions_webhooks import AlertSubscriptionsWebhooks
from extremecloudiq.apis.paths.alert_subscriptions_webhooks_delete import AlertSubscriptionsWebhooksDelete
from extremecloudiq.apis.paths.alert_subscriptions_emails import AlertSubscriptionsEmails
from extremecloudiq.apis.paths.alert_subscriptions_emails_id_verify import AlertSubscriptionsEmailsIdVerify
from extremecloudiq.apis.paths.alert_subscriptions_emails_delete import AlertSubscriptionsEmailsDelete
from extremecloudiq.apis.paths.alert_policies import AlertPolicies
from extremecloudiq.apis.paths.alert_policies_policy_id_rules_rule_id_enable import AlertPoliciesPolicyIdRulesRuleIdEnable
from extremecloudiq.apis.paths.alert_policies_policy_id_rules_rule_id_disable import AlertPoliciesPolicyIdRulesRuleIdDisable
from extremecloudiq.apis.paths.account_viq_import import AccountViqImport
from extremecloudiq.apis.paths.account_viq_export import AccountViqExport
from extremecloudiq.apis.paths.account_viq_backup import AccountViqBackup
from extremecloudiq.apis.paths.account_switch import AccountSwitch
from extremecloudiq.apis.paths.vlan_profiles_id import VlanProfilesId
from extremecloudiq.apis.paths.users_id import UsersId
from extremecloudiq.apis.paths.users_external_id import UsersExternalId
from extremecloudiq.apis.paths.users_me import UsersMe
from extremecloudiq.apis.paths.user_profile_assignments_id import UserProfileAssignmentsId
from extremecloudiq.apis.paths.ucp_id_engines_installed import UcpIdEnginesInstalled
from extremecloudiq.apis.paths.thread_topology import ThreadTopology
from extremecloudiq.apis.paths.thread_routers import ThreadRouters
from extremecloudiq.apis.paths.thread_networks import ThreadNetworks
from extremecloudiq.apis.paths.ssids import Ssids
from extremecloudiq.apis.paths.sms_templates import SmsTemplates
from extremecloudiq.apis.paths.radius_servers_internal_devices import RadiusServersInternalDevices
from extremecloudiq.apis.paths.radius_proxies_devices import RadiusProxiesDevices
from extremecloudiq.apis.paths.radio_operating_modes_product_type import RadioOperatingModesProductType
from extremecloudiq.apis.paths.packetcaptures_id import PacketcapturesId
from extremecloudiq.apis.paths.packetcaptures_files import PacketcapturesFiles
from extremecloudiq.apis.paths.operations_operation_id import OperationsOperationId
from extremecloudiq.apis.paths.network_scorecard_wifi_health_location_id import NetworkScorecardWifiHealthLocationId
from extremecloudiq.apis.paths.network_scorecard_services_health_location_id import NetworkScorecardServicesHealthLocationId
from extremecloudiq.apis.paths.network_scorecard_network_health_location_id import NetworkScorecardNetworkHealthLocationId
from extremecloudiq.apis.paths.network_scorecard_device_health_location_id import NetworkScorecardDeviceHealthLocationId
from extremecloudiq.apis.paths.network_scorecard_client_health_location_id import NetworkScorecardClientHealthLocationId
from extremecloudiq.apis.paths.network_policies_id_ssids import NetworkPoliciesIdSsids
from extremecloudiq.apis.paths.logs_sms import LogsSms
from extremecloudiq.apis.paths.logs_email import LogsEmail
from extremecloudiq.apis.paths.logs_credential import LogsCredential
from extremecloudiq.apis.paths.logs_auth import LogsAuth
from extremecloudiq.apis.paths.logs_audit import LogsAudit
from extremecloudiq.apis.paths.logs_audit_reports_id import LogsAuditReportsId
from extremecloudiq.apis.paths.logs_audit_full_descriptions_id import LogsAuditFullDescriptionsId
from extremecloudiq.apis.paths.logs_accounting import LogsAccounting
from extremecloudiq.apis.paths.locations_tree import LocationsTree
from extremecloudiq.apis.paths.locations_tree_maps import LocationsTreeMaps
from extremecloudiq.apis.paths.locations_tree_devices import LocationsTreeDevices
from extremecloudiq.apis.paths.hiq_status import HiqStatus
from extremecloudiq.apis.paths.essentials_eloc_clients_client_mac_last_known_location import EssentialsElocClientsClientMacLastKnownLocation
from extremecloudiq.apis.paths.email_templates import EmailTemplates
from extremecloudiq.apis.paths.devices import Devices
from extremecloudiq.apis.paths.devices_id import DevicesId
from extremecloudiq.apis.paths.devices_id_ssid_status import DevicesIdSsidStatus
from extremecloudiq.apis.paths.devices_id_monitor_refresh_status import DevicesIdMonitorRefreshStatus
from extremecloudiq.apis.paths.devices_id_iot import DevicesIdIot
from extremecloudiq.apis.paths.devices_id_interfaces_wifi import DevicesIdInterfacesWifi
from extremecloudiq.apis.paths.devices_id_installation_report import DevicesIdInstallationReport
from extremecloudiq.apis.paths.devices_id_ibeacon import DevicesIdIbeacon
from extremecloudiq.apis.paths.devices_id_history_cpu_mem import DevicesIdHistoryCpuMem
from extremecloudiq.apis.paths.devices_id_geolocation import DevicesIdGeolocation
from extremecloudiq.apis.paths.devices_id_gallery_image import DevicesIdGalleryImage
from extremecloudiq.apis.paths.devices_id_alarms import DevicesIdAlarms
from extremecloudiq.apis.paths.devices_stats import DevicesStats
from extremecloudiq.apis.paths.devices_radio_information import DevicesRadioInformation
from extremecloudiq.apis.paths.devices_network_policy_policy_id import DevicesNetworkPolicyPolicyId
from extremecloudiq.apis.paths.devices_digital_twin import DevicesDigitalTwin
from extremecloudiq.apis.paths.deployments_deployment_id_status import DeploymentsDeploymentIdStatus
from extremecloudiq.apis.paths.deployments_status import DeploymentsStatus
from extremecloudiq.apis.paths.deployments_overview import DeploymentsOverview
from extremecloudiq.apis.paths.cwps import Cwps
from extremecloudiq.apis.paths.countries import Countries
from extremecloudiq.apis.paths.countries_country_code_validate import CountriesCountryCodeValidate
from extremecloudiq.apis.paths.countries_country_alpha2_code_states import CountriesCountryAlpha2CodeStates
from extremecloudiq.apis.paths.copilot_connectivity_wireless_views import CopilotConnectivityWirelessViews
from extremecloudiq.apis.paths.copilot_connectivity_wireless_time_to_connect import CopilotConnectivityWirelessTimeToConnect
from extremecloudiq.apis.paths.copilot_connectivity_wireless_quality_index import CopilotConnectivityWirelessQualityIndex
from extremecloudiq.apis.paths.copilot_connectivity_wireless_performance import CopilotConnectivityWirelessPerformance
from extremecloudiq.apis.paths.copilot_connectivity_wireless_locations_time_to_connect import CopilotConnectivityWirelessLocationsTimeToConnect
from extremecloudiq.apis.paths.copilot_connectivity_wireless_locations_quality_index import CopilotConnectivityWirelessLocationsQualityIndex
from extremecloudiq.apis.paths.copilot_connectivity_wireless_locations_performance import CopilotConnectivityWirelessLocationsPerformance
from extremecloudiq.apis.paths.copilot_connectivity_wireless_locations_events import CopilotConnectivityWirelessLocationsEvents
from extremecloudiq.apis.paths.copilot_connectivity_wireless_experience import CopilotConnectivityWirelessExperience
from extremecloudiq.apis.paths.copilot_connectivity_wireless_events import CopilotConnectivityWirelessEvents
from extremecloudiq.apis.paths.copilot_connectivity_wireless_apps import CopilotConnectivityWirelessApps
from extremecloudiq.apis.paths.copilot_connectivity_wired_quality_index import CopilotConnectivityWiredQualityIndex
from extremecloudiq.apis.paths.copilot_connectivity_wired_locations_hardware import CopilotConnectivityWiredLocationsHardware
from extremecloudiq.apis.paths.copilot_connectivity_wired_hardware import CopilotConnectivityWiredHardware
from extremecloudiq.apis.paths.copilot_connectivity_wired_experience import CopilotConnectivityWiredExperience
from extremecloudiq.apis.paths.copilot_connectivity_wired_events import CopilotConnectivityWiredEvents
from extremecloudiq.apis.paths.copilot_connectivity_locations import CopilotConnectivityLocations
from extremecloudiq.apis.paths.copilot_connectivity_client_type import CopilotConnectivityClientType
from extremecloudiq.apis.paths.copilot_assurance_scans_overview import CopilotAssuranceScansOverview
from extremecloudiq.apis.paths.copilot_anomalies_wifi_efficiency_stats import CopilotAnomaliesWifiEfficiencyStats
from extremecloudiq.apis.paths.copilot_anomalies_wifi_efficiency_client_list import CopilotAnomaliesWifiEfficiencyClientList
from extremecloudiq.apis.paths.copilot_anomalies_wifi_capacity_stats import CopilotAnomaliesWifiCapacityStats
from extremecloudiq.apis.paths.copilot_anomalies_wifi_capacity_client_list import CopilotAnomaliesWifiCapacityClientList
from extremecloudiq.apis.paths.copilot_anomalies_report import CopilotAnomaliesReport
from extremecloudiq.apis.paths.copilot_anomalies_port_efficiency_stats import CopilotAnomaliesPortEfficiencyStats
from extremecloudiq.apis.paths.copilot_anomalies_port_efficiency_speed_duplex_stats import CopilotAnomaliesPortEfficiencySpeedDuplexStats
from extremecloudiq.apis.paths.copilot_anomalies_poeflapping_trends import CopilotAnomaliesPoeflappingTrends
from extremecloudiq.apis.paths.copilot_anomalies_poeflapping_stats import CopilotAnomaliesPoeflappingStats
from extremecloudiq.apis.paths.copilot_anomalies_poeflapping_lldp_cdp_info import CopilotAnomaliesPoeflappingLldpCdpInfo
from extremecloudiq.apis.paths.copilot_anomalies_notifications import CopilotAnomaliesNotifications
from extremecloudiq.apis.paths.copilot_anomalies_missing_vlan_count import CopilotAnomaliesMissingVlanCount
from extremecloudiq.apis.paths.copilot_anomalies_locations import CopilotAnomaliesLocations
from extremecloudiq.apis.paths.copilot_anomalies_hardware_health_stats import CopilotAnomaliesHardwareHealthStats
from extremecloudiq.apis.paths.copilot_anomalies_hardware_health_cpu_mem_stats import CopilotAnomaliesHardwareHealthCpuMemStats
from extremecloudiq.apis.paths.copilot_anomalies_hardware_health_client_list import CopilotAnomaliesHardwareHealthClientList
from extremecloudiq.apis.paths.copilot_anomalies_excluded_vlans_list import CopilotAnomaliesExcludedVlansList
from extremecloudiq.apis.paths.copilot_anomalies_dfs_recurrence_count_stats import CopilotAnomaliesDfsRecurrenceCountStats
from extremecloudiq.apis.paths.copilot_anomalies_dfs_recurrence_channel_stats import CopilotAnomaliesDfsRecurrenceChannelStats
from extremecloudiq.apis.paths.copilot_anomalies_devices_with_locations import CopilotAnomaliesDevicesWithLocations
from extremecloudiq.apis.paths.copilot_anomalies_devices_by_location import CopilotAnomaliesDevicesByLocation
from extremecloudiq.apis.paths.copilot_anomalies_anomalies_by_category import CopilotAnomaliesAnomaliesByCategory
from extremecloudiq.apis.paths.copilot_anomalies_adverse_traffic_packet_counts import CopilotAnomaliesAdverseTrafficPacketCounts
from extremecloudiq.apis.paths.copilot_anomalies_adverse_traffic_device_stats import CopilotAnomaliesAdverseTrafficDeviceStats
from extremecloudiq.apis.paths.clients_id import ClientsId
from extremecloudiq.apis.paths.clients_usage import ClientsUsage
from extremecloudiq.apis.paths.clients_summary import ClientsSummary
from extremecloudiq.apis.paths.clients_by_mac_client_mac import ClientsByMacClientMac
from extremecloudiq.apis.paths.clients_active import ClientsActive
from extremecloudiq.apis.paths.clients_active_count import ClientsActiveCount
from extremecloudiq.apis.paths.certificates import Certificates
from extremecloudiq.apis.paths.auth_permissions import AuthPermissions
from extremecloudiq.apis.paths.auth_apitoken_info import AuthApitokenInfo
from extremecloudiq.apis.paths.aps_afc_query_ import ApsAfcQuery
from extremecloudiq.apis.paths.applications import Applications
from extremecloudiq.apis.paths.applications_id_clients_topn import ApplicationsIdClientsTopn
from extremecloudiq.apis.paths.applications_topn import ApplicationsTopn
from extremecloudiq.apis.paths.ap_afc_interface_details_sn import ApAfcInterfaceDetailsSn
from extremecloudiq.apis.paths.ap_afc_diagnostics_id import ApAfcDiagnosticsId
from extremecloudiq.apis.paths.alerts import Alerts
from extremecloudiq.apis.paths.alerts_reports_id import AlertsReportsId
from extremecloudiq.apis.paths.alerts_count_by_group import AlertsCountByGroup
from extremecloudiq.apis.paths.alert_policies_available_sites import AlertPoliciesAvailableSites
from extremecloudiq.apis.paths.afcserver import Afcserver
from extremecloudiq.apis.paths.afcserver_server_id import AfcserverServerId
from extremecloudiq.apis.paths.afcserver_statistics_server_id import AfcserverStatisticsServerId
from extremecloudiq.apis.paths.ad_servers import AdServers
from extremecloudiq.apis.paths.account_viq import AccountViq
from extremecloudiq.apis.paths.account_viq_export_import_status import AccountViqExportImportStatus
from extremecloudiq.apis.paths.account_viq_download import AccountViqDownload
from extremecloudiq.apis.paths.account_home import AccountHome
from extremecloudiq.apis.paths.account_external import AccountExternal
from extremecloudiq.apis.paths.subscriptions_webhook_id import SubscriptionsWebhookId
from extremecloudiq.apis.paths.rtts_id import RttsId
from extremecloudiq.apis.paths.pcgs_key_based_network_policy_policy_id import PcgsKeyBasedNetworkPolicyPolicyId
from extremecloudiq.apis.paths.network_services_id import NetworkServicesId
from extremecloudiq.apis.paths.hiq_organizations_id import HiqOrganizationsId
from extremecloudiq.apis.paths.devices_radius_proxy_revoke import DevicesRadiusProxyRevoke

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USERGROUPS_ID: UsergroupsId,
        PathValues.USERPROFILES_ID: UserProfilesId,
        PathValues.TUNNELCONCENTRATORS_ID: TunnelConcentratorsId,
        PathValues.SSIDS_ID_PSK_PASSWORD: SsidsIdPskPassword,
        PathValues.SSIDS_ID_MODE_WEP: SsidsIdModeWep,
        PathValues.SSIDS_ID_MODE_PSK: SsidsIdModePsk,
        PathValues.SSIDS_ID_MODE_PPSK: SsidsIdModePpsk,
        PathValues.SSIDS_ID_MODE_OPEN: SsidsIdModeOpen,
        PathValues.SSIDS_ID_MODE_DOT1X: SsidsIdModeDot1x,
        PathValues.SSIDS_ADVANCEDSETTINGS_ID: SsidsAdvancedSettingsId,
        PathValues.SITE_AFC_SCHEDULE: SiteAfcSchedule,
        PathValues.RADIUSSERVERS_INTERNAL_ID: RadiusServersInternalId,
        PathValues.RADIUSSERVERS_EXTERNAL_ID: RadiusServersExternalId,
        PathValues.RADIUSPROXIES_ID: RadiusProxiesId,
        PathValues.RADIUSCLIENTOBJECTS_ID: RadiusClientObjectsId,
        PathValues.RADIOPROFILES_ID: RadioProfilesId,
        PathValues.RADIOPROFILES_WMMQOS_ID: RadioProfilesWmmQosId,
        PathValues.RADIOPROFILES_SENSORSCAN_ID: RadioProfilesSensorScanId,
        PathValues.RADIOPROFILES_RADIOUSAGEOPT_ID: RadioProfilesRadioUsageOptId,
        PathValues.RADIOPROFILES_NEIGHBORHOODANALYSIS_ID: RadioProfilesNeighborhoodAnalysisId,
        PathValues.RADIOPROFILES_MISCELLANEOUS_ID: RadioProfilesMiscellaneousId,
        PathValues.RADIOPROFILES_MACOUIS_ID: RadioProfilesMacOuisId,
        PathValues.RADIOPROFILES_CHANNELSELECTION_ID: RadioProfilesChannelSelectionId,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_USERS: PcgsKeyBasedNetworkPolicyPolicyIdUsers,
        PathValues.NETWORKPOLICIES_ID: NetworkPoliciesId,
        PathValues.MACOBJECTPROFILES_ID: MacObjectProfilesId,
        PathValues.MACFIREWALLPOLICIES_ID: MacFirewallPoliciesId,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.LOCATIONS_SITE_ID: LocationsSiteId,
        PathValues.LOCATIONS_FLOOR_ID: LocationsFloorId,
        PathValues.LOCATIONS_BUILDING_ID: LocationsBuildingId,
        PathValues.LDAPSERVERS_ID: LdapServersId,
        PathValues.L3ADDRESSPROFILES_ID: L3AddressProfilesId,
        PathValues.IPFIREWALLPOLICIES_ID: IpFirewallPoliciesId,
        PathValues.IOTPROFILES_ID: IotProfilesId,
        PathValues.HOTSPOTSERVICEPROVIDERPROFILES_ID: HotspotServiceProviderProfilesId,
        PathValues.HOTSPOTPROFILES_ID: HotspotProfilesId,
        PathValues.HIQ_CONTEXT: HiqContext,
        PathValues.HIQ_CONTEXT_READING: HiqContextReading,
        PathValues.HIQ_CONTEXT_CREATING: HiqContextCreating,
        PathValues.ENDUSERS_ID: EndusersId,
        PathValues.DEVICES_ID_RADIOOPERATINGMODE: DevicesIdRadioOperatingMode,
        PathValues.DEVICES_ID_NETWORKPOLICY: DevicesIdNetworkPolicy,
        PathValues.DEVICES_ID_LOCATION: DevicesIdLocation,
        PathValues.DEVICES_ID_HOSTNAME: DevicesIdHostname,
        PathValues.DEVICES_ID_FTMSETTINGS: DevicesIdFtmSettings,
        PathValues.DEVICES_ID_DESCRIPTION: DevicesIdDescription,
        PathValues.DEVICES_ID_CLIENTMONITOR: DevicesIdClientMonitor,
        PathValues.DEVICES_RADIUSPROXY_ASSIGN: DevicesRadiusProxyAssign,
        PathValues.DEVICES_IBEACON: DevicesIbeacon,
        PathValues.DEPLOYMENTS_DEPLOYMENT_ID: DeploymentsDeploymentId,
        PathValues.COPILOT_ANOMALIES_UPDATEDEVICEACTION: CopilotAnomaliesUpdateDeviceAction,
        PathValues.COPILOT_ANOMALIES_UPDATEACTION: CopilotAnomaliesUpdateAction,
        PathValues.COPILOT_ANOMALIES_DEVICES_UPDATEACTION: CopilotAnomaliesDevicesUpdateAction,
        PathValues.COPILOT_ANOMALIES_DEVICES_FEEDBACK: CopilotAnomaliesDevicesFeedback,
        PathValues.CLIENTS_ALIAS: ClientsAlias,
        PathValues.CLIENTMONITORPROFILES_ID: ClientMonitorProfilesId,
        PathValues.CLASSIFICATIONRULES_ID: ClassificationRulesId,
        PathValues.CCGS_ID: CcgsId,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS_ID: AlertSubscriptionsWebhooksId,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_ID: AlertSubscriptionsEmailsId,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID: AlertPoliciesPolicyIdRulesRuleId,
        PathValues.ALERTPOLICIES_ID: AlertPoliciesId,
        PathValues.ACCOUNT_VIQ_DEFAULTDEVICEPASSWORD: AccountViqDefaultDevicePassword,
        PathValues.VLANPROFILES: VlanProfiles,
        PathValues.VLANPROFILES_DELETE: VlanProfilesDelete,
        PathValues.USERS: Users,
        PathValues.USERS_EXTERNAL: UsersExternal,
        PathValues.USERGROUPS: Usergroups,
        PathValues.USERPROFILES: UserProfiles,
        PathValues.USERPROFILES_ID_MACFIREWALLPOLICIES_DETACH: UserProfilesIdMacFirewallPoliciesDetach,
        PathValues.USERPROFILES_ID_MACFIREWALLPOLICIES_ATTACH: UserProfilesIdMacFirewallPoliciesAttach,
        PathValues.USERPROFILES_ID_IPFIREWALLPOLICIES_DETACH: UserProfilesIdIpFirewallPoliciesDetach,
        PathValues.USERPROFILES_ID_IPFIREWALLPOLICIES_ATTACH: UserProfilesIdIpFirewallPoliciesAttach,
        PathValues.USERPROFILEASSIGNMENTS: UserProfileAssignments,
        PathValues.TUNNELCONCENTRATORS: TunnelConcentrators,
        PathValues.SUBSCRIPTIONS_WEBHOOK: SubscriptionsWebhook,
        PathValues.SSIDS_ID_USERPROFILE_ATTACH: SsidsIdUserProfileAttach,
        PathValues.SSIDS_ID_USERPROFILEASSIGNMENT_ATTACH: SsidsIdUserProfileAssignmentAttach,
        PathValues.SSIDS_ID_RADIUSSERVERGROUP_ATTACH: SsidsIdRadiusServerGroupAttach,
        PathValues.SSIDS_ID_RADIUSCLIENTPROFILE_ATTACH: SsidsIdRadiusClientProfileAttach,
        PathValues.SSIDS_ID_CWP_ENABLE: SsidsIdCwpEnable,
        PathValues.SSIDS_ID_CWP_DISABLE: SsidsIdCwpDisable,
        PathValues.SSIDS_ID_CWP_ATTACH: SsidsIdCwpAttach,
        PathValues.SSIDS_ID_CLIENTMONITORPROFILE_ATTACH: SsidsIdClientMonitorProfileAttach,
        PathValues.SSIDS_ID_RENAME: SsidsIdRename,
        PathValues.SITE_SPECTRUM_: SiteSpectrum,
        PathValues.RTTS: Rtts,
        PathValues.RADIUSSERVERS_INTERNAL: RadiusServersInternal,
        PathValues.RADIUSSERVERS_EXTERNAL: RadiusServersExternal,
        PathValues.RADIUSPROXIES: RadiusProxies,
        PathValues.RADIUSCLIENTOBJECTS: RadiusClientObjects,
        PathValues.RADIOPROFILES: RadioProfiles,
        PathValues.RADIOPROFILES_MACOUIS: RadioProfilesMacOuis,
        PathValues.PCGS_KEYBASED: PcgsKeyBased,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_PORTASSIGNMENTS: PcgsKeyBasedNetworkPolicyPolicyIdPortAssignments,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_KEYS_GENERATE: PcgsKeyBasedNetworkPolicyPolicyIdKeysGenerate,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_KEYS_EMAIL: PcgsKeyBasedNetworkPolicyPolicyIdKeysEmail,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_ONBOARD: PcgsKeyBasedNetworkPolicyPolicyIdOnboard,
        PathValues.PACKETCAPTURES: Packetcaptures,
        PathValues.PACKETCAPTURES_ID_UPLOAD: PacketcapturesIdUpload,
        PathValues.PACKETCAPTURES_ID_STOP: PacketcapturesIdStop,
        PathValues.OPERATIONS_OPERATION_ID_CANCEL: OperationsOperationIdCancel,
        PathValues.NOS_DEVICE_DEVICE_ID_NOSAPI: NosDeviceDeviceIdNosApi,
        PathValues.NETWORKSERVICES: NetworkServices,
        PathValues.NETWORKPOLICIES: NetworkPolicies,
        PathValues.NETWORKPOLICIES_ID_SSIDS_REMOVE: NetworkPoliciesIdSsidsRemove,
        PathValues.NETWORKPOLICIES_ID_SSIDS_ADD: NetworkPoliciesIdSsidsAdd,
        PathValues.MACOBJECTPROFILES: MacObjectProfiles,
        PathValues.MACFIREWALLPOLICIES: MacFirewallPolicies,
        PathValues.MACFIREWALLPOLICIES_ID_MACFIREWALLRULE_DETACH: MacFirewallPoliciesIdMacFirewallRuleDetach,
        PathValues.MACFIREWALLPOLICIES_ID_MACFIREWALLRULE_ATTACH: MacFirewallPoliciesIdMacFirewallRuleAttach,
        PathValues.LOGS_AUDIT_REPORTS: LogsAuditReports,
        PathValues.LOGOUT: Logout,
        PathValues.LOGIN: Login,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_SITE: LocationsSite,
        PathValues.LOCATIONS_IMPORT_EKAHAU: LocationsImportEkahau,
        PathValues.LOCATIONS_FLOORPLAN: LocationsFloorplan,
        PathValues.LOCATIONS_FLOOR: LocationsFloor,
        PathValues.LOCATIONS_BUILDING: LocationsBuilding,
        PathValues.LOCATIONS_INIT: LocationsInit,
        PathValues.LDAPSERVERS: LdapServers,
        PathValues.L3ADDRESSPROFILES: L3AddressProfiles,
        PathValues.IPFIREWALLPOLICIES: IpFirewallPolicies,
        PathValues.IPFIREWALLPOLICIES_ID_IPFIREWALLRULE_DETACH: IpFirewallPoliciesIdIpFirewallRuleDetach,
        PathValues.IPFIREWALLPOLICIES_ID_IPFIREWALLRULE_ATTACH: IpFirewallPoliciesIdIpFirewallRuleAttach,
        PathValues.IOTPROFILES: IotProfiles,
        PathValues.HOTSPOTSERVICEPROVIDERPROFILES: HotspotServiceProviderProfiles,
        PathValues.HOTSPOTPROFILES: HotspotProfiles,
        PathValues.HIQ_ORGANIZATIONS: HiqOrganizations,
        PathValues.HIQ_ORGANIZATIONS_ID_RENAME: HiqOrganizationsIdRename,
        PathValues.ENDUSERS: Endusers,
        PathValues.ENDUSERS_ID_REGENERATEPASSWORD: EndusersIdRegeneratePassword,
        PathValues.DEVICES_ID_THREAD_COMMISSIONER_STOP: DevicesIdThreadCommissionerStop,
        PathValues.DEVICES_ID_THREAD_COMMISSIONER_START: DevicesIdThreadCommissionerStart,
        PathValues.DEVICES_ID_SSID_STATUS_CHANGE: DevicesIdSsidStatusChange,
        PathValues.DEVICES_ID_SSID_OVERRIDE: DevicesIdSsidOverride,
        PathValues.DEVICES_ID_MONITOR_REFRESH: DevicesIdMonitorRefresh,
        PathValues.DEVICES_ID_IOT_ENABLE: DevicesIdIotEnable,
        PathValues.DEVICES_ID_IOT_DISABLE: DevicesIdIotDisable,
        PathValues.DEVICES_ID_BOUNCEPORT: DevicesIdBouncePort,
        PathValues.DEVICES_ID_UNMANAGE: DevicesIdUnmanage,
        PathValues.DEVICES_ID_RESET: DevicesIdReset,
        PathValues.DEVICES_ID_REBOOT: DevicesIdReboot,
        PathValues.DEVICES_ID_MANAGE: DevicesIdManage,
        PathValues.DEVICES_ID_CLI: DevicesIdCli,
        PathValues.DEVICES_OS_CHANGE: DevicesOsChange,
        PathValues.DEVICES_NETWORKPOLICY_REVOKE: DevicesNetworkPolicyRevoke,
        PathValues.DEVICES_NETWORKPOLICY_QUERY: DevicesNetworkPolicyQuery,
        PathValues.DEVICES_NETWORKPOLICY_ASSIGN: DevicesNetworkPolicyAssign,
        PathValues.DEVICES_LOCATION_REVOKE: DevicesLocationRevoke,
        PathValues.DEVICES_LOCATION_QUERY: DevicesLocationQuery,
        PathValues.DEVICES_LOCATION_ASSIGN: DevicesLocationAssign,
        PathValues.DEVICES_COUNTRYCODE_ASSIGN: DevicesCountryCodeAssign,
        PathValues.DEVICES_CLIENTMONITOR_REVOKE: DevicesClientMonitorRevoke,
        PathValues.DEVICES_CLIENTMONITOR_QUERY: DevicesClientMonitorQuery,
        PathValues.DEVICES_CLIENTMONITOR_ASSIGN: DevicesClientMonitorAssign,
        PathValues.DEVICES_UNMANAGE: DevicesUnmanage,
        PathValues.DEVICES_REBOOT: DevicesReboot,
        PathValues.DEVICES_ONBOARD: DevicesOnboard,
        PathValues.DEVICES_MANAGE: DevicesManage,
        PathValues.DEVICES_DELETE: DevicesDelete,
        PathValues.DEVICES_CLI: DevicesCli,
        PathValues.DEVICES_CHECKOWNERSHIP: DevicesCheckOwnership,
        PathValues.DEVICES_ADVANCEDONBOARD: DevicesAdvancedOnboard,
        PathValues.DEPLOYMENTS: Deployments,
        PathValues.DEPLOYMENTS_FIRMWAREMETADATAS: DeploymentsFirmwareMetadatas,
        PathValues.COPILOT_ANOMALIES_EXCLUDEVLANS: CopilotAnomaliesExcludeVlans,
        PathValues.COPILOT_ANOMALIES_EXCLUDEVLANSCSV: CopilotAnomaliesExcludeVlansCsv,
        PathValues.CLIENTMONITORPROFILES: ClientMonitorProfiles,
        PathValues.CLASSIFICATIONRULES: ClassificationRules,
        PathValues.CCGS: Ccgs,
        PathValues.AUTH_PERMISSIONS_CHECK: AuthPermissionsCheck,
        PathValues.AUTH_APITOKEN: AuthApitoken,
        PathValues.AUTH_APITOKEN_VALIDATE: AuthApitokenValidate,
        PathValues.APS_AFC_UPDATE: ApsAfcUpdate,
        PathValues.AP_SPECTRUM_: ApSpectrum,
        PathValues.ALERTS_REPORTS: AlertsReports,
        PathValues.ALERTS_ACKNOWLEDGE: AlertsAcknowledge,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS: AlertSubscriptionsWebhooks,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS_DELETE: AlertSubscriptionsWebhooksDelete,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS: AlertSubscriptionsEmails,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_ID_VERIFY: AlertSubscriptionsEmailsIdVerify,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_DELETE: AlertSubscriptionsEmailsDelete,
        PathValues.ALERTPOLICIES: AlertPolicies,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID_ENABLE: AlertPoliciesPolicyIdRulesRuleIdEnable,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID_DISABLE: AlertPoliciesPolicyIdRulesRuleIdDisable,
        PathValues.ACCOUNT_VIQ_IMPORT: AccountViqImport,
        PathValues.ACCOUNT_VIQ_EXPORT: AccountViqExport,
        PathValues.ACCOUNT_VIQ_BACKUP: AccountViqBackup,
        PathValues.ACCOUNT_SWITCH: AccountSwitch,
        PathValues.VLANPROFILES_ID: VlanProfilesId,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_EXTERNAL_ID: UsersExternalId,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERPROFILEASSIGNMENTS_ID: UserProfileAssignmentsId,
        PathValues.UCP_ID_ENGINES_INSTALLED: UcpIdEnginesInstalled,
        PathValues.THREAD_TOPOLOGY: ThreadTopology,
        PathValues.THREAD_ROUTERS: ThreadRouters,
        PathValues.THREAD_NETWORKS: ThreadNetworks,
        PathValues.SSIDS: Ssids,
        PathValues.SMSTEMPLATES: SmsTemplates,
        PathValues.RADIUSSERVERS_INTERNAL_DEVICES: RadiusServersInternalDevices,
        PathValues.RADIUSPROXIES_DEVICES: RadiusProxiesDevices,
        PathValues.RADIOOPERATINGMODES_PRODUCT_TYPE: RadioOperatingModesProductType,
        PathValues.PACKETCAPTURES_ID: PacketcapturesId,
        PathValues.PACKETCAPTURES_FILES: PacketcapturesFiles,
        PathValues.OPERATIONS_OPERATION_ID: OperationsOperationId,
        PathValues.NETWORKSCORECARD_WIFI_HEALTH_LOCATION_ID: NetworkScorecardWifiHealthLocationId,
        PathValues.NETWORKSCORECARD_SERVICES_HEALTH_LOCATION_ID: NetworkScorecardServicesHealthLocationId,
        PathValues.NETWORKSCORECARD_NETWORK_HEALTH_LOCATION_ID: NetworkScorecardNetworkHealthLocationId,
        PathValues.NETWORKSCORECARD_DEVICE_HEALTH_LOCATION_ID: NetworkScorecardDeviceHealthLocationId,
        PathValues.NETWORKSCORECARD_CLIENT_HEALTH_LOCATION_ID: NetworkScorecardClientHealthLocationId,
        PathValues.NETWORKPOLICIES_ID_SSIDS: NetworkPoliciesIdSsids,
        PathValues.LOGS_SMS: LogsSms,
        PathValues.LOGS_EMAIL: LogsEmail,
        PathValues.LOGS_CREDENTIAL: LogsCredential,
        PathValues.LOGS_AUTH: LogsAuth,
        PathValues.LOGS_AUDIT: LogsAudit,
        PathValues.LOGS_AUDIT_REPORTS_ID: LogsAuditReportsId,
        PathValues.LOGS_AUDIT_FULLDESCRIPTIONS_ID: LogsAuditFullDescriptionsId,
        PathValues.LOGS_ACCOUNTING: LogsAccounting,
        PathValues.LOCATIONS_TREE: LocationsTree,
        PathValues.LOCATIONS_TREE_MAPS: LocationsTreeMaps,
        PathValues.LOCATIONS_TREE_DEVICES: LocationsTreeDevices,
        PathValues.HIQ_STATUS: HiqStatus,
        PathValues.ESSENTIALS_ELOC_CLIENTS_CLIENT_MAC_LASTKNOWNLOCATION: EssentialsElocClientsClientMacLastKnownLocation,
        PathValues.EMAILTEMPLATES: EmailTemplates,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_SSID_STATUS: DevicesIdSsidStatus,
        PathValues.DEVICES_ID_MONITOR_REFRESH_STATUS: DevicesIdMonitorRefreshStatus,
        PathValues.DEVICES_ID_IOT: DevicesIdIot,
        PathValues.DEVICES_ID_INTERFACES_WIFI: DevicesIdInterfacesWifi,
        PathValues.DEVICES_ID_INSTALLATIONREPORT: DevicesIdInstallationReport,
        PathValues.DEVICES_ID_IBEACON: DevicesIdIbeacon,
        PathValues.DEVICES_ID_HISTORY_CPUMEM: DevicesIdHistoryCpuMem,
        PathValues.DEVICES_ID_GEOLOCATION: DevicesIdGeolocation,
        PathValues.DEVICES_ID_GALLERYIMAGE: DevicesIdGalleryImage,
        PathValues.DEVICES_ID_ALARMS: DevicesIdAlarms,
        PathValues.DEVICES_STATS: DevicesStats,
        PathValues.DEVICES_RADIOINFORMATION: DevicesRadioInformation,
        PathValues.DEVICES_NETWORKPOLICY_POLICY_ID: DevicesNetworkPolicyPolicyId,
        PathValues.DEVICES_DIGITALTWIN: DevicesDigitalTwin,
        PathValues.DEPLOYMENTS_DEPLOYMENT_ID_STATUS: DeploymentsDeploymentIdStatus,
        PathValues.DEPLOYMENTS_STATUS: DeploymentsStatus,
        PathValues.DEPLOYMENTS_OVERVIEW: DeploymentsOverview,
        PathValues.CWPS: Cwps,
        PathValues.COUNTRIES: Countries,
        PathValues.COUNTRIES_COUNTRY_CODE_VALIDATE: CountriesCountryCodeValidate,
        PathValues.COUNTRIES_COUNTRY_ALPHA2CODE_STATES: CountriesCountryAlpha2CodeStates,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_VIEWS: CopilotConnectivityWirelessViews,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_TIMETOCONNECT: CopilotConnectivityWirelessTimeToConnect,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_QUALITYINDEX: CopilotConnectivityWirelessQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_PERFORMANCE: CopilotConnectivityWirelessPerformance,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_TIMETOCONNECT: CopilotConnectivityWirelessLocationsTimeToConnect,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_QUALITYINDEX: CopilotConnectivityWirelessLocationsQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_PERFORMANCE: CopilotConnectivityWirelessLocationsPerformance,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_EVENTS: CopilotConnectivityWirelessLocationsEvents,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_EXPERIENCE: CopilotConnectivityWirelessExperience,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_EVENTS: CopilotConnectivityWirelessEvents,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_APPS: CopilotConnectivityWirelessApps,
        PathValues.COPILOT_CONNECTIVITY_WIRED_QUALITYINDEX: CopilotConnectivityWiredQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRED_LOCATIONS_HARDWARE: CopilotConnectivityWiredLocationsHardware,
        PathValues.COPILOT_CONNECTIVITY_WIRED_HARDWARE: CopilotConnectivityWiredHardware,
        PathValues.COPILOT_CONNECTIVITY_WIRED_EXPERIENCE: CopilotConnectivityWiredExperience,
        PathValues.COPILOT_CONNECTIVITY_WIRED_EVENTS: CopilotConnectivityWiredEvents,
        PathValues.COPILOT_CONNECTIVITY_LOCATIONS: CopilotConnectivityLocations,
        PathValues.COPILOT_CONNECTIVITY_CLIENTTYPE: CopilotConnectivityClientType,
        PathValues.COPILOT_ASSURANCESCANS_OVERVIEW: CopilotAssuranceScansOverview,
        PathValues.COPILOT_ANOMALIES_WIFIEFFICIENCY_STATS: CopilotAnomaliesWifiEfficiencyStats,
        PathValues.COPILOT_ANOMALIES_WIFIEFFICIENCY_CLIENTLIST: CopilotAnomaliesWifiEfficiencyClientList,
        PathValues.COPILOT_ANOMALIES_WIFICAPACITY_STATS: CopilotAnomaliesWifiCapacityStats,
        PathValues.COPILOT_ANOMALIES_WIFICAPACITY_CLIENTLIST: CopilotAnomaliesWifiCapacityClientList,
        PathValues.COPILOT_ANOMALIES_REPORT: CopilotAnomaliesReport,
        PathValues.COPILOT_ANOMALIES_PORTEFFICIENCY_STATS: CopilotAnomaliesPortEfficiencyStats,
        PathValues.COPILOT_ANOMALIES_PORTEFFICIENCY_SPEEDDUPLEXSTATS: CopilotAnomaliesPortEfficiencySpeedDuplexStats,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_TRENDS: CopilotAnomaliesPoeflappingTrends,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_STATS: CopilotAnomaliesPoeflappingStats,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_LLDPCDPINFO: CopilotAnomaliesPoeflappingLldpCdpInfo,
        PathValues.COPILOT_ANOMALIES_NOTIFICATIONS: CopilotAnomaliesNotifications,
        PathValues.COPILOT_ANOMALIES_MISSINGVLAN_COUNT: CopilotAnomaliesMissingVlanCount,
        PathValues.COPILOT_ANOMALIES_LOCATIONS: CopilotAnomaliesLocations,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_STATS: CopilotAnomaliesHardwareHealthStats,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_CPUMEMSTATS: CopilotAnomaliesHardwareHealthCpuMemStats,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_CLIENTLIST: CopilotAnomaliesHardwareHealthClientList,
        PathValues.COPILOT_ANOMALIES_EXCLUDEDVLANSLIST: CopilotAnomaliesExcludedVlansList,
        PathValues.COPILOT_ANOMALIES_DFSRECURRENCE_COUNTSTATS: CopilotAnomaliesDfsRecurrenceCountStats,
        PathValues.COPILOT_ANOMALIES_DFSRECURRENCE_CHANNELSTATS: CopilotAnomaliesDfsRecurrenceChannelStats,
        PathValues.COPILOT_ANOMALIES_DEVICESWITHLOCATIONS: CopilotAnomaliesDevicesWithLocations,
        PathValues.COPILOT_ANOMALIES_DEVICESBYLOCATION: CopilotAnomaliesDevicesByLocation,
        PathValues.COPILOT_ANOMALIES_ANOMALIESBYCATEGORY: CopilotAnomaliesAnomaliesByCategory,
        PathValues.COPILOT_ANOMALIES_ADVERSETRAFFIC_PACKETCOUNTS: CopilotAnomaliesAdverseTrafficPacketCounts,
        PathValues.COPILOT_ANOMALIES_ADVERSETRAFFIC_DEVICESTATS: CopilotAnomaliesAdverseTrafficDeviceStats,
        PathValues.CLIENTS_ID: ClientsId,
        PathValues.CLIENTS_USAGE: ClientsUsage,
        PathValues.CLIENTS_SUMMARY: ClientsSummary,
        PathValues.CLIENTS_BY_MAC_CLIENT_MAC: ClientsByMacClientMac,
        PathValues.CLIENTS_ACTIVE: ClientsActive,
        PathValues.CLIENTS_ACTIVE_COUNT: ClientsActiveCount,
        PathValues.CERTIFICATES: Certificates,
        PathValues.AUTH_PERMISSIONS: AuthPermissions,
        PathValues.AUTH_APITOKEN_INFO: AuthApitokenInfo,
        PathValues.APS_AFC_QUERY_: ApsAfcQuery,
        PathValues.APPLICATIONS: Applications,
        PathValues.APPLICATIONS_ID_CLIENTS_TOPN: ApplicationsIdClientsTopn,
        PathValues.APPLICATIONS_TOPN: ApplicationsTopn,
        PathValues.AP_AFC_INTERFACE_DETAILS_SN: ApAfcInterfaceDetailsSn,
        PathValues.AP_AFC_DIAGNOSTICS_ID: ApAfcDiagnosticsId,
        PathValues.ALERTS: Alerts,
        PathValues.ALERTS_REPORTS_ID: AlertsReportsId,
        PathValues.ALERTS_COUNTBYGROUP: AlertsCountByGroup,
        PathValues.ALERTPOLICIES_AVAILABLESITES: AlertPoliciesAvailableSites,
        PathValues.AFCSERVER: Afcserver,
        PathValues.AFCSERVER_SERVER_ID: AfcserverServerId,
        PathValues.AFCSERVER_STATISTICS_SERVER_ID: AfcserverStatisticsServerId,
        PathValues.ADSERVERS: AdServers,
        PathValues.ACCOUNT_VIQ: AccountViq,
        PathValues.ACCOUNT_VIQ_EXPORTIMPORTSTATUS: AccountViqExportImportStatus,
        PathValues.ACCOUNT_VIQ_DOWNLOAD: AccountViqDownload,
        PathValues.ACCOUNT_HOME: AccountHome,
        PathValues.ACCOUNT_EXTERNAL: AccountExternal,
        PathValues.SUBSCRIPTIONS_WEBHOOK_ID: SubscriptionsWebhookId,
        PathValues.RTTS_ID: RttsId,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID: PcgsKeyBasedNetworkPolicyPolicyId,
        PathValues.NETWORKSERVICES_ID: NetworkServicesId,
        PathValues.HIQ_ORGANIZATIONS_ID: HiqOrganizationsId,
        PathValues.DEVICES_RADIUSPROXY_REVOKE: DevicesRadiusProxyRevoke,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USERGROUPS_ID: UsergroupsId,
        PathValues.USERPROFILES_ID: UserProfilesId,
        PathValues.TUNNELCONCENTRATORS_ID: TunnelConcentratorsId,
        PathValues.SSIDS_ID_PSK_PASSWORD: SsidsIdPskPassword,
        PathValues.SSIDS_ID_MODE_WEP: SsidsIdModeWep,
        PathValues.SSIDS_ID_MODE_PSK: SsidsIdModePsk,
        PathValues.SSIDS_ID_MODE_PPSK: SsidsIdModePpsk,
        PathValues.SSIDS_ID_MODE_OPEN: SsidsIdModeOpen,
        PathValues.SSIDS_ID_MODE_DOT1X: SsidsIdModeDot1x,
        PathValues.SSIDS_ADVANCEDSETTINGS_ID: SsidsAdvancedSettingsId,
        PathValues.SITE_AFC_SCHEDULE: SiteAfcSchedule,
        PathValues.RADIUSSERVERS_INTERNAL_ID: RadiusServersInternalId,
        PathValues.RADIUSSERVERS_EXTERNAL_ID: RadiusServersExternalId,
        PathValues.RADIUSPROXIES_ID: RadiusProxiesId,
        PathValues.RADIUSCLIENTOBJECTS_ID: RadiusClientObjectsId,
        PathValues.RADIOPROFILES_ID: RadioProfilesId,
        PathValues.RADIOPROFILES_WMMQOS_ID: RadioProfilesWmmQosId,
        PathValues.RADIOPROFILES_SENSORSCAN_ID: RadioProfilesSensorScanId,
        PathValues.RADIOPROFILES_RADIOUSAGEOPT_ID: RadioProfilesRadioUsageOptId,
        PathValues.RADIOPROFILES_NEIGHBORHOODANALYSIS_ID: RadioProfilesNeighborhoodAnalysisId,
        PathValues.RADIOPROFILES_MISCELLANEOUS_ID: RadioProfilesMiscellaneousId,
        PathValues.RADIOPROFILES_MACOUIS_ID: RadioProfilesMacOuisId,
        PathValues.RADIOPROFILES_CHANNELSELECTION_ID: RadioProfilesChannelSelectionId,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_USERS: PcgsKeyBasedNetworkPolicyPolicyIdUsers,
        PathValues.NETWORKPOLICIES_ID: NetworkPoliciesId,
        PathValues.MACOBJECTPROFILES_ID: MacObjectProfilesId,
        PathValues.MACFIREWALLPOLICIES_ID: MacFirewallPoliciesId,
        PathValues.LOCATIONS_ID: LocationsId,
        PathValues.LOCATIONS_SITE_ID: LocationsSiteId,
        PathValues.LOCATIONS_FLOOR_ID: LocationsFloorId,
        PathValues.LOCATIONS_BUILDING_ID: LocationsBuildingId,
        PathValues.LDAPSERVERS_ID: LdapServersId,
        PathValues.L3ADDRESSPROFILES_ID: L3AddressProfilesId,
        PathValues.IPFIREWALLPOLICIES_ID: IpFirewallPoliciesId,
        PathValues.IOTPROFILES_ID: IotProfilesId,
        PathValues.HOTSPOTSERVICEPROVIDERPROFILES_ID: HotspotServiceProviderProfilesId,
        PathValues.HOTSPOTPROFILES_ID: HotspotProfilesId,
        PathValues.HIQ_CONTEXT: HiqContext,
        PathValues.HIQ_CONTEXT_READING: HiqContextReading,
        PathValues.HIQ_CONTEXT_CREATING: HiqContextCreating,
        PathValues.ENDUSERS_ID: EndusersId,
        PathValues.DEVICES_ID_RADIOOPERATINGMODE: DevicesIdRadioOperatingMode,
        PathValues.DEVICES_ID_NETWORKPOLICY: DevicesIdNetworkPolicy,
        PathValues.DEVICES_ID_LOCATION: DevicesIdLocation,
        PathValues.DEVICES_ID_HOSTNAME: DevicesIdHostname,
        PathValues.DEVICES_ID_FTMSETTINGS: DevicesIdFtmSettings,
        PathValues.DEVICES_ID_DESCRIPTION: DevicesIdDescription,
        PathValues.DEVICES_ID_CLIENTMONITOR: DevicesIdClientMonitor,
        PathValues.DEVICES_RADIUSPROXY_ASSIGN: DevicesRadiusProxyAssign,
        PathValues.DEVICES_IBEACON: DevicesIbeacon,
        PathValues.DEPLOYMENTS_DEPLOYMENT_ID: DeploymentsDeploymentId,
        PathValues.COPILOT_ANOMALIES_UPDATEDEVICEACTION: CopilotAnomaliesUpdateDeviceAction,
        PathValues.COPILOT_ANOMALIES_UPDATEACTION: CopilotAnomaliesUpdateAction,
        PathValues.COPILOT_ANOMALIES_DEVICES_UPDATEACTION: CopilotAnomaliesDevicesUpdateAction,
        PathValues.COPILOT_ANOMALIES_DEVICES_FEEDBACK: CopilotAnomaliesDevicesFeedback,
        PathValues.CLIENTS_ALIAS: ClientsAlias,
        PathValues.CLIENTMONITORPROFILES_ID: ClientMonitorProfilesId,
        PathValues.CLASSIFICATIONRULES_ID: ClassificationRulesId,
        PathValues.CCGS_ID: CcgsId,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS_ID: AlertSubscriptionsWebhooksId,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_ID: AlertSubscriptionsEmailsId,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID: AlertPoliciesPolicyIdRulesRuleId,
        PathValues.ALERTPOLICIES_ID: AlertPoliciesId,
        PathValues.ACCOUNT_VIQ_DEFAULTDEVICEPASSWORD: AccountViqDefaultDevicePassword,
        PathValues.VLANPROFILES: VlanProfiles,
        PathValues.VLANPROFILES_DELETE: VlanProfilesDelete,
        PathValues.USERS: Users,
        PathValues.USERS_EXTERNAL: UsersExternal,
        PathValues.USERGROUPS: Usergroups,
        PathValues.USERPROFILES: UserProfiles,
        PathValues.USERPROFILES_ID_MACFIREWALLPOLICIES_DETACH: UserProfilesIdMacFirewallPoliciesDetach,
        PathValues.USERPROFILES_ID_MACFIREWALLPOLICIES_ATTACH: UserProfilesIdMacFirewallPoliciesAttach,
        PathValues.USERPROFILES_ID_IPFIREWALLPOLICIES_DETACH: UserProfilesIdIpFirewallPoliciesDetach,
        PathValues.USERPROFILES_ID_IPFIREWALLPOLICIES_ATTACH: UserProfilesIdIpFirewallPoliciesAttach,
        PathValues.USERPROFILEASSIGNMENTS: UserProfileAssignments,
        PathValues.TUNNELCONCENTRATORS: TunnelConcentrators,
        PathValues.SUBSCRIPTIONS_WEBHOOK: SubscriptionsWebhook,
        PathValues.SSIDS_ID_USERPROFILE_ATTACH: SsidsIdUserProfileAttach,
        PathValues.SSIDS_ID_USERPROFILEASSIGNMENT_ATTACH: SsidsIdUserProfileAssignmentAttach,
        PathValues.SSIDS_ID_RADIUSSERVERGROUP_ATTACH: SsidsIdRadiusServerGroupAttach,
        PathValues.SSIDS_ID_RADIUSCLIENTPROFILE_ATTACH: SsidsIdRadiusClientProfileAttach,
        PathValues.SSIDS_ID_CWP_ENABLE: SsidsIdCwpEnable,
        PathValues.SSIDS_ID_CWP_DISABLE: SsidsIdCwpDisable,
        PathValues.SSIDS_ID_CWP_ATTACH: SsidsIdCwpAttach,
        PathValues.SSIDS_ID_CLIENTMONITORPROFILE_ATTACH: SsidsIdClientMonitorProfileAttach,
        PathValues.SSIDS_ID_RENAME: SsidsIdRename,
        PathValues.SITE_SPECTRUM_: SiteSpectrum,
        PathValues.RTTS: Rtts,
        PathValues.RADIUSSERVERS_INTERNAL: RadiusServersInternal,
        PathValues.RADIUSSERVERS_EXTERNAL: RadiusServersExternal,
        PathValues.RADIUSPROXIES: RadiusProxies,
        PathValues.RADIUSCLIENTOBJECTS: RadiusClientObjects,
        PathValues.RADIOPROFILES: RadioProfiles,
        PathValues.RADIOPROFILES_MACOUIS: RadioProfilesMacOuis,
        PathValues.PCGS_KEYBASED: PcgsKeyBased,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_PORTASSIGNMENTS: PcgsKeyBasedNetworkPolicyPolicyIdPortAssignments,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_KEYS_GENERATE: PcgsKeyBasedNetworkPolicyPolicyIdKeysGenerate,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_KEYS_EMAIL: PcgsKeyBasedNetworkPolicyPolicyIdKeysEmail,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID_ONBOARD: PcgsKeyBasedNetworkPolicyPolicyIdOnboard,
        PathValues.PACKETCAPTURES: Packetcaptures,
        PathValues.PACKETCAPTURES_ID_UPLOAD: PacketcapturesIdUpload,
        PathValues.PACKETCAPTURES_ID_STOP: PacketcapturesIdStop,
        PathValues.OPERATIONS_OPERATION_ID_CANCEL: OperationsOperationIdCancel,
        PathValues.NOS_DEVICE_DEVICE_ID_NOSAPI: NosDeviceDeviceIdNosApi,
        PathValues.NETWORKSERVICES: NetworkServices,
        PathValues.NETWORKPOLICIES: NetworkPolicies,
        PathValues.NETWORKPOLICIES_ID_SSIDS_REMOVE: NetworkPoliciesIdSsidsRemove,
        PathValues.NETWORKPOLICIES_ID_SSIDS_ADD: NetworkPoliciesIdSsidsAdd,
        PathValues.MACOBJECTPROFILES: MacObjectProfiles,
        PathValues.MACFIREWALLPOLICIES: MacFirewallPolicies,
        PathValues.MACFIREWALLPOLICIES_ID_MACFIREWALLRULE_DETACH: MacFirewallPoliciesIdMacFirewallRuleDetach,
        PathValues.MACFIREWALLPOLICIES_ID_MACFIREWALLRULE_ATTACH: MacFirewallPoliciesIdMacFirewallRuleAttach,
        PathValues.LOGS_AUDIT_REPORTS: LogsAuditReports,
        PathValues.LOGOUT: Logout,
        PathValues.LOGIN: Login,
        PathValues.LOCATIONS: Locations,
        PathValues.LOCATIONS_SITE: LocationsSite,
        PathValues.LOCATIONS_IMPORT_EKAHAU: LocationsImportEkahau,
        PathValues.LOCATIONS_FLOORPLAN: LocationsFloorplan,
        PathValues.LOCATIONS_FLOOR: LocationsFloor,
        PathValues.LOCATIONS_BUILDING: LocationsBuilding,
        PathValues.LOCATIONS_INIT: LocationsInit,
        PathValues.LDAPSERVERS: LdapServers,
        PathValues.L3ADDRESSPROFILES: L3AddressProfiles,
        PathValues.IPFIREWALLPOLICIES: IpFirewallPolicies,
        PathValues.IPFIREWALLPOLICIES_ID_IPFIREWALLRULE_DETACH: IpFirewallPoliciesIdIpFirewallRuleDetach,
        PathValues.IPFIREWALLPOLICIES_ID_IPFIREWALLRULE_ATTACH: IpFirewallPoliciesIdIpFirewallRuleAttach,
        PathValues.IOTPROFILES: IotProfiles,
        PathValues.HOTSPOTSERVICEPROVIDERPROFILES: HotspotServiceProviderProfiles,
        PathValues.HOTSPOTPROFILES: HotspotProfiles,
        PathValues.HIQ_ORGANIZATIONS: HiqOrganizations,
        PathValues.HIQ_ORGANIZATIONS_ID_RENAME: HiqOrganizationsIdRename,
        PathValues.ENDUSERS: Endusers,
        PathValues.ENDUSERS_ID_REGENERATEPASSWORD: EndusersIdRegeneratePassword,
        PathValues.DEVICES_ID_THREAD_COMMISSIONER_STOP: DevicesIdThreadCommissionerStop,
        PathValues.DEVICES_ID_THREAD_COMMISSIONER_START: DevicesIdThreadCommissionerStart,
        PathValues.DEVICES_ID_SSID_STATUS_CHANGE: DevicesIdSsidStatusChange,
        PathValues.DEVICES_ID_SSID_OVERRIDE: DevicesIdSsidOverride,
        PathValues.DEVICES_ID_MONITOR_REFRESH: DevicesIdMonitorRefresh,
        PathValues.DEVICES_ID_IOT_ENABLE: DevicesIdIotEnable,
        PathValues.DEVICES_ID_IOT_DISABLE: DevicesIdIotDisable,
        PathValues.DEVICES_ID_BOUNCEPORT: DevicesIdBouncePort,
        PathValues.DEVICES_ID_UNMANAGE: DevicesIdUnmanage,
        PathValues.DEVICES_ID_RESET: DevicesIdReset,
        PathValues.DEVICES_ID_REBOOT: DevicesIdReboot,
        PathValues.DEVICES_ID_MANAGE: DevicesIdManage,
        PathValues.DEVICES_ID_CLI: DevicesIdCli,
        PathValues.DEVICES_OS_CHANGE: DevicesOsChange,
        PathValues.DEVICES_NETWORKPOLICY_REVOKE: DevicesNetworkPolicyRevoke,
        PathValues.DEVICES_NETWORKPOLICY_QUERY: DevicesNetworkPolicyQuery,
        PathValues.DEVICES_NETWORKPOLICY_ASSIGN: DevicesNetworkPolicyAssign,
        PathValues.DEVICES_LOCATION_REVOKE: DevicesLocationRevoke,
        PathValues.DEVICES_LOCATION_QUERY: DevicesLocationQuery,
        PathValues.DEVICES_LOCATION_ASSIGN: DevicesLocationAssign,
        PathValues.DEVICES_COUNTRYCODE_ASSIGN: DevicesCountryCodeAssign,
        PathValues.DEVICES_CLIENTMONITOR_REVOKE: DevicesClientMonitorRevoke,
        PathValues.DEVICES_CLIENTMONITOR_QUERY: DevicesClientMonitorQuery,
        PathValues.DEVICES_CLIENTMONITOR_ASSIGN: DevicesClientMonitorAssign,
        PathValues.DEVICES_UNMANAGE: DevicesUnmanage,
        PathValues.DEVICES_REBOOT: DevicesReboot,
        PathValues.DEVICES_ONBOARD: DevicesOnboard,
        PathValues.DEVICES_MANAGE: DevicesManage,
        PathValues.DEVICES_DELETE: DevicesDelete,
        PathValues.DEVICES_CLI: DevicesCli,
        PathValues.DEVICES_CHECKOWNERSHIP: DevicesCheckOwnership,
        PathValues.DEVICES_ADVANCEDONBOARD: DevicesAdvancedOnboard,
        PathValues.DEPLOYMENTS: Deployments,
        PathValues.DEPLOYMENTS_FIRMWAREMETADATAS: DeploymentsFirmwareMetadatas,
        PathValues.COPILOT_ANOMALIES_EXCLUDEVLANS: CopilotAnomaliesExcludeVlans,
        PathValues.COPILOT_ANOMALIES_EXCLUDEVLANSCSV: CopilotAnomaliesExcludeVlansCsv,
        PathValues.CLIENTMONITORPROFILES: ClientMonitorProfiles,
        PathValues.CLASSIFICATIONRULES: ClassificationRules,
        PathValues.CCGS: Ccgs,
        PathValues.AUTH_PERMISSIONS_CHECK: AuthPermissionsCheck,
        PathValues.AUTH_APITOKEN: AuthApitoken,
        PathValues.AUTH_APITOKEN_VALIDATE: AuthApitokenValidate,
        PathValues.APS_AFC_UPDATE: ApsAfcUpdate,
        PathValues.AP_SPECTRUM_: ApSpectrum,
        PathValues.ALERTS_REPORTS: AlertsReports,
        PathValues.ALERTS_ACKNOWLEDGE: AlertsAcknowledge,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS: AlertSubscriptionsWebhooks,
        PathValues.ALERTSUBSCRIPTIONS_WEBHOOKS_DELETE: AlertSubscriptionsWebhooksDelete,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS: AlertSubscriptionsEmails,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_ID_VERIFY: AlertSubscriptionsEmailsIdVerify,
        PathValues.ALERTSUBSCRIPTIONS_EMAILS_DELETE: AlertSubscriptionsEmailsDelete,
        PathValues.ALERTPOLICIES: AlertPolicies,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID_ENABLE: AlertPoliciesPolicyIdRulesRuleIdEnable,
        PathValues.ALERTPOLICIES_POLICY_ID_RULES_RULE_ID_DISABLE: AlertPoliciesPolicyIdRulesRuleIdDisable,
        PathValues.ACCOUNT_VIQ_IMPORT: AccountViqImport,
        PathValues.ACCOUNT_VIQ_EXPORT: AccountViqExport,
        PathValues.ACCOUNT_VIQ_BACKUP: AccountViqBackup,
        PathValues.ACCOUNT_SWITCH: AccountSwitch,
        PathValues.VLANPROFILES_ID: VlanProfilesId,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_EXTERNAL_ID: UsersExternalId,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERPROFILEASSIGNMENTS_ID: UserProfileAssignmentsId,
        PathValues.UCP_ID_ENGINES_INSTALLED: UcpIdEnginesInstalled,
        PathValues.THREAD_TOPOLOGY: ThreadTopology,
        PathValues.THREAD_ROUTERS: ThreadRouters,
        PathValues.THREAD_NETWORKS: ThreadNetworks,
        PathValues.SSIDS: Ssids,
        PathValues.SMSTEMPLATES: SmsTemplates,
        PathValues.RADIUSSERVERS_INTERNAL_DEVICES: RadiusServersInternalDevices,
        PathValues.RADIUSPROXIES_DEVICES: RadiusProxiesDevices,
        PathValues.RADIOOPERATINGMODES_PRODUCT_TYPE: RadioOperatingModesProductType,
        PathValues.PACKETCAPTURES_ID: PacketcapturesId,
        PathValues.PACKETCAPTURES_FILES: PacketcapturesFiles,
        PathValues.OPERATIONS_OPERATION_ID: OperationsOperationId,
        PathValues.NETWORKSCORECARD_WIFI_HEALTH_LOCATION_ID: NetworkScorecardWifiHealthLocationId,
        PathValues.NETWORKSCORECARD_SERVICES_HEALTH_LOCATION_ID: NetworkScorecardServicesHealthLocationId,
        PathValues.NETWORKSCORECARD_NETWORK_HEALTH_LOCATION_ID: NetworkScorecardNetworkHealthLocationId,
        PathValues.NETWORKSCORECARD_DEVICE_HEALTH_LOCATION_ID: NetworkScorecardDeviceHealthLocationId,
        PathValues.NETWORKSCORECARD_CLIENT_HEALTH_LOCATION_ID: NetworkScorecardClientHealthLocationId,
        PathValues.NETWORKPOLICIES_ID_SSIDS: NetworkPoliciesIdSsids,
        PathValues.LOGS_SMS: LogsSms,
        PathValues.LOGS_EMAIL: LogsEmail,
        PathValues.LOGS_CREDENTIAL: LogsCredential,
        PathValues.LOGS_AUTH: LogsAuth,
        PathValues.LOGS_AUDIT: LogsAudit,
        PathValues.LOGS_AUDIT_REPORTS_ID: LogsAuditReportsId,
        PathValues.LOGS_AUDIT_FULLDESCRIPTIONS_ID: LogsAuditFullDescriptionsId,
        PathValues.LOGS_ACCOUNTING: LogsAccounting,
        PathValues.LOCATIONS_TREE: LocationsTree,
        PathValues.LOCATIONS_TREE_MAPS: LocationsTreeMaps,
        PathValues.LOCATIONS_TREE_DEVICES: LocationsTreeDevices,
        PathValues.HIQ_STATUS: HiqStatus,
        PathValues.ESSENTIALS_ELOC_CLIENTS_CLIENT_MAC_LASTKNOWNLOCATION: EssentialsElocClientsClientMacLastKnownLocation,
        PathValues.EMAILTEMPLATES: EmailTemplates,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_SSID_STATUS: DevicesIdSsidStatus,
        PathValues.DEVICES_ID_MONITOR_REFRESH_STATUS: DevicesIdMonitorRefreshStatus,
        PathValues.DEVICES_ID_IOT: DevicesIdIot,
        PathValues.DEVICES_ID_INTERFACES_WIFI: DevicesIdInterfacesWifi,
        PathValues.DEVICES_ID_INSTALLATIONREPORT: DevicesIdInstallationReport,
        PathValues.DEVICES_ID_IBEACON: DevicesIdIbeacon,
        PathValues.DEVICES_ID_HISTORY_CPUMEM: DevicesIdHistoryCpuMem,
        PathValues.DEVICES_ID_GEOLOCATION: DevicesIdGeolocation,
        PathValues.DEVICES_ID_GALLERYIMAGE: DevicesIdGalleryImage,
        PathValues.DEVICES_ID_ALARMS: DevicesIdAlarms,
        PathValues.DEVICES_STATS: DevicesStats,
        PathValues.DEVICES_RADIOINFORMATION: DevicesRadioInformation,
        PathValues.DEVICES_NETWORKPOLICY_POLICY_ID: DevicesNetworkPolicyPolicyId,
        PathValues.DEVICES_DIGITALTWIN: DevicesDigitalTwin,
        PathValues.DEPLOYMENTS_DEPLOYMENT_ID_STATUS: DeploymentsDeploymentIdStatus,
        PathValues.DEPLOYMENTS_STATUS: DeploymentsStatus,
        PathValues.DEPLOYMENTS_OVERVIEW: DeploymentsOverview,
        PathValues.CWPS: Cwps,
        PathValues.COUNTRIES: Countries,
        PathValues.COUNTRIES_COUNTRY_CODE_VALIDATE: CountriesCountryCodeValidate,
        PathValues.COUNTRIES_COUNTRY_ALPHA2CODE_STATES: CountriesCountryAlpha2CodeStates,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_VIEWS: CopilotConnectivityWirelessViews,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_TIMETOCONNECT: CopilotConnectivityWirelessTimeToConnect,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_QUALITYINDEX: CopilotConnectivityWirelessQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_PERFORMANCE: CopilotConnectivityWirelessPerformance,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_TIMETOCONNECT: CopilotConnectivityWirelessLocationsTimeToConnect,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_QUALITYINDEX: CopilotConnectivityWirelessLocationsQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_PERFORMANCE: CopilotConnectivityWirelessLocationsPerformance,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_LOCATIONS_EVENTS: CopilotConnectivityWirelessLocationsEvents,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_EXPERIENCE: CopilotConnectivityWirelessExperience,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_EVENTS: CopilotConnectivityWirelessEvents,
        PathValues.COPILOT_CONNECTIVITY_WIRELESS_APPS: CopilotConnectivityWirelessApps,
        PathValues.COPILOT_CONNECTIVITY_WIRED_QUALITYINDEX: CopilotConnectivityWiredQualityIndex,
        PathValues.COPILOT_CONNECTIVITY_WIRED_LOCATIONS_HARDWARE: CopilotConnectivityWiredLocationsHardware,
        PathValues.COPILOT_CONNECTIVITY_WIRED_HARDWARE: CopilotConnectivityWiredHardware,
        PathValues.COPILOT_CONNECTIVITY_WIRED_EXPERIENCE: CopilotConnectivityWiredExperience,
        PathValues.COPILOT_CONNECTIVITY_WIRED_EVENTS: CopilotConnectivityWiredEvents,
        PathValues.COPILOT_CONNECTIVITY_LOCATIONS: CopilotConnectivityLocations,
        PathValues.COPILOT_CONNECTIVITY_CLIENTTYPE: CopilotConnectivityClientType,
        PathValues.COPILOT_ASSURANCESCANS_OVERVIEW: CopilotAssuranceScansOverview,
        PathValues.COPILOT_ANOMALIES_WIFIEFFICIENCY_STATS: CopilotAnomaliesWifiEfficiencyStats,
        PathValues.COPILOT_ANOMALIES_WIFIEFFICIENCY_CLIENTLIST: CopilotAnomaliesWifiEfficiencyClientList,
        PathValues.COPILOT_ANOMALIES_WIFICAPACITY_STATS: CopilotAnomaliesWifiCapacityStats,
        PathValues.COPILOT_ANOMALIES_WIFICAPACITY_CLIENTLIST: CopilotAnomaliesWifiCapacityClientList,
        PathValues.COPILOT_ANOMALIES_REPORT: CopilotAnomaliesReport,
        PathValues.COPILOT_ANOMALIES_PORTEFFICIENCY_STATS: CopilotAnomaliesPortEfficiencyStats,
        PathValues.COPILOT_ANOMALIES_PORTEFFICIENCY_SPEEDDUPLEXSTATS: CopilotAnomaliesPortEfficiencySpeedDuplexStats,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_TRENDS: CopilotAnomaliesPoeflappingTrends,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_STATS: CopilotAnomaliesPoeflappingStats,
        PathValues.COPILOT_ANOMALIES_POEFLAPPING_LLDPCDPINFO: CopilotAnomaliesPoeflappingLldpCdpInfo,
        PathValues.COPILOT_ANOMALIES_NOTIFICATIONS: CopilotAnomaliesNotifications,
        PathValues.COPILOT_ANOMALIES_MISSINGVLAN_COUNT: CopilotAnomaliesMissingVlanCount,
        PathValues.COPILOT_ANOMALIES_LOCATIONS: CopilotAnomaliesLocations,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_STATS: CopilotAnomaliesHardwareHealthStats,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_CPUMEMSTATS: CopilotAnomaliesHardwareHealthCpuMemStats,
        PathValues.COPILOT_ANOMALIES_HARDWAREHEALTH_CLIENTLIST: CopilotAnomaliesHardwareHealthClientList,
        PathValues.COPILOT_ANOMALIES_EXCLUDEDVLANSLIST: CopilotAnomaliesExcludedVlansList,
        PathValues.COPILOT_ANOMALIES_DFSRECURRENCE_COUNTSTATS: CopilotAnomaliesDfsRecurrenceCountStats,
        PathValues.COPILOT_ANOMALIES_DFSRECURRENCE_CHANNELSTATS: CopilotAnomaliesDfsRecurrenceChannelStats,
        PathValues.COPILOT_ANOMALIES_DEVICESWITHLOCATIONS: CopilotAnomaliesDevicesWithLocations,
        PathValues.COPILOT_ANOMALIES_DEVICESBYLOCATION: CopilotAnomaliesDevicesByLocation,
        PathValues.COPILOT_ANOMALIES_ANOMALIESBYCATEGORY: CopilotAnomaliesAnomaliesByCategory,
        PathValues.COPILOT_ANOMALIES_ADVERSETRAFFIC_PACKETCOUNTS: CopilotAnomaliesAdverseTrafficPacketCounts,
        PathValues.COPILOT_ANOMALIES_ADVERSETRAFFIC_DEVICESTATS: CopilotAnomaliesAdverseTrafficDeviceStats,
        PathValues.CLIENTS_ID: ClientsId,
        PathValues.CLIENTS_USAGE: ClientsUsage,
        PathValues.CLIENTS_SUMMARY: ClientsSummary,
        PathValues.CLIENTS_BY_MAC_CLIENT_MAC: ClientsByMacClientMac,
        PathValues.CLIENTS_ACTIVE: ClientsActive,
        PathValues.CLIENTS_ACTIVE_COUNT: ClientsActiveCount,
        PathValues.CERTIFICATES: Certificates,
        PathValues.AUTH_PERMISSIONS: AuthPermissions,
        PathValues.AUTH_APITOKEN_INFO: AuthApitokenInfo,
        PathValues.APS_AFC_QUERY_: ApsAfcQuery,
        PathValues.APPLICATIONS: Applications,
        PathValues.APPLICATIONS_ID_CLIENTS_TOPN: ApplicationsIdClientsTopn,
        PathValues.APPLICATIONS_TOPN: ApplicationsTopn,
        PathValues.AP_AFC_INTERFACE_DETAILS_SN: ApAfcInterfaceDetailsSn,
        PathValues.AP_AFC_DIAGNOSTICS_ID: ApAfcDiagnosticsId,
        PathValues.ALERTS: Alerts,
        PathValues.ALERTS_REPORTS_ID: AlertsReportsId,
        PathValues.ALERTS_COUNTBYGROUP: AlertsCountByGroup,
        PathValues.ALERTPOLICIES_AVAILABLESITES: AlertPoliciesAvailableSites,
        PathValues.AFCSERVER: Afcserver,
        PathValues.AFCSERVER_SERVER_ID: AfcserverServerId,
        PathValues.AFCSERVER_STATISTICS_SERVER_ID: AfcserverStatisticsServerId,
        PathValues.ADSERVERS: AdServers,
        PathValues.ACCOUNT_VIQ: AccountViq,
        PathValues.ACCOUNT_VIQ_EXPORTIMPORTSTATUS: AccountViqExportImportStatus,
        PathValues.ACCOUNT_VIQ_DOWNLOAD: AccountViqDownload,
        PathValues.ACCOUNT_HOME: AccountHome,
        PathValues.ACCOUNT_EXTERNAL: AccountExternal,
        PathValues.SUBSCRIPTIONS_WEBHOOK_ID: SubscriptionsWebhookId,
        PathValues.RTTS_ID: RttsId,
        PathValues.PCGS_KEYBASED_NETWORKPOLICYPOLICY_ID: PcgsKeyBasedNetworkPolicyPolicyId,
        PathValues.NETWORKSERVICES_ID: NetworkServicesId,
        PathValues.HIQ_ORGANIZATIONS_ID: HiqOrganizationsId,
        PathValues.DEVICES_RADIUSPROXY_REVOKE: DevicesRadiusProxyRevoke,
    }
)
