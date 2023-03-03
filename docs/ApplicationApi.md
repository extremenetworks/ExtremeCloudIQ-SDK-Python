# extremecloudiq.ApplicationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_application_top_clients_usage**](ApplicationApi.md#list_application_top_clients_usage) | **GET** /applications/{id}/clients/top{n} | List the TopN clients for a application
[**list_applications**](ApplicationApi.md#list_applications) | **GET** /applications | List the applications
[**list_top_applications_usage**](ApplicationApi.md#list_top_applications_usage) | **GET** /applications/top{n} | List the TopN applications


# **list_application_top_clients_usage**
> list[XiqApplicationTopClientsUsage] list_application_top_clients_usage(id, n, start_time, end_time)

List the TopN clients for a application

List the TopN clients by usage for a specific application.

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
    api_instance = extremecloudiq.ApplicationApi(api_client)
    id = 56 # int | The application ID
n = 56 # int | The TopN number
start_time = 56 # int | The start time for querying top client usage of application
end_time = 56 # int | The end time for querying top application usage of application

    try:
        # List the TopN clients for a application
        api_response = api_instance.list_application_top_clients_usage(id, n, start_time, end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->list_application_top_clients_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The application ID | 
 **n** | **int**| The TopN number | 
 **start_time** | **int**| The start time for querying top client usage of application | 
 **end_time** | **int**| The end time for querying top application usage of application | 

### Return type

[**list[XiqApplicationTopClientsUsage]**](XiqApplicationTopClientsUsage.md)

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

# **list_applications**
> PagedXiqApplication list_applications(page=page, limit=limit, name=name, detection_protocol=detection_protocol, detection_type=detection_type, predefined=predefined, sort_field=sort_field, order=order)

List the applications

List a page of applications by filter.

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
    api_instance = extremecloudiq.ApplicationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
name = 'name_example' # str | Application Name (optional)
detection_protocol = extremecloudiq.XiqApplicationDetectionProtocol() # XiqApplicationDetectionProtocol | Application Detection Protocol, only for custom Application (optional)
detection_type = extremecloudiq.XiqApplicationDetectionType() # XiqApplicationDetectionType | Application Detection Type, only for custom Application (optional)
predefined = true # bool | Flag to filter predefined or custom Application (optional)
sort_field = extremecloudiq.XiqApplicationSortField() # XiqApplicationSortField | The sort field (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order (ascending by default) (optional)

    try:
        # List the applications
        api_response = api_instance.list_applications(page=page, limit=limit, name=name, detection_protocol=detection_protocol, detection_type=detection_type, predefined=predefined, sort_field=sort_field, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **name** | **str**| Application Name | [optional] 
 **detection_protocol** | [**XiqApplicationDetectionProtocol**](.md)| Application Detection Protocol, only for custom Application | [optional] 
 **detection_type** | [**XiqApplicationDetectionType**](.md)| Application Detection Type, only for custom Application | [optional] 
 **predefined** | **bool**| Flag to filter predefined or custom Application | [optional] 
 **sort_field** | [**XiqApplicationSortField**](.md)| The sort field | [optional] 
 **order** | [**XiqSortOrder**](.md)| The sort order (ascending by default) | [optional] 

### Return type

[**PagedXiqApplication**](PagedXiqApplication.md)

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

# **list_top_applications_usage**
> list[XiqTopApplicationsUsage] list_top_applications_usage(n, start_time, end_time)

List the TopN applications

List the TopN applications by usage.

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
    api_instance = extremecloudiq.ApplicationApi(api_client)
    n = 56 # int | The TopN number
start_time = 56 # int | The start time for querying top application usage
end_time = 56 # int | The end time for querying top application usage

    try:
        # List the TopN applications
        api_response = api_instance.list_top_applications_usage(n, start_time, end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->list_top_applications_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The TopN number | 
 **start_time** | **int**| The start time for querying top application usage | 
 **end_time** | **int**| The end time for querying top application usage | 

### Return type

[**list[XiqTopApplicationsUsage]**](XiqTopApplicationsUsage.md)

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

