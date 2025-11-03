<a id="__pageTop"></a>
# extremecloudiq.apis.tags.authorization_api.AuthorizationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_permissions**](#check_permissions) | **post** /auth/permissions/:check | Check permissions
[**generate_api_token**](#generate_api_token) | **post** /auth/apitoken | Generate new API token
[**get_current_api_token_info**](#get_current_api_token_info) | **get** /auth/apitoken/info | Get current API token details
[**list_permissions**](#list_permissions) | **get** /auth/permissions | Get permissions for current login user
[**validate_api_token**](#validate_api_token) | **post** /auth/apitoken/:validate | Validate API token

# **check_permissions**
<a id="check_permissions"></a>
> XiqCheckPermissionResponse check_permissions(xiq_check_permission_request)

Check permissions

Get required permissions for given HTTP request.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import authorization_api
from extremecloudiq.model.xiq_check_permission_request import XiqCheckPermissionRequest
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_check_permission_response import XiqCheckPermissionResponse
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
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqCheckPermissionRequest(
        uri="uri_example",
        method="method_example",
    )
    try:
        # Check permissions
        api_response = api_instance.check_permissions(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AuthorizationApi->check_permissions: %s\n" % e)
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
[**XiqCheckPermissionRequest**](../../models/XiqCheckPermissionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#check_permissions.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#check_permissions.ApiResponseFor403) | Access Denied
200 | [ApiResponseFor200](#check_permissions.ApiResponseFor200) | Successful operation
401 | [ApiResponseFor401](#check_permissions.ApiResponseFor401) | Unauthorized

#### check_permissions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### check_permissions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### check_permissions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCheckPermissionResponse**](../../models/XiqCheckPermissionResponse.md) |  | 


#### check_permissions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **generate_api_token**
<a id="generate_api_token"></a>
> XiqGenerateApiTokenResponse generate_api_token(xiq_generate_api_token_request)

Generate new API token

Generate a new API token with given permissions and expiration time.  The available permission list can be found via 'GET /auth/permissions' endpoint.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import authorization_api
from extremecloudiq.model.xiq_generate_api_token_response import XiqGenerateApiTokenResponse
from extremecloudiq.model.xiq_generate_api_token_request import XiqGenerateApiTokenRequest
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
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqGenerateApiTokenRequest(
        expire_time=1,
        description="description_example",
        permissions=[
            "permissions_example"
        ],
    )
    try:
        # Generate new API token
        api_response = api_instance.generate_api_token(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AuthorizationApi->generate_api_token: %s\n" % e)
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
[**XiqGenerateApiTokenRequest**](../../models/XiqGenerateApiTokenRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#generate_api_token.ApiResponseFor200) | OK

#### generate_api_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqGenerateApiTokenResponse**](../../models/XiqGenerateApiTokenResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_current_api_token_info**
<a id="get_current_api_token_info"></a>
> XiqApiTokenInfo get_current_api_token_info()

Get current API token details

Introspect current API token and get detail information.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import authorization_api
from extremecloudiq.model.xiq_api_token_info import XiqApiTokenInfo
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
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current API token details
        api_response = api_instance.get_current_api_token_info()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AuthorizationApi->get_current_api_token_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_current_api_token_info.ApiResponseFor200) | OK

#### get_current_api_token_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqApiTokenInfo**](../../models/XiqApiTokenInfo.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_permissions**
<a id="list_permissions"></a>
> str list_permissions()

Get permissions for current login user

Get permissions for current login user, which are allowed for generating new API tokens.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import authorization_api
from extremecloudiq.model.xiq_error import XiqError
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
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get permissions for current login user
        api_response = api_instance.list_permissions()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AuthorizationApi->list_permissions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#list_permissions.ApiResponseFor401) | UNAUTHORIZED
403 | [ApiResponseFor403](#list_permissions.ApiResponseFor403) | Access denied
400 | [ApiResponseFor400](#list_permissions.ApiResponseFor400) | Bad request
200 | [ApiResponseFor200](#list_permissions.ApiResponseFor200) | Successful operation

#### list_permissions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_permissions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_permissions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_permissions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_api_token**
<a id="validate_api_token"></a>
> validate_api_token(body)

Validate API token

Validate JWT format API token

### Example

```python
import extremecloudiq
from extremecloudiq.apis.tags import authorization_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorization_api.AuthorizationApi(api_client)

    # example passing only required values which don't have defaults set
    body = "body_example"
    try:
        # Validate API token
        api_response = api_instance.validate_api_token(
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling AuthorizationApi->validate_api_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyTextPlain] | required |
content_type | str | optional, default is 'text/plain' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyTextPlain

The API token to be validated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The API token to be validated | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#validate_api_token.ApiResponseFor200) | OK

#### validate_api_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

