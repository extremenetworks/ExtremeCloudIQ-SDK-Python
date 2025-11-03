<a id="__pageTop"></a>
# extremecloudiq.apis.tags.dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_device_health_report**](#download_device_health_report) | **get** /dashboard/wireless/device-health/reports/{id} | Download the  report
[**export_to_csv2**](#export_to_csv2) | **post** /dashboard/wireless/device-health/export | Export all Wireless Device Health Data to CSV
[**get_device_cpu_usage_issue_count**](#get_device_cpu_usage_issue_count) | **post** /dashboard/wireless/device-health/issues/cpu-usage-issues | CPU usage issues for wireless devices
[**get_device_health_grid**](#get_device_health_grid) | **post** /dashboard/wireless/device-health/grid | Wireless device health grid
[**get_device_memory_usage_issue_count**](#get_device_memory_usage_issue_count) | **post** /dashboard/wireless/device-health/issues/memory-usage-issues | Memory usage issues for wireless devices
[**get_device_poe_usage_issues_count**](#get_device_poe_usage_issues_count) | **post** /dashboard/wireless/device-health/issues/poe-usage-issues | PoE usage issues for wireless devices
[**get_device_reboot_summary**](#get_device_reboot_summary) | **get** /dashboard/wireless/device-health/reboot/summary | 
[**get_device_summary**](#get_device_summary) | **post** /dashboard/wireless/device-health/summary | Device health summary for wireless devices

# **download_device_health_report**
<a id="download_device_health_report"></a>
> [str] download_device_health_report(id)

Download the  report

Download report of Metrics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the  report
        api_response = api_instance.download_device_health_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->download_device_health_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_device_health_report.ApiResponseFor200) | OK

#### download_device_health_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_to_csv2**
<a id="export_to_csv2"></a>
> XiqMetricReport export_to_csv2(xiq_wireless_device_health_grid_filter)

Export all Wireless Device Health Data to CSV

Export all Wireless Device Health Data to a CSV file.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_wireless_device_health_sort_field import XiqWirelessDeviceHealthSortField
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_wireless_device_health_grid_filter import XiqWirelessDeviceHealthGridFilter
from extremecloudiq.model.xiq_metric_report import XiqMetricReport
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqWirelessDeviceHealthGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        has_device_health_issues=True,
        has_poe_issues=True,
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
    )
    try:
        # Export all Wireless Device Health Data to CSV
        api_response = api_instance.export_to_csv2(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->export_to_csv2: %s\n" % e)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
        'sortField': XiqWirelessDeviceHealthSortField("HOSTNAME"),
        'sortOrder': XiqSortOrder("ASC"),
        'includeUnassigned': False,
    }
    body = XiqWirelessDeviceHealthGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        has_device_health_issues=True,
        has_poe_issues=True,
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
    )
    try:
        # Export all Wireless Device Health Data to CSV
        api_response = api_instance.export_to_csv2(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->export_to_csv2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessDeviceHealthGridFilter**](../../models/XiqWirelessDeviceHealthGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
includeUnassigned | IncludeUnassignedSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessDeviceHealthSortField**](../../models/XiqWirelessDeviceHealthSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_to_csv2.ApiResponseFor200) | OK

#### export_to_csv2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqMetricReport**](../../models/XiqMetricReport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_cpu_usage_issue_count**
<a id="get_device_cpu_usage_issue_count"></a>
> XiqDeviceCpuUsageIssueCount get_device_cpu_usage_issue_count(xiq_dashboard_filter)

CPU usage issues for wireless devices

Returns the count of wireless devices having CPU usage issues (CPU usage >= 95%) based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_device_cpu_usage_issue_count import XiqDeviceCpuUsageIssueCount
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # CPU usage issues for wireless devices
        api_response = api_instance.get_device_cpu_usage_issue_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_cpu_usage_issue_count: %s\n" % e)

    # example passing only optional values
    query_params = {
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # CPU usage issues for wireless devices
        api_response = api_instance.get_device_cpu_usage_issue_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_cpu_usage_issue_count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDashboardFilter**](../../models/XiqDashboardFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeUnassigned | IncludeUnassignedSchema | | optional


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_cpu_usage_issue_count.ApiResponseFor200) | OK

#### get_device_cpu_usage_issue_count.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDeviceCpuUsageIssueCount**](../../models/XiqDeviceCpuUsageIssueCount.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_health_grid**
<a id="get_device_health_grid"></a>
> PagedXiqDeviceHealthGridResponse get_device_health_grid(xiq_wireless_device_health_grid_filter)

Wireless device health grid

Returns the device health grid of wireless devices based on the provided filters. The results can be filtered by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_wireless_device_health_sort_field import XiqWirelessDeviceHealthSortField
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_wireless_device_health_grid_filter import XiqWirelessDeviceHealthGridFilter
from extremecloudiq.model.paged_xiq_device_health_grid_response import PagedXiqDeviceHealthGridResponse
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqWirelessDeviceHealthGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        has_device_health_issues=True,
        has_poe_issues=True,
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
    )
    try:
        # Wireless device health grid
        api_response = api_instance.get_device_health_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_health_grid: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'keyword': "keyword_example",
        'sortField': XiqWirelessDeviceHealthSortField("HOSTNAME"),
        'sortOrder': XiqSortOrder("ASC"),
        'includeUnassigned': False,
    }
    body = XiqWirelessDeviceHealthGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        has_device_health_issues=True,
        has_poe_issues=True,
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
    )
    try:
        # Wireless device health grid
        api_response = api_instance.get_device_health_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_health_grid: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessDeviceHealthGridFilter**](../../models/XiqWirelessDeviceHealthGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
keyword | KeywordSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
includeUnassigned | IncludeUnassignedSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessDeviceHealthSortField**](../../models/XiqWirelessDeviceHealthSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_health_grid.ApiResponseFor200) | OK

#### get_device_health_grid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqDeviceHealthGridResponse**](../../models/PagedXiqDeviceHealthGridResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_memory_usage_issue_count**
<a id="get_device_memory_usage_issue_count"></a>
> XiqDeviceMemoryUsageIssueCount get_device_memory_usage_issue_count(xiq_dashboard_filter)

Memory usage issues for wireless devices

Returns the count of wireless devices having Memory usage issues based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_device_memory_usage_issue_count import XiqDeviceMemoryUsageIssueCount
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Memory usage issues for wireless devices
        api_response = api_instance.get_device_memory_usage_issue_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_memory_usage_issue_count: %s\n" % e)

    # example passing only optional values
    query_params = {
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Memory usage issues for wireless devices
        api_response = api_instance.get_device_memory_usage_issue_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_memory_usage_issue_count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDashboardFilter**](../../models/XiqDashboardFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeUnassigned | IncludeUnassignedSchema | | optional


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_memory_usage_issue_count.ApiResponseFor200) | OK

#### get_device_memory_usage_issue_count.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDeviceMemoryUsageIssueCount**](../../models/XiqDeviceMemoryUsageIssueCount.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_poe_usage_issues_count**
<a id="get_device_poe_usage_issues_count"></a>
> XiqDevicePoeUsageIssuesCount get_device_poe_usage_issues_count(xiq_dashboard_filter)

PoE usage issues for wireless devices

Returns the count of wireless devices having PoE usage issues (Non-adequate power) based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_device_poe_usage_issues_count import XiqDevicePoeUsageIssuesCount
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # PoE usage issues for wireless devices
        api_response = api_instance.get_device_poe_usage_issues_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_poe_usage_issues_count: %s\n" % e)

    # example passing only optional values
    query_params = {
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # PoE usage issues for wireless devices
        api_response = api_instance.get_device_poe_usage_issues_count(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_poe_usage_issues_count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDashboardFilter**](../../models/XiqDashboardFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeUnassigned | IncludeUnassignedSchema | | optional


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_poe_usage_issues_count.ApiResponseFor200) | OK

#### get_device_poe_usage_issues_count.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDevicePoeUsageIssuesCount**](../../models/XiqDevicePoeUsageIssuesCount.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_reboot_summary**
<a id="get_device_reboot_summary"></a>
> PagedXiqDeviceRebootSummary get_device_reboot_summary()



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.paged_xiq_device_reboot_summary import PagedXiqDeviceRebootSummary
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'deviceId': 1,
    }
    try:
        api_response = api_instance.get_device_reboot_summary(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_reboot_summary: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
deviceId | DeviceIdSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_reboot_summary.ApiResponseFor200) | OK

#### get_device_reboot_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqDeviceRebootSummary**](../../models/PagedXiqDeviceRebootSummary.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_summary**
<a id="get_device_summary"></a>
> XiqDeviceSummary get_device_summary(xiq_dashboard_filter)

Device health summary for wireless devices

Returns the count of total wireless devices and total devices with health issues based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_device_health_api
from extremecloudiq.model.xiq_device_summary import XiqDeviceSummary
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
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
    api_instance = dashboard_wireless_device_health_api.DashboardWirelessDeviceHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Device health summary for wireless devices
        api_response = api_instance.get_device_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_summary: %s\n" % e)

    # example passing only optional values
    query_params = {
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Device health summary for wireless devices
        api_response = api_instance.get_device_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessDeviceHealthApi->get_device_summary: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDashboardFilter**](../../models/XiqDashboardFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeUnassigned | IncludeUnassignedSchema | | optional


# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_summary.ApiResponseFor200) | OK

#### get_device_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDeviceSummary**](../../models/XiqDeviceSummary.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

