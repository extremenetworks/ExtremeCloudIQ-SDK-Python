# extremecloudiq.AuthorizationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_permissions**](AuthorizationApi.md#check_permissions) | **POST** /auth/permissions/:check | Check permissions
[**generate_api_token**](AuthorizationApi.md#generate_api_token) | **POST** /auth/apitoken | Generate new API token
[**get_current_api_token_info**](AuthorizationApi.md#get_current_api_token_info) | **GET** /auth/apitoken/info | Get current API token details
[**list_permissions**](AuthorizationApi.md#list_permissions) | **GET** /auth/permissions | Get permissions for current login user
[**validate_api_token**](AuthorizationApi.md#validate_api_token) | **POST** /auth/apitoken/:validate | Validate API token


# **check_permissions**
> XiqCheckPermissionResponse check_permissions(xiq_check_permission_request)

Check permissions

Get required permissions for given HTTP request.

### Example

* Bearer (JWT) Authentication (Bearer):
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

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.AuthorizationApi(api_client)
    xiq_check_permission_request = extremecloudiq.XiqCheckPermissionRequest() # XiqCheckPermissionRequest | 

    try:
        # Check permissions
        api_response = api_instance.check_permissions(xiq_check_permission_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationApi->check_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_check_permission_request** | [**XiqCheckPermissionRequest**](XiqCheckPermissionRequest.md)|  | 

### Return type

[**XiqCheckPermissionResponse**](XiqCheckPermissionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**403** | Access Denied |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_token**
> XiqGenerateApiTokenResponse generate_api_token(xiq_generate_api_token_request)

Generate new API token

Generate a new API token with given permissions and expiration time.  The available permission list can be found via 'GET /auth/permissions' endpoint.

### Example

* Bearer (JWT) Authentication (Bearer):
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

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.AuthorizationApi(api_client)
    xiq_generate_api_token_request = {"description":"Token for reading account info only","expire_time":1604737598,"permissions":["account:r"]} # XiqGenerateApiTokenRequest | Generate API token request body

    try:
        # Generate new API token
        api_response = api_instance.generate_api_token(xiq_generate_api_token_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationApi->generate_api_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_generate_api_token_request** | [**XiqGenerateApiTokenRequest**](XiqGenerateApiTokenRequest.md)| Generate API token request body | 

### Return type

[**XiqGenerateApiTokenResponse**](XiqGenerateApiTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_api_token_info**
> XiqApiTokenInfo get_current_api_token_info()

Get current API token details

Introspect current API token and get detail information.

### Example

* Bearer (JWT) Authentication (Bearer):
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

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.AuthorizationApi(api_client)
    
    try:
        # Get current API token details
        api_response = api_instance.get_current_api_token_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationApi->get_current_api_token_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqApiTokenInfo**](XiqApiTokenInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **list_permissions**
> str list_permissions()

Get permissions for current login user

Get permissions for current login user, which are allowed for generating new API tokens.

### Example

* Bearer (JWT) Authentication (Bearer):
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

# Configure Bearer authorization (JWT): Bearer
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.AuthorizationApi(api_client)
    
    try:
        # Get permissions for current login user
        api_response = api_instance.list_permissions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorizationApi->list_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | UNAUTHORIZED |  -  |
**400** | Bad request |  -  |
**500** | Internal Server Error |  -  |
**403** | Access denied |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_api_token**
> validate_api_token(body)

Validate API token

Validate JWT format API token

### Example

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


# Enter a context with an instance of the API client
with extremecloudiq.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.AuthorizationApi(api_client)
    body = 'body_example' # str | 

    try:
        # Validate API token
        api_instance.validate_api_token(body)
    except ApiException as e:
        print("Exception when calling AuthorizationApi->validate_api_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

