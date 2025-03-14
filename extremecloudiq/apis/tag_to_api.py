import typing_extensions

from extremecloudiq.apis.tags import TagValues
from extremecloudiq.apis.tags.authentication_api import AuthenticationApi
from extremecloudiq.apis.tags.authorization_api import AuthorizationApi
from extremecloudiq.apis.tags.operation_api import OperationApi
from extremecloudiq.apis.tags.account_api import AccountApi
from extremecloudiq.apis.tags.user_api import UserApi
from extremecloudiq.apis.tags.hiq_api import HIQApi
from extremecloudiq.apis.tags.location_api import LocationApi
from extremecloudiq.apis.tags.device_api import DeviceApi
from extremecloudiq.apis.tags.network_policy_api import NetworkPolicyApi
from extremecloudiq.apis.tags.client_api import ClientApi
from extremecloudiq.apis.tags.client_details_api import ClientDetailsApi
from extremecloudiq.apis.tags.d360_api import D360Api
from extremecloudiq.apis.tags.dashboard_api import DashboardApi
from extremecloudiq.apis.tags.dashboard_wireless_usage_and_capacity_api import DashboardWirelessUsageAndCapacityApi
from extremecloudiq.apis.tags.dashboard_wireless_client_health_api import DashboardWirelessClientHealthApi
from extremecloudiq.apis.tags.dashboard_wireless_device_health_api import DashboardWirelessDeviceHealthApi
from extremecloudiq.apis.tags.geo_view_api import GeoViewApi
from extremecloudiq.apis.tags.application_api import ApplicationApi
from extremecloudiq.apis.tags.alert_api import AlertApi
from extremecloudiq.apis.tags.log_api import LogApi
from extremecloudiq.apis.tags.notification_api import NotificationApi
from extremecloudiq.apis.tags.administration_api import AdministrationApi
from extremecloudiq.apis.tags.nos_api import NOSApi
from extremecloudiq.apis.tags.configuration_deployment_api import ConfigurationDeploymentApi
from extremecloudiq.apis.tags.configuration_basic_api import ConfigurationBasicApi
from extremecloudiq.apis.tags.configuration_user_management_api import ConfigurationUserManagementApi
from extremecloudiq.apis.tags.configuration_policy_api import ConfigurationPolicyApi
from extremecloudiq.apis.tags.configuration_network_api import ConfigurationNetworkApi
from extremecloudiq.apis.tags.configuration_authentication_api import ConfigurationAuthenticationApi
from extremecloudiq.apis.tags.configuration_certificate_api import ConfigurationCertificateApi
from extremecloudiq.apis.tags.copilot_connectivity_experience_api import CopilotConnectivityExperienceApi
from extremecloudiq.apis.tags.copilot_anomalies_api import CopilotAnomaliesApi
from extremecloudiq.apis.tags.packet_capture_api import PacketCaptureApi
from extremecloudiq.apis.tags.network_scorecard_api import NetworkScorecardApi
from extremecloudiq.apis.tags.essentials_extreme_location_api import EssentialsExtremeLocationApi
from extremecloudiq.apis.tags.misc_api import MiscApi
from extremecloudiq.apis.tags.thread_api import ThreadApi
from extremecloudiq.apis.tags.universal_compute_platform_api import UniversalComputePlatformApi
from extremecloudiq.apis.tags.afc_endpoint_api import AfcEndpointApi
from extremecloudiq.apis.tags.rtts_endpoint_api import RttsEndpointApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.OPERATION: OperationApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.USER: UserApi,
        TagValues.HIQ: HIQApi,
        TagValues.LOCATION: LocationApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.NETWORK_POLICY: NetworkPolicyApi,
        TagValues.CLIENT: ClientApi,
        TagValues.CLIENT__DETAILS: ClientDetailsApi,
        TagValues.D360: D360Api,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.DASHBOARD_WIRELESS_USAGE_AND_CAPACITY: DashboardWirelessUsageAndCapacityApi,
        TagValues.DASHBOARD_WIRELESS_CLIENT_HEALTH: DashboardWirelessClientHealthApi,
        TagValues.DASHBOARD_WIRELESS_DEVICE_HEALTH: DashboardWirelessDeviceHealthApi,
        TagValues.GEO_VIEW: GeoViewApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.ALERT: AlertApi,
        TagValues.LOG: LogApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ADMINISTRATION: AdministrationApi,
        TagValues.NOS: NOSApi,
        TagValues.CONFIGURATION__DEPLOYMENT: ConfigurationDeploymentApi,
        TagValues.CONFIGURATION__BASIC: ConfigurationBasicApi,
        TagValues.CONFIGURATION__USER_MANAGEMENT: ConfigurationUserManagementApi,
        TagValues.CONFIGURATION__POLICY: ConfigurationPolicyApi,
        TagValues.CONFIGURATION__NETWORK: ConfigurationNetworkApi,
        TagValues.CONFIGURATION__AUTHENTICATION: ConfigurationAuthenticationApi,
        TagValues.CONFIGURATION__CERTIFICATE: ConfigurationCertificateApi,
        TagValues.COPILOT__CONNECTIVITY_EXPERIENCE: CopilotConnectivityExperienceApi,
        TagValues.COPILOT__ANOMALIES: CopilotAnomaliesApi,
        TagValues.PACKET_CAPTURE: PacketCaptureApi,
        TagValues.NETWORK_SCORECARD: NetworkScorecardApi,
        TagValues.ESSENTIALS__EXTREME_LOCATION: EssentialsExtremeLocationApi,
        TagValues.MISC: MiscApi,
        TagValues.THREAD: ThreadApi,
        TagValues.UNIVERSAL_COMPUTE_PLATFORM: UniversalComputePlatformApi,
        TagValues.AFCENDPOINT: AfcEndpointApi,
        TagValues.RTTSENDPOINT: RttsEndpointApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.OPERATION: OperationApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.USER: UserApi,
        TagValues.HIQ: HIQApi,
        TagValues.LOCATION: LocationApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.NETWORK_POLICY: NetworkPolicyApi,
        TagValues.CLIENT: ClientApi,
        TagValues.CLIENT__DETAILS: ClientDetailsApi,
        TagValues.D360: D360Api,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.DASHBOARD_WIRELESS_USAGE_AND_CAPACITY: DashboardWirelessUsageAndCapacityApi,
        TagValues.DASHBOARD_WIRELESS_CLIENT_HEALTH: DashboardWirelessClientHealthApi,
        TagValues.DASHBOARD_WIRELESS_DEVICE_HEALTH: DashboardWirelessDeviceHealthApi,
        TagValues.GEO_VIEW: GeoViewApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.ALERT: AlertApi,
        TagValues.LOG: LogApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ADMINISTRATION: AdministrationApi,
        TagValues.NOS: NOSApi,
        TagValues.CONFIGURATION__DEPLOYMENT: ConfigurationDeploymentApi,
        TagValues.CONFIGURATION__BASIC: ConfigurationBasicApi,
        TagValues.CONFIGURATION__USER_MANAGEMENT: ConfigurationUserManagementApi,
        TagValues.CONFIGURATION__POLICY: ConfigurationPolicyApi,
        TagValues.CONFIGURATION__NETWORK: ConfigurationNetworkApi,
        TagValues.CONFIGURATION__AUTHENTICATION: ConfigurationAuthenticationApi,
        TagValues.CONFIGURATION__CERTIFICATE: ConfigurationCertificateApi,
        TagValues.COPILOT__CONNECTIVITY_EXPERIENCE: CopilotConnectivityExperienceApi,
        TagValues.COPILOT__ANOMALIES: CopilotAnomaliesApi,
        TagValues.PACKET_CAPTURE: PacketCaptureApi,
        TagValues.NETWORK_SCORECARD: NetworkScorecardApi,
        TagValues.ESSENTIALS__EXTREME_LOCATION: EssentialsExtremeLocationApi,
        TagValues.MISC: MiscApi,
        TagValues.THREAD: ThreadApi,
        TagValues.UNIVERSAL_COMPUTE_PLATFORM: UniversalComputePlatformApi,
        TagValues.AFCENDPOINT: AfcEndpointApi,
        TagValues.RTTSENDPOINT: RttsEndpointApi,
    }
)
