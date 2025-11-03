<a id="__pageTop"></a>
# extremecloudiq.apis.tags.dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_client_health_report**](#download_client_health_report) | **get** /dashboard/wireless/client-health/reports/{id} | Download the  report
[**export_to_csv3**](#export_to_csv3) | **post** /dashboard/wireless/client-health/export | Export all Client Health Data to CSV
[**get_client_association_issues**](#get_client_association_issues) | **post** /dashboard/wireless/client-health/issue/association | Association issue for wireless client
[**get_client_auth_issues**](#get_client_auth_issues) | **post** /dashboard/wireless/client-health/issue/authentication | Authentication issue for wireless client
[**get_client_frequency_distribution**](#get_client_frequency_distribution) | **post** /dashboard/wireless/client-health/frequency-distribution | Wireless clients count with frequency distribution
[**get_client_health_connectivity_issues**](#get_client_health_connectivity_issues) | **post** /dashboard/wireless/client-health/connectivity-issues | Wireless clients count with connectivity issues
[**get_client_health_grid**](#get_client_health_grid) | **post** /dashboard/wireless/client-health/grid | Wireless client health grid
[**get_client_health_grid_filter_metadata**](#get_client_health_grid_filter_metadata) | **post** /dashboard/wireless/client-health/filter-metadata | 
[**get_client_health_roaming_issues**](#get_client_health_roaming_issues) | **post** /dashboard/wireless/client-health/roaming-issues | Wireless clients count with roaming issues
[**get_client_ip_address_issues**](#get_client_ip_address_issues) | **post** /dashboard/wireless/client-health/issue/ipaddress | Ip Address issue for Wireless client
[**get_client_roaming_issues**](#get_client_roaming_issues) | **post** /dashboard/wireless/client-health/issue/roaming | Roaming issue for wireless client

# **download_client_health_report**
<a id="download_client_health_report"></a>
> [str] download_client_health_report(id)

Download the  report

Download report of Metrics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the  report
        api_response = api_instance.download_client_health_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->download_client_health_report: %s\n" % e)
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
200 | [ApiResponseFor200](#download_client_health_report.ApiResponseFor200) | OK

#### download_client_health_report.ApiResponseFor200
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
> XiqMetricReport export_to_csv3(xiq_client_grid_filter)

Export all Client Health Data to CSV

Export all Client Health Data to a CSV file.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_client_connection_status import XiqClientConnectionStatus
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_client_health_sort_field import XiqClientHealthSortField
from extremecloudiq.model.xiq_metric_report import XiqMetricReport
from extremecloudiq.model.xiq_client_grid_filter import XiqClientGridFilter
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqClientGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        alias=[
            "alias_example"
        ],
        auth_methods=[
            "auth_methods_example"
        ],
        encryption_methods=[
            "encryption_methods_example"
        ],
        operating_systems=[
            "operating_systems_example"
        ],
        ssids=[
            "ssids_example"
        ],
        user_profiles=[
            "user_profiles_example"
        ],
        frequency=[
            "frequency_example"
        ],
        category_assignments=[
            "category_assignments_example"
        ],
        has_authentication_issues=True,
        has_association_issues=True,
        has_ip_address_issues=True,
        has_roaming_issues=True,
        is_client_unhealthy=True,
    )
    try:
        # Export all Client Health Data to CSV
        api_response = api_instance.export_to_csv3(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->export_to_csv3: %s\n" % e)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
        'connectionStatus': XiqClientConnectionStatus("CONNECTED"),
        'sortField': XiqClientHealthSortField("OPERATING_SYSTEM"),
        'sortOrder': XiqSortOrder("ASC"),
        'includeUnassigned': False,
    }
    body = XiqClientGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        alias=[
            "alias_example"
        ],
        auth_methods=[
            "auth_methods_example"
        ],
        encryption_methods=[
            "encryption_methods_example"
        ],
        operating_systems=[
            "operating_systems_example"
        ],
        ssids=[
            "ssids_example"
        ],
        user_profiles=[
            "user_profiles_example"
        ],
        frequency=[
            "frequency_example"
        ],
        category_assignments=[
            "category_assignments_example"
        ],
        has_authentication_issues=True,
        has_association_issues=True,
        has_ip_address_issues=True,
        has_roaming_issues=True,
        is_client_unhealthy=True,
    )
    try:
        # Export all Client Health Data to CSV
        api_response = api_instance.export_to_csv3(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->export_to_csv3: %s\n" % e)
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
[**XiqClientGridFilter**](../../models/XiqClientGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional
connectionStatus | ConnectionStatusSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
includeUnassigned | IncludeUnassignedSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectionStatusSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientConnectionStatus**](../../models/XiqClientConnectionStatus.md) |  | 


# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthSortField**](../../models/XiqClientHealthSortField.md) |  | 


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

# **get_client_association_issues**
<a id="get_client_association_issues"></a>
> [XiqIssueClientAssociation] get_client_association_issues(mac_addressxiq_dashboard_filter)

Association issue for wireless client

Returns association issue list for wireless client based on the provided filters. You can filter the results by sites and macAddress.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_issue_client_association import XiqIssueClientAssociation
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'macAddress': "macAddress_example",
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Association issue for wireless client
        api_response = api_instance.get_client_association_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_association_issues: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'macAddress': "macAddress_example",
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Association issue for wireless client
        api_response = api_instance.get_client_association_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_association_issues: %s\n" % e)
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
macAddress | MacAddressSchema | | 
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

# MacAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_association_issues.ApiResponseFor200) | OK

#### get_client_association_issues.ApiResponseFor200
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
[**XiqIssueClientAssociation**]({{complexTypePrefix}}XiqIssueClientAssociation.md) | [**XiqIssueClientAssociation**]({{complexTypePrefix}}XiqIssueClientAssociation.md) | [**XiqIssueClientAssociation**]({{complexTypePrefix}}XiqIssueClientAssociation.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_auth_issues**
<a id="get_client_auth_issues"></a>
> [XiqIssueClientAuth] get_client_auth_issues(mac_addressxiq_dashboard_filter)

Authentication issue for wireless client

Returns authentication issue list for wireless client based on the provided filters. You can filter the results by sites and mac address.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_issue_client_auth import XiqIssueClientAuth
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'macAddress': "macAddress_example",
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Authentication issue for wireless client
        api_response = api_instance.get_client_auth_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_auth_issues: %s\n" % e)

    # example passing only optional values
    query_params = {
        'macAddress': "macAddress_example",
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Authentication issue for wireless client
        api_response = api_instance.get_client_auth_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_auth_issues: %s\n" % e)
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
macAddress | MacAddressSchema | | 
includeUnassigned | IncludeUnassignedSchema | | optional


# MacAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_auth_issues.ApiResponseFor200) | OK

#### get_client_auth_issues.ApiResponseFor200
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
[**XiqIssueClientAuth**]({{complexTypePrefix}}XiqIssueClientAuth.md) | [**XiqIssueClientAuth**]({{complexTypePrefix}}XiqIssueClientAuth.md) | [**XiqIssueClientAuth**]({{complexTypePrefix}}XiqIssueClientAuth.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_frequency_distribution**
<a id="get_client_frequency_distribution"></a>
> XiqClientHealthFrequencyDistribution get_client_frequency_distribution(xiq_dashboard_filter)

Wireless clients count with frequency distribution

Returns the wireless clients with different frequency distribution based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_client_health_frequency_distribution import XiqClientHealthFrequencyDistribution
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Wireless clients count with frequency distribution
        api_response = api_instance.get_client_frequency_distribution(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_frequency_distribution: %s\n" % e)

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
        # Wireless clients count with frequency distribution
        api_response = api_instance.get_client_frequency_distribution(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_frequency_distribution: %s\n" % e)
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
200 | [ApiResponseFor200](#get_client_frequency_distribution.ApiResponseFor200) | OK

#### get_client_frequency_distribution.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthFrequencyDistribution**](../../models/XiqClientHealthFrequencyDistribution.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_health_connectivity_issues**
<a id="get_client_health_connectivity_issues"></a>
> XiqClientHealthConnectivityIssues get_client_health_connectivity_issues(xiq_dashboard_filter)

Wireless clients count with connectivity issues

Returns the wireless clients with connectivity issues based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_client_health_connectivity_issues import XiqClientHealthConnectivityIssues
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Wireless clients count with connectivity issues
        api_response = api_instance.get_client_health_connectivity_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_connectivity_issues: %s\n" % e)

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
        # Wireless clients count with connectivity issues
        api_response = api_instance.get_client_health_connectivity_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_connectivity_issues: %s\n" % e)
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
200 | [ApiResponseFor200](#get_client_health_connectivity_issues.ApiResponseFor200) | OK

#### get_client_health_connectivity_issues.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthConnectivityIssues**](../../models/XiqClientHealthConnectivityIssues.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_health_grid**
<a id="get_client_health_grid"></a>
> PagedXiqClientHealthGridResponse get_client_health_grid(xiq_client_grid_filter)

Wireless client health grid

Returns the client health grid of wireless devices based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_client_connection_status import XiqClientConnectionStatus
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_client_health_sort_field import XiqClientHealthSortField
from extremecloudiq.model.paged_xiq_client_health_grid_response import PagedXiqClientHealthGridResponse
from extremecloudiq.model.xiq_client_grid_filter import XiqClientGridFilter
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqClientGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        alias=[
            "alias_example"
        ],
        auth_methods=[
            "auth_methods_example"
        ],
        encryption_methods=[
            "encryption_methods_example"
        ],
        operating_systems=[
            "operating_systems_example"
        ],
        ssids=[
            "ssids_example"
        ],
        user_profiles=[
            "user_profiles_example"
        ],
        frequency=[
            "frequency_example"
        ],
        category_assignments=[
            "category_assignments_example"
        ],
        has_authentication_issues=True,
        has_association_issues=True,
        has_ip_address_issues=True,
        has_roaming_issues=True,
        is_client_unhealthy=True,
    )
    try:
        # Wireless client health grid
        api_response = api_instance.get_client_health_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_grid: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'keyword': "keyword_example",
        'connectionStatus': XiqClientConnectionStatus("CONNECTED"),
        'sortField': XiqClientHealthSortField("OPERATING_SYSTEM"),
        'sortOrder': XiqSortOrder("ASC"),
        'includeUnassigned': False,
    }
    body = XiqClientGridFilter(
        site_ids=[
            1
        ],
        device_ids=[
            1
        ],
        number_filter=[
            XiqNumberFilter(
                column_name="column_name_example",
                filter_type=XiqFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        alias=[
            "alias_example"
        ],
        auth_methods=[
            "auth_methods_example"
        ],
        encryption_methods=[
            "encryption_methods_example"
        ],
        operating_systems=[
            "operating_systems_example"
        ],
        ssids=[
            "ssids_example"
        ],
        user_profiles=[
            "user_profiles_example"
        ],
        frequency=[
            "frequency_example"
        ],
        category_assignments=[
            "category_assignments_example"
        ],
        has_authentication_issues=True,
        has_association_issues=True,
        has_ip_address_issues=True,
        has_roaming_issues=True,
        is_client_unhealthy=True,
    )
    try:
        # Wireless client health grid
        api_response = api_instance.get_client_health_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_grid: %s\n" % e)
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
[**XiqClientGridFilter**](../../models/XiqClientGridFilter.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
keyword | KeywordSchema | | optional
connectionStatus | ConnectionStatusSchema | | optional
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

# ConnectionStatusSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientConnectionStatus**](../../models/XiqClientConnectionStatus.md) |  | 


# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthSortField**](../../models/XiqClientHealthSortField.md) |  | 


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
200 | [ApiResponseFor200](#get_client_health_grid.ApiResponseFor200) | OK

#### get_client_health_grid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqClientHealthGridResponse**](../../models/PagedXiqClientHealthGridResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_health_grid_filter_metadata**
<a id="get_client_health_grid_filter_metadata"></a>
> XiqWirelessClientHealthGridFilterMetadata get_client_health_grid_filter_metadata(xiq_dashboard_filter)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_wireless_client_health_grid_filter_metadata import XiqWirelessClientHealthGridFilterMetadata
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        api_response = api_instance.get_client_health_grid_filter_metadata(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_grid_filter_metadata: %s\n" % e)

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
        api_response = api_instance.get_client_health_grid_filter_metadata(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_grid_filter_metadata: %s\n" % e)
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
200 | [ApiResponseFor200](#get_client_health_grid_filter_metadata.ApiResponseFor200) | OK

#### get_client_health_grid_filter_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessClientHealthGridFilterMetadata**](../../models/XiqWirelessClientHealthGridFilterMetadata.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_health_roaming_issues**
<a id="get_client_health_roaming_issues"></a>
> XiqClientHealthRoamingIssues get_client_health_roaming_issues(xiq_dashboard_filter)

Wireless clients count with roaming issues

Returns the wireless clients with roaming issues based on the provided filters. You can filter the results by sites.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_client_health_roaming_issues import XiqClientHealthRoamingIssues
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Wireless clients count with roaming issues
        api_response = api_instance.get_client_health_roaming_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_roaming_issues: %s\n" % e)

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
        # Wireless clients count with roaming issues
        api_response = api_instance.get_client_health_roaming_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_health_roaming_issues: %s\n" % e)
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
200 | [ApiResponseFor200](#get_client_health_roaming_issues.ApiResponseFor200) | OK

#### get_client_health_roaming_issues.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientHealthRoamingIssues**](../../models/XiqClientHealthRoamingIssues.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_ip_address_issues**
<a id="get_client_ip_address_issues"></a>
> [XiqIssueClientIpAddress] get_client_ip_address_issues(mac_addressxiq_dashboard_filter)

Ip Address issue for Wireless client

Returns ip address issue for wireless client based on the provided filters. You can filter the results by sites and mac address.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_issue_client_ip_address import XiqIssueClientIpAddress
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'macAddress': "macAddress_example",
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Ip Address issue for Wireless client
        api_response = api_instance.get_client_ip_address_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_ip_address_issues: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'macAddress': "macAddress_example",
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Ip Address issue for Wireless client
        api_response = api_instance.get_client_ip_address_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_ip_address_issues: %s\n" % e)
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
macAddress | MacAddressSchema | | 
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

# MacAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_ip_address_issues.ApiResponseFor200) | OK

#### get_client_ip_address_issues.ApiResponseFor200
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
[**XiqIssueClientIpAddress**]({{complexTypePrefix}}XiqIssueClientIpAddress.md) | [**XiqIssueClientIpAddress**]({{complexTypePrefix}}XiqIssueClientIpAddress.md) | [**XiqIssueClientIpAddress**]({{complexTypePrefix}}XiqIssueClientIpAddress.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_roaming_issues**
<a id="get_client_roaming_issues"></a>
> [XiqIssueClientRoaming] get_client_roaming_issues(mac_addressxiq_dashboard_filter)

Roaming issue for wireless client

Returns roaming issue for wireless client based on the provided filters. You can filter the results by sites and mac address.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import dashboard_wireless_client_health_api
from extremecloudiq.model.xiq_dashboard_filter import XiqDashboardFilter
from extremecloudiq.model.xiq_issue_client_roaming import XiqIssueClientRoaming
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
    api_instance = dashboard_wireless_client_health_api.DashboardWirelessClientHealthApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'macAddress': "macAddress_example",
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Roaming issue for wireless client
        api_response = api_instance.get_client_roaming_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_roaming_issues: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'macAddress': "macAddress_example",
        'includeUnassigned': False,
    }
    body = XiqDashboardFilter(
        site_ids=[
            1
        ],
    )
    try:
        # Roaming issue for wireless client
        api_response = api_instance.get_client_roaming_issues(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling DashboardWirelessClientHealthApi->get_client_roaming_issues: %s\n" % e)
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
macAddress | MacAddressSchema | | 
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

# MacAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeUnassignedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_roaming_issues.ApiResponseFor200) | OK

#### get_client_roaming_issues.ApiResponseFor200
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
[**XiqIssueClientRoaming**]({{complexTypePrefix}}XiqIssueClientRoaming.md) | [**XiqIssueClientRoaming**]({{complexTypePrefix}}XiqIssueClientRoaming.md) | [**XiqIssueClientRoaming**]({{complexTypePrefix}}XiqIssueClientRoaming.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

