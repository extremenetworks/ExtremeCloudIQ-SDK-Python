<a id="__pageTop"></a>
# extremecloudiq.apis.tags.dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_usage_and_capacity_report**](#download_usage_and_capacity_report) | **get** /dashboard/wireless/usage-capacity/reports/{id} | Download the  report
[**export_to_csv**](#export_to_csv) | **post** /dashboard/wireless/usage-capacity/export | Export all Wireless Usage Capacity Data to CSV
[**get_count_excessive_retries**](#get_count_excessive_retries) | **post** /dashboard/wireless/usage-capacity/excessive-retries | Count of APs with excessive retries
[**get_packet_loss_excessive_response**](#get_packet_loss_excessive_response) | **post** /dashboard/wireless/usage-capacity/excessive-packet-loss | Count of APs with excessive packet loss
[**get_usage_capacity_grid**](#get_usage_capacity_grid) | **post** /dashboard/wireless/usage-capacity/grid | Wireless usage &amp; capacity grid
[**get_wireless_usage_capacity_excessive_utilization**](#get_wireless_usage_capacity_excessive_utilization) | **post** /dashboard/wireless/usage-capacity/excessive-utilization | Count of APs with excessive utilization

# **download_usage_and_capacity_report**
<a id="download_usage_and_capacity_report"></a>
> [str] download_usage_and_capacity_report(id)

Download the  report

Download report of Metrics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the  report
        api_response = api_instance.download_usage_and_capacity_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->download_usage_and_capacity_report: %s\n" % e)
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
200 | [ApiResponseFor200](#download_usage_and_capacity_report.ApiResponseFor200) | OK

#### download_usage_and_capacity_report.ApiResponseFor200
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

# **export_to_csv**
<a id="export_to_csv"></a>
> XiqMetricReport export_to_csv(xiq_usage_and_capacity_grid_filter)

Export all Wireless Usage Capacity Data to CSV

Export all Wireless Usage Capacity  Data to a CSV file.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_usage_and_capacity_grid_filter import XiqUsageAndCapacityGridFilter
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqUsageAndCapacityGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        building_ids=[
            1
        ],
        buildings=[
            "buildings_example"
        ],
        floors=[
            "floors_example"
        ],
        has_usage_capacity_issues=True,
        number_filters=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        has_packet_loss_issues=True,
        has_retries_issues=True,
    )
    try:
        # Export all Wireless Usage Capacity Data to CSV
        api_response = api_instance.export_to_csv(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->export_to_csv: %s\n" % e)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
        'sortField': "HOSTNAME",
        'sortOrder': XiqSortOrder("ASC"),
        'unassigned_devices': False,
    }
    body = XiqUsageAndCapacityGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        building_ids=[
            1
        ],
        buildings=[
            "buildings_example"
        ],
        floors=[
            "floors_example"
        ],
        has_usage_capacity_issues=True,
        number_filters=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        has_packet_loss_issues=True,
        has_retries_issues=True,
    )
    try:
        # Export all Wireless Usage Capacity Data to CSV
        api_response = api_instance.export_to_csv(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->export_to_csv: %s\n" % e)
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
[**XiqUsageAndCapacityGridFilter**](../../models/XiqUsageAndCapacityGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
unassigned_devices | UnassignedDevicesSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["HOSTNAME", "SITE", "RADIO_2DOT4G_UTILIZATION_SCORE", "RADIO_5G_UTILIZATION_SCORE", "RADIO_6G_UTILIZATION_SCORE", "WIFI0_RETRY_SCORE", "WIFI1_RETRY_SCORE", "WIFI2_RETRY_SCORE", "WIFI0_PACKET_LOSS", "WIFI1_PACKET_LOSS", "WIFI2_PACKET_LOSS", "ETH0_UNICAST_SCORE", "ETH0_BROADCAST_SCORE", "ETH0_MULTICAST_SCORE", "ETH1_UNICAST_SCORE", "ETH1_BROADCAST_SCORE", "ETH1_MULTICAST_SCORE", "WIFI0_INTERFERENCE_SCORE", "WIFI1_INTERFERENCE_SCORE", "WIFI2_INTERFERENCE_SCORE", "WIFI0_NOISE", "WIFI1_NOISE", "WIFI2_NOISE", "TOTAL_ETH0_SCORE", "TOTAL_ETH1_SCORE", ] 

# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_to_csv.ApiResponseFor200) | OK

#### export_to_csv.ApiResponseFor200
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

# **get_count_excessive_retries**
<a id="get_count_excessive_retries"></a>
> XiqCountApWithExcessiveRetriesResponse get_count_excessive_retries(xiq_dashboard_filter)

Count of APs with excessive retries

Returns the count of wireless devices having excessive retries based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_count_ap_with_excessive_retries_response import XiqCountApWithExcessiveRetriesResponse
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Count of APs with excessive retries
        api_response = api_instance.get_count_excessive_retries(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_count_excessive_retries: %s\n" % e)

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
        # Count of APs with excessive retries
        api_response = api_instance.get_count_excessive_retries(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_count_excessive_retries: %s\n" % e)
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
200 | [ApiResponseFor200](#get_count_excessive_retries.ApiResponseFor200) | OK

#### get_count_excessive_retries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCountApWithExcessiveRetriesResponse**](../../models/XiqCountApWithExcessiveRetriesResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_packet_loss_excessive_response**
<a id="get_packet_loss_excessive_response"></a>
> XiqCountApWithPacketLossExcessiveResponse get_packet_loss_excessive_response(xiq_dashboard_filter)

Count of APs with excessive packet loss

Returns the count of wireless devices having excessive packet loss based on the provided filters. You can filter the results by sites

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
from extremecloudiq.model.xiq_count_ap_with_packet_loss_excessive_response import XiqCountApWithPacketLossExcessiveResponse
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Count of APs with excessive packet loss
        api_response = api_instance.get_packet_loss_excessive_response(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_packet_loss_excessive_response: %s\n" % e)

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
        # Count of APs with excessive packet loss
        api_response = api_instance.get_packet_loss_excessive_response(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_packet_loss_excessive_response: %s\n" % e)
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
200 | [ApiResponseFor200](#get_packet_loss_excessive_response.ApiResponseFor200) | OK

#### get_packet_loss_excessive_response.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCountApWithPacketLossExcessiveResponse**](../../models/XiqCountApWithPacketLossExcessiveResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_usage_capacity_grid**
<a id="get_usage_capacity_grid"></a>
> PagedXiqUsageCapacityGridResponse get_usage_capacity_grid(xiq_usage_and_capacity_grid_filter)

Wireless usage & capacity grid

Returns the usage & capacity grid of wireless devices based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
from extremecloudiq.model.paged_xiq_usage_capacity_grid_response import PagedXiqUsageCapacityGridResponse
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_usage_and_capacity_grid_filter import XiqUsageAndCapacityGridFilter
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqUsageAndCapacityGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        building_ids=[
            1
        ],
        buildings=[
            "buildings_example"
        ],
        floors=[
            "floors_example"
        ],
        has_usage_capacity_issues=True,
        number_filters=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        has_packet_loss_issues=True,
        has_retries_issues=True,
    )
    try:
        # Wireless usage & capacity grid
        api_response = api_instance.get_usage_capacity_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_usage_capacity_grid: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'keyword': "keyword_example",
        'sortField': "HOSTNAME",
        'sortOrder': XiqSortOrder("ASC"),
        'unassigned_devices': False,
    }
    body = XiqUsageAndCapacityGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        building_ids=[
            1
        ],
        buildings=[
            "buildings_example"
        ],
        floors=[
            "floors_example"
        ],
        has_usage_capacity_issues=True,
        number_filters=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        has_packet_loss_issues=True,
        has_retries_issues=True,
    )
    try:
        # Wireless usage & capacity grid
        api_response = api_instance.get_usage_capacity_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_usage_capacity_grid: %s\n" % e)
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
[**XiqUsageAndCapacityGridFilter**](../../models/XiqUsageAndCapacityGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
keyword | KeywordSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
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

# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["HOSTNAME", "SITE", "RADIO_2DOT4G_UTILIZATION_SCORE", "RADIO_5G_UTILIZATION_SCORE", "RADIO_6G_UTILIZATION_SCORE", "WIFI0_RETRY_SCORE", "WIFI1_RETRY_SCORE", "WIFI2_RETRY_SCORE", "WIFI0_PACKET_LOSS", "WIFI1_PACKET_LOSS", "WIFI2_PACKET_LOSS", "ETH0_UNICAST_SCORE", "ETH0_BROADCAST_SCORE", "ETH0_MULTICAST_SCORE", "ETH1_UNICAST_SCORE", "ETH1_BROADCAST_SCORE", "ETH1_MULTICAST_SCORE", "WIFI0_INTERFERENCE_SCORE", "WIFI1_INTERFERENCE_SCORE", "WIFI2_INTERFERENCE_SCORE", "WIFI0_NOISE", "WIFI1_NOISE", "WIFI2_NOISE", "TOTAL_ETH0_SCORE", "TOTAL_ETH1_SCORE", ] 

# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# UnassignedDevicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_usage_capacity_grid.ApiResponseFor200) | OK

#### get_usage_capacity_grid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqUsageCapacityGridResponse**](../../models/PagedXiqUsageCapacityGridResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_usage_capacity_excessive_utilization**
<a id="get_wireless_usage_capacity_excessive_utilization"></a>
> XiqWirelessUsageCapacityExcessiveUtilization get_wireless_usage_capacity_excessive_utilization(xiq_dashboard_filter)

Count of APs with excessive utilization

Returns the count of wireless devices having excessive channel utilization based on the provided filters. You can filter the results by sites, device types, and a specific timestamp.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_usage_and_capacity_api
from extremecloudiq.model.xiq_wireless_usage_capacity_excessive_utilization import XiqWirelessUsageCapacityExcessiveUtilization
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
    api_instance = dashboard_wireless_usage_and_capacity_api.DashboardWirelessUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Count of APs with excessive utilization
        api_response = api_instance.get_wireless_usage_capacity_excessive_utilization(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_wireless_usage_capacity_excessive_utilization: %s\n" % e)

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
        # Count of APs with excessive utilization
        api_response = api_instance.get_wireless_usage_capacity_excessive_utilization(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessUsageAndCapacityApi->get_wireless_usage_capacity_excessive_utilization: %s\n" % e)
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
200 | [ApiResponseFor200](#get_wireless_usage_capacity_excessive_utilization.ApiResponseFor200) | OK

#### get_wireless_usage_capacity_excessive_utilization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessUsageCapacityExcessiveUtilization**](../../models/XiqWirelessUsageCapacityExcessiveUtilization.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

