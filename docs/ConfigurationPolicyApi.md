# extremecloudiq.ConfigurationPolicyApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_client_monitor_profile_to_ssid**](ConfigurationPolicyApi.md#attach_client_monitor_profile_to_ssid) | **POST** /ssids/{id}/client-monitor-profile/:attach | Attach client monitor profile to an SSID
[**attach_cwp_to_ssid**](ConfigurationPolicyApi.md#attach_cwp_to_ssid) | **POST** /ssids/{id}/cwp/:attach | Attach CWP to an SSID
[**attach_ip_firewall_policy_to_user_profile**](ConfigurationPolicyApi.md#attach_ip_firewall_policy_to_user_profile) | **POST** /user-profiles/{id}/ip-firewall-policies/:attach | Attach IP Firewall Policy to an User Profile
[**attach_mac_firewall_policy_to_user_profile**](ConfigurationPolicyApi.md#attach_mac_firewall_policy_to_user_profile) | **POST** /user-profiles/{id}/mac-firewall-policies/:attach | Attach MAC Firewall Policy to an User Profile
[**attach_radius_client_profile_to_ssid**](ConfigurationPolicyApi.md#attach_radius_client_profile_to_ssid) | **POST** /ssids/{id}/radius-client-profile/:attach | Attach RADIUS client profile to an SSID
[**attach_radius_server_group_to_ssid**](ConfigurationPolicyApi.md#attach_radius_server_group_to_ssid) | **POST** /ssids/{id}/radius-server-group/:attach | Attach radius server group to an SSID
[**attach_service_to_ip_firewall_policy**](ConfigurationPolicyApi.md#attach_service_to_ip_firewall_policy) | **POST** /ip-firewall-policies/{id}/ip-firewall-rule/:attach | Attach IP Firewall Rule to IP Firewall policy
[**attach_service_to_mac_firewall_policy**](ConfigurationPolicyApi.md#attach_service_to_mac_firewall_policy) | **POST** /mac-firewall-policies/{id}/mac-firewall-rule/:attach | Attach MAC Firewall Rule to MAC Firewall policy
[**attach_user_profile_assignment_to_ssid**](ConfigurationPolicyApi.md#attach_user_profile_assignment_to_ssid) | **POST** /ssids/{id}/user-profile-assignment/:attach | Attach user profile assignment to an SSID
[**attach_user_profile_to_ssid**](ConfigurationPolicyApi.md#attach_user_profile_to_ssid) | **POST** /ssids/{id}/user-profile/:attach | Attach user profile to an SSID
[**change_psk_password**](ConfigurationPolicyApi.md#change_psk_password) | **PUT** /ssids/{id}/psk/password | Change the SSID PSK password
[**create_classification_rule**](ConfigurationPolicyApi.md#create_classification_rule) | **POST** /classification-rules | Create classification rule
[**create_client_monitor_profile**](ConfigurationPolicyApi.md#create_client_monitor_profile) | **POST** /client-monitor-profiles | Create a client monitor profile
[**create_cloud_config_group**](ConfigurationPolicyApi.md#create_cloud_config_group) | **POST** /ccgs | Create new cloud config group
[**create_iot_profile**](ConfigurationPolicyApi.md#create_iot_profile) | **POST** /iot-profiles | Create a IoT profile
[**create_ip_firewall_policy**](ConfigurationPolicyApi.md#create_ip_firewall_policy) | **POST** /ip-firewall-policies | Create IP Firewall policy
[**create_l3_address_profile**](ConfigurationPolicyApi.md#create_l3_address_profile) | **POST** /l3-address-profiles | Create a L3 address profile
[**create_mac_firewall_policy**](ConfigurationPolicyApi.md#create_mac_firewall_policy) | **POST** /mac-firewall-policies | Create MAC Firewall policy
[**create_mac_object**](ConfigurationPolicyApi.md#create_mac_object) | **POST** /mac-object-profiles | Create a mac object
[**create_mac_oui_profile**](ConfigurationPolicyApi.md#create_mac_oui_profile) | **POST** /radio-profiles/mac-ouis | Create a MAC OUI profile
[**create_radio_profile**](ConfigurationPolicyApi.md#create_radio_profile) | **POST** /radio-profiles | Create a radio profile
[**create_user_profile**](ConfigurationPolicyApi.md#create_user_profile) | **POST** /user-profiles | Create a user profile
[**create_user_profile_assignment**](ConfigurationPolicyApi.md#create_user_profile_assignment) | **POST** /user-profile-assignments | Create a user profile assignment
[**delete_classification_rule**](ConfigurationPolicyApi.md#delete_classification_rule) | **DELETE** /classification-rules/{id} | Delete classification rule by ID
[**delete_client_monitor_profile**](ConfigurationPolicyApi.md#delete_client_monitor_profile) | **DELETE** /client-monitor-profiles/{id} | Delete an client monitor profile by ID
[**delete_cloud_config_group**](ConfigurationPolicyApi.md#delete_cloud_config_group) | **DELETE** /ccgs/{id} | Delete a cloud config group
[**delete_co_user_profile**](ConfigurationPolicyApi.md#delete_co_user_profile) | **DELETE** /user-profiles/{id} | Delete an user profile by ID
[**delete_iot_profile**](ConfigurationPolicyApi.md#delete_iot_profile) | **DELETE** /iot-profiles/{id} | Delete IoT profile by ID
[**delete_ip_firewall_policy**](ConfigurationPolicyApi.md#delete_ip_firewall_policy) | **DELETE** /ip-firewall-policies/{id} | Delete IP Firewall policy by ID
[**delete_l3_address_profile**](ConfigurationPolicyApi.md#delete_l3_address_profile) | **DELETE** /l3-address-profiles/{id} | Delete a L3 address profile by ID
[**delete_mac_firewall_policy**](ConfigurationPolicyApi.md#delete_mac_firewall_policy) | **DELETE** /mac-firewall-policies/{id} | Delete MAC Firewall policy by ID
[**delete_mac_object_profiles**](ConfigurationPolicyApi.md#delete_mac_object_profiles) | **DELETE** /mac-object-profiles/{id} | Delete a MAC object by ID
[**delete_radio_profile**](ConfigurationPolicyApi.md#delete_radio_profile) | **DELETE** /radio-profiles/{id} | Delete radio profile by ID
[**delete_rp_mac_oui_profile**](ConfigurationPolicyApi.md#delete_rp_mac_oui_profile) | **DELETE** /radio-profiles/mac-ouis/{id} | Delete MAC OUI profile
[**delete_user_profile_assignment**](ConfigurationPolicyApi.md#delete_user_profile_assignment) | **DELETE** /user-profile-assignments/{id} | Delete an user profile assignment by ID
[**detach_ip_firewall_policy_from_user_profile**](ConfigurationPolicyApi.md#detach_ip_firewall_policy_from_user_profile) | **POST** /user-profiles/{id}/ip-firewall-policies/:detach | Detach IP Firewall Policy from an User Profile
[**detach_mac_firewall_policy_from_user_profile**](ConfigurationPolicyApi.md#detach_mac_firewall_policy_from_user_profile) | **POST** /user-profiles/{id}/mac-firewall-policies/:detach | Detach MAC Firewall Policy from an User Profile
[**detach_service_to_ip_firewall_policy**](ConfigurationPolicyApi.md#detach_service_to_ip_firewall_policy) | **POST** /ip-firewall-policies/{id}/ip-firewall-rule/:detach | Detach IP Firewall Rule from IP Firewall policy
[**detach_service_to_mac_firewall_policy**](ConfigurationPolicyApi.md#detach_service_to_mac_firewall_policy) | **POST** /mac-firewall-policies/{id}/mac-firewall-rule/:detach | Detach MAC Firewall Rule from MAC Firewall policy
[**disable_ssid_cwp**](ConfigurationPolicyApi.md#disable_ssid_cwp) | **POST** /ssids/{id}/cwp/:disable | Disable the CWP on the SSID
[**enable_ssid_cwp**](ConfigurationPolicyApi.md#enable_ssid_cwp) | **POST** /ssids/{id}/cwp/:enable | Enable and attach the CWP on the SSID
[**get_classification_rule**](ConfigurationPolicyApi.md#get_classification_rule) | **GET** /classification-rules/{id} | Get a classification rule by ID
[**get_client_monitor_profile**](ConfigurationPolicyApi.md#get_client_monitor_profile) | **GET** /client-monitor-profiles/{id} | Get client monitor profile by ID
[**get_cloud_config_group**](ConfigurationPolicyApi.md#get_cloud_config_group) | **GET** /ccgs/{id} | Get a cloud config group
[**get_iot_profile**](ConfigurationPolicyApi.md#get_iot_profile) | **GET** /iot-profiles/{id} | Get IoT profile by ID
[**get_ip_firewall_policy**](ConfigurationPolicyApi.md#get_ip_firewall_policy) | **GET** /ip-firewall-policies/{id} | Get IP Firewall Policy by ID
[**get_l3_address_profile**](ConfigurationPolicyApi.md#get_l3_address_profile) | **GET** /l3-address-profiles/{id} | Get a L3 address profile by ID
[**get_mac_firewall_policy**](ConfigurationPolicyApi.md#get_mac_firewall_policy) | **GET** /mac-firewall-policies/{id} | Get MAC Firewall Policy by ID
[**get_mac_object**](ConfigurationPolicyApi.md#get_mac_object) | **GET** /mac-object-profiles/{id} | Get MAC Object by ID
[**get_neighborhood_analysis**](ConfigurationPolicyApi.md#get_neighborhood_analysis) | **GET** /radio-profiles/neighborhood-analysis/{id} | Get neighborhood analysis settings
[**get_radio_operating_modes**](ConfigurationPolicyApi.md#get_radio_operating_modes) | **GET** /radio-operating-modes/{productType} | Get Radio Operating Modes by product type
[**get_radio_profile**](ConfigurationPolicyApi.md#get_radio_profile) | **GET** /radio-profiles/{id} | Get radio profile by ID
[**get_rp_channel_selection**](ConfigurationPolicyApi.md#get_rp_channel_selection) | **GET** /radio-profiles/channel-selection/{id} | Get channel selection settings
[**get_rp_mac_oui_profile**](ConfigurationPolicyApi.md#get_rp_mac_oui_profile) | **GET** /radio-profiles/mac-ouis/{id} | Get MAC OUI profile
[**get_rp_miscellaneous_settings**](ConfigurationPolicyApi.md#get_rp_miscellaneous_settings) | **GET** /radio-profiles/miscellaneous/{id} | Get radio miscellaneous settings
[**get_rp_radio_usage_optimization**](ConfigurationPolicyApi.md#get_rp_radio_usage_optimization) | **GET** /radio-profiles/radio-usage-opt/{id} | Get radio usage optimization settings
[**get_rp_sensor_scan_settings**](ConfigurationPolicyApi.md#get_rp_sensor_scan_settings) | **GET** /radio-profiles/sensor-scan/{id} | Get sensor scan settings
[**get_rp_wmm_qos_settings**](ConfigurationPolicyApi.md#get_rp_wmm_qos_settings) | **GET** /radio-profiles/wmm-qos/{id} | Get Wmm QoS settings
[**get_ssid_advanced_settings**](ConfigurationPolicyApi.md#get_ssid_advanced_settings) | **GET** /ssids/advanced-settings/{id} | Get SSID advanced settings
[**get_user_profile**](ConfigurationPolicyApi.md#get_user_profile) | **GET** /user-profiles/{id} | Get user profile by ID
[**get_user_profile_assignment**](ConfigurationPolicyApi.md#get_user_profile_assignment) | **GET** /user-profile-assignments/{id} | Get user profile assignment by ID
[**list_classification_rules**](ConfigurationPolicyApi.md#list_classification_rules) | **GET** /classification-rules | List classification rules
[**list_client_monitor_profiles**](ConfigurationPolicyApi.md#list_client_monitor_profiles) | **GET** /client-monitor-profiles | List client monitor profiles
[**list_cloud_config_groups**](ConfigurationPolicyApi.md#list_cloud_config_groups) | **GET** /ccgs | List clould config groups
[**list_iot_profiles**](ConfigurationPolicyApi.md#list_iot_profiles) | **GET** /iot-profiles | List IoT profiles
[**list_ip_firewall_policies**](ConfigurationPolicyApi.md#list_ip_firewall_policies) | **GET** /ip-firewall-policies | List IP Firewall policies
[**list_l3_address_profiles**](ConfigurationPolicyApi.md#list_l3_address_profiles) | **GET** /l3-address-profiles | List L3 address profiles
[**list_mac_firewall_policies**](ConfigurationPolicyApi.md#list_mac_firewall_policies) | **GET** /mac-firewall-policies | List MAC Firewall policies
[**list_mac_object_profiles**](ConfigurationPolicyApi.md#list_mac_object_profiles) | **GET** /mac-object-profiles | List mac object profiles
[**list_radio_profiles**](ConfigurationPolicyApi.md#list_radio_profiles) | **GET** /radio-profiles | List radio profiles
[**list_rp_mac_oui_profiles**](ConfigurationPolicyApi.md#list_rp_mac_oui_profiles) | **GET** /radio-profiles/mac-ouis | List MAC OUI profiles
[**list_ssids**](ConfigurationPolicyApi.md#list_ssids) | **GET** /ssids | List SSIDs
[**list_user_profile_assignments**](ConfigurationPolicyApi.md#list_user_profile_assignments) | **GET** /user-profile-assignments | List user profile assignments
[**list_user_profiles**](ConfigurationPolicyApi.md#list_user_profiles) | **GET** /user-profiles | List user profiles
[**rename_ssid**](ConfigurationPolicyApi.md#rename_ssid) | **POST** /ssids/{id}/:rename | Rename SSID (Wireless name)
[**set_ssid_mode_dot1x**](ConfigurationPolicyApi.md#set_ssid_mode_dot1x) | **PUT** /ssids/{id}/mode/dot1x | Change the SSID mode to 802.1x
[**set_ssid_mode_open**](ConfigurationPolicyApi.md#set_ssid_mode_open) | **PUT** /ssids/{id}/mode/open | Change the SSID mode to open access
[**set_ssid_mode_ppsk**](ConfigurationPolicyApi.md#set_ssid_mode_ppsk) | **PUT** /ssids/{id}/mode/ppsk | Change the SSID mode to PPSK
[**set_ssid_mode_psk**](ConfigurationPolicyApi.md#set_ssid_mode_psk) | **PUT** /ssids/{id}/mode/psk | Change the SSID mode to PSK
[**set_ssid_mode_wep**](ConfigurationPolicyApi.md#set_ssid_mode_wep) | **PUT** /ssids/{id}/mode/wep | Change the SSID mode to WEP
[**update_classification_rule**](ConfigurationPolicyApi.md#update_classification_rule) | **PUT** /classification-rules/{id} | Update classification rule
[**update_client_monitor_profile**](ConfigurationPolicyApi.md#update_client_monitor_profile) | **PUT** /client-monitor-profiles/{id} | Update client monitor profile
[**update_cloud_config_group**](ConfigurationPolicyApi.md#update_cloud_config_group) | **PUT** /ccgs/{id} | Update cloud config group information
[**update_co_user_profile**](ConfigurationPolicyApi.md#update_co_user_profile) | **PUT** /user-profiles/{id} | Update user profile
[**update_iot_profile**](ConfigurationPolicyApi.md#update_iot_profile) | **PUT** /iot-profiles/{id} | Update IoT profile by ID
[**update_ip_policy_request**](ConfigurationPolicyApi.md#update_ip_policy_request) | **PUT** /ip-firewall-policies/{id} | Update IP Firewall policy by ID
[**update_l3_address_profile**](ConfigurationPolicyApi.md#update_l3_address_profile) | **PUT** /l3-address-profiles/{id} | Update a L3 address profile
[**update_mac_firewall_policy**](ConfigurationPolicyApi.md#update_mac_firewall_policy) | **PUT** /mac-firewall-policies/{id} | Update MAC Firewall policy by ID
[**update_mac_object**](ConfigurationPolicyApi.md#update_mac_object) | **PUT** /mac-object-profiles/{id} | Update MAC Object by ID
[**update_neighborhood_analysis**](ConfigurationPolicyApi.md#update_neighborhood_analysis) | **PUT** /radio-profiles/neighborhood-analysis/{id} | Update neighborhood analysis settings
[**update_radio_profile**](ConfigurationPolicyApi.md#update_radio_profile) | **PUT** /radio-profiles/{id} | Update radio profile by ID
[**update_rp_channel_selection**](ConfigurationPolicyApi.md#update_rp_channel_selection) | **PUT** /radio-profiles/channel-selection/{id} | Update channel selection settings
[**update_rp_mac_oui_profile**](ConfigurationPolicyApi.md#update_rp_mac_oui_profile) | **PUT** /radio-profiles/mac-ouis/{id} | Update MAC OUI profile
[**update_rp_miscellaneous_settings**](ConfigurationPolicyApi.md#update_rp_miscellaneous_settings) | **PUT** /radio-profiles/miscellaneous/{id} | Update radio miscellaneous settings
[**update_rp_radio_usage_optimization**](ConfigurationPolicyApi.md#update_rp_radio_usage_optimization) | **PUT** /radio-profiles/radio-usage-opt/{id} | Update radio usage optimization settings
[**update_rp_sensor_scan_settings**](ConfigurationPolicyApi.md#update_rp_sensor_scan_settings) | **PUT** /radio-profiles/sensor-scan/{id} | Update sensor scan settings
[**update_rp_wmm_qos_settings**](ConfigurationPolicyApi.md#update_rp_wmm_qos_settings) | **PUT** /radio-profiles/wmm-qos/{id} | Update Wmm QoS settings
[**update_ssid_advanced_settings**](ConfigurationPolicyApi.md#update_ssid_advanced_settings) | **PUT** /ssids/advanced-settings/{id} | Update SSID advanced settings


# **attach_client_monitor_profile_to_ssid**
> attach_client_monitor_profile_to_ssid(id, xiq_attach_client_monitor_profile_request)

Attach client monitor profile to an SSID

Attach client monitor profile to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_attach_client_monitor_profile_request = extremecloudiq.XiqAttachClientMonitorProfileRequest() # XiqAttachClientMonitorProfileRequest | The client monitor profile ID to be attached to the SSID

    try:
        # Attach client monitor profile to an SSID
        api_instance.attach_client_monitor_profile_to_ssid(id, xiq_attach_client_monitor_profile_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_client_monitor_profile_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_attach_client_monitor_profile_request** | [**XiqAttachClientMonitorProfileRequest**](XiqAttachClientMonitorProfileRequest.md)| The client monitor profile ID to be attached to the SSID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_cwp_to_ssid**
> attach_cwp_to_ssid(id, body)

Attach CWP to an SSID

Attach CWP to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 56 # int | The CWP ID to be attached to the SSID. For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service.

    try:
        # Attach CWP to an SSID
        api_instance.attach_cwp_to_ssid(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_cwp_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **int**| The CWP ID to be attached to the SSID. For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_ip_firewall_policy_to_user_profile**
> attach_ip_firewall_policy_to_user_profile(id, xiq_attach_ip_firewall_policy_to_user_profile_request)

Attach IP Firewall Policy to an User Profile

Attach IP Firewall to an User Profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The User Profile ID
xiq_attach_ip_firewall_policy_to_user_profile_request = extremecloudiq.XiqAttachIpFirewallPolicyToUserProfileRequest() # XiqAttachIpFirewallPolicyToUserProfileRequest | The IP Firewall Policy ID to be attached to the User Profile

    try:
        # Attach IP Firewall Policy to an User Profile
        api_instance.attach_ip_firewall_policy_to_user_profile(id, xiq_attach_ip_firewall_policy_to_user_profile_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_ip_firewall_policy_to_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The User Profile ID | 
 **xiq_attach_ip_firewall_policy_to_user_profile_request** | [**XiqAttachIpFirewallPolicyToUserProfileRequest**](XiqAttachIpFirewallPolicyToUserProfileRequest.md)| The IP Firewall Policy ID to be attached to the User Profile | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_mac_firewall_policy_to_user_profile**
> attach_mac_firewall_policy_to_user_profile(id, xiq_attach_mac_firewall_policy_to_user_profile_request)

Attach MAC Firewall Policy to an User Profile

Attach MAC Firewall to an User Profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The User Profile ID
xiq_attach_mac_firewall_policy_to_user_profile_request = extremecloudiq.XiqAttachMacFirewallPolicyToUserProfileRequest() # XiqAttachMacFirewallPolicyToUserProfileRequest | The MAC Firewall Policy ID to be attached to the User Profile

    try:
        # Attach MAC Firewall Policy to an User Profile
        api_instance.attach_mac_firewall_policy_to_user_profile(id, xiq_attach_mac_firewall_policy_to_user_profile_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_mac_firewall_policy_to_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The User Profile ID | 
 **xiq_attach_mac_firewall_policy_to_user_profile_request** | [**XiqAttachMacFirewallPolicyToUserProfileRequest**](XiqAttachMacFirewallPolicyToUserProfileRequest.md)| The MAC Firewall Policy ID to be attached to the User Profile | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_radius_client_profile_to_ssid**
> attach_radius_client_profile_to_ssid(id, body)

Attach RADIUS client profile to an SSID

Attach RADIUS client profile to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 56 # int | The radius client profile to be attached to the SSID

    try:
        # Attach RADIUS client profile to an SSID
        api_instance.attach_radius_client_profile_to_ssid(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_radius_client_profile_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **int**| The radius client profile to be attached to the SSID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_radius_server_group_to_ssid**
> attach_radius_server_group_to_ssid(id, body)

Attach radius server group to an SSID

Attach radius server group to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 56 # int | The radius server group ID to be attached to the SSID

    try:
        # Attach radius server group to an SSID
        api_instance.attach_radius_server_group_to_ssid(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_radius_server_group_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **int**| The radius server group ID to be attached to the SSID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_service_to_ip_firewall_policy**
> attach_service_to_ip_firewall_policy(id, xiq_ip_firewall_rule_request)

Attach IP Firewall Rule to IP Firewall policy

Attach IP Firewall Rule to IP Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The IP Firewall Policy ID
xiq_ip_firewall_rule_request = extremecloudiq.XiqIpFirewallRuleRequest() # XiqIpFirewallRuleRequest | The IP Firewall Rule to be attached to the IP Firewall Policy.

    try:
        # Attach IP Firewall Rule to IP Firewall policy
        api_instance.attach_service_to_ip_firewall_policy(id, xiq_ip_firewall_rule_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_service_to_ip_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The IP Firewall Policy ID | 
 **xiq_ip_firewall_rule_request** | [**XiqIpFirewallRuleRequest**](XiqIpFirewallRuleRequest.md)| The IP Firewall Rule to be attached to the IP Firewall Policy. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_service_to_mac_firewall_policy**
> attach_service_to_mac_firewall_policy(id, xiq_mac_firewall_rule_request)

Attach MAC Firewall Rule to MAC Firewall policy

Attach MAC Firewall Rule to MAC Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Firewall Policy ID
xiq_mac_firewall_rule_request = extremecloudiq.XiqMacFirewallRuleRequest() # XiqMacFirewallRuleRequest | The MAC Firewall Rule to be attached to the MAC Firewall Policy.

    try:
        # Attach MAC Firewall Rule to MAC Firewall policy
        api_instance.attach_service_to_mac_firewall_policy(id, xiq_mac_firewall_rule_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_service_to_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Firewall Policy ID | 
 **xiq_mac_firewall_rule_request** | [**XiqMacFirewallRuleRequest**](XiqMacFirewallRuleRequest.md)| The MAC Firewall Rule to be attached to the MAC Firewall Policy. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_user_profile_assignment_to_ssid**
> attach_user_profile_assignment_to_ssid(id, xiq_attach_up_assignment_request)

Attach user profile assignment to an SSID

Attach user profile assignment to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_attach_up_assignment_request = extremecloudiq.XiqAttachUPAssignmentRequest() # XiqAttachUPAssignmentRequest | The user profile assignment ID to be attached to the SSID

    try:
        # Attach user profile assignment to an SSID
        api_instance.attach_user_profile_assignment_to_ssid(id, xiq_attach_up_assignment_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_user_profile_assignment_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_attach_up_assignment_request** | [**XiqAttachUPAssignmentRequest**](XiqAttachUPAssignmentRequest.md)| The user profile assignment ID to be attached to the SSID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_user_profile_to_ssid**
> attach_user_profile_to_ssid(id, body)

Attach user profile to an SSID

Attach user profile to an SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 56 # int | The user profile ID to be attached to the SSID

    try:
        # Attach user profile to an SSID
        api_instance.attach_user_profile_to_ssid(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->attach_user_profile_to_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **int**| The user profile ID to be attached to the SSID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_psk_password**
> change_psk_password(id, body)

Change the SSID PSK password

Change the SSID PSK password.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 'body_example' # str | The new SSID PSK password

    try:
        # Change the SSID PSK password
        api_instance.change_psk_password(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->change_psk_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **str**| The new SSID PSK password | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classification_rule**
> XiqClassificationRule create_classification_rule(xiq_create_classification_rule_request)

Create classification rule

Create a new classification rule.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_classification_rule_request = extremecloudiq.XiqCreateClassificationRuleRequest() # XiqCreateClassificationRuleRequest | The payload to create a new classification rule

    try:
        # Create classification rule
        api_response = api_instance.create_classification_rule(xiq_create_classification_rule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_classification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_classification_rule_request** | [**XiqCreateClassificationRuleRequest**](XiqCreateClassificationRuleRequest.md)| The payload to create a new classification rule | 

### Return type

[**XiqClassificationRule**](XiqClassificationRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_monitor_profile**
> XiqClientMonitorProfile create_client_monitor_profile(xiq_client_monitor_profile_request)

Create a client monitor profile

Create a new client monitor profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_client_monitor_profile_request = extremecloudiq.XiqClientMonitorProfileRequest() # XiqClientMonitorProfileRequest | The request body to create new client monitor profile.

    try:
        # Create a client monitor profile
        api_response = api_instance.create_client_monitor_profile(xiq_client_monitor_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_client_monitor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_client_monitor_profile_request** | [**XiqClientMonitorProfileRequest**](XiqClientMonitorProfileRequest.md)| The request body to create new client monitor profile. | 

### Return type

[**XiqClientMonitorProfile**](XiqClientMonitorProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_config_group**
> XiqCloudConfigGroup create_cloud_config_group(xiq_create_cloud_config_group_request)

Create new cloud config group

Create a new cloud config group.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_cloud_config_group_request = extremecloudiq.XiqCreateCloudConfigGroupRequest() # XiqCreateCloudConfigGroupRequest | Create new cloud config group request body

    try:
        # Create new cloud config group
        api_response = api_instance.create_cloud_config_group(xiq_create_cloud_config_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_cloud_config_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_cloud_config_group_request** | [**XiqCreateCloudConfigGroupRequest**](XiqCreateCloudConfigGroupRequest.md)| Create new cloud config group request body | 

### Return type

[**XiqCloudConfigGroup**](XiqCloudConfigGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iot_profile**
> XiqIotProfile create_iot_profile(xiq_iot_profile_request)

Create a IoT profile

Create a new IoT profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_iot_profile_request = extremecloudiq.XiqIotProfileRequest() # XiqIotProfileRequest | The request body to create new IoT profile.

    try:
        # Create a IoT profile
        api_response = api_instance.create_iot_profile(xiq_iot_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_iot_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_iot_profile_request** | [**XiqIotProfileRequest**](XiqIotProfileRequest.md)| The request body to create new IoT profile. | 

### Return type

[**XiqIotProfile**](XiqIotProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_firewall_policy**
> XiqIpFirewall create_ip_firewall_policy(xiq_ip_firewall_policy_request)

Create IP Firewall policy

Create a new IP Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_ip_firewall_policy_request = extremecloudiq.XiqIpFirewallPolicyRequest() # XiqIpFirewallPolicyRequest | The payload to create a new IP Firewall policy.

    try:
        # Create IP Firewall policy
        api_response = api_instance.create_ip_firewall_policy(xiq_ip_firewall_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_ip_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_ip_firewall_policy_request** | [**XiqIpFirewallPolicyRequest**](XiqIpFirewallPolicyRequest.md)| The payload to create a new IP Firewall policy. | 

### Return type

[**XiqIpFirewall**](XiqIpFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_l3_address_profile**
> XiqL3AddressProfileResponse create_l3_address_profile(xiq_create_l3_address_profile_request)

Create a L3 address profile

Create a new L3 address profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_l3_address_profile_request = extremecloudiq.XiqCreateL3AddressProfileRequest() # XiqCreateL3AddressProfileRequest | The request body to create new L3 address profile.

    try:
        # Create a L3 address profile
        api_response = api_instance.create_l3_address_profile(xiq_create_l3_address_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_l3_address_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_l3_address_profile_request** | [**XiqCreateL3AddressProfileRequest**](XiqCreateL3AddressProfileRequest.md)| The request body to create new L3 address profile. | 

### Return type

[**XiqL3AddressProfileResponse**](XiqL3AddressProfileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mac_firewall_policy**
> XiqMacFirewall create_mac_firewall_policy(xiq_mac_firewall_policy_request)

Create MAC Firewall policy

Create a new MAC Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_mac_firewall_policy_request = extremecloudiq.XiqMacFirewallPolicyRequest() # XiqMacFirewallPolicyRequest | The payload to create a new MAC Firewall policy.

    try:
        # Create MAC Firewall policy
        api_response = api_instance.create_mac_firewall_policy(xiq_mac_firewall_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_mac_firewall_policy_request** | [**XiqMacFirewallPolicyRequest**](XiqMacFirewallPolicyRequest.md)| The payload to create a new MAC Firewall policy. | 

### Return type

[**XiqMacFirewall**](XiqMacFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mac_object**
> XiqMacObject create_mac_object(xiq_create_mac_object_request)

Create a mac object

Create a new mac object

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_mac_object_request = extremecloudiq.XiqCreateMacObjectRequest() # XiqCreateMacObjectRequest | The request body to create new mac object.

    try:
        # Create a mac object
        api_response = api_instance.create_mac_object(xiq_create_mac_object_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_mac_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_mac_object_request** | [**XiqCreateMacObjectRequest**](XiqCreateMacObjectRequest.md)| The request body to create new mac object. | 

### Return type

[**XiqMacObject**](XiqMacObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mac_oui_profile**
> XiqRpMacOuiProfile create_mac_oui_profile(xiq_create_rp_mac_oui_profile_request)

Create a MAC OUI profile

Create a new MAC OUI profile for radio usage optimization.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_rp_mac_oui_profile_request = extremecloudiq.XiqCreateRpMacOuiProfileRequest() # XiqCreateRpMacOuiProfileRequest | The request body to create new user profile.

    try:
        # Create a MAC OUI profile
        api_response = api_instance.create_mac_oui_profile(xiq_create_rp_mac_oui_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_mac_oui_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_rp_mac_oui_profile_request** | [**XiqCreateRpMacOuiProfileRequest**](XiqCreateRpMacOuiProfileRequest.md)| The request body to create new user profile. | 

### Return type

[**XiqRpMacOuiProfile**](XiqRpMacOuiProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_radio_profile**
> XiqRadioProfile create_radio_profile(xiq_create_radio_profile_request)

Create a radio profile

Create a new radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_radio_profile_request = extremecloudiq.XiqCreateRadioProfileRequest() # XiqCreateRadioProfileRequest | The request body to create new user profile.

    try:
        # Create a radio profile
        api_response = api_instance.create_radio_profile(xiq_create_radio_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_radio_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_radio_profile_request** | [**XiqCreateRadioProfileRequest**](XiqCreateRadioProfileRequest.md)| The request body to create new user profile. | 

### Return type

[**XiqRadioProfile**](XiqRadioProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_profile**
> XiqUserProfile create_user_profile(xiq_create_user_profile_request)

Create a user profile

Create a new user profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_user_profile_request = extremecloudiq.XiqCreateUserProfileRequest() # XiqCreateUserProfileRequest | The request body to create new user profile.

    try:
        # Create a user profile
        api_response = api_instance.create_user_profile(xiq_create_user_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_user_profile_request** | [**XiqCreateUserProfileRequest**](XiqCreateUserProfileRequest.md)| The request body to create new user profile. | 

### Return type

[**XiqUserProfile**](XiqUserProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_profile_assignment**
> XiqUserProfileAssignment create_user_profile_assignment(xiq_create_user_profile_assignment_request)

Create a user profile assignment

Create a new user profile assignment.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    xiq_create_user_profile_assignment_request = extremecloudiq.XiqCreateUserProfileAssignmentRequest() # XiqCreateUserProfileAssignmentRequest | The request body to create new user profile.

    try:
        # Create a user profile assignment
        api_response = api_instance.create_user_profile_assignment(xiq_create_user_profile_assignment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->create_user_profile_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_user_profile_assignment_request** | [**XiqCreateUserProfileAssignmentRequest**](XiqCreateUserProfileAssignmentRequest.md)| The request body to create new user profile. | 

### Return type

[**XiqUserProfileAssignment**](XiqUserProfileAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_classification_rule**
> delete_classification_rule(id)

Delete classification rule by ID

Delete an existing classification rule by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The classification rule ID

    try:
        # Delete classification rule by ID
        api_instance.delete_classification_rule(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_classification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The classification rule ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_monitor_profile**
> delete_client_monitor_profile(id)

Delete an client monitor profile by ID

Delete an existing client monitor profile by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The client monitor profile ID

    try:
        # Delete an client monitor profile by ID
        api_instance.delete_client_monitor_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_client_monitor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The client monitor profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_config_group**
> delete_cloud_config_group(id)

Delete a cloud config group

Delete a specific cloud config group by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The cloud config group ID

    try:
        # Delete a cloud config group
        api_instance.delete_cloud_config_group(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_cloud_config_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The cloud config group ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_co_user_profile**
> delete_co_user_profile(id)

Delete an user profile by ID

Delete an existing user profile by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The user profile ID

    try:
        # Delete an user profile by ID
        api_instance.delete_co_user_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_co_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iot_profile**
> delete_iot_profile(id)

Delete IoT profile by ID

Delete the existing IoT profile by the profile ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The IoT profile ID

    try:
        # Delete IoT profile by ID
        api_instance.delete_iot_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_iot_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The IoT profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_firewall_policy**
> delete_ip_firewall_policy(id)

Delete IP Firewall policy by ID

Delete an existing IP Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The Ip Firewall Policy ID

    try:
        # Delete IP Firewall policy by ID
        api_instance.delete_ip_firewall_policy(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_ip_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Ip Firewall Policy ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_l3_address_profile**
> delete_l3_address_profile(id)

Delete a L3 address profile by ID

Delete an existing L3 address profile by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The L3 address profile ID

    try:
        # Delete a L3 address profile by ID
        api_instance.delete_l3_address_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_l3_address_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The L3 address profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mac_firewall_policy**
> delete_mac_firewall_policy(id)

Delete MAC Firewall policy by ID

Delete an existing MAC Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Firewall Policy ID

    try:
        # Delete MAC Firewall policy by ID
        api_instance.delete_mac_firewall_policy(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Firewall Policy ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mac_object_profiles**
> delete_mac_object_profiles(id)

Delete a MAC object by ID

Delete an existing MAC object by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The Mac object ID

    try:
        # Delete a MAC object by ID
        api_instance.delete_mac_object_profiles(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_mac_object_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Mac object ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_radio_profile**
> delete_radio_profile(id)

Delete radio profile by ID

Delete the existing radio profile by the profile ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio profile ID

    try:
        # Delete radio profile by ID
        api_instance.delete_radio_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_radio_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rp_mac_oui_profile**
> delete_rp_mac_oui_profile(id)

Delete MAC OUI profile

Delete the existing MAC OUI profile for radio usage optimization.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC OUI profile ID

    try:
        # Delete MAC OUI profile
        api_instance.delete_rp_mac_oui_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_rp_mac_oui_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC OUI profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_profile_assignment**
> delete_user_profile_assignment(id)

Delete an user profile assignment by ID

Delete an existing user profile assignment by ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The user profile ID

    try:
        # Delete an user profile assignment by ID
        api_instance.delete_user_profile_assignment(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->delete_user_profile_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user profile ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_ip_firewall_policy_from_user_profile**
> detach_ip_firewall_policy_from_user_profile(id, xiq_attach_ip_firewall_policy_to_user_profile_request)

Detach IP Firewall Policy from an User Profile

Detach IP Firewall from an User Profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The User Profile ID
xiq_attach_ip_firewall_policy_to_user_profile_request = extremecloudiq.XiqAttachIpFirewallPolicyToUserProfileRequest() # XiqAttachIpFirewallPolicyToUserProfileRequest | The IP Firewall Policy ID to be detached from the User Profile

    try:
        # Detach IP Firewall Policy from an User Profile
        api_instance.detach_ip_firewall_policy_from_user_profile(id, xiq_attach_ip_firewall_policy_to_user_profile_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->detach_ip_firewall_policy_from_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The User Profile ID | 
 **xiq_attach_ip_firewall_policy_to_user_profile_request** | [**XiqAttachIpFirewallPolicyToUserProfileRequest**](XiqAttachIpFirewallPolicyToUserProfileRequest.md)| The IP Firewall Policy ID to be detached from the User Profile | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_mac_firewall_policy_from_user_profile**
> detach_mac_firewall_policy_from_user_profile(id, xiq_attach_mac_firewall_policy_to_user_profile_request)

Detach MAC Firewall Policy from an User Profile

Detach MAC Firewall from an User Profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The User Profile ID
xiq_attach_mac_firewall_policy_to_user_profile_request = extremecloudiq.XiqAttachMacFirewallPolicyToUserProfileRequest() # XiqAttachMacFirewallPolicyToUserProfileRequest | The MAC Firewall Policy ID to be detached from the User Profile

    try:
        # Detach MAC Firewall Policy from an User Profile
        api_instance.detach_mac_firewall_policy_from_user_profile(id, xiq_attach_mac_firewall_policy_to_user_profile_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->detach_mac_firewall_policy_from_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The User Profile ID | 
 **xiq_attach_mac_firewall_policy_to_user_profile_request** | [**XiqAttachMacFirewallPolicyToUserProfileRequest**](XiqAttachMacFirewallPolicyToUserProfileRequest.md)| The MAC Firewall Policy ID to be detached from the User Profile | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_service_to_ip_firewall_policy**
> detach_service_to_ip_firewall_policy(id, body)

Detach IP Firewall Rule from IP Firewall policy

Detach IP Firewall Rule from IP Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The IP Firewall Policy ID
body = 56 # int | The IP Firewall Rule to be detached from the IP Firewall Policy.

    try:
        # Detach IP Firewall Rule from IP Firewall policy
        api_instance.detach_service_to_ip_firewall_policy(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->detach_service_to_ip_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The IP Firewall Policy ID | 
 **body** | **int**| The IP Firewall Rule to be detached from the IP Firewall Policy. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_service_to_mac_firewall_policy**
> detach_service_to_mac_firewall_policy(id, body)

Detach MAC Firewall Rule from MAC Firewall policy

Detach MAC Firewall Rule from MAC Firewall policy.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Firewall Policy ID
body = 56 # int | The MAC Firewall Rule to be detached from the MAC Firewall Policy.

    try:
        # Detach MAC Firewall Rule from MAC Firewall policy
        api_instance.detach_service_to_mac_firewall_policy(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->detach_service_to_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Firewall Policy ID | 
 **body** | **int**| The MAC Firewall Rule to be detached from the MAC Firewall Policy. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ssid_cwp**
> disable_ssid_cwp(id)

Disable the CWP on the SSID

Disable the CWP on the SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID

    try:
        # Disable the CWP on the SSID
        api_instance.disable_ssid_cwp(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->disable_ssid_cwp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_ssid_cwp**
> enable_ssid_cwp(id, body)

Enable and attach the CWP on the SSID

Enable and attach the CWP on the SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 56 # int | The new CWP ID.  For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service.

    try:
        # Enable and attach the CWP on the SSID
        api_instance.enable_ssid_cwp(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->enable_ssid_cwp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **int**| The new CWP ID.  For CWP with only User Auth on Captive Web Portal enabled, please also attach a RADIUS server group or enable ExtremeCloud IQ Authentication Service. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification_rule**
> XiqClassificationRule get_classification_rule(id)

Get a classification rule by ID

Get a specific classification rule.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The classification Rule ID

    try:
        # Get a classification rule by ID
        api_response = api_instance.get_classification_rule(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_classification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The classification Rule ID | 

### Return type

[**XiqClassificationRule**](XiqClassificationRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_monitor_profile**
> XiqClientMonitorProfile get_client_monitor_profile(id)

Get client monitor profile by ID

Get client monitor profile details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The client monitor profile ID

    try:
        # Get client monitor profile by ID
        api_response = api_instance.get_client_monitor_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_client_monitor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The client monitor profile ID | 

### Return type

[**XiqClientMonitorProfile**](XiqClientMonitorProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_config_group**
> XiqCloudConfigGroup get_cloud_config_group(id)

Get a cloud config group

Get cloud config group info for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The cloud config group ID

    try:
        # Get a cloud config group
        api_response = api_instance.get_cloud_config_group(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_cloud_config_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The cloud config group ID | 

### Return type

[**XiqCloudConfigGroup**](XiqCloudConfigGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iot_profile**
> XiqIotProfile get_iot_profile(id)

Get IoT profile by ID

Get IoT profile details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The IoT profile ID

    try:
        # Get IoT profile by ID
        api_response = api_instance.get_iot_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_iot_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The IoT profile ID | 

### Return type

[**XiqIotProfile**](XiqIotProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_firewall_policy**
> XiqIpFirewall get_ip_firewall_policy(id)

Get IP Firewall Policy by ID

Get an existing IP Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The ip firewall policy ID

    try:
        # Get IP Firewall Policy by ID
        api_response = api_instance.get_ip_firewall_policy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_ip_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ip firewall policy ID | 

### Return type

[**XiqIpFirewall**](XiqIpFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l3_address_profile**
> XiqL3AddressProfileResponse get_l3_address_profile(id)

Get a L3 address profile by ID

Get L3 address profile details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The L3 address profile ID

    try:
        # Get a L3 address profile by ID
        api_response = api_instance.get_l3_address_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_l3_address_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The L3 address profile ID | 

### Return type

[**XiqL3AddressProfileResponse**](XiqL3AddressProfileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mac_firewall_policy**
> XiqMacFirewall get_mac_firewall_policy(id)

Get MAC Firewall Policy by ID

Get an existing MAC Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC firewall policy ID

    try:
        # Get MAC Firewall Policy by ID
        api_response = api_instance.get_mac_firewall_policy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC firewall policy ID | 

### Return type

[**XiqMacFirewall**](XiqMacFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mac_object**
> XiqMacObject get_mac_object(id)

Get MAC Object by ID

Get an existing MAC object by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Object ID

    try:
        # Get MAC Object by ID
        api_response = api_instance.get_mac_object(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_mac_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Object ID | 

### Return type

[**XiqMacObject**](XiqMacObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_neighborhood_analysis**
> XiqRpNeighborhoodAnalysis get_neighborhood_analysis(id)

Get neighborhood analysis settings

Get the neighborhood analysis settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The neighborhood analysis settings ID

    try:
        # Get neighborhood analysis settings
        api_response = api_instance.get_neighborhood_analysis(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_neighborhood_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The neighborhood analysis settings ID | 

### Return type

[**XiqRpNeighborhoodAnalysis**](XiqRpNeighborhoodAnalysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_radio_operating_modes**
> list[XiqRadioOperatingModes] get_radio_operating_modes(product_type)

Get Radio Operating Modes by product type

Modern AP hardware types include dual or triple band radios.         A limited subset of band combinations are supported.         Operating mode defines the supported band combinations per radio.             Access Points with fixed band radios use GENERIC operating mode.           SERVICE_2_5_6:   wifi0-2.4Ghz, wifi1-5Ghz, wifi2-6Ghz         SENSOR_SERVICE_5_6: wifi0-Tri-band sensor, wifi1-5Ghz, wifi2-6Ghz         SERVICE_5L_5H_6: wifi0-5G Low, wifi1-5G High, wifi2-6Ghz         SENSOR_SERVICE_5_2: wifi0-Tri-band sensor, wifi1-5GHz, wifi2-2.4Ghz         SERVICE_5L_5H_2: wifi0-5G Low, wifi1-5G High, wifi2-2.4Ghz         SERVICE_6L_5_6H: wifi0-6G Low, wifi1-5GHz, wifi2-6Ghz.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    product_type = 'product_type_example' # str | Product Type/Model

    try:
        # Get Radio Operating Modes by product type
        api_response = api_instance.get_radio_operating_modes(product_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_radio_operating_modes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**| Product Type/Model | 

### Return type

[**list[XiqRadioOperatingModes]**](XiqRadioOperatingModes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_radio_profile**
> XiqRadioProfile get_radio_profile(id)

Get radio profile by ID

Get radio profile details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio profile ID

    try:
        # Get radio profile by ID
        api_response = api_instance.get_radio_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_radio_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio profile ID | 

### Return type

[**XiqRadioProfile**](XiqRadioProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_channel_selection**
> XiqRpChannelSelection get_rp_channel_selection(id)

Get channel selection settings

Get the channel selection settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The channel selection settings ID

    try:
        # Get channel selection settings
        api_response = api_instance.get_rp_channel_selection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_channel_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The channel selection settings ID | 

### Return type

[**XiqRpChannelSelection**](XiqRpChannelSelection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_mac_oui_profile**
> XiqRpMacOuiProfile get_rp_mac_oui_profile(id)

Get MAC OUI profile

Get the MAC OUI profile belonging the radio optimization settings.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC OUI profile ID

    try:
        # Get MAC OUI profile
        api_response = api_instance.get_rp_mac_oui_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_mac_oui_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC OUI profile ID | 

### Return type

[**XiqRpMacOuiProfile**](XiqRpMacOuiProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_miscellaneous_settings**
> XiqRpMiscellaneousSettings get_rp_miscellaneous_settings(id)

Get radio miscellaneous settings

Get the radio miscellaneous settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio miscellaneous settings ID

    try:
        # Get radio miscellaneous settings
        api_response = api_instance.get_rp_miscellaneous_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_miscellaneous_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio miscellaneous settings ID | 

### Return type

[**XiqRpMiscellaneousSettings**](XiqRpMiscellaneousSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_radio_usage_optimization**
> XiqRpRadioUsageOptimization get_rp_radio_usage_optimization(id)

Get radio usage optimization settings

Get the radio usage optimization settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio usage optimization settings ID

    try:
        # Get radio usage optimization settings
        api_response = api_instance.get_rp_radio_usage_optimization(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_radio_usage_optimization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio usage optimization settings ID | 

### Return type

[**XiqRpRadioUsageOptimization**](XiqRpRadioUsageOptimization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_sensor_scan_settings**
> XiqRpSensorScanSettings get_rp_sensor_scan_settings(id)

Get sensor scan settings

Get the sensor scan settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The sensor scan settings ID

    try:
        # Get sensor scan settings
        api_response = api_instance.get_rp_sensor_scan_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_sensor_scan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The sensor scan settings ID | 

### Return type

[**XiqRpSensorScanSettings**](XiqRpSensorScanSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rp_wmm_qos_settings**
> XiqRpWmmQosSettings get_rp_wmm_qos_settings(id)

Get Wmm QoS settings

Get the Wi-Fi Multimedia (WMM) QoS settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio QoS settings ID

    try:
        # Get Wmm QoS settings
        api_response = api_instance.get_rp_wmm_qos_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_rp_wmm_qos_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio QoS settings ID | 

### Return type

[**XiqRpWmmQosSettings**](XiqRpWmmQosSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssid_advanced_settings**
> XiqSsidAdvancedSettings get_ssid_advanced_settings(id)

Get SSID advanced settings

Get the advanced settings belonging to the SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID's advanced settings ID

    try:
        # Get SSID advanced settings
        api_response = api_instance.get_ssid_advanced_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_ssid_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID&#39;s advanced settings ID | 

### Return type

[**XiqSsidAdvancedSettings**](XiqSsidAdvancedSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> XiqUserProfile get_user_profile(id)

Get user profile by ID

Get user profile details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The user profile ID

    try:
        # Get user profile by ID
        api_response = api_instance.get_user_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user profile ID | 

### Return type

[**XiqUserProfile**](XiqUserProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile_assignment**
> XiqUserProfileAssignment get_user_profile_assignment(id)

Get user profile assignment by ID

Get user profile assignment details for the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The user profile assignment ID

    try:
        # Get user profile assignment by ID
        api_response = api_instance.get_user_profile_assignment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->get_user_profile_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user profile assignment ID | 

### Return type

[**XiqUserProfileAssignment**](XiqUserProfileAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classification_rules**
> PagedXiqClassificationRule list_classification_rules(page=page, limit=limit)

List classification rules

List a page of classification rules.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List classification rules
        api_response = api_instance.list_classification_rules(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_classification_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqClassificationRule**](PagedXiqClassificationRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_monitor_profiles**
> PagedXiqClientMonitorProfile list_client_monitor_profiles(page=page, limit=limit)

List client monitor profiles

List a page of client monitor profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List client monitor profiles
        api_response = api_instance.list_client_monitor_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_client_monitor_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqClientMonitorProfile**](PagedXiqClientMonitorProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_config_groups**
> PagedXiqCloudConfigGroup list_cloud_config_groups(page=page, limit=limit, sort_field=sort_field, order=order)

List clould config groups

List a papge of cloud config groups.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqCloudConfigGroupSortField() # XiqCloudConfigGroupSortField | The Sort field (Name by default) (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The Sort order (ascending by default) (optional)

    try:
        # List clould config groups
        api_response = api_instance.list_cloud_config_groups(page=page, limit=limit, sort_field=sort_field, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_cloud_config_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqCloudConfigGroupSortField**](.md)| The Sort field (Name by default) | [optional] 
 **order** | [**XiqSortOrder**](.md)| The Sort order (ascending by default) | [optional] 

### Return type

[**PagedXiqCloudConfigGroup**](PagedXiqCloudConfigGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_iot_profiles**
> PagedXiqIotProfile list_iot_profiles(page=page, limit=limit, app_id=app_id, app_supported=app_supported)

List IoT profiles

List a page of IoT profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
app_id = extremecloudiq.XiqIotApplicationId() # XiqIotApplicationId | Application ID, e.g. THREAD_GATEWAY (optional)
app_supported = extremecloudiq.XiqIotApplicationSupported() # XiqIotApplicationSupported | Application Supported, e.g. SINGLE or MULTI (optional)

    try:
        # List IoT profiles
        api_response = api_instance.list_iot_profiles(page=page, limit=limit, app_id=app_id, app_supported=app_supported)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_iot_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **app_id** | [**XiqIotApplicationId**](.md)| Application ID, e.g. THREAD_GATEWAY | [optional] 
 **app_supported** | [**XiqIotApplicationSupported**](.md)| Application Supported, e.g. SINGLE or MULTI | [optional] 

### Return type

[**PagedXiqIotProfile**](PagedXiqIotProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_firewall_policies**
> PagedXiqIpFirewall list_ip_firewall_policies(page=page, limit=limit)

List IP Firewall policies

List a page of IP Firewall policies.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List IP Firewall policies
        api_response = api_instance.list_ip_firewall_policies(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_ip_firewall_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqIpFirewall**](PagedXiqIpFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_l3_address_profiles**
> list[XiqL3AddressProfile] list_l3_address_profiles(address_type)

List L3 address profiles

List all L3 Address Profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    address_type = 'address_type_example' # str | The address type

    try:
        # List L3 address profiles
        api_response = api_instance.list_l3_address_profiles(address_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_l3_address_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_type** | **str**| The address type | 

### Return type

[**list[XiqL3AddressProfile]**](XiqL3AddressProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mac_firewall_policies**
> PagedXiqMacFirewall list_mac_firewall_policies(page=page, limit=limit)

List MAC Firewall policies

List a page of MAC Firewall policies.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List MAC Firewall policies
        api_response = api_instance.list_mac_firewall_policies(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_mac_firewall_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqMacFirewall**](PagedXiqMacFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mac_object_profiles**
> PagedXiqMacObject list_mac_object_profiles(page=page, limit=limit)

List mac object profiles

List a page of mac object profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List mac object profiles
        api_response = api_instance.list_mac_object_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_mac_object_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqMacObject**](PagedXiqMacObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_radio_profiles**
> PagedXiqRadioProfile list_radio_profiles(page=page, limit=limit)

List radio profiles

List a page of radio profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List radio profiles
        api_response = api_instance.list_radio_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_radio_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqRadioProfile**](PagedXiqRadioProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rp_mac_oui_profiles**
> PagedXiqRpMacOuiProfile list_rp_mac_oui_profiles(page=page, limit=limit)

List MAC OUI profiles

List a page of MAC OUI profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List MAC OUI profiles
        api_response = api_instance.list_rp_mac_oui_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_rp_mac_oui_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqRpMacOuiProfile**](PagedXiqRpMacOuiProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ssids**
> PagedXiqSsid list_ssids(page=page, limit=limit)

List SSIDs

List SSIDs with filter and pagination.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List SSIDs
        api_response = api_instance.list_ssids(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_ssids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqSsid**](PagedXiqSsid.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_profile_assignments**
> PagedXiqUserProfileAssignment list_user_profile_assignments(page=page, limit=limit)

List user profile assignments

List a page of user profile assignments.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List user profile assignments
        api_response = api_instance.list_user_profile_assignments(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_user_profile_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqUserProfileAssignment**](PagedXiqUserProfileAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_profiles**
> PagedXiqUserProfile list_user_profiles(page=page, limit=limit)

List user profiles

List a page of user profiles.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List user profiles
        api_response = api_instance.list_user_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->list_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqUserProfile**](PagedXiqUserProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_ssid**
> rename_ssid(id, body)

Rename SSID (Wireless name)

Change SSID broadcast name (Wireless name).

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
body = 'body_example' # str | The new SSID name

    try:
        # Rename SSID (Wireless name)
        api_instance.rename_ssid(id, body)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->rename_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **body** | **str**| The new SSID name | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ssid_mode_dot1x**
> set_ssid_mode_dot1x(id, xiq_set_ssid_mode_dot1x_request)

Change the SSID mode to 802.1x

Change the SSID mode to 802.1x.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_set_ssid_mode_dot1x_request = extremecloudiq.XiqSetSsidModeDot1xRequest() # XiqSetSsidModeDot1xRequest | The payload to change the SSID mode to 802.1x

    try:
        # Change the SSID mode to 802.1x
        api_instance.set_ssid_mode_dot1x(id, xiq_set_ssid_mode_dot1x_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->set_ssid_mode_dot1x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_set_ssid_mode_dot1x_request** | [**XiqSetSsidModeDot1xRequest**](XiqSetSsidModeDot1xRequest.md)| The payload to change the SSID mode to 802.1x | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ssid_mode_open**
> set_ssid_mode_open(id)

Change the SSID mode to open access

Change the SSID mode to open access.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID

    try:
        # Change the SSID mode to open access
        api_instance.set_ssid_mode_open(id)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->set_ssid_mode_open: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ssid_mode_ppsk**
> set_ssid_mode_ppsk(id, xiq_set_ssid_mode_ppsk_request)

Change the SSID mode to PPSK

Change the SSID mode to PPSK.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_set_ssid_mode_ppsk_request = extremecloudiq.XiqSetSsidModePpskRequest() # XiqSetSsidModePpskRequest | The payload to change the SSID mode to PPSK

    try:
        # Change the SSID mode to PPSK
        api_instance.set_ssid_mode_ppsk(id, xiq_set_ssid_mode_ppsk_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->set_ssid_mode_ppsk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_set_ssid_mode_ppsk_request** | [**XiqSetSsidModePpskRequest**](XiqSetSsidModePpskRequest.md)| The payload to change the SSID mode to PPSK | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ssid_mode_psk**
> set_ssid_mode_psk(id, xiq_set_ssid_mode_psk_request)

Change the SSID mode to PSK

Change the SSID mode to PSK.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_set_ssid_mode_psk_request = extremecloudiq.XiqSetSsidModePskRequest() # XiqSetSsidModePskRequest | The payload to change the SSID mode to PSK

    try:
        # Change the SSID mode to PSK
        api_instance.set_ssid_mode_psk(id, xiq_set_ssid_mode_psk_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->set_ssid_mode_psk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_set_ssid_mode_psk_request** | [**XiqSetSsidModePskRequest**](XiqSetSsidModePskRequest.md)| The payload to change the SSID mode to PSK | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ssid_mode_wep**
> set_ssid_mode_wep(id, xiq_set_ssid_mode_wep_request)

Change the SSID mode to WEP

Change the SSID mode to WEP.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID ID
xiq_set_ssid_mode_wep_request = extremecloudiq.XiqSetSsidModeWepRequest() # XiqSetSsidModeWepRequest | The payload to change the SSID mode to WEP

    try:
        # Change the SSID mode to WEP
        api_instance.set_ssid_mode_wep(id, xiq_set_ssid_mode_wep_request)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->set_ssid_mode_wep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID ID | 
 **xiq_set_ssid_mode_wep_request** | [**XiqSetSsidModeWepRequest**](XiqSetSsidModeWepRequest.md)| The payload to change the SSID mode to WEP | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification_rule**
> XiqClassificationRule update_classification_rule(id, xiq_update_classification_rule_request)

Update classification rule

Update the exist classification rule.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The classification rule ID
xiq_update_classification_rule_request = extremecloudiq.XiqUpdateClassificationRuleRequest() # XiqUpdateClassificationRuleRequest | The payload to update exist classification rule

    try:
        # Update classification rule
        api_response = api_instance.update_classification_rule(id, xiq_update_classification_rule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_classification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The classification rule ID | 
 **xiq_update_classification_rule_request** | [**XiqUpdateClassificationRuleRequest**](XiqUpdateClassificationRuleRequest.md)| The payload to update exist classification rule | 

### Return type

[**XiqClassificationRule**](XiqClassificationRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_monitor_profile**
> XiqClientMonitorProfile update_client_monitor_profile(id, xiq_update_client_monitor_profile_request)

Update client monitor profile

Update an existing client monitor profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The client monitor profile ID.
xiq_update_client_monitor_profile_request = extremecloudiq.XiqUpdateClientMonitorProfileRequest() # XiqUpdateClientMonitorProfileRequest | The payload of client monitor profile.

    try:
        # Update client monitor profile
        api_response = api_instance.update_client_monitor_profile(id, xiq_update_client_monitor_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_client_monitor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The client monitor profile ID. | 
 **xiq_update_client_monitor_profile_request** | [**XiqUpdateClientMonitorProfileRequest**](XiqUpdateClientMonitorProfileRequest.md)| The payload of client monitor profile. | 

### Return type

[**XiqClientMonitorProfile**](XiqClientMonitorProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_config_group**
> XiqCloudConfigGroup update_cloud_config_group(id, xiq_update_cloud_config_group_request)

Update cloud config group information

Update the cloud config group details having the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The cloud config group ID
xiq_update_cloud_config_group_request = extremecloudiq.XiqUpdateCloudConfigGroupRequest() # XiqUpdateCloudConfigGroupRequest | Update cloud config group request body

    try:
        # Update cloud config group information
        api_response = api_instance.update_cloud_config_group(id, xiq_update_cloud_config_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_cloud_config_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The cloud config group ID | 
 **xiq_update_cloud_config_group_request** | [**XiqUpdateCloudConfigGroupRequest**](XiqUpdateCloudConfigGroupRequest.md)| Update cloud config group request body | 

### Return type

[**XiqCloudConfigGroup**](XiqCloudConfigGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_co_user_profile**
> XiqUserProfile update_co_user_profile(id, xiq_update_user_profile_request)

Update user profile

Update an existing user profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The user profile ID.
xiq_update_user_profile_request = extremecloudiq.XiqUpdateUserProfileRequest() # XiqUpdateUserProfileRequest | The payload of user profile.

    try:
        # Update user profile
        api_response = api_instance.update_co_user_profile(id, xiq_update_user_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_co_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user profile ID. | 
 **xiq_update_user_profile_request** | [**XiqUpdateUserProfileRequest**](XiqUpdateUserProfileRequest.md)| The payload of user profile. | 

### Return type

[**XiqUserProfile**](XiqUserProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iot_profile**
> XiqIotProfile update_iot_profile(id, xiq_iot_profile_request)

Update IoT profile by ID

Update the existing IoT profile by the profile ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The IoT profile ID.
xiq_iot_profile_request = extremecloudiq.XiqIotProfileRequest() # XiqIotProfileRequest | The payload of the update IoT profile request.

    try:
        # Update IoT profile by ID
        api_response = api_instance.update_iot_profile(id, xiq_iot_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_iot_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The IoT profile ID. | 
 **xiq_iot_profile_request** | [**XiqIotProfileRequest**](XiqIotProfileRequest.md)| The payload of the update IoT profile request. | 

### Return type

[**XiqIotProfile**](XiqIotProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_policy_request**
> XiqIpFirewall update_ip_policy_request(id, xiq_ip_firewall_policy_request)

Update IP Firewall policy by ID

Update an existing IP Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The Ip Firewall Policy ID.
xiq_ip_firewall_policy_request = extremecloudiq.XiqIpFirewallPolicyRequest() # XiqIpFirewallPolicyRequest | The payload of the update IP Firewall policy request.

    try:
        # Update IP Firewall policy by ID
        api_response = api_instance.update_ip_policy_request(id, xiq_ip_firewall_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_ip_policy_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Ip Firewall Policy ID. | 
 **xiq_ip_firewall_policy_request** | [**XiqIpFirewallPolicyRequest**](XiqIpFirewallPolicyRequest.md)| The payload of the update IP Firewall policy request. | 

### Return type

[**XiqIpFirewall**](XiqIpFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_l3_address_profile**
> XiqL3AddressProfileResponse update_l3_address_profile(id, xiq_update_l3_address_profile_request)

Update a L3 address profile

Update an existing address profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The L3 address profile ID.
xiq_update_l3_address_profile_request = extremecloudiq.XiqUpdateL3AddressProfileRequest() # XiqUpdateL3AddressProfileRequest | The payload of L3 address profile.

    try:
        # Update a L3 address profile
        api_response = api_instance.update_l3_address_profile(id, xiq_update_l3_address_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_l3_address_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The L3 address profile ID. | 
 **xiq_update_l3_address_profile_request** | [**XiqUpdateL3AddressProfileRequest**](XiqUpdateL3AddressProfileRequest.md)| The payload of L3 address profile. | 

### Return type

[**XiqL3AddressProfileResponse**](XiqL3AddressProfileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mac_firewall_policy**
> XiqMacFirewall update_mac_firewall_policy(id, xiq_mac_firewall_policy_request)

Update MAC Firewall policy by ID

Update an existing MAC Firewall policy by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Firewall Policy ID.
xiq_mac_firewall_policy_request = extremecloudiq.XiqMacFirewallPolicyRequest() # XiqMacFirewallPolicyRequest | The payload of the update MAC Firewall policy request.

    try:
        # Update MAC Firewall policy by ID
        api_response = api_instance.update_mac_firewall_policy(id, xiq_mac_firewall_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_mac_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Firewall Policy ID. | 
 **xiq_mac_firewall_policy_request** | [**XiqMacFirewallPolicyRequest**](XiqMacFirewallPolicyRequest.md)| The payload of the update MAC Firewall policy request. | 

### Return type

[**XiqMacFirewall**](XiqMacFirewall.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mac_object**
> XiqMacObject update_mac_object(id, xiq_update_mac_object_request)

Update MAC Object by ID

Update an existing MAC object by the specified ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC Object ID.
xiq_update_mac_object_request = extremecloudiq.XiqUpdateMacObjectRequest() # XiqUpdateMacObjectRequest | The payload of the update MAC Object request.

    try:
        # Update MAC Object by ID
        api_response = api_instance.update_mac_object(id, xiq_update_mac_object_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_mac_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC Object ID. | 
 **xiq_update_mac_object_request** | [**XiqUpdateMacObjectRequest**](XiqUpdateMacObjectRequest.md)| The payload of the update MAC Object request. | 

### Return type

[**XiqMacObject**](XiqMacObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_neighborhood_analysis**
> XiqRpNeighborhoodAnalysis update_neighborhood_analysis(id, xiq_update_rp_neighborhood_analysis_request)

Update neighborhood analysis settings

Update the neighborhood analysis settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The neighborhood analysis settings ID.
xiq_update_rp_neighborhood_analysis_request = extremecloudiq.XiqUpdateRpNeighborhoodAnalysisRequest() # XiqUpdateRpNeighborhoodAnalysisRequest | The payload of the update neighborhood analysis settings request.

    try:
        # Update neighborhood analysis settings
        api_response = api_instance.update_neighborhood_analysis(id, xiq_update_rp_neighborhood_analysis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_neighborhood_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The neighborhood analysis settings ID. | 
 **xiq_update_rp_neighborhood_analysis_request** | [**XiqUpdateRpNeighborhoodAnalysisRequest**](XiqUpdateRpNeighborhoodAnalysisRequest.md)| The payload of the update neighborhood analysis settings request. | 

### Return type

[**XiqRpNeighborhoodAnalysis**](XiqRpNeighborhoodAnalysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_radio_profile**
> XiqRadioProfile update_radio_profile(id, xiq_update_radio_profile_request)

Update radio profile by ID

Update the existing radio profile by the profile ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio profile ID.
xiq_update_radio_profile_request = extremecloudiq.XiqUpdateRadioProfileRequest() # XiqUpdateRadioProfileRequest | The payload of the update radio profile request.

    try:
        # Update radio profile by ID
        api_response = api_instance.update_radio_profile(id, xiq_update_radio_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_radio_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio profile ID. | 
 **xiq_update_radio_profile_request** | [**XiqUpdateRadioProfileRequest**](XiqUpdateRadioProfileRequest.md)| The payload of the update radio profile request. | 

### Return type

[**XiqRadioProfile**](XiqRadioProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_channel_selection**
> XiqRpChannelSelection update_rp_channel_selection(id, xiq_update_rp_channel_selection_request)

Update channel selection settings

Update the channel selection settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The channel selection settings ID.
xiq_update_rp_channel_selection_request = extremecloudiq.XiqUpdateRpChannelSelectionRequest() # XiqUpdateRpChannelSelectionRequest | The payload of the update channel selection settings request.

    try:
        # Update channel selection settings
        api_response = api_instance.update_rp_channel_selection(id, xiq_update_rp_channel_selection_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_channel_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The channel selection settings ID. | 
 **xiq_update_rp_channel_selection_request** | [**XiqUpdateRpChannelSelectionRequest**](XiqUpdateRpChannelSelectionRequest.md)| The payload of the update channel selection settings request. | 

### Return type

[**XiqRpChannelSelection**](XiqRpChannelSelection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_mac_oui_profile**
> XiqRpMacOuiProfile update_rp_mac_oui_profile(id, xiq_update_rp_mac_oui_profile_request)

Update MAC OUI profile

Update the existing MAC OUI profile for radio usage optimization.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The MAC OUI profile ID.
xiq_update_rp_mac_oui_profile_request = extremecloudiq.XiqUpdateRpMacOuiProfileRequest() # XiqUpdateRpMacOuiProfileRequest | The payload of the update MAC OUI profile request.

    try:
        # Update MAC OUI profile
        api_response = api_instance.update_rp_mac_oui_profile(id, xiq_update_rp_mac_oui_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_mac_oui_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MAC OUI profile ID. | 
 **xiq_update_rp_mac_oui_profile_request** | [**XiqUpdateRpMacOuiProfileRequest**](XiqUpdateRpMacOuiProfileRequest.md)| The payload of the update MAC OUI profile request. | 

### Return type

[**XiqRpMacOuiProfile**](XiqRpMacOuiProfile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_miscellaneous_settings**
> XiqRpMiscellaneousSettings update_rp_miscellaneous_settings(id, xiq_update_rp_miscellaneous_settings_request)

Update radio miscellaneous settings

Update the radio miscellaneous settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio miscellaneous settings ID.
xiq_update_rp_miscellaneous_settings_request = extremecloudiq.XiqUpdateRpMiscellaneousSettingsRequest() # XiqUpdateRpMiscellaneousSettingsRequest | The payload of the update radio miscellaneous settings request.

    try:
        # Update radio miscellaneous settings
        api_response = api_instance.update_rp_miscellaneous_settings(id, xiq_update_rp_miscellaneous_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_miscellaneous_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio miscellaneous settings ID. | 
 **xiq_update_rp_miscellaneous_settings_request** | [**XiqUpdateRpMiscellaneousSettingsRequest**](XiqUpdateRpMiscellaneousSettingsRequest.md)| The payload of the update radio miscellaneous settings request. | 

### Return type

[**XiqRpMiscellaneousSettings**](XiqRpMiscellaneousSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_radio_usage_optimization**
> XiqRpRadioUsageOptimization update_rp_radio_usage_optimization(id, xiq_update_rp_radio_usage_optimization_request)

Update radio usage optimization settings

Update the radio usage optimization settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The radio usage optimization settings ID.
xiq_update_rp_radio_usage_optimization_request = extremecloudiq.XiqUpdateRpRadioUsageOptimizationRequest() # XiqUpdateRpRadioUsageOptimizationRequest | The payload of the update radio usage optimization settings request.

    try:
        # Update radio usage optimization settings
        api_response = api_instance.update_rp_radio_usage_optimization(id, xiq_update_rp_radio_usage_optimization_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_radio_usage_optimization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The radio usage optimization settings ID. | 
 **xiq_update_rp_radio_usage_optimization_request** | [**XiqUpdateRpRadioUsageOptimizationRequest**](XiqUpdateRpRadioUsageOptimizationRequest.md)| The payload of the update radio usage optimization settings request. | 

### Return type

[**XiqRpRadioUsageOptimization**](XiqRpRadioUsageOptimization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_sensor_scan_settings**
> XiqRpSensorScanSettings update_rp_sensor_scan_settings(id, xiq_update_rp_sensor_scan_settings_request)

Update sensor scan settings

Update the sensor scan settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The sensor scan settings ID.
xiq_update_rp_sensor_scan_settings_request = extremecloudiq.XiqUpdateRpSensorScanSettingsRequest() # XiqUpdateRpSensorScanSettingsRequest | The payload of the update sensor scan settings request.

    try:
        # Update sensor scan settings
        api_response = api_instance.update_rp_sensor_scan_settings(id, xiq_update_rp_sensor_scan_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_sensor_scan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The sensor scan settings ID. | 
 **xiq_update_rp_sensor_scan_settings_request** | [**XiqUpdateRpSensorScanSettingsRequest**](XiqUpdateRpSensorScanSettingsRequest.md)| The payload of the update sensor scan settings request. | 

### Return type

[**XiqRpSensorScanSettings**](XiqRpSensorScanSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rp_wmm_qos_settings**
> XiqRpWmmQosSettings update_rp_wmm_qos_settings(id, xiq_update_rp_wmm_qos_settings_request)

Update Wmm QoS settings

Update the Wi-Fi Multimedia (WMM) QoS settings belonging to a radio profile.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The Wmm QoS settings ID.
xiq_update_rp_wmm_qos_settings_request = extremecloudiq.XiqUpdateRpWmmQosSettingsRequest() # XiqUpdateRpWmmQosSettingsRequest | The payload of the update Wmm QoS settings request.

    try:
        # Update Wmm QoS settings
        api_response = api_instance.update_rp_wmm_qos_settings(id, xiq_update_rp_wmm_qos_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_rp_wmm_qos_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Wmm QoS settings ID. | 
 **xiq_update_rp_wmm_qos_settings_request** | [**XiqUpdateRpWmmQosSettingsRequest**](XiqUpdateRpWmmQosSettingsRequest.md)| The payload of the update Wmm QoS settings request. | 

### Return type

[**XiqRpWmmQosSettings**](XiqRpWmmQosSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssid_advanced_settings**
> XiqSsidAdvancedSettings update_ssid_advanced_settings(id, xiq_update_ssid_advanced_settings_request)

Update SSID advanced settings

Update the advanced settings belonging to the SSID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationPolicyApi(api_client)
    id = 56 # int | The SSID advanced settings ID.
xiq_update_ssid_advanced_settings_request = extremecloudiq.XiqUpdateSsidAdvancedSettingsRequest() # XiqUpdateSsidAdvancedSettingsRequest | The payload of the update advanced settings request.

    try:
        # Update SSID advanced settings
        api_response = api_instance.update_ssid_advanced_settings(id, xiq_update_ssid_advanced_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationPolicyApi->update_ssid_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The SSID advanced settings ID. | 
 **xiq_update_ssid_advanced_settings_request** | [**XiqUpdateSsidAdvancedSettingsRequest**](XiqUpdateSsidAdvancedSettingsRequest.md)| The payload of the update advanced settings request. | 

### Return type

[**XiqSsidAdvancedSettings**](XiqSsidAdvancedSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

