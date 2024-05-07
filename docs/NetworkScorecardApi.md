# extremecloudiq.NetworkScorecardApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_health**](NetworkScorecardApi.md#get_client_health) | **GET** /network-scorecard/clientHealth/{locationId} | Get the overall client health score
[**get_device_health**](NetworkScorecardApi.md#get_device_health) | **GET** /network-scorecard/deviceHealth/{locationId} | Get the overall device health score
[**get_network_health**](NetworkScorecardApi.md#get_network_health) | **GET** /network-scorecard/networkHealth/{locationId} | Get the overall network health score
[**get_services_health**](NetworkScorecardApi.md#get_services_health) | **GET** /network-scorecard/servicesHealth/{locationId} | Get the overall services health score
[**get_wifi_health**](NetworkScorecardApi.md#get_wifi_health) | **GET** /network-scorecard/wifiHealth/{locationId} | Get the overall wifi health score


# **get_client_health**
> ClientHealth get_client_health(location_id, start_time=start_time, end_time=end_time)

Get the overall client health score

Get the clients health score over the period

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
    api_instance = extremecloudiq.NetworkScorecardApi(api_client)
    location_id = 56 # int | The location folder ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970 (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        # Get the overall client health score
        api_response = api_instance.get_client_health(location_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkScorecardApi->get_client_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location folder ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**ClientHealth**](ClientHealth.md)

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

# **get_device_health**
> DeviceHealth get_device_health(location_id, start_time=start_time, end_time=end_time)

Get the overall device health score

Get the devices health score over the period

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
    api_instance = extremecloudiq.NetworkScorecardApi(api_client)
    location_id = 56 # int | The location folder ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970 (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        # Get the overall device health score
        api_response = api_instance.get_device_health(location_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkScorecardApi->get_device_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location folder ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**DeviceHealth**](DeviceHealth.md)

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

# **get_network_health**
> NetworkHealth get_network_health(location_id, start_time=start_time, end_time=end_time)

Get the overall network health score

Get the network health score over the period

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
    api_instance = extremecloudiq.NetworkScorecardApi(api_client)
    location_id = 56 # int | The location folder ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970 (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        # Get the overall network health score
        api_response = api_instance.get_network_health(location_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkScorecardApi->get_network_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location folder ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**NetworkHealth**](NetworkHealth.md)

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

# **get_services_health**
> ServicesHealth get_services_health(location_id, start_time=start_time, end_time=end_time)

Get the overall services health score

Get the  health score over the period

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
    api_instance = extremecloudiq.NetworkScorecardApi(api_client)
    location_id = 56 # int | The location folder ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970 (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        # Get the overall services health score
        api_response = api_instance.get_services_health(location_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkScorecardApi->get_services_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location folder ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**ServicesHealth**](ServicesHealth.md)

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

# **get_wifi_health**
> WifiHealth get_wifi_health(location_id, start_time=start_time, end_time=end_time)

Get the overall wifi health score

Get the wifi health score over the period

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
    api_instance = extremecloudiq.NetworkScorecardApi(api_client)
    location_id = 56 # int | The location folder ID
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970 (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        # Get the overall wifi health score
        api_response = api_instance.get_wifi_health(location_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkScorecardApi->get_wifi_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| The location folder ID | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**WifiHealth**](WifiHealth.md)

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

