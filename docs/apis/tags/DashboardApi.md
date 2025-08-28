<a id="__pageTop"></a>
# extremecloudiq.apis.tags.dashboard_api.DashboardApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wireless_diagnostics_criteria_param**](#create_wireless_diagnostics_criteria_param) | **post** /dashboard/wireless/dashboard/criteria | Create Criteria for Wireless Diagnostics Dashboard
[**download_site_with_issue_report**](#download_site_with_issue_report) | **get** /dashboard/reports/{id} | Download the  report
[**export_to_csv3**](#export_to_csv3) | **post** /dashboard/export | Export all dashboard data to CSV
[**get_alert_diagnostics**](#get_alert_diagnostics) | **post** /dashboard/alerts | Alert statistics
[**get_all_diagnostics_device_types**](#get_all_diagnostics_device_types) | **get** /dashboard/device-types | Get all diagnostics device types
[**get_asset_diagnostics**](#get_asset_diagnostics) | **post** /dashboard/assets | Asset statistics
[**get_client_health_diagnostics**](#get_client_health_diagnostics) | **post** /dashboard/clients | Client health statistics
[**get_device_health_diagnostics**](#get_device_health_diagnostics) | **post** /dashboard/devices | Device health statistics
[**get_sites_with_issues_diagnostics**](#get_sites_with_issues_diagnostics) | **post** /dashboard/sites-with-issues | Sites with issues
[**get_usage_and_capacity_diagnostics**](#get_usage_and_capacity_diagnostics) | **post** /dashboard/usage-capacity | Usage &amp; capacity statistics
[**get_wireless_diagnostics_dashboard_criteria_param**](#get_wireless_diagnostics_dashboard_criteria_param) | **get** /dashboard/wireless/dashboard/criteria | Criteria for Wireless Diagnostics Dashboard

# **create_wireless_diagnostics_criteria_param**
<a id="create_wireless_diagnostics_criteria_param"></a>
> XiqCreateWirelessDashboardCriteriaParamResponse create_wireless_diagnostics_criteria_param(xiq_create_wireless_dashboard_criteria_param_request)

Create Criteria for Wireless Diagnostics Dashboard

Creates the criteria for wireless diagnostics dashboard, including client health, device health, and usage and capacity issues.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_create_wireless_dashboard_criteria_param_request import XiqCreateWirelessDashboardCriteriaParamRequest
from extremecloudiq.model.xiq_create_wireless_dashboard_criteria_param_response import XiqCreateWirelessDashboardCriteriaParamResponse
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqCreateWirelessDashboardCriteriaParamRequest(
        device_health_criteria=XiqCreateWirelessDeviceHealthCriteria(
            cpu_utilization=3.14,
            memory_utilization=3.14,
            poe=3.14,
            wired_port_multicast=3.14,
            wired_port_broadcast=3.14,
        ),
        client_health_criteria=XiqCreateWirelessClientHealthCriteria(
            assoc_param_slow=3.14,
            assoc_unit_slow="assoc_unit_slow_example",
            auth_param_slow=3.14,
            auth_unit_slow="auth_unit_slow_example",
            dhcp_param_slow=3.14,
            dhcp_unit_slow="dhcp_unit_slow_example",
            roams_param_slow=3.14,
            roams_unit_slow="roams_unit_slow_example",
            rssi_param=3.14,
            rssi_unit="rssi_unit_example",
            snr_param=3.14,
            snr_unit="snr_unit_example",
            onboard_param=3.14,
            onboard_unit="onboard_unit_example",
        ),
        usage_capacity_criteria=XiqCreateWirelessUsageCapacityCriteria(
            channel_utilization=3.14,
            lnk_err=3.14,
            retries=3.14,
            pkt_loss=3.14,
            interference=3.14,
            noise=3.14,
            noise_unit="noise_unit_example",
        ),
    )
    try:
        # Create Criteria for Wireless Diagnostics Dashboard
        api_response = api_instance.create_wireless_diagnostics_criteria_param(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->create_wireless_diagnostics_criteria_param: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCreateWirelessDashboardCriteriaParamRequest**](../../models/XiqCreateWirelessDashboardCriteriaParamRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_wireless_diagnostics_criteria_param.ApiResponseFor200) | OK

#### create_wireless_diagnostics_criteria_param.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCreateWirelessDashboardCriteriaParamResponse**](../../models/XiqCreateWirelessDashboardCriteriaParamResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_site_with_issue_report**
<a id="download_site_with_issue_report"></a>
> [str] download_site_with_issue_report(id)

Download the  report

Download report of Metrics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the  report
        api_response = api_instance.download_site_with_issue_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->download_site_with_issue_report: %s\n" % e)
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
200 | [ApiResponseFor200](#download_site_with_issue_report.ApiResponseFor200) | OK

#### download_site_with_issue_report.ApiResponseFor200
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

# **export_to_csv3**
<a id="export_to_csv3"></a>
> XiqMetricReport export_to_csv3(xiq_dashboard_filter)

Export all dashboard data to CSV

Export all dashboard data to a CSV file.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Export all dashboard data to CSV
        api_response = api_instance.export_to_csv3(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->export_to_csv3: %s\n" % e)

    # example passing only optional values
    query_params = {
        'sortField': "ALERTS",
        'sortOrder': XiqSortOrder("ASC"),
        'keyword': "keyword_example",
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Export all dashboard data to CSV
        api_response = api_instance.export_to_csv3(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->export_to_csv3: %s\n" % e)
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
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
keyword | KeywordSchema | | optional
unassigned_devices | UnassignedDevicesSchema | | optional


# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ALERTS", "STATUS", "DEVICE_HEALTH", "CLIENT_HEALTH", "USAGE_CAPACITY", "SITE_NAME", ] 

# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_to_csv3.ApiResponseFor200) | OK

#### export_to_csv3.ApiResponseFor200
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

# **get_alert_diagnostics**
<a id="get_alert_diagnostics"></a>
> XiqAlertDashboard get_alert_diagnostics(xiq_dashboard_filter)

Alert statistics

Returns the count of different types of alerts (critical, warning, information, and total unacknowledged) based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_alert_dashboard import XiqAlertDashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Alert statistics
        api_response = api_instance.get_alert_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_alert_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Alert statistics
        api_response = api_instance.get_alert_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_alert_diagnostics: %s\n" % e)
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
unassigned_devices | UnassignedDevicesSchema | | optional


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_alert_diagnostics.ApiResponseFor200) | OK

#### get_alert_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAlertDashboard**](../../models/XiqAlertDashboard.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_diagnostics_device_types**
<a id="get_all_diagnostics_device_types"></a>
> [str] get_all_diagnostics_device_types()

Get all diagnostics device types

Returns all available diagnostics device types (unspecified, wired, wireless, or all).

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all diagnostics device types
        api_response = api_instance.get_all_diagnostics_device_types()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_all_diagnostics_device_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_diagnostics_device_types.ApiResponseFor200) | OK

#### get_all_diagnostics_device_types.ApiResponseFor200
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

# **get_asset_diagnostics**
<a id="get_asset_diagnostics"></a>
> XiqAssetDashboard get_asset_diagnostics(xiq_dashboard_filter)

Asset statistics

Returns the count of total devices, total offline devices, wired offline devices, and wireless offline devices based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_asset_dashboard import XiqAssetDashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Asset statistics
        api_response = api_instance.get_asset_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_asset_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Asset statistics
        api_response = api_instance.get_asset_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_asset_diagnostics: %s\n" % e)
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
unassigned_devices | UnassignedDevicesSchema | | optional


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_diagnostics.ApiResponseFor200) | OK

#### get_asset_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAssetDashboard**](../../models/XiqAssetDashboard.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_health_diagnostics**
<a id="get_client_health_diagnostics"></a>
> XiqClientHealthDashboard get_client_health_diagnostics(xiq_dashboard_filter)

Client health statistics

Returns the count of total clients, total unhealthy clients, wired unhealthy clients, and wireless unhealthy clients based on the provided filters.You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_client_health_dashboard import XiqClientHealthDashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Client health statistics
        api_response = api_instance.get_client_health_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_client_health_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Client health statistics
        api_response = api_instance.get_client_health_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_client_health_diagnostics: %s\n" % e)
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
unassigned_devices | UnassignedDevicesSchema | | optional


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_health_diagnostics.ApiResponseFor200) | OK

#### get_client_health_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthDashboard**](../../models/XiqClientHealthDashboard.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_health_diagnostics**
<a id="get_device_health_diagnostics"></a>
> XiqDeviceHealthDashboard get_device_health_diagnostics(xiq_dashboard_filter)

Device health statistics

Returns the count of total devices, total unhealthy devices, wired unhealthy devices, and wireless unhealthy devices based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_device_health_dashboard import XiqDeviceHealthDashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Device health statistics
        api_response = api_instance.get_device_health_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_device_health_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Device health statistics
        api_response = api_instance.get_device_health_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_device_health_diagnostics: %s\n" % e)
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
unassigned_devices | UnassignedDevicesSchema | | optional


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_health_diagnostics.ApiResponseFor200) | OK

#### get_device_health_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqDeviceHealthDashboard**](../../models/XiqDeviceHealthDashboard.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sites_with_issues_diagnostics**
<a id="get_sites_with_issues_diagnostics"></a>
> PagedXiqSiteDashboardResponse get_sites_with_issues_diagnostics(xiq_dashboard_filter)

Sites with issues

Returns the site names along with alerts, usage and capacity, assets, client health, and device health based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.paged_xiq_site_dashboard_response import PagedXiqSiteDashboardResponse
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Sites with issues
        api_response = api_instance.get_sites_with_issues_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_sites_with_issues_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'sortField': "ALERTS",
        'sortOrder': XiqSortOrder("ASC"),
        'keyword': "keyword_example",
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Sites with issues
        api_response = api_instance.get_sites_with_issues_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_sites_with_issues_diagnostics: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
keyword | KeywordSchema | | optional
unassigned_devices | UnassignedDevicesSchema | | optional


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

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ALERTS", "STATUS", "DEVICE_HEALTH", "CLIENT_HEALTH", "USAGE_CAPACITY", "SITE_NAME", ] 

# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sites_with_issues_diagnostics.ApiResponseFor200) | OK

#### get_sites_with_issues_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqSiteDashboardResponse**](../../models/PagedXiqSiteDashboardResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_usage_and_capacity_diagnostics**
<a id="get_usage_and_capacity_diagnostics"></a>
> XiqUsageAndCapacityDashboard get_usage_and_capacity_diagnostics(xiq_dashboard_filter)

Usage & capacity statistics

Returns the count of wired, wireless and total usage & capacity issues based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_usage_and_capacity_dashboard import XiqUsageAndCapacityDashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Usage & capacity statistics
        api_response = api_instance.get_usage_and_capacity_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_usage_and_capacity_diagnostics: %s\n" % e)

    # example passing only optional values
    query_params = {
        'unassigned_devices': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Usage & capacity statistics
        api_response = api_instance.get_usage_and_capacity_diagnostics(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_usage_and_capacity_diagnostics: %s\n" % e)
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
unassigned_devices | UnassignedDevicesSchema | | optional


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_usage_and_capacity_diagnostics.ApiResponseFor200) | OK

#### get_usage_and_capacity_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUsageAndCapacityDashboard**](../../models/XiqUsageAndCapacityDashboard.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_diagnostics_dashboard_criteria_param**
<a id="get_wireless_diagnostics_dashboard_criteria_param"></a>
> XiqWirelessDashboardCriteriaParamResponse get_wireless_diagnostics_dashboard_criteria_param()

Criteria for Wireless Diagnostics Dashboard

Returns the criteria for wireless diagnostics dashboard, including client health, device health, and usage and capacity issues.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_api
from extremecloudiq.model.xiq_wireless_dashboard_criteria_param_response import XiqWirelessDashboardCriteriaParamResponse
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
    api_instance = dashboard_api.DashboardApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Criteria for Wireless Diagnostics Dashboard
        api_response = api_instance.get_wireless_diagnostics_dashboard_criteria_param()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardApi->get_wireless_diagnostics_dashboard_criteria_param: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_diagnostics_dashboard_criteria_param.ApiResponseFor200) | OK

#### get_wireless_diagnostics_dashboard_criteria_param.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessDashboardCriteriaParamResponse**](../../models/XiqWirelessDashboardCriteriaParamResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

