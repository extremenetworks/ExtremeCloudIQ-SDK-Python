<a id="__pageTop"></a>
# extremecloudiq.apis.tags.application_api.ApplicationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_export_csv_file1**](#download_export_csv_file1) | **get** /applications/reports/{id} | Download the Export CSV file
[**export_application_usage_summary**](#export_application_usage_summary) | **post** /applications/usage/summary/export | Export the application usage summary
[**list_app_usage_summary_meta_data**](#list_app_usage_summary_meta_data) | **get** /applications/usage/summary/meta-data | Application usage summary meta data
[**list_application_top_clients_usage**](#list_application_top_clients_usage) | **get** /applications/{id}/clients/top{n} | List the TopN clients for a application
[**list_application_usage_summary**](#list_application_usage_summary) | **post** /applications/usage/summary | List the application usage summary
[**list_applications**](#list_applications) | **get** /applications | List the applications
[**list_top_applications_usage**](#list_top_applications_usage) | **get** /applications/top{n} | List the TopN applications

# **download_export_csv_file1**
<a id="download_export_csv_file1"></a>
> [str] download_export_csv_file1(id)

Download the Export CSV file

Download the Export CSV file for Application Usage Summary

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the Export CSV file
        api_response = api_instance.download_export_csv_file1(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->download_export_csv_file1: %s\n" % e)
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
200 | [ApiResponseFor200](#download_export_csv_file1.ApiResponseFor200) | OK

#### download_export_csv_file1.ApiResponseFor200
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

# **export_application_usage_summary**
<a id="export_application_usage_summary"></a>
> XiqAppUsageSummaryExport export_application_usage_summary(xiq_app_usage_summary_filter)

Export the application usage summary

Export of application usage summary by filter.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_app_usage_summary_export import XiqAppUsageSummaryExport
from extremecloudiq.model.xiq_app_usage_summary_sort_field import XiqAppUsageSummarySortField
from extremecloudiq.model.xiq_app_usage_summary_filter import XiqAppUsageSummaryFilter
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqAppUsageSummaryFilter(
        site_ids=[
            1
        ],
        application_name=[
            "application_name_example"
        ],
        category_name=[
            "category_name_example"
        ],
        number_filter=[
            XiqAppUsageSummaryNumberFilter(
                column_name="column_name_example",
                filter_type=XiqAppUsageSummaryNumberEnumFilter("GT"),
                value=3.14,
                min=3.14,
                max=3.14,
            )
        ],
    )
    try:
        # Export the application usage summary
        api_response = api_instance.export_application_usage_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->export_application_usage_summary: %s\n" % e)

    # example passing only optional values
    query_params = {
        'sortField': XiqAppUsageSummarySortField("USAGE"),
        'order': XiqSortOrder("ASC"),
        'name': "name_example",
        'async': False,
    }
    body = XiqAppUsageSummaryFilter(
        site_ids=[
            1
        ],
        application_name=[
            "application_name_example"
        ],
        category_name=[
            "category_name_example"
        ],
        number_filter=[
            XiqAppUsageSummaryNumberFilter(
                column_name="column_name_example",
                filter_type=XiqAppUsageSummaryNumberEnumFilter("GT"),
                value=3.14,
                min=3.14,
                max=3.14,
            )
        ],
    )
    try:
        # Export the application usage summary
        api_response = api_instance.export_application_usage_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->export_application_usage_summary: %s\n" % e)
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
[**XiqAppUsageSummaryFilter**](../../models/XiqAppUsageSummaryFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sortField | SortFieldSchema | | optional
order | OrderSchema | | optional
name | NameSchema | | optional
async | ModelAsyncSchema | | optional


# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAppUsageSummarySortField**](../../models/XiqAppUsageSummarySortField.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelAsyncSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_application_usage_summary.ApiResponseFor200) | OK

#### export_application_usage_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAppUsageSummaryExport**](../../models/XiqAppUsageSummaryExport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_app_usage_summary_meta_data**
<a id="list_app_usage_summary_meta_data"></a>
> XiqAppUsageSummaryMetaData list_app_usage_summary_meta_data()

Application usage summary meta data

List the application usage summary meta data

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.xiq_app_usage_summary_meta_data import XiqAppUsageSummaryMetaData
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
    api_instance = application_api.ApplicationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Application usage summary meta data
        api_response = api_instance.list_app_usage_summary_meta_data()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_app_usage_summary_meta_data: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_app_usage_summary_meta_data.ApiResponseFor200) | OK

#### list_app_usage_summary_meta_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAppUsageSummaryMetaData**](../../models/XiqAppUsageSummaryMetaData.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_application_top_clients_usage**
<a id="list_application_top_clients_usage"></a>
> [XiqApplicationTopClientsUsage] list_application_top_clients_usage(idnstart_timeend_time)

List the TopN clients for a application

List the TopN clients by usage for a specific application.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.xiq_application_top_clients_usage import XiqApplicationTopClientsUsage
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
        'n': 1,
    }
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        # List the TopN clients for a application
        api_response = api_instance.list_application_top_clients_usage(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_application_top_clients_usage: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 


# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
n | NSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# NSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_application_top_clients_usage.ApiResponseFor200) | OK

#### list_application_top_clients_usage.ApiResponseFor200
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
[**XiqApplicationTopClientsUsage**]({{complexTypePrefix}}XiqApplicationTopClientsUsage.md) | [**XiqApplicationTopClientsUsage**]({{complexTypePrefix}}XiqApplicationTopClientsUsage.md) | [**XiqApplicationTopClientsUsage**]({{complexTypePrefix}}XiqApplicationTopClientsUsage.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_application_usage_summary**
<a id="list_application_usage_summary"></a>
> PagedXiqAppUsageSummary list_application_usage_summary(xiq_app_usage_summary_filter)

List the application usage summary

List a page of application usage summary by filter.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.paged_xiq_app_usage_summary import PagedXiqAppUsageSummary
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_app_usage_summary_sort_field import XiqAppUsageSummarySortField
from extremecloudiq.model.xiq_app_usage_summary_filter import XiqAppUsageSummaryFilter
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqAppUsageSummaryFilter(
        site_ids=[
            1
        ],
        application_name=[
            "application_name_example"
        ],
        category_name=[
            "category_name_example"
        ],
        number_filter=[
            XiqAppUsageSummaryNumberFilter(
                column_name="column_name_example",
                filter_type=XiqAppUsageSummaryNumberEnumFilter("GT"),
                value=3.14,
                min=3.14,
                max=3.14,
            )
        ],
    )
    try:
        # List the application usage summary
        api_response = api_instance.list_application_usage_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_application_usage_summary: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'sortField': XiqAppUsageSummarySortField("USAGE"),
        'order': XiqSortOrder("ASC"),
        'name': "name_example",
        'async': False,
    }
    body = XiqAppUsageSummaryFilter(
        site_ids=[
            1
        ],
        application_name=[
            "application_name_example"
        ],
        category_name=[
            "category_name_example"
        ],
        number_filter=[
            XiqAppUsageSummaryNumberFilter(
                column_name="column_name_example",
                filter_type=XiqAppUsageSummaryNumberEnumFilter("GT"),
                value=3.14,
                min=3.14,
                max=3.14,
            )
        ],
    )
    try:
        # List the application usage summary
        api_response = api_instance.list_application_usage_summary(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_application_usage_summary: %s\n" % e)
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
[**XiqAppUsageSummaryFilter**](../../models/XiqAppUsageSummaryFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
sortField | SortFieldSchema | | optional
order | OrderSchema | | optional
name | NameSchema | | optional
async | ModelAsyncSchema | | optional


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
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAppUsageSummarySortField**](../../models/XiqAppUsageSummarySortField.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelAsyncSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_application_usage_summary.ApiResponseFor200) | OK

#### list_application_usage_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqAppUsageSummary**](../../models/PagedXiqAppUsageSummary.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_applications**
<a id="list_applications"></a>
> PagedXiqApplication list_applications()

List the applications

List a page of applications by filter.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_application_detection_type import XiqApplicationDetectionType
from extremecloudiq.model.xiq_application_sort_field import XiqApplicationSortField
from extremecloudiq.model.xiq_application_detection_protocol import XiqApplicationDetectionProtocol
from extremecloudiq.model.paged_xiq_application import PagedXiqApplication
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'name': "name_example",
        'detectionProtocol': XiqApplicationDetectionProtocol("HTTP"),
        'detectionType': XiqApplicationDetectionType("HOST_NAME"),
        'predefined': True,
        'sortField': XiqApplicationSortField("NAME"),
        'order': XiqSortOrder("ASC"),
    }
    try:
        # List the applications
        api_response = api_instance.list_applications(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_applications: %s\n" % e)
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
name | NameSchema | | optional
detectionProtocol | DetectionProtocolSchema | | optional
detectionType | DetectionTypeSchema | | optional
predefined | PredefinedSchema | | optional
sortField | SortFieldSchema | | optional
order | OrderSchema | | optional


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DetectionProtocolSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqApplicationDetectionProtocol**](../../models/XiqApplicationDetectionProtocol.md) |  | 


# DetectionTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqApplicationDetectionType**](../../models/XiqApplicationDetectionType.md) |  | 


# PredefinedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqApplicationSortField**](../../models/XiqApplicationSortField.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_applications.ApiResponseFor200) | OK

#### list_applications.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqApplication**](../../models/PagedXiqApplication.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_top_applications_usage**
<a id="list_top_applications_usage"></a>
> [XiqTopApplicationsUsage] list_top_applications_usage(nstart_timeend_time)

List the TopN applications

List the TopN applications by usage.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import application_api
from extremecloudiq.model.xiq_top_applications_usage import XiqTopApplicationsUsage
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
    api_instance = application_api.ApplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'n': 1,
    }
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        # List the TopN applications
        api_response = api_instance.list_top_applications_usage(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ApplicationApi->list_top_applications_usage: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 


# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
n | NSchema | | 

# NSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_top_applications_usage.ApiResponseFor200) | OK

#### list_top_applications_usage.ApiResponseFor200
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
[**XiqTopApplicationsUsage**]({{complexTypePrefix}}XiqTopApplicationsUsage.md) | [**XiqTopApplicationsUsage**]({{complexTypePrefix}}XiqTopApplicationsUsage.md) | [**XiqTopApplicationsUsage**]({{complexTypePrefix}}XiqTopApplicationsUsage.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

