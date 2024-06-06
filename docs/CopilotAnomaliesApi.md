# extremecloudiq.CopilotAnomaliesApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anomalies_notifications**](CopilotAnomaliesApi.md#get_anomalies_notifications) | **GET** /copilot/anomalies/notifications | 
[**get_anomalies_report**](CopilotAnomaliesApi.md#get_anomalies_report) | **GET** /copilot/anomalies/report | 
[**get_assurance_scans_overview_data**](CopilotAnomaliesApi.md#get_assurance_scans_overview_data) | **GET** /copilot/assurance-scans/overview | 
[**get_atp_device_stats**](CopilotAnomaliesApi.md#get_atp_device_stats) | **GET** /copilot/anomalies/adverse-traffic/device-stats | 
[**get_atp_packet_counts**](CopilotAnomaliesApi.md#get_atp_packet_counts) | **GET** /copilot/anomalies/adverse-traffic/packet-counts | 
[**get_copilot_anomaliesby_category**](CopilotAnomaliesApi.md#get_copilot_anomaliesby_category) | **GET** /copilot/anomalies/anomalies-by-category | 
[**get_copilot_devices_with_locations**](CopilotAnomaliesApi.md#get_copilot_devices_with_locations) | **GET** /copilot/anomalies/devices-with-locations | 
[**get_devices_by_location**](CopilotAnomaliesApi.md#get_devices_by_location) | **GET** /copilot/anomalies/devices-by-location | 
[**get_dfs_recurrence_channel_stats**](CopilotAnomaliesApi.md#get_dfs_recurrence_channel_stats) | **GET** /copilot/anomalies/dfs-recurrence/channel-stats | 
[**get_dfs_recurrence_count_stats**](CopilotAnomaliesApi.md#get_dfs_recurrence_count_stats) | **GET** /copilot/anomalies/dfs-recurrence/count-stats | 
[**get_lldp_cdp_info**](CopilotAnomaliesApi.md#get_lldp_cdp_info) | **GET** /copilot/anomalies/poeflapping/lldp-cdp-info | 
[**get_poe_flapping_stats**](CopilotAnomaliesApi.md#get_poe_flapping_stats) | **GET** /copilot/anomalies/poeflapping/stats | 
[**get_poe_flapping_trends**](CopilotAnomaliesApi.md#get_poe_flapping_trends) | **GET** /copilot/anomalies/poeflapping/trends | 
[**get_port_efficiency_speed_duplex_stats**](CopilotAnomaliesApi.md#get_port_efficiency_speed_duplex_stats) | **GET** /copilot/anomalies/port-efficiency/speed-duplex-stats | 
[**get_port_efficiency_stats**](CopilotAnomaliesApi.md#get_port_efficiency_stats) | **GET** /copilot/anomalies/port-efficiency/stats | 
[**get_wifi_capacity_client_list**](CopilotAnomaliesApi.md#get_wifi_capacity_client_list) | **GET** /copilot/anomalies/wifi-capacity/client-list | 
[**get_wifi_capacity_stats**](CopilotAnomaliesApi.md#get_wifi_capacity_stats) | **GET** /copilot/anomalies/wifi-capacity/stats | 
[**get_wifi_efficiency_client_list**](CopilotAnomaliesApi.md#get_wifi_efficiency_client_list) | **GET** /copilot/anomalies/wifi-efficiency/client-list | 
[**get_wifi_efficiency_stats**](CopilotAnomaliesApi.md#get_wifi_efficiency_stats) | **GET** /copilot/anomalies/wifi-efficiency/stats | 
[**list_anomaly_locations**](CopilotAnomaliesApi.md#list_anomaly_locations) | **GET** /copilot/anomalies/locations | 
[**update_anomalies_feedback**](CopilotAnomaliesApi.md#update_anomalies_feedback) | **PUT** /copilot/anomalies/devices/feedback | 
[**update_anomaly_action**](CopilotAnomaliesApi.md#update_anomaly_action) | **PUT** /copilot/anomalies/update-action | 
[**update_anomaly_device_action**](CopilotAnomaliesApi.md#update_anomaly_device_action) | **PUT** /copilot/anomalies/devices/update-action | 
[**update_copilot_anomalies_devices_action**](CopilotAnomaliesApi.md#update_copilot_anomalies_devices_action) | **PUT** /copilot/anomalies/update-device-action | [LRO] Update Anomalies and Devices


# **get_anomalies_notifications**
> XiqAnomaliesNotificationsResponse get_anomalies_notifications()



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    
    try:
        api_response = api_instance.get_anomalies_notifications()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_anomalies_notifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqAnomaliesNotificationsResponse**](XiqAnomaliesNotificationsResponse.md)

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

# **get_anomalies_report**
> file get_anomalies_report(start_time, end_time, offset_time, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted, sort_field=sort_field, sort_order=sort_order, search_key=search_key, file_type=file_type)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
offset_time = 56 # int | The offset value
anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | The type of anomaly (optional)
building_id = 56 # int | The location identifier (optional)
severity = extremecloudiq.XiqAnomalySeverity() # XiqAnomalySeverity | The severity of anomaly (optional)
exclude_muted = False # bool | Exclude muted anomalies (optional) (default to False)
sort_field = extremecloudiq.XiqAnomalySortField() # XiqAnomalySortField | The sorting field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
search_key = '' # str | The search key (optional) (default to '')
file_type = 'csv' # str | The file format (optional) (default to 'csv')

    try:
        api_response = api_instance.get_anomalies_report(start_time, end_time, offset_time, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted, sort_field=sort_field, sort_order=sort_order, search_key=search_key, file_type=file_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_anomalies_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **offset_time** | **int**| The offset value | 
 **anomaly_type** | [**XiqAnomalyType**](.md)| The type of anomaly | [optional] 
 **building_id** | **int**| The location identifier | [optional] 
 **severity** | [**XiqAnomalySeverity**](.md)| The severity of anomaly | [optional] 
 **exclude_muted** | **bool**| Exclude muted anomalies | [optional] [default to False]
 **sort_field** | [**XiqAnomalySortField**](.md)| The sorting field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **search_key** | **str**| The search key | [optional] [default to &#39;&#39;]
 **file_type** | **str**| The file format | [optional] [default to &#39;csv&#39;]

### Return type

**file**

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

# **get_assurance_scans_overview_data**
> XiqAssuranceScansOverviewResponse get_assurance_scans_overview_data()



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    
    try:
        api_response = api_instance.get_assurance_scans_overview_data()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_assurance_scans_overview_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqAssuranceScansOverviewResponse**](XiqAssuranceScansOverviewResponse.md)

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

# **get_atp_device_stats**
> XiqAtpDeviceStatsResponse get_atp_device_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_atp_device_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_atp_device_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqAtpDeviceStatsResponse**](XiqAtpDeviceStatsResponse.md)

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

# **get_atp_packet_counts**
> XiqAtpPacketCountsResponse get_atp_packet_counts(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_atp_packet_counts(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_atp_packet_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqAtpPacketCountsResponse**](XiqAtpPacketCountsResponse.md)

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

# **get_copilot_anomaliesby_category**
> XiqCopilotAnomaliesByCategory get_copilot_anomaliesby_category(start_time, end_time, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | The type of anomaly (optional)
building_id = 56 # int | The location identifier (optional)
severity = extremecloudiq.XiqAnomalySeverity() # XiqAnomalySeverity | The severity od anomaly (optional)
exclude_muted = False # bool | exclude muted (optional) (default to False)

    try:
        api_response = api_instance.get_copilot_anomaliesby_category(start_time, end_time, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_copilot_anomaliesby_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **anomaly_type** | [**XiqAnomalyType**](.md)| The type of anomaly | [optional] 
 **building_id** | **int**| The location identifier | [optional] 
 **severity** | [**XiqAnomalySeverity**](.md)| The severity od anomaly | [optional] 
 **exclude_muted** | **bool**| exclude muted | [optional] [default to False]

### Return type

[**XiqCopilotAnomaliesByCategory**](XiqCopilotAnomaliesByCategory.md)

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

# **get_copilot_devices_with_locations**
> XiqCopilotPagedXiqAnomalyDeviceWithLocation get_copilot_devices_with_locations(start_time, end_time, page=page, limit=limit, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted, sort_field=sort_field, sort_order=sort_order, search_key=search_key)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Number of Records, min = 1, max = 100 (optional) (default to 10)
anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | The type of anomaly (optional)
building_id = 56 # int | The location identifier (optional)
severity = extremecloudiq.XiqAnomalySeverity() # XiqAnomalySeverity | The severity of anomaly (optional)
exclude_muted = False # bool | Exclude muted anomalies (optional) (default to False)
sort_field = extremecloudiq.XiqAnomalySortField() # XiqAnomalySortField | The sorting field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
search_key = '' # str | The search key (optional) (default to '')

    try:
        api_response = api_instance.get_copilot_devices_with_locations(start_time, end_time, page=page, limit=limit, anomaly_type=anomaly_type, building_id=building_id, severity=severity, exclude_muted=exclude_muted, sort_field=sort_field, sort_order=sort_order, search_key=search_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_copilot_devices_with_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Number of Records, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **anomaly_type** | [**XiqAnomalyType**](.md)| The type of anomaly | [optional] 
 **building_id** | **int**| The location identifier | [optional] 
 **severity** | [**XiqAnomalySeverity**](.md)| The severity of anomaly | [optional] 
 **exclude_muted** | **bool**| Exclude muted anomalies | [optional] [default to False]
 **sort_field** | [**XiqAnomalySortField**](.md)| The sorting field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **search_key** | **str**| The search key | [optional] [default to &#39;&#39;]

### Return type

[**XiqCopilotPagedXiqAnomalyDeviceWithLocation**](XiqCopilotPagedXiqAnomalyDeviceWithLocation.md)

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

# **get_devices_by_location**
> XiqAnomalyDevicesByLocationResponse get_devices_by_location(location_ids, anomaly_type=anomaly_type)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    location_ids = [56] # list[int] | The location IDs
anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | Anomaly type (optional)

    try:
        api_response = api_instance.get_devices_by_location(location_ids, anomaly_type=anomaly_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_devices_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | [**list[int]**](int.md)| The location IDs | 
 **anomaly_type** | [**XiqAnomalyType**](.md)| Anomaly type | [optional] 

### Return type

[**XiqAnomalyDevicesByLocationResponse**](XiqAnomalyDevicesByLocationResponse.md)

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

# **get_dfs_recurrence_channel_stats**
> XiqDfsRecurenceChannelStatsResponse get_dfs_recurrence_channel_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_dfs_recurrence_channel_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_dfs_recurrence_channel_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqDfsRecurenceChannelStatsResponse**](XiqDfsRecurenceChannelStatsResponse.md)

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

# **get_dfs_recurrence_count_stats**
> XiqDfsRecurenceCountStatsResponse get_dfs_recurrence_count_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_dfs_recurrence_count_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_dfs_recurrence_count_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqDfsRecurenceCountStatsResponse**](XiqDfsRecurenceCountStatsResponse.md)

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

# **get_lldp_cdp_info**
> XiqCopilotLldpCdpInfo get_lldp_cdp_info(anomaly_id, device_id, last_detected_time)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly ID
device_id = 56 # int | The device ID
last_detected_time = 56 # int | The last detected timestamp of anomaly

    try:
        api_response = api_instance.get_lldp_cdp_info(anomaly_id, device_id, last_detected_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_lldp_cdp_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly ID | 
 **device_id** | **int**| The device ID | 
 **last_detected_time** | **int**| The last detected timestamp of anomaly | 

### Return type

[**XiqCopilotLldpCdpInfo**](XiqCopilotLldpCdpInfo.md)

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

# **get_poe_flapping_stats**
> XiqPoeFlappingStatsResponse get_poe_flapping_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_poe_flapping_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_poe_flapping_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqPoeFlappingStatsResponse**](XiqPoeFlappingStatsResponse.md)

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

# **get_poe_flapping_trends**
> XiqPoeTrendGraphsResponse get_poe_flapping_trends(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_poe_flapping_trends(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_poe_flapping_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqPoeTrendGraphsResponse**](XiqPoeTrendGraphsResponse.md)

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

# **get_port_efficiency_speed_duplex_stats**
> XiqPortEfficiencySpeedDuplexStatsResponse get_port_efficiency_speed_duplex_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_port_efficiency_speed_duplex_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_port_efficiency_speed_duplex_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqPortEfficiencySpeedDuplexStatsResponse**](XiqPortEfficiencySpeedDuplexStatsResponse.md)

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

# **get_port_efficiency_stats**
> XiqPortEfficiencyStatsResponse get_port_efficiency_stats(anomaly_id, offset_time=offset_time)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id
offset_time = 56 # int | The offset value (optional)

    try:
        api_response = api_instance.get_port_efficiency_stats(anomaly_id, offset_time=offset_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_port_efficiency_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 
 **offset_time** | **int**| The offset value | [optional] 

### Return type

[**XiqPortEfficiencyStatsResponse**](XiqPortEfficiencyStatsResponse.md)

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

# **get_wifi_capacity_client_list**
> XiqWifiCapacityClientListResponse get_wifi_capacity_client_list(device_id, channel, timestamp)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    device_id = 56 # int | The device id
channel = 56 # int | The channel
timestamp = 56 # int | The timestamp

    try:
        api_response = api_instance.get_wifi_capacity_client_list(device_id, channel, timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_wifi_capacity_client_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The device id | 
 **channel** | **int**| The channel | 
 **timestamp** | **int**| The timestamp | 

### Return type

[**XiqWifiCapacityClientListResponse**](XiqWifiCapacityClientListResponse.md)

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

# **get_wifi_capacity_stats**
> XiqWifiCapacityStatsResponse get_wifi_capacity_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_wifi_capacity_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_wifi_capacity_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqWifiCapacityStatsResponse**](XiqWifiCapacityStatsResponse.md)

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

# **get_wifi_efficiency_client_list**
> XiqWifiEfficiencyClientListResponse get_wifi_efficiency_client_list(device_id, channel, timestamp)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    device_id = 56 # int | The device id
channel = 56 # int | The channel number
timestamp = 56 # int | The timestamp

    try:
        api_response = api_instance.get_wifi_efficiency_client_list(device_id, channel, timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_wifi_efficiency_client_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The device id | 
 **channel** | **int**| The channel number | 
 **timestamp** | **int**| The timestamp | 

### Return type

[**XiqWifiEfficiencyClientListResponse**](XiqWifiEfficiencyClientListResponse.md)

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

# **get_wifi_efficiency_stats**
> XiqWifiEfficiencyStatsResponse get_wifi_efficiency_stats(anomaly_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id

    try:
        api_response = api_instance.get_wifi_efficiency_stats(anomaly_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_wifi_efficiency_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 

### Return type

[**XiqWifiEfficiencyStatsResponse**](XiqWifiEfficiencyStatsResponse.md)

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

# **list_anomaly_locations**
> XiqCopilotPagedXiqAnomalyLocationEntity list_anomaly_locations(anomaly_type=anomaly_type, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, exclude_muted=exclude_muted)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | Anomaly type (optional)
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Number of Records, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqAnomalySortField() # XiqAnomalySortField | sort by field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
exclude_muted = False # bool | exclude muted (optional) (default to False)

    try:
        api_response = api_instance.list_anomaly_locations(anomaly_type=anomaly_type, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, exclude_muted=exclude_muted)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->list_anomaly_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_type** | [**XiqAnomalyType**](.md)| Anomaly type | [optional] 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Number of Records, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqAnomalySortField**](.md)| sort by field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **exclude_muted** | **bool**| exclude muted | [optional] [default to False]

### Return type

[**XiqCopilotPagedXiqAnomalyLocationEntity**](XiqCopilotPagedXiqAnomalyLocationEntity.md)

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

# **update_anomalies_feedback**
> XiqCopilotAnomaliesActionResponse update_anomalies_feedback(xiq_anomalies_feedback_request)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    xiq_anomalies_feedback_request = extremecloudiq.XiqAnomaliesFeedbackRequest() # XiqAnomaliesFeedbackRequest | 

    try:
        api_response = api_instance.update_anomalies_feedback(xiq_anomalies_feedback_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->update_anomalies_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_anomalies_feedback_request** | [**XiqAnomaliesFeedbackRequest**](XiqAnomaliesFeedbackRequest.md)|  | 

### Return type

[**XiqCopilotAnomaliesActionResponse**](XiqCopilotAnomaliesActionResponse.md)

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

# **update_anomaly_action**
> XiqCopilotAnomaliesActionResponse update_anomaly_action(xiq_anomalies_update_action_request)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    xiq_anomalies_update_action_request = extremecloudiq.XiqAnomaliesUpdateActionRequest() # XiqAnomaliesUpdateActionRequest | 

    try:
        api_response = api_instance.update_anomaly_action(xiq_anomalies_update_action_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->update_anomaly_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_anomalies_update_action_request** | [**XiqAnomaliesUpdateActionRequest**](XiqAnomaliesUpdateActionRequest.md)|  | 

### Return type

[**XiqCopilotAnomaliesActionResponse**](XiqCopilotAnomaliesActionResponse.md)

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

# **update_anomaly_device_action**
> XiqCopilotAnomaliesActionResponse update_anomaly_device_action(xiq_anomalies_device_update_action_request)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    xiq_anomalies_device_update_action_request = extremecloudiq.XiqAnomaliesDeviceUpdateActionRequest() # XiqAnomaliesDeviceUpdateActionRequest | 

    try:
        api_response = api_instance.update_anomaly_device_action(xiq_anomalies_device_update_action_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->update_anomaly_device_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_anomalies_device_update_action_request** | [**XiqAnomaliesDeviceUpdateActionRequest**](XiqAnomaliesDeviceUpdateActionRequest.md)|  | 

### Return type

[**XiqCopilotAnomaliesActionResponse**](XiqCopilotAnomaliesActionResponse.md)

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

# **update_copilot_anomalies_devices_action**
> update_copilot_anomalies_devices_action(xiq_update_anomalies_and_devices_request, _async=_async)

[LRO] Update Anomalies and Devices

Update Anomalies and Devices.

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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    xiq_update_anomalies_and_devices_request = extremecloudiq.XiqUpdateAnomaliesAndDevicesRequest() # XiqUpdateAnomaliesAndDevicesRequest | 
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Update Anomalies and Devices
        api_instance.update_copilot_anomalies_devices_action(xiq_update_anomalies_and_devices_request, _async=_async)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->update_copilot_anomalies_devices_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_update_anomalies_and_devices_request** | [**XiqUpdateAnomaliesAndDevicesRequest**](XiqUpdateAnomaliesAndDevicesRequest.md)|  | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

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

