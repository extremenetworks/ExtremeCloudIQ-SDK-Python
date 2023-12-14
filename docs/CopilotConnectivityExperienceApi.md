# extremecloudiq.CopilotConnectivityExperienceApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connectivity_details_by_client_type**](CopilotConnectivityExperienceApi.md#get_connectivity_details_by_client_type) | **GET** /copilot/connectivity/client-type | 
[**get_connectivity_details_by_locations**](CopilotConnectivityExperienceApi.md#get_connectivity_details_by_locations) | **GET** /copilot/connectivity/locations | 
[**get_wired_connectivity_experience**](CopilotConnectivityExperienceApi.md#get_wired_connectivity_experience) | **GET** /copilot/connectivity/wired/experience | 
[**get_wired_events**](CopilotConnectivityExperienceApi.md#get_wired_events) | **GET** /copilot/connectivity/wired/events | 
[**get_wired_hardware**](CopilotConnectivityExperienceApi.md#get_wired_hardware) | **GET** /copilot/connectivity/wired/hardware | 
[**get_wired_hardware_by_location**](CopilotConnectivityExperienceApi.md#get_wired_hardware_by_location) | **GET** /copilot/connectivity/wired/locations/hardware | 
[**get_wired_quality_index**](CopilotConnectivityExperienceApi.md#get_wired_quality_index) | **GET** /copilot/connectivity/wired/quality-index | 
[**get_wireless_apps**](CopilotConnectivityExperienceApi.md#get_wireless_apps) | **GET** /copilot/connectivity/wireless/apps | 
[**get_wireless_connectivity_experience**](CopilotConnectivityExperienceApi.md#get_wireless_connectivity_experience) | **GET** /copilot/connectivity/wireless/experience | 
[**get_wireless_events**](CopilotConnectivityExperienceApi.md#get_wireless_events) | **GET** /copilot/connectivity/wireless/events | 
[**get_wireless_events_by_location**](CopilotConnectivityExperienceApi.md#get_wireless_events_by_location) | **GET** /copilot/connectivity/wireless/locations/events | 
[**get_wireless_performance**](CopilotConnectivityExperienceApi.md#get_wireless_performance) | **GET** /copilot/connectivity/wireless/performance | 
[**get_wireless_performance_by_location**](CopilotConnectivityExperienceApi.md#get_wireless_performance_by_location) | **GET** /copilot/connectivity/wireless/locations/performance | 
[**get_wireless_quality_index**](CopilotConnectivityExperienceApi.md#get_wireless_quality_index) | **GET** /copilot/connectivity/wireless/quality-index | 
[**get_wireless_quality_index_by_location**](CopilotConnectivityExperienceApi.md#get_wireless_quality_index_by_location) | **GET** /copilot/connectivity/wireless/locations/quality-index | 
[**get_wireless_time_to_connect**](CopilotConnectivityExperienceApi.md#get_wireless_time_to_connect) | **GET** /copilot/connectivity/wireless/time-to-connect | 
[**get_wireless_time_to_connect_by_location**](CopilotConnectivityExperienceApi.md#get_wireless_time_to_connect_by_location) | **GET** /copilot/connectivity/wireless/locations/time-to-connect | 
[**get_wireless_views**](CopilotConnectivityExperienceApi.md#get_wireless_views) | **GET** /copilot/connectivity/wireless/views | 


# **get_connectivity_details_by_client_type**
> XiqConnectivityDetailsByClientTypeResponse get_connectivity_details_by_client_type(start_time, end_time, location_id=location_id, client_type=client_type, forensic_bucket=forensic_bucket)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
location_id = 0 # int | The location Id (optional) (default to 0)
client_type = extremecloudiq.XiqClientType() # XiqClientType | The client type (optional)
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)

    try:
        api_response = api_instance.get_connectivity_details_by_client_type(start_time, end_time, location_id=location_id, client_type=client_type, forensic_bucket=forensic_bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_client_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **location_id** | **int**| The location Id | [optional] [default to 0]
 **client_type** | [**XiqClientType**](.md)| The client type | [optional] 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 

### Return type

[**XiqConnectivityDetailsByClientTypeResponse**](XiqConnectivityDetailsByClientTypeResponse.md)

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

# **get_connectivity_details_by_locations**
> PagedXiqConnectivityExperienceData get_connectivity_details_by_locations(start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, location_id=location_id, search_key=search_key, client_type=client_type, forensic_bucket=forensic_bucket, quality_index=quality_index)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqSortField() # XiqSortField | sort by name or quality index (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
location_id = 0 # int | The location Id (optional) (default to 0)
search_key = '' # str | The search value (optional) (default to '')
client_type = extremecloudiq.XiqClientType() # XiqClientType | The client type (optional)
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
quality_index = extremecloudiq.XiqQualityIndex() # XiqQualityIndex | The quality index value (optional)

    try:
        api_response = api_instance.get_connectivity_details_by_locations(start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, location_id=location_id, search_key=search_key, client_type=client_type, forensic_bucket=forensic_bucket, quality_index=quality_index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqSortField**](.md)| sort by name or quality index | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **location_id** | **int**| The location Id | [optional] [default to 0]
 **search_key** | **str**| The search value | [optional] [default to &#39;&#39;]
 **client_type** | [**XiqClientType**](.md)| The client type | [optional] 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **quality_index** | [**XiqQualityIndex**](.md)| The quality index value | [optional] 

### Return type

[**PagedXiqConnectivityExperienceData**](PagedXiqConnectivityExperienceData.md)

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

# **get_wired_connectivity_experience**
> PagedXiqConnectivityExperienceData get_wired_connectivity_experience(view_type, start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqWiredViewType() # XiqWiredViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqSortField() # XiqSortField | sort by name or quality index (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)

    try:
        api_response = api_instance.get_wired_connectivity_experience(view_type, start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_connectivity_experience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqWiredViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqSortField**](.md)| sort by name or quality index | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 

### Return type

[**PagedXiqConnectivityExperienceData**](PagedXiqConnectivityExperienceData.md)

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

# **get_wired_events**
> PagedXiqWiredEventEntity get_wired_events(view_type, start_time, end_time, forensic_bucket, score_type, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, view_id=view_id, search_key=search_key, location_type=location_type, location_id=location_id, timestamp=timestamp)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqWiredViewType() # XiqWiredViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The selected time bucket
score_type = extremecloudiq.XiqCopilotWiredEventsScoreType() # XiqCopilotWiredEventsScoreType | The selected score type
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_by = extremecloudiq.XiqCopilotEventsWiredSortField() # XiqCopilotEventsWiredSortField | The sort field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
view_id = '' # str | The view id based on view type (optional) (default to '')
search_key = '' # str | The selected search key (optional) (default to '')
location_type = '' # str | The selected location type (optional) (default to '')
location_id = '0' # str | The selected location id (optional) (default to '0')
timestamp = 56 # int | The timestamp to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        api_response = api_instance.get_wired_events(view_type, start_time, end_time, forensic_bucket, score_type, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, view_id=view_id, search_key=search_key, location_type=location_type, location_id=location_id, timestamp=timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqWiredViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The selected time bucket | 
 **score_type** | [**XiqCopilotWiredEventsScoreType**](.md)| The selected score type | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_by** | [**XiqCopilotEventsWiredSortField**](.md)| The sort field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **view_id** | **str**| The view id based on view type | [optional] [default to &#39;&#39;]
 **search_key** | **str**| The selected search key | [optional] [default to &#39;&#39;]
 **location_type** | **str**| The selected location type | [optional] [default to &#39;&#39;]
 **location_id** | **str**| The selected location id | [optional] [default to &#39;0&#39;]
 **timestamp** | **int**| The timestamp to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**PagedXiqWiredEventEntity**](PagedXiqWiredEventEntity.md)

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

# **get_wired_hardware**
> XiqWiredHardwareResponse get_wired_hardware(view_type, start_time, end_time, forensic_bucket, view_id=view_id)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqWiredViewType() # XiqWiredViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The selected time bucket
view_id = '' # str | The view id based on view type (optional) (default to '')

    try:
        api_response = api_instance.get_wired_hardware(view_type, start_time, end_time, forensic_bucket, view_id=view_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqWiredViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The selected time bucket | 
 **view_id** | **str**| The view id based on view type | [optional] [default to &#39;&#39;]

### Return type

[**XiqWiredHardwareResponse**](XiqWiredHardwareResponse.md)

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

# **get_wired_hardware_by_location**
> XiqWiredHardwareByLocationResponse get_wired_hardware_by_location(start_time, end_time, forensic_bucket, view_type=view_type, view_id=view_id)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The selected time bucket
view_type = extremecloudiq.XiqWiredViewType() # XiqWiredViewType | The type of View (optional)
view_id = '' # str | The view id based on view type (optional) (default to '')

    try:
        api_response = api_instance.get_wired_hardware_by_location(start_time, end_time, forensic_bucket, view_type=view_type, view_id=view_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The selected time bucket | 
 **view_type** | [**XiqWiredViewType**](.md)| The type of View | [optional] 
 **view_id** | **str**| The view id based on view type | [optional] [default to &#39;&#39;]

### Return type

[**XiqWiredHardwareByLocationResponse**](XiqWiredHardwareByLocationResponse.md)

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

# **get_wired_quality_index**
> XiqWiredQualityIndexResponse get_wired_quality_index(start_time, end_time, view_type=view_type, view_id=view_id, forensic_bucket=forensic_bucket)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
view_type = extremecloudiq.XiqWiredViewType() # XiqWiredViewType | The type of View (optional)
view_id = '' # str | The view id based on view type (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The selected time bucket (optional)

    try:
        api_response = api_instance.get_wired_quality_index(start_time, end_time, view_type=view_type, view_id=view_id, forensic_bucket=forensic_bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_quality_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **view_type** | [**XiqWiredViewType**](.md)| The type of View | [optional] 
 **view_id** | **str**| The view id based on view type | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The selected time bucket | [optional] 

### Return type

[**XiqWiredQualityIndexResponse**](XiqWiredQualityIndexResponse.md)

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

# **get_wireless_apps**
> XiqWirelessAppsResponse get_wireless_apps(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
view_id = '' # str | The view type identifier (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
location_id = '0' # str | The location identifier (optional) (default to '0')
location_type = '' # str | The location type (optional) (default to '')

    try:
        api_response = api_instance.get_wireless_apps(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **view_id** | **str**| The view type identifier | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **location_id** | **str**| The location identifier | [optional] [default to &#39;0&#39;]
 **location_type** | **str**| The location type | [optional] [default to &#39;&#39;]

### Return type

[**XiqWirelessAppsResponse**](XiqWirelessAppsResponse.md)

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

# **get_wireless_connectivity_experience**
> PagedXiqConnectivityExperienceData get_wireless_connectivity_experience(view_type, start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | View by location, ssid or osTypes
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Number of Records, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqSortField() # XiqSortField | sort by name or quality index (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)

    try:
        api_response = api_instance.get_wireless_connectivity_experience(view_type, start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_connectivity_experience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| View by location, ssid or osTypes | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Number of Records, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqSortField**](.md)| sort by name or quality index | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 

### Return type

[**PagedXiqConnectivityExperienceData**](PagedXiqConnectivityExperienceData.md)

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

# **get_wireless_events**
> PagedXiqCopilotWirelessEvent get_wireless_events(view_type, start_time, end_time, score_type, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, view_id=view_id, forensic_bucket=forensic_bucket, search_key=search_key, location_id=location_id, location_type=location_type, timestamp=timestamp)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | View by location, ssid or osTypes
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
score_type = extremecloudiq.XiqCopilotWirelessEventsScoreType() # XiqCopilotWirelessEventsScoreType | The wireless score type
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Number of Records, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqCopilotEventsWirelessSortField() # XiqCopilotEventsWirelessSortField | the sort field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
view_id = '' # str | The view type identifier (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
search_key = '' # str | The search key (optional) (default to '')
location_id = '0' # str | The location identifier (optional) (default to '0')
location_type = 'location_type_example' # str | The location type (optional)
timestamp = 56 # int | The timestamp to query, epoch time in milliseconds since 1/1/1970 (optional)

    try:
        api_response = api_instance.get_wireless_events(view_type, start_time, end_time, score_type, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, view_id=view_id, forensic_bucket=forensic_bucket, search_key=search_key, location_id=location_id, location_type=location_type, timestamp=timestamp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| View by location, ssid or osTypes | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **score_type** | [**XiqCopilotWirelessEventsScoreType**](.md)| The wireless score type | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Number of Records, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqCopilotEventsWirelessSortField**](.md)| the sort field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **view_id** | **str**| The view type identifier | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **search_key** | **str**| The search key | [optional] [default to &#39;&#39;]
 **location_id** | **str**| The location identifier | [optional] [default to &#39;0&#39;]
 **location_type** | **str**| The location type | [optional] 
 **timestamp** | **int**| The timestamp to query, epoch time in milliseconds since 1/1/1970 | [optional] 

### Return type

[**PagedXiqCopilotWirelessEvent**](PagedXiqCopilotWirelessEvent.md)

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

# **get_wireless_events_by_location**
> PagedXiqCopilotWirelessEvent get_wireless_events_by_location(start_time, end_time, score_type, location_id, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, forensic_bucket=forensic_bucket, search_key=search_key, timestamp=timestamp, ssid=ssid, os_type=os_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
score_type = extremecloudiq.XiqCopilotWirelessEventsScoreType() # XiqCopilotWirelessEventsScoreType | The wireless score type
location_id = 'location_id_example' # str | The location identifier
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Number of Records, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqCopilotEventsWirelessSortField() # XiqCopilotEventsWirelessSortField | the sort field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
search_key = '' # str | The search key (optional) (default to '')
timestamp = 56 # int | The timestamp to query, epoch time in milliseconds since 1/1/1970 (optional)
ssid = '' # str | The ssid (optional) (default to '')
os_type = '' # str | The os type (optional) (default to '')

    try:
        api_response = api_instance.get_wireless_events_by_location(start_time, end_time, score_type, location_id, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, forensic_bucket=forensic_bucket, search_key=search_key, timestamp=timestamp, ssid=ssid, os_type=os_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **score_type** | [**XiqCopilotWirelessEventsScoreType**](.md)| The wireless score type | 
 **location_id** | **str**| The location identifier | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Number of Records, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqCopilotEventsWirelessSortField**](.md)| the sort field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **search_key** | **str**| The search key | [optional] [default to &#39;&#39;]
 **timestamp** | **int**| The timestamp to query, epoch time in milliseconds since 1/1/1970 | [optional] 
 **ssid** | **str**| The ssid | [optional] [default to &#39;&#39;]
 **os_type** | **str**| The os type | [optional] [default to &#39;&#39;]

### Return type

[**PagedXiqCopilotWirelessEvent**](PagedXiqCopilotWirelessEvent.md)

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

# **get_wireless_performance**
> XiqWirelessConnectivityPerformanceResponse get_wireless_performance(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
view_id = '' # str | The view type identifier (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
location_id = '0' # str | The location identifier (optional) (default to '0')
location_type = '' # str | The location type (optional) (default to '')

    try:
        api_response = api_instance.get_wireless_performance(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **view_id** | **str**| The view type identifier | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **location_id** | **str**| The location identifier | [optional] [default to &#39;0&#39;]
 **location_type** | **str**| The location type | [optional] [default to &#39;&#39;]

### Return type

[**XiqWirelessConnectivityPerformanceResponse**](XiqWirelessConnectivityPerformanceResponse.md)

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

# **get_wireless_performance_by_location**
> XiqWirelessConnectivityPerformanceResponse get_wireless_performance_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    location_id = 'location_id_example' # str | The location identifier
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
ssid = '' # str | The ssid (optional) (default to '')
os_type = '' # str | The client type (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)

    try:
        api_response = api_instance.get_wireless_performance_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The location identifier | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **ssid** | **str**| The ssid | [optional] [default to &#39;&#39;]
 **os_type** | **str**| The client type | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 

### Return type

[**XiqWirelessConnectivityPerformanceResponse**](XiqWirelessConnectivityPerformanceResponse.md)

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

# **get_wireless_quality_index**
> XiqWirelessQualityIndexResponse get_wireless_quality_index(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
view_id = '' # str | The view type identifier (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
location_id = '0' # str | The location identifier (optional) (default to '0')
location_type = 'location_type_example' # str | The location type (optional)

    try:
        api_response = api_instance.get_wireless_quality_index(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **view_id** | **str**| The view type identifier | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **location_id** | **str**| The location identifier | [optional] [default to &#39;0&#39;]
 **location_type** | **str**| The location type | [optional] 

### Return type

[**XiqWirelessQualityIndexResponse**](XiqWirelessQualityIndexResponse.md)

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

# **get_wireless_quality_index_by_location**
> XiqWirelessQualityIndexByLocationResponse get_wireless_quality_index_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    location_id = 'location_id_example' # str | The location identifier
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
ssid = '' # str | The ssid (optional) (default to '')
os_type = '' # str | The os type (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)

    try:
        api_response = api_instance.get_wireless_quality_index_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The location identifier | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **ssid** | **str**| The ssid | [optional] [default to &#39;&#39;]
 **os_type** | **str**| The os type | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 

### Return type

[**XiqWirelessQualityIndexByLocationResponse**](XiqWirelessQualityIndexByLocationResponse.md)

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

# **get_wireless_time_to_connect**
> XiqWirelessTimeToConnectResponse get_wireless_time_to_connect(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqConnectivityExperienceViewType() # XiqConnectivityExperienceViewType | The type of View
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
view_id = '' # str | The view type identifier (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)
location_id = '0' # str | The location identifier (optional) (default to '0')
location_type = 'location_type_example' # str | The location type (optional)

    try:
        api_response = api_instance.get_wireless_time_to_connect(view_type, start_time, end_time, view_id=view_id, forensic_bucket=forensic_bucket, location_id=location_id, location_type=location_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqConnectivityExperienceViewType**](.md)| The type of View | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **view_id** | **str**| The view type identifier | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 
 **location_id** | **str**| The location identifier | [optional] [default to &#39;0&#39;]
 **location_type** | **str**| The location type | [optional] 

### Return type

[**XiqWirelessTimeToConnectResponse**](XiqWirelessTimeToConnectResponse.md)

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

# **get_wireless_time_to_connect_by_location**
> XiqWirelessTimeToConnectResponse get_wireless_time_to_connect_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    location_id = 'location_id_example' # str | The location identifier
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970
ssid = '' # str | The ssid (optional) (default to '')
os_type = '' # str | The client type (optional) (default to '')
forensic_bucket = extremecloudiq.XiqForensicBucket() # XiqForensicBucket | The time period bucket detected (optional)

    try:
        api_response = api_instance.get_wireless_time_to_connect_by_location(location_id, start_time, end_time, ssid=ssid, os_type=os_type, forensic_bucket=forensic_bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The location identifier | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 
 **ssid** | **str**| The ssid | [optional] [default to &#39;&#39;]
 **os_type** | **str**| The client type | [optional] [default to &#39;&#39;]
 **forensic_bucket** | [**XiqForensicBucket**](.md)| The time period bucket detected | [optional] 

### Return type

[**XiqWirelessTimeToConnectResponse**](XiqWirelessTimeToConnectResponse.md)

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

# **get_wireless_views**
> XiqWirelessViewsTypeResponse get_wireless_views(view_type)



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
    api_instance = extremecloudiq.CopilotConnectivityExperienceApi(api_client)
    view_type = extremecloudiq.XiqWirelessViewsListType() # XiqWirelessViewsListType | The type of View

    try:
        api_response = api_instance.get_wireless_views(view_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_type** | [**XiqWirelessViewsListType**](.md)| The type of View | 

### Return type

[**XiqWirelessViewsTypeResponse**](XiqWirelessViewsTypeResponse.md)

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

