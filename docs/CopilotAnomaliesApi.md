# extremecloudiq.CopilotAnomaliesApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices_by_location**](CopilotAnomaliesApi.md#get_devices_by_location) | **GET** /copilot/anomalies/devices-by-location | 
[**get_poe_flapping_stats**](CopilotAnomaliesApi.md#get_poe_flapping_stats) | **GET** /copilot/anomalies/poeflapping/stats | 
[**list_anomaly_locations**](CopilotAnomaliesApi.md#list_anomaly_locations) | **GET** /copilot/anomalies/locations | 


# **get_devices_by_location**
> XiqAnomalyDevicesByLocationResponse get_devices_by_location(anomaly_type=anomaly_type, location_id=location_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_type = extremecloudiq.XiqAnomalyType() # XiqAnomalyType | Anomaly type (optional)
location_id = 0 # int | The location id (optional) (default to 0)

    try:
        api_response = api_instance.get_devices_by_location(anomaly_type=anomaly_type, location_id=location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_devices_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_type** | [**XiqAnomalyType**](.md)| Anomaly type | [optional] 
 **location_id** | **int**| The location id | [optional] [default to 0]

### Return type

[**XiqAnomalyDevicesByLocationResponse**](XiqAnomalyDevicesByLocationResponse.md)

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

# **get_poe_flapping_stats**
> XiqPoeFlappingStatsResponse get_poe_flapping_stats(anomaly_id, location_id=location_id)



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
    api_instance = extremecloudiq.CopilotAnomaliesApi(api_client)
    anomaly_id = 'anomaly_id_example' # str | The anomaly id
location_id = 0 # int | The location id (optional) (default to 0)

    try:
        api_response = api_instance.get_poe_flapping_stats(anomaly_id, location_id=location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotAnomaliesApi->get_poe_flapping_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_id** | **str**| The anomaly id | 
 **location_id** | **int**| The location id | [optional] [default to 0]

### Return type

[**XiqPoeFlappingStatsResponse**](XiqPoeFlappingStatsResponse.md)

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

# **list_anomaly_locations**
> XiqCopilotPagedXiqAnomalyLocationEntity list_anomaly_locations(anomaly_type=anomaly_type, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, exclude_muted=exclude_muted)



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

