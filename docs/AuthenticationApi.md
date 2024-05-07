# extremecloudiq.AuthenticationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /login | User login with username and password
[**logout**](AuthenticationApi.md#logout) | **POST** /logout | User logout (Revoke the current access token)


# **login**
> XiqLoginResponse login(xiq_login_request)

User login with username and password

Get access token via username and password authentication. The client must present Bearer token to access the protected API endpoints.The Bearer token should be present in the \"Authorization\" request header field and use the \"Bearer\" HTTP authentication scheme to transmit the access token.

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
    api_instance = extremecloudiq.AuthenticationApi(api_client)
    xiq_login_request = {"username":"username@company.com","password":"ChangeMe"} # XiqLoginRequest | Login request body

    try:
        # User login with username and password
        api_response = api_instance.login(xiq_login_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_login_request** | [**XiqLoginRequest**](XiqLoginRequest.md)| Login request body | 

### Return type

[**XiqLoginResponse**](XiqLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | UNAUTHORIZED |  -  |
**400** | Bad request |  -  |
**500** | Internal Server Error |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

User logout (Revoke the current access token)

User logout, the current access token will be revoked and the following access with the same token will be immediately denied.

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
    api_instance = extremecloudiq.AuthenticationApi(api_client)
    
    try:
        # User logout (Revoke the current access token)
        api_instance.logout()
    except ApiException as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

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

