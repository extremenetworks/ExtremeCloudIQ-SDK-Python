<a id="__pageTop"></a>
# extremecloudiq.apis.tags.user_api.UserApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](#create_user) | **post** /users | Create new user
[**delete_user**](#delete_user) | **delete** /users/{id} | Delete user by ID
[**download_users_report**](#download_users_report) | **get** /users/reports/{id} | Download the  report
[**export_to_csv**](#export_to_csv) | **post** /users/grid_export | Export the Users grid data
[**get_current_user**](#get_current_user) | **get** /users/me | Get current user info
[**get_external_user**](#get_external_user) | **get** /users/external/{id} | Get external access info
[**get_user**](#get_user) | **get** /users/{id} | Get user info by ID
[**get_user_data_usage**](#get_user_data_usage) | **post** /users/data_usage | Get user data usage
[**get_user_type_distribution**](#get_user_type_distribution) | **post** /users/type_distribution | Get user type distribution
[**grant_external_user**](#grant_external_user) | **post** /users/external | Grant external access
[**list_external_users**](#list_external_users) | **get** /users/external | List external access users
[**list_user_grid_filter_metadata**](#list_user_grid_filter_metadata) | **post** /users/filter_metadata | List user grid filter metadata
[**list_users**](#list_users) | **get** /users | List all users
[**list_users_grid**](#list_users_grid) | **post** /users/grid | List Users
[**revoke_external_user**](#revoke_external_user) | **delete** /users/external/{id} | Revoke external access
[**update_external_user**](#update_external_user) | **patch** /users/external/{id} | Update external access info
[**update_user**](#update_user) | **patch** /users/{id} | Update user info

# **create_user**
<a id="create_user"></a>
> XiqUser create_user(xiq_create_user_request)

Create new user

Create a new user to access.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_create_user_request import XiqCreateUserRequest
from extremecloudiq.model.xiq_user import XiqUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqCreateUserRequest(
        login_name="login_name_example",
        display_name="display_name_example",
        idle_timeout=1,
        user_role=XiqUserRole("ADMINISTRATOR"),
        location_ids=[
            1
        ],
        access_scope=1,
        viq_access_control=1,
    )
    try:
        # Create new user
        api_response = api_instance.create_user(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
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
[**XiqCreateUserRequest**](../../models/XiqCreateUserRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_user.ApiResponseFor201) | Created

#### create_user.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUser**](../../models/XiqUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user**
<a id="delete_user"></a>
> delete_user(id)

Delete user by ID

Delete a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Delete user by ID
        api_response = api_instance.delete_user(
            path_params=path_params,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_user.ApiResponseFor200) | OK

#### delete_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_users_report**
<a id="download_users_report"></a>
> [str] download_users_report(id)

Download the  report

Download report of Users

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the  report
        api_response = api_instance.download_users_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->download_users_report: %s\n" % e)
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
200 | [ApiResponseFor200](#download_users_report.ApiResponseFor200) | OK

#### download_users_report.ApiResponseFor200
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
> RmMetricReport export_to_csv(start_timeend_timerm_user_grid_request)

Export the Users grid data

Export the Users grid data as a CSV file.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.rm_sort_order import RmSortOrder
from extremecloudiq.model.rm_metric_report import RmMetricReport
from extremecloudiq.model.rm_user_grid_sort_field import RmUserGridSortField
from extremecloudiq.model.rm_user_grid_request import RmUserGridRequest
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserGridRequest(
        user_name=[
            "user_name_example"
        ],
        source=[
            "source_example"
        ],
        site_ids=[
            1
        ],
        status=True,
        duration=[
            RmUserNumberFilter(
                column_name="column_name_example",
                filter_type=RmUserFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        user_ids=[
            1
        ],
    )
    try:
        # Export the Users grid data
        api_response = api_instance.export_to_csv(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->export_to_csv: %s\n" % e)

    # example passing only optional values
    query_params = {
        'search': "search_example",
        'sortField': RmUserGridSortField("USER_NAME"),
        'order': RmSortOrder("ASC"),
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserGridRequest(
        user_name=[
            "user_name_example"
        ],
        source=[
            "source_example"
        ],
        site_ids=[
            1
        ],
        status=True,
        duration=[
            RmUserNumberFilter(
                column_name="column_name_example",
                filter_type=RmUserFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        user_ids=[
            1
        ],
    )
    try:
        # Export the Users grid data
        api_response = api_instance.export_to_csv(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->export_to_csv: %s\n" % e)
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
[**RmUserGridRequest**](../../models/RmUserGridRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
search | SearchSchema | | optional
sortField | SortFieldSchema | | optional
order | OrderSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 


# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RmUserGridSortField**](../../models/RmUserGridSortField.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RmSortOrder**](../../models/RmSortOrder.md) |  | 


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
[**RmMetricReport**](../../models/RmMetricReport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_current_user**
<a id="get_current_user"></a>
> XiqUser get_current_user()

Get current user info

Get currently login user info.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_user import XiqUser
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current user info
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->get_current_user: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_current_user.ApiResponseFor200) | OK

#### get_current_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUser**](../../models/XiqUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_external_user**
<a id="get_external_user"></a>
> XiqExternalUser get_external_user(id)

Get external access info

Get external access info for a specific external user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_external_user import XiqExternalUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get external access info
        api_response = api_instance.get_external_user(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->get_external_user: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_external_user.ApiResponseFor200) | OK

#### get_external_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqExternalUser**](../../models/XiqExternalUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user**
<a id="get_user"></a>
> XiqUser get_user(id)

Get user info by ID

Get user info for a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_user import XiqUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get user info by ID
        api_response = api_instance.get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user.ApiResponseFor200) | OK

#### get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUser**](../../models/XiqUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_data_usage**
<a id="get_user_data_usage"></a>
> RmUserDataUsage get_user_data_usage(start_timeend_timerm_user_filter_request)

Get user data usage

Returns data usage in bytes for each user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.rm_user_filter_request import RmUserFilterRequest
from extremecloudiq.model.rm_user_data_usage import RmUserDataUsage
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserFilterRequest(
        site_ids=[
            1
        ],
    )
    try:
        # Get user data usage
        api_response = api_instance.get_user_data_usage(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->get_user_data_usage: %s\n" % e)
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
[**RmUserFilterRequest**](../../models/RmUserFilterRequest.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_data_usage.ApiResponseFor200) | OK

#### get_user_data_usage.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RmUserDataUsage**](../../models/RmUserDataUsage.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_type_distribution**
<a id="get_user_type_distribution"></a>
> RmUserTypeDistribution get_user_type_distribution(start_timeend_timerm_user_filter_request)

Get user type distribution

User type distribution and total connected users

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.rm_user_filter_request import RmUserFilterRequest
from extremecloudiq.model.rm_user_type_distribution import RmUserTypeDistribution
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserFilterRequest(
        site_ids=[
            1
        ],
    )
    try:
        # Get user type distribution
        api_response = api_instance.get_user_type_distribution(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->get_user_type_distribution: %s\n" % e)
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
[**RmUserFilterRequest**](../../models/RmUserFilterRequest.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_type_distribution.ApiResponseFor200) | OK

#### get_user_type_distribution.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RmUserTypeDistribution**](../../models/RmUserTypeDistribution.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **grant_external_user**
<a id="grant_external_user"></a>
> XiqExternalUser grant_external_user(xiq_grant_external_user_request)

Grant external access

Grant external access to a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_external_user import XiqExternalUser
from extremecloudiq.model.xiq_grant_external_user_request import XiqGrantExternalUserRequest
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqGrantExternalUserRequest(
        login_name="login_name_example",
        user_role=XiqUserRole("ADMINISTRATOR"),
        org_id=1,
        location_ids=[
            1
        ],
        access_scope=1,
        viq_access_control=1,
    )
    try:
        # Grant external access
        api_response = api_instance.grant_external_user(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->grant_external_user: %s\n" % e)
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
[**XiqGrantExternalUserRequest**](../../models/XiqGrantExternalUserRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#grant_external_user.ApiResponseFor200) | OK

#### grant_external_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqExternalUser**](../../models/XiqExternalUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_external_users**
<a id="list_external_users"></a>
> PagedXiqExternalUser list_external_users()

List external access users

List a page of external access users.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.paged_xiq_external_user import PagedXiqExternalUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
    }
    try:
        # List external access users
        api_response = api_instance.list_external_users(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->list_external_users: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_external_users.ApiResponseFor200) | OK

#### list_external_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqExternalUser**](../../models/PagedXiqExternalUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_user_grid_filter_metadata**
<a id="list_user_grid_filter_metadata"></a>
> RmUsersGridFilterMetadata list_user_grid_filter_metadata(start_timeend_timerm_user_filter_request)

List user grid filter metadata

Lists of values for user grid filters

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.rm_user_filter_request import RmUserFilterRequest
from extremecloudiq.model.rm_users_grid_filter_metadata import RmUsersGridFilterMetadata
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserFilterRequest(
        site_ids=[
            1
        ],
    )
    try:
        # List user grid filter metadata
        api_response = api_instance.list_user_grid_filter_metadata(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->list_user_grid_filter_metadata: %s\n" % e)
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
[**RmUserFilterRequest**](../../models/RmUserFilterRequest.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_user_grid_filter_metadata.ApiResponseFor200) | OK

#### list_user_grid_filter_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RmUsersGridFilterMetadata**](../../models/RmUsersGridFilterMetadata.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_users**
<a id="list_users"></a>
> PagedXiqUser list_users()

List all users

List users with pagination.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.paged_xiq_user import PagedXiqUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
    }
    try:
        # List all users
        api_response = api_instance.list_users(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_users.ApiResponseFor200) | OK

#### list_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqUser**](../../models/PagedXiqUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_users_grid**
<a id="list_users_grid"></a>
> PagedRmUsersGridResponse list_users_grid(start_timeend_timerm_user_grid_request)

List Users

Returns a paginated list of users with support for search, filter, and sort.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.rm_sort_order import RmSortOrder
from extremecloudiq.model.paged_rm_users_grid_response import PagedRmUsersGridResponse
from extremecloudiq.model.rm_user_grid_sort_field import RmUserGridSortField
from extremecloudiq.model.rm_user_grid_request import RmUserGridRequest
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserGridRequest(
        user_name=[
            "user_name_example"
        ],
        source=[
            "source_example"
        ],
        site_ids=[
            1
        ],
        status=True,
        duration=[
            RmUserNumberFilter(
                column_name="column_name_example",
                filter_type=RmUserFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        user_ids=[
            1
        ],
    )
    try:
        # List Users
        api_response = api_instance.list_users_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->list_users_grid: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'search': "search_example",
        'sortField': RmUserGridSortField("USER_NAME"),
        'order': RmSortOrder("ASC"),
        'startTime': 1,
        'endTime': 1,
    }
    body = RmUserGridRequest(
        user_name=[
            "user_name_example"
        ],
        source=[
            "source_example"
        ],
        site_ids=[
            1
        ],
        status=True,
        duration=[
            RmUserNumberFilter(
                column_name="column_name_example",
                filter_type=RmUserFilterType("GT"),
                value=1,
                min=1,
                max=1,
            )
        ],
        user_ids=[
            1
        ],
    )
    try:
        # List Users
        api_response = api_instance.list_users_grid(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->list_users_grid: %s\n" % e)
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
[**RmUserGridRequest**](../../models/RmUserGridRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
search | SearchSchema | | optional
sortField | SortFieldSchema | | optional
order | OrderSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 


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

# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RmUserGridSortField**](../../models/RmUserGridSortField.md) |  | 


# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RmSortOrder**](../../models/RmSortOrder.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_users_grid.ApiResponseFor200) | OK

#### list_users_grid.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedRmUsersGridResponse**](../../models/PagedRmUsersGridResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revoke_external_user**
<a id="revoke_external_user"></a>
> revoke_external_user(id)

Revoke external access

Revoke external acccess for a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Revoke external access
        api_response = api_instance.revoke_external_user(
            path_params=path_params,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->revoke_external_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#revoke_external_user.ApiResponseFor200) | OK

#### revoke_external_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_external_user**
<a id="update_external_user"></a>
> update_external_user(idxiq_update_external_user_request)

Update external access info

Updates external access info for a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_update_external_user_request import XiqUpdateExternalUserRequest
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = XiqUpdateExternalUserRequest(
        user_role=XiqUserRole("ADMINISTRATOR"),
        org_id=1,
        location_ids=[
            1
        ],
        access_scope=1,
        viq_access_control=1,
    )
    try:
        # Update external access info
        api_response = api_instance.update_external_user(
            path_params=path_params,
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->update_external_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUpdateExternalUserRequest**](../../models/XiqUpdateExternalUserRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_external_user.ApiResponseFor200) | OK

#### update_external_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user**
<a id="update_user"></a>
> XiqUser update_user(idxiq_update_user_request)

Update user info

Updates user info for a specific user.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import user_api
from extremecloudiq.model.xiq_user import XiqUser
from extremecloudiq.model.xiq_update_user_request import XiqUpdateUserRequest
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = XiqUpdateUserRequest(
        login_name="login_name_example",
        display_name="display_name_example",
        idle_timeout=1,
        user_role=XiqUserRole("ADMINISTRATOR"),
        location_ids=[
            1
        ],
        access_scope=1,
        viq_access_control=1,
    )
    try:
        # Update user info
        api_response = api_instance.update_user(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUpdateUserRequest**](../../models/XiqUpdateUserRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_user.ApiResponseFor200) | OK

#### update_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUser**](../../models/XiqUser.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

