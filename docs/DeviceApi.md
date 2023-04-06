# extremecloudiq.DeviceApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_device_location**](DeviceApi.md#assign_device_location) | **PUT** /devices/{id}/location | Assign location to a device
[**assign_device_network_policy**](DeviceApi.md#assign_device_network_policy) | **PUT** /devices/{id}/network-policy | Assign network policy to a device
[**assign_devices_country_code**](DeviceApi.md#assign_devices_country_code) | **POST** /devices/country-code/:assign | Assign a country code to devices
[**assign_devices_location**](DeviceApi.md#assign_devices_location) | **POST** /devices/location/:assign | Assign location to multiple devices
[**assign_devices_network_policy**](DeviceApi.md#assign_devices_network_policy) | **POST** /devices/network-policy/:assign | Assign network policy to multiple devices
[**assign_devices_radius_proxy**](DeviceApi.md#assign_devices_radius_proxy) | **PUT** /devices/radius-proxy/:assign | Assign RADIUS proxy to devices
[**bounce_device_port**](DeviceApi.md#bounce_device_port) | **POST** /devices/{id}/bounce-port | Bounce port of a device
[**change_device_description**](DeviceApi.md#change_device_description) | **PUT** /devices/{id}/description | Change description for a device
[**change_device_level_ssid_status**](DeviceApi.md#change_device_level_ssid_status) | **POST** /devices/{id}/ssid/status/:change | Enable or disable SSID for a device
[**change_device_status_to_manage**](DeviceApi.md#change_device_status_to_manage) | **POST** /devices/{id}/:manage | Change admin state to &#39;Managed&#39; for a device
[**change_device_status_to_unmanage**](DeviceApi.md#change_device_status_to_unmanage) | **POST** /devices/{id}/:unmanage | Change admin state to &#39;Unmanaged&#39; for a device
[**change_devices_ibeacon**](DeviceApi.md#change_devices_ibeacon) | **PUT** /devices/ibeacon | Change iBeacon settings for devices
[**change_devices_os_mode**](DeviceApi.md#change_devices_os_mode) | **POST** /devices/os/:change | Change device OS mode
[**change_hostname**](DeviceApi.md#change_hostname) | **PUT** /devices/{id}/hostname | Change hostname for a device
[**change_status_to_manage**](DeviceApi.md#change_status_to_manage) | **POST** /devices/:manage | Change status to Managed
[**change_status_to_unmanage**](DeviceApi.md#change_status_to_unmanage) | **POST** /devices/:unmanage | Change status to Unmanaged
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /devices/{id} | Delete a device
[**delete_devices**](DeviceApi.md#delete_devices) | **POST** /devices/:delete | Delete devices
[**get_device**](DeviceApi.md#get_device) | **GET** /devices/{id} | Get device info for a specific device
[**get_device_cpu_memory_history**](DeviceApi.md#get_device_cpu_memory_history) | **GET** /devices/{id}/history/cpu-mem | Get device CPU/memory usage history
[**get_device_ibeacon**](DeviceApi.md#get_device_ibeacon) | **GET** /devices/{id}/ibeacon | Get the device iBeacon setting
[**get_device_level_ssid_status**](DeviceApi.md#get_device_level_ssid_status) | **GET** /devices/{id}/ssid/status | Get SSID status for a device
[**get_device_location**](DeviceApi.md#get_device_location) | **GET** /devices/{id}/location | Get location for a device
[**get_device_network_policy**](DeviceApi.md#get_device_network_policy) | **GET** /devices/{id}/network-policy | Get network policy for a device
[**get_device_stats**](DeviceApi.md#get_device_stats) | **GET** /devices/stats | Get device stats
[**get_device_wifi_interface**](DeviceApi.md#get_device_wifi_interface) | **GET** /devices/{id}/interfaces/wifi | Get the device WiFi interfaces stats
[**get_xiq_device_installation_report**](DeviceApi.md#get_xiq_device_installation_report) | **GET** /devices/{id}/installation-report | Get device installation report
[**list_device_alarm**](DeviceApi.md#list_device_alarm) | **GET** /devices/{id}/alarms | List alarms for a device
[**list_devices**](DeviceApi.md#list_devices) | **GET** /devices | [LRO] List devices
[**list_devices_by_network_policy**](DeviceApi.md#list_devices_by_network_policy) | **GET** /devices/network-policy/{policyId} | List assigned devices for network policy
[**onboard_devices**](DeviceApi.md#onboard_devices) | **POST** /devices/:onboard | Onboard Devices
[**override_device_level_ssid**](DeviceApi.md#override_device_level_ssid) | **POST** /devices/{id}/ssid/:override | Override SSID for a device
[**query_devices_location**](DeviceApi.md#query_devices_location) | **POST** /devices/location/:query | Query location for multiple devices
[**query_devices_network_policy**](DeviceApi.md#query_devices_network_policy) | **POST** /devices/network-policy/:query | Query network policy for multiple devices
[**reboot_device**](DeviceApi.md#reboot_device) | **POST** /devices/{id}/:reboot | Reboot a device
[**reboot_devices**](DeviceApi.md#reboot_devices) | **POST** /devices/:reboot | Reboot devices
[**reset_device**](DeviceApi.md#reset_device) | **POST** /devices/{id}/:reset | [LRO] Reset a device to factory default
[**revoke_device_location**](DeviceApi.md#revoke_device_location) | **DELETE** /devices/{id}/location | Revoke location for a device
[**revoke_device_network_policy**](DeviceApi.md#revoke_device_network_policy) | **DELETE** /devices/{id}/network-policy | Revoke network policy for a device
[**revoke_devices_location**](DeviceApi.md#revoke_devices_location) | **POST** /devices/location/:revoke | Revoke location for multiple devices
[**revoke_devices_network_policy**](DeviceApi.md#revoke_devices_network_policy) | **POST** /devices/network-policy/:revoke | Revoke network policy for multiple devices
[**revoke_devices_radius_proxy**](DeviceApi.md#revoke_devices_radius_proxy) | **DELETE** /devices/radius-proxy/:revoke | Revoke RADIUS proxy from multiple devices
[**send_cli_to_device**](DeviceApi.md#send_cli_to_device) | **POST** /devices/{id}/:cli | Send CLI to a device
[**send_cli_to_devices**](DeviceApi.md#send_cli_to_devices) | **POST** /devices/:cli | [LRO] Send CLI to devices


# **assign_device_location**
> assign_device_location(id, xiq_device_location_assignment)

Assign location to a device

Assign a location to a specific device with extra map and geographical properties.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
xiq_device_location_assignment = extremecloudiq.XiqDeviceLocationAssignment() # XiqDeviceLocationAssignment | 

    try:
        # Assign location to a device
        api_instance.assign_device_location(id, xiq_device_location_assignment)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_device_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **xiq_device_location_assignment** | [**XiqDeviceLocationAssignment**](XiqDeviceLocationAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **assign_device_network_policy**
> assign_device_network_policy(id, network_policy_id)

Assign network policy to a device

Assign a network policy to a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
network_policy_id = 56 # int | The network policy ID to assign

    try:
        # Assign network policy to a device
        api_instance.assign_device_network_policy(id, network_policy_id)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_device_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **network_policy_id** | **int**| The network policy ID to assign | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **assign_devices_country_code**
> assign_devices_country_code(xiq_assign_devices_country_code_request)

Assign a country code to devices

Assign the country code to one or more devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_assign_devices_country_code_request = extremecloudiq.XiqAssignDevicesCountryCodeRequest() # XiqAssignDevicesCountryCodeRequest | 

    try:
        # Assign a country code to devices
        api_instance.assign_devices_country_code(xiq_assign_devices_country_code_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_devices_country_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_assign_devices_country_code_request** | [**XiqAssignDevicesCountryCodeRequest**](XiqAssignDevicesCountryCodeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **assign_devices_location**
> assign_devices_location(xiq_assign_devices_location_request)

Assign location to multiple devices

Assign the location to the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_assign_devices_location_request = extremecloudiq.XiqAssignDevicesLocationRequest() # XiqAssignDevicesLocationRequest | 

    try:
        # Assign location to multiple devices
        api_instance.assign_devices_location(xiq_assign_devices_location_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_devices_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_assign_devices_location_request** | [**XiqAssignDevicesLocationRequest**](XiqAssignDevicesLocationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **assign_devices_network_policy**
> assign_devices_network_policy(xiq_assign_devices_network_policy_request)

Assign network policy to multiple devices

Assign the network policy to the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_assign_devices_network_policy_request = extremecloudiq.XiqAssignDevicesNetworkPolicyRequest() # XiqAssignDevicesNetworkPolicyRequest | 

    try:
        # Assign network policy to multiple devices
        api_instance.assign_devices_network_policy(xiq_assign_devices_network_policy_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_devices_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_assign_devices_network_policy_request** | [**XiqAssignDevicesNetworkPolicyRequest**](XiqAssignDevicesNetworkPolicyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **assign_devices_radius_proxy**
> assign_devices_radius_proxy(ids, radius_proxy_id)

Assign RADIUS proxy to devices

Assign a RADIUS proxy to multiple devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    ids = [56] # list[int] | The device IDs
radius_proxy_id = 56 # int | The RADIUS proxy ID to assign

    try:
        # Assign RADIUS proxy to devices
        api_instance.assign_devices_radius_proxy(ids, radius_proxy_id)
    except ApiException as e:
        print("Exception when calling DeviceApi->assign_devices_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| The device IDs | 
 **radius_proxy_id** | **int**| The RADIUS proxy ID to assign | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **bounce_device_port**
> XiqBounceDevicePortResponse bounce_device_port(id, xiq_bounce_device_port_request)

Bounce port of a device

Bounce port for the given device id.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device id
xiq_bounce_device_port_request = extremecloudiq.XiqBounceDevicePortRequest() # XiqBounceDevicePortRequest | 

    try:
        # Bounce port of a device
        api_response = api_instance.bounce_device_port(id, xiq_bounce_device_port_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->bounce_device_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device id | 
 **xiq_bounce_device_port_request** | [**XiqBounceDevicePortRequest**](XiqBounceDevicePortRequest.md)|  | 

### Return type

[**XiqBounceDevicePortResponse**](XiqBounceDevicePortResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_device_description**
> change_device_description(id, body)

Change description for a device

Change description for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
body = 'body_example' # str | The device description

    try:
        # Change description for a device
        api_instance.change_device_description(id, body)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_device_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **body** | **str**| The device description | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_device_level_ssid_status**
> change_device_level_ssid_status(id, xiq_update_device_level_ssid_status)

Enable or disable SSID for a device

Enable or disable SSIDs on the given wifi interfaces for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
xiq_update_device_level_ssid_status = extremecloudiq.XiqUpdateDeviceLevelSsidStatus() # XiqUpdateDeviceLevelSsidStatus | 

    try:
        # Enable or disable SSID for a device
        api_instance.change_device_level_ssid_status(id, xiq_update_device_level_ssid_status)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_device_level_ssid_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **xiq_update_device_level_ssid_status** | [**XiqUpdateDeviceLevelSsidStatus**](XiqUpdateDeviceLevelSsidStatus.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_device_status_to_manage**
> change_device_status_to_manage(id)

Change admin state to 'Managed' for a device

Change device management status to Managed for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Change admin state to 'Managed' for a device
        api_instance.change_device_status_to_manage(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_device_status_to_manage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_device_status_to_unmanage**
> change_device_status_to_unmanage(id)

Change admin state to 'Unmanaged' for a device

Change device admin state to 'Unmanaged' for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Change admin state to 'Unmanaged' for a device
        api_instance.change_device_status_to_unmanage(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_device_status_to_unmanage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_devices_ibeacon**
> change_devices_ibeacon(xiq_change_devices_ibeacon_request)

Change iBeacon settings for devices

Update the existing or create new iBeacon settings for multiple devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_change_devices_ibeacon_request = extremecloudiq.XiqChangeDevicesIbeaconRequest() # XiqChangeDevicesIbeaconRequest | 

    try:
        # Change iBeacon settings for devices
        api_instance.change_devices_ibeacon(xiq_change_devices_ibeacon_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_devices_ibeacon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_change_devices_ibeacon_request** | [**XiqChangeDevicesIbeaconRequest**](XiqChangeDevicesIbeaconRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_devices_os_mode**
> change_devices_os_mode(xiq_change_devices_os_mode_request)

Change device OS mode

Change OS mode for AP or Switch.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_change_devices_os_mode_request = extremecloudiq.XiqChangeDevicesOsModeRequest() # XiqChangeDevicesOsModeRequest | 

    try:
        # Change device OS mode
        api_instance.change_devices_os_mode(xiq_change_devices_os_mode_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_devices_os_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_change_devices_os_mode_request** | [**XiqChangeDevicesOsModeRequest**](XiqChangeDevicesOsModeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_hostname**
> change_hostname(id, hostname)

Change hostname for a device

Change hostname for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
hostname = 'hostname_example' # str | The new hostname

    try:
        # Change hostname for a device
        api_instance.change_hostname(id, hostname)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_hostname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **hostname** | **str**| The new hostname | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_status_to_manage**
> change_status_to_manage(xiq_device_filter)

Change status to Managed

Change device management status to Managed for the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Change status to Managed
        api_instance.change_status_to_manage(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_status_to_manage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **change_status_to_unmanage**
> change_status_to_unmanage(xiq_device_filter)

Change status to Unmanaged

Change device management status to Unmanaged for the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | The device filter

    try:
        # Change status to Unmanaged
        api_instance.change_status_to_unmanage(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->change_status_to_unmanage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)| The device filter | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **delete_device**
> delete_device(id)

Delete a device

Delete a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Delete a device
        api_instance.delete_device(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **delete_devices**
> delete_devices(xiq_device_filter)

Delete devices

Bulk delete the devices matching the filter criteria.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Delete devices
        api_instance.delete_devices(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->delete_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device**
> XiqDevice get_device(id, views=views, fields=fields)

Get device info for a specific device

Get device info for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
views = [extremecloudiq.XiqDeviceView()] # list[XiqDeviceView] | The views to return device fields (Check details at XiqDeviceView schema) (optional)
fields = [extremecloudiq.XiqDeviceField()] # list[XiqDeviceField] | The device fields to return (optional)

    try:
        # Get device info for a specific device
        api_response = api_instance.get_device(id, views=views, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **views** | [**list[XiqDeviceView]**](XiqDeviceView.md)| The views to return device fields (Check details at XiqDeviceView schema) | [optional] 
 **fields** | [**list[XiqDeviceField]**](XiqDeviceField.md)| The device fields to return | [optional] 

### Return type

[**XiqDevice**](XiqDevice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_cpu_memory_history**
> list[XiqDeviceCpuMemoryUsage] get_device_cpu_memory_history(id, start_time, end_time, interval)

Get device CPU/memory usage history

Get average device CPU and memory usage history.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | Device ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
interval = 56 # int | The aggregate interval in milliseconds

    try:
        # Get device CPU/memory usage history
        api_response = api_instance.get_device_cpu_memory_history(id, start_time, end_time, interval)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_cpu_memory_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **interval** | **int**| The aggregate interval in milliseconds | 

### Return type

[**list[XiqDeviceCpuMemoryUsage]**](XiqDeviceCpuMemoryUsage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_ibeacon**
> XiqDeviceIbeacon get_device_ibeacon(id)

Get the device iBeacon setting

Get the device iBeacon setting by device ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Get the device iBeacon setting
        api_response = api_instance.get_device_ibeacon(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_ibeacon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

[**XiqDeviceIbeacon**](XiqDeviceIbeacon.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_level_ssid_status**
> dict(str, XiqDeviceLevelSsidStatus) get_device_level_ssid_status(id)

Get SSID status for a device

Get the SSIDs status on each wifi interface for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Get SSID status for a device
        api_response = api_instance.get_device_level_ssid_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_level_ssid_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

[**dict(str, XiqDeviceLevelSsidStatus)**](XiqDeviceLevelSsidStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_location**
> XiqDeviceLocation get_device_location(id)

Get location for a device

Get the location info for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Get location for a device
        api_response = api_instance.get_device_location(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

[**XiqDeviceLocation**](XiqDeviceLocation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_network_policy**
> XiqNetworkPolicy get_device_network_policy(id)

Get network policy for a device

Get the network policy for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Get network policy for a device
        api_response = api_instance.get_device_network_policy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

[**XiqNetworkPolicy**](XiqNetworkPolicy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_stats**
> XiqDeviceStats get_device_stats(location_id=location_id)

Get device stats

Get device stats, such as total device count, managed device count, connected device count, etc.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    location_id = 56 # int | The location ID (optional)

    try:
        # Get device stats
        api_response = api_instance.get_device_stats(location_id=location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location ID | [optional] 

### Return type

[**XiqDeviceStats**](XiqDeviceStats.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_device_wifi_interface**
> list[XiqDeviceWifiInterface] get_device_wifi_interface(id, start_time, end_time)

Get the device WiFi interfaces stats

Get the device WiFi interfaces stats by device ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
start_time = 56 # int | The start time for collecting the wifi interfaces stat
end_time = 56 # int | The end time for collecting the wifi interfaces stat

    try:
        # Get the device WiFi interfaces stats
        api_response = api_instance.get_device_wifi_interface(id, start_time, end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_device_wifi_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **start_time** | **int**| The start time for collecting the wifi interfaces stat | 
 **end_time** | **int**| The end time for collecting the wifi interfaces stat | 

### Return type

[**list[XiqDeviceWifiInterface]**](XiqDeviceWifiInterface.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_xiq_device_installation_report**
> XiqDeviceInstallationReport get_xiq_device_installation_report(id)

Get device installation report

Get device installation report of a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Get device installation report
        api_response = api_instance.get_xiq_device_installation_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->get_xiq_device_installation_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

[**XiqDeviceInstallationReport**](XiqDeviceInstallationReport.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **list_device_alarm**
> PagedXiqDeviceAlarm list_device_alarm(id, start_time, end_time, page=page, limit=limit)

List alarms for a device

List alarms for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | Device ID
start_time = 56 # int | The start time for query alarm
end_time = 56 # int | The end time for query alarm
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List alarms for a device
        api_response = api_instance.list_device_alarm(id, start_time, end_time, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->list_device_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device ID | 
 **start_time** | **int**| The start time for query alarm | 
 **end_time** | **int**| The end time for query alarm | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqDeviceAlarm**](PagedXiqDeviceAlarm.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **list_devices**
> PagedXiqDevice list_devices(page=page, limit=limit, location_id=location_id, connected=connected, admin_states=admin_states, mac_addresses=mac_addresses, sns=sns, hostnames=hostnames, sort_field=sort_field, order=order, views=views, fields=fields, device_types=device_types, _async=_async)

[LRO] List devices

List devices with filters and pagination.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
location_id = 56 # int | Location Id (optional)
connected = True # bool | The device connect status (optional)
admin_states = [extremecloudiq.XiqDeviceAdminState()] # list[XiqDeviceAdminState] | The device admin states (optional)
mac_addresses = ['mac_addresses_example'] # list[str] | The device mac addresses (optional)
sns = ['sns_example'] # list[str] | The device serial numbers (optional)
hostnames = ['hostnames_example'] # list[str] | The device host names (optional)
sort_field = extremecloudiq.XiqDeviceSortField() # XiqDeviceSortField | The sort field (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order (ascending by default) (optional)
views = [extremecloudiq.XiqDeviceView()] # list[XiqDeviceView] | The views to return device fields (Check fields for each view at XiqDeviceView schema) (optional)
fields = [extremecloudiq.XiqDeviceField()] # list[XiqDeviceField] | The device fields to return (optional)
device_types = ["REAL"] # list[XiqDeviceType] | The device types to return (optional) (default to ["REAL"])
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] List devices
        api_response = api_instance.list_devices(page=page, limit=limit, location_id=location_id, connected=connected, admin_states=admin_states, mac_addresses=mac_addresses, sns=sns, hostnames=hostnames, sort_field=sort_field, order=order, views=views, fields=fields, device_types=device_types, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->list_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **location_id** | **int**| Location Id | [optional] 
 **connected** | **bool**| The device connect status | [optional] 
 **admin_states** | [**list[XiqDeviceAdminState]**](XiqDeviceAdminState.md)| The device admin states | [optional] 
 **mac_addresses** | [**list[str]**](str.md)| The device mac addresses | [optional] 
 **sns** | [**list[str]**](str.md)| The device serial numbers | [optional] 
 **hostnames** | [**list[str]**](str.md)| The device host names | [optional] 
 **sort_field** | [**XiqDeviceSortField**](.md)| The sort field | [optional] 
 **order** | [**XiqSortOrder**](.md)| The sort order (ascending by default) | [optional] 
 **views** | [**list[XiqDeviceView]**](XiqDeviceView.md)| The views to return device fields (Check fields for each view at XiqDeviceView schema) | [optional] 
 **fields** | [**list[XiqDeviceField]**](XiqDeviceField.md)| The device fields to return | [optional] 
 **device_types** | [**list[XiqDeviceType]**](XiqDeviceType.md)| The device types to return | [optional] [default to [&quot;REAL&quot;]]
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**PagedXiqDevice**](PagedXiqDevice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **list_devices_by_network_policy**
> PagedXiqDevice list_devices_by_network_policy(policy_id, page=page, limit=limit)

List assigned devices for network policy

List assigned devices for the network policy with pagination.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    policy_id = 56 # int | The network policy ID
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List assigned devices for network policy
        api_response = api_instance.list_devices_by_network_policy(policy_id, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->list_devices_by_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqDevice**](PagedXiqDevice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **onboard_devices**
> onboard_devices(xiq_onboard_device_request)

Onboard Devices

Onboard devices for all devices, such as Extreme/Aerohive, EXOS, VOSS, WiNG, and Dell. This is asynchronized operation to support massive device onboarding.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_onboard_device_request = extremecloudiq.XiqOnboardDeviceRequest() # XiqOnboardDeviceRequest | 

    try:
        # Onboard Devices
        api_instance.onboard_devices(xiq_onboard_device_request)
    except ApiException as e:
        print("Exception when calling DeviceApi->onboard_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_onboard_device_request** | [**XiqOnboardDeviceRequest**](XiqOnboardDeviceRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_device_level_ssid**
> override_device_level_ssid(id, xiq_device_level_ssid)

Override SSID for a device

Override SSID broadcast name/passphrase for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
xiq_device_level_ssid = extremecloudiq.XiqDeviceLevelSsid() # XiqDeviceLevelSsid | 

    try:
        # Override SSID for a device
        api_instance.override_device_level_ssid(id, xiq_device_level_ssid)
    except ApiException as e:
        print("Exception when calling DeviceApi->override_device_level_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **xiq_device_level_ssid** | [**XiqDeviceLevelSsid**](XiqDeviceLevelSsid.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **query_devices_location**
> dict(str, XiqDeviceLocation) query_devices_location(xiq_device_filter)

Query location for multiple devices

Query the location for the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Query location for multiple devices
        api_response = api_instance.query_devices_location(xiq_device_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->query_devices_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

[**dict(str, XiqDeviceLocation)**](XiqDeviceLocation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **query_devices_network_policy**
> dict(str, XiqNetworkPolicy) query_devices_network_policy(xiq_device_filter)

Query network policy for multiple devices

Query the network policy for the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Query network policy for multiple devices
        api_response = api_instance.query_devices_network_policy(xiq_device_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->query_devices_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

[**dict(str, XiqNetworkPolicy)**](XiqNetworkPolicy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **reboot_device**
> reboot_device(id)

Reboot a device

Reboot a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Reboot a device
        api_instance.reboot_device(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->reboot_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **reboot_devices**
> reboot_devices(xiq_device_filter)

Reboot devices

Reboot the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Reboot devices
        api_instance.reboot_devices(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->reboot_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **reset_device**
> reset_device(id, _async=_async)

[LRO] Reset a device to factory default

Reset a device to factory default settings.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Reset a device to factory default
        api_instance.reset_device(id, _async=_async)
    except ApiException as e:
        print("Exception when calling DeviceApi->reset_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **revoke_device_location**
> revoke_device_location(id)

Revoke location for a device

Revoke the assigned location for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Revoke location for a device
        api_instance.revoke_device_location(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->revoke_device_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **revoke_device_network_policy**
> revoke_device_network_policy(id)

Revoke network policy for a device

Revoke the assigned network policy for a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID

    try:
        # Revoke network policy for a device
        api_instance.revoke_device_network_policy(id)
    except ApiException as e:
        print("Exception when calling DeviceApi->revoke_device_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **revoke_devices_location**
> revoke_devices_location(xiq_device_filter)

Revoke location for multiple devices

Revoke the location from the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Revoke location for multiple devices
        api_instance.revoke_devices_location(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->revoke_devices_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **revoke_devices_network_policy**
> revoke_devices_network_policy(xiq_device_filter)

Revoke network policy for multiple devices

Revoke the network policy from the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_device_filter = extremecloudiq.XiqDeviceFilter() # XiqDeviceFilter | 

    try:
        # Revoke network policy for multiple devices
        api_instance.revoke_devices_network_policy(xiq_device_filter)
    except ApiException as e:
        print("Exception when calling DeviceApi->revoke_devices_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_device_filter** | [**XiqDeviceFilter**](XiqDeviceFilter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **revoke_devices_radius_proxy**
> revoke_devices_radius_proxy(ids)

Revoke RADIUS proxy from multiple devices

Revoke the RADIUS proxy from the target devices.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    ids = [56] # list[int] | The device IDs

    try:
        # Revoke RADIUS proxy from multiple devices
        api_instance.revoke_devices_radius_proxy(ids)
    except ApiException as e:
        print("Exception when calling DeviceApi->revoke_devices_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| The device IDs | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **send_cli_to_device**
> XiqSendCliResponse send_cli_to_device(id, request_body)

Send CLI to a device

Send CLI commands to a specific device.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    id = 56 # int | The device ID
request_body = ['request_body_example'] # list[str] | The one or multiple CLIs to send

    try:
        # Send CLI to a device
        api_response = api_instance.send_cli_to_device(id, request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->send_cli_to_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The device ID | 
 **request_body** | [**list[str]**](str.md)| The one or multiple CLIs to send | 

### Return type

[**XiqSendCliResponse**](XiqSendCliResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **send_cli_to_devices**
> XiqSendCliResponse send_cli_to_devices(xiq_send_cli_request, _async=_async)

[LRO] Send CLI to devices

Send CLI commands to the target devices. This API can be run at async mode, please follow the Long-Running Operation (LRO) guide to track the progress and the result.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.DeviceApi(api_client)
    xiq_send_cli_request = extremecloudiq.XiqSendCliRequest() # XiqSendCliRequest | 
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Send CLI to devices
        api_response = api_instance.send_cli_to_devices(xiq_send_cli_request, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->send_cli_to_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_send_cli_request** | [**XiqSendCliRequest**](XiqSendCliRequest.md)|  | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**XiqSendCliResponse**](XiqSendCliResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

