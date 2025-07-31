<a id="__pageTop"></a>
# extremecloudiq.apis.tags.dashboard_wired_usage_and_capacity_api.DashboardWiredUsageAndCapacityApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wired_usage_capacity_congestion**](#get_wired_usage_capacity_congestion) | **post** /dashboard/wired/usage-capacity/wired-congestion | Wired devices congestion
[**get_wired_usage_capacity_grid**](#get_wired_usage_capacity_grid) | **post** /dashboard/wired/usage-capacity/grid | Wired Usage and Capacity grid
[**get_wired_usage_capacity_throughput**](#get_wired_usage_capacity_throughput) | **post** /dashboard/wired/usage-capacity/wired-throughput | Wired devices throughput
[**get_wired_usage_capacity_usage_utilization**](#get_wired_usage_capacity_usage_utilization) | **post** /dashboard/wired/usage-capacity/usage-utilization | Wired devices total utilized bandwidth

# **get_wired_usage_capacity_congestion**
<a id="get_wired_usage_capacity_congestion"></a>
> XiqWiredUsageCapacityCongestionResponse get_wired_usage_capacity_congestion(xiq_wired_usage_capacity_throughput_request)

Wired devices congestion

Returns the congestion for wired devices based on the provided filters. The result can be filtered by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wired_usage_and_capacity_api
from extremecloudiq.model.xiq_wired_usage_capacity_throughput_request import XiqWiredUsageCapacityThroughputRequest
from extremecloudiq.model.xiq_wired_usage_capacity_congestion_response import XiqWiredUsageCapacityCongestionResponse
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
    api_instance = dashboard_wired_usage_and_capacity_api.DashboardWiredUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqWiredUsageCapacityThroughputRequest(
        site_ids=[
            1
        ],
    )
    try:
        # Wired devices congestion
        api_response = api_instance.get_wired_usage_capacity_congestion(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWiredUsageAndCapacityApi->get_wired_usage_capacity_congestion: %s\n" % e)
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
[**XiqWiredUsageCapacityThroughputRequest**](../../models/XiqWiredUsageCapacityThroughputRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_usage_capacity_congestion.ApiResponseFor200) | OK

#### get_wired_usage_capacity_congestion.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredUsageCapacityCongestionResponse**](../../models/XiqWiredUsageCapacityCongestionResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_usage_capacity_grid**
<a id="get_wired_usage_capacity_grid"></a>
> PagedXiqWiredUsageCapacityGridResponse get_wired_usage_capacity_grid(xiq_wired_usage_capacity_grid_request)

Wired Usage and Capacity grid

Returns information related to usage and capacity for wired devices based on the provided filters. The result can be filtered by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wired_usage_and_capacity_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.paged_xiq_wired_usage_capacity_grid_response import PagedXiqWiredUsageCapacityGridResponse
from extremecloudiq.model.xiq_wired_usage_and_capacity_sort_field import XiqWiredUsageAndCapacitySortField
from extremecloudiq.model.xiq_wired_usage_capacity_grid_request import XiqWiredUsageCapacityGridRequest
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
    api_instance = dashboard_wired_usage_and_capacity_api.DashboardWiredUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqWiredUsageCapacityGridRequest(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        filter_field=[
            XiqWiredUsageAndCapacityFilterType("UNSPECIFIED")
        ],
    )
    try:
        # Wired Usage and Capacity grid
        api_response = api_instance.get_wired_usage_capacity_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWiredUsageAndCapacityApi->get_wired_usage_capacity_grid: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'keyword': "keyword_example",
        'sortField': XiqWiredUsageAndCapacitySortField("UNSPECIFIED"),
        'sortOrder': XiqSortOrder("ASC"),
    }
    body = XiqWiredUsageCapacityGridRequest(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        filter_field=[
            XiqWiredUsageAndCapacityFilterType("UNSPECIFIED")
        ],
    )
    try:
        # Wired Usage and Capacity grid
        api_response = api_instance.get_wired_usage_capacity_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWiredUsageAndCapacityApi->get_wired_usage_capacity_grid: %s\n" % e)
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
[**XiqWiredUsageCapacityGridRequest**](../../models/XiqWiredUsageCapacityGridRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
keyword | KeywordSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional


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
[**XiqWiredUsageAndCapacitySortField**](../../models/XiqWiredUsageAndCapacitySortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_usage_capacity_grid.ApiResponseFor200) | OK

#### get_wired_usage_capacity_grid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqWiredUsageCapacityGridResponse**](../../models/PagedXiqWiredUsageCapacityGridResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_usage_capacity_throughput**
<a id="get_wired_usage_capacity_throughput"></a>
> XiqWiredUsageCapacityThroughputResponse get_wired_usage_capacity_throughput(xiq_wired_usage_capacity_throughput_request)

Wired devices throughput

Returns the throughput for wired devices based on the provided filters. The result can be filtered by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wired_usage_and_capacity_api
from extremecloudiq.model.xiq_wired_usage_capacity_throughput_request import XiqWiredUsageCapacityThroughputRequest
from extremecloudiq.model.xiq_wired_usage_capacity_throughput_response import XiqWiredUsageCapacityThroughputResponse
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
    api_instance = dashboard_wired_usage_and_capacity_api.DashboardWiredUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqWiredUsageCapacityThroughputRequest(
        site_ids=[
            1
        ],
    )
    try:
        # Wired devices throughput
        api_response = api_instance.get_wired_usage_capacity_throughput(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWiredUsageAndCapacityApi->get_wired_usage_capacity_throughput: %s\n" % e)
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
[**XiqWiredUsageCapacityThroughputRequest**](../../models/XiqWiredUsageCapacityThroughputRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_usage_capacity_throughput.ApiResponseFor200) | OK

#### get_wired_usage_capacity_throughput.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredUsageCapacityThroughputResponse**](../../models/XiqWiredUsageCapacityThroughputResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_usage_capacity_usage_utilization**
<a id="get_wired_usage_capacity_usage_utilization"></a>
> XiqWiredUsageCapacityUsageUtilizationResponse get_wired_usage_capacity_usage_utilization(xiq_wired_usage_capacity_usage_utilization_request)

Wired devices total utilized bandwidth

Returns total bandwidth utilized by wired devices based on the provided filters. The result can be filtered by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wired_usage_and_capacity_api
from extremecloudiq.model.xiq_wired_usage_capacity_usage_utilization_response import XiqWiredUsageCapacityUsageUtilizationResponse
from extremecloudiq.model.xiq_wired_usage_capacity_usage_utilization_request import XiqWiredUsageCapacityUsageUtilizationRequest
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
    api_instance = dashboard_wired_usage_and_capacity_api.DashboardWiredUsageAndCapacityApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqWiredUsageCapacityUsageUtilizationRequest(
        site_ids=[
            1
        ],
    )
    try:
        # Wired devices total utilized bandwidth
        api_response = api_instance.get_wired_usage_capacity_usage_utilization(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWiredUsageAndCapacityApi->get_wired_usage_capacity_usage_utilization: %s\n" % e)
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
[**XiqWiredUsageCapacityUsageUtilizationRequest**](../../models/XiqWiredUsageCapacityUsageUtilizationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_usage_capacity_usage_utilization.ApiResponseFor200) | OK

#### get_wired_usage_capacity_usage_utilization.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredUsageCapacityUsageUtilizationResponse**](../../models/XiqWiredUsageCapacityUsageUtilizationResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

