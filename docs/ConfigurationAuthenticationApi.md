# extremecloudiq.ConfigurationAuthenticationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_radius_server**](ConfigurationAuthenticationApi.md#create_external_radius_server) | **POST** /radius-servers/external | Create external RADIUS server configuration
[**create_internal_radius_server**](ConfigurationAuthenticationApi.md#create_internal_radius_server) | **POST** /radius-servers/internal | Create internal RADIUS server configuration
[**create_ldap_server**](ConfigurationAuthenticationApi.md#create_ldap_server) | **POST** /ldap-servers | Create LDAP server
[**create_radius_client_object**](ConfigurationAuthenticationApi.md#create_radius_client_object) | **POST** /radius-client-objects | Create RADIUS client object configuration
[**create_radius_proxy**](ConfigurationAuthenticationApi.md#create_radius_proxy) | **POST** /radius-proxies | Create RADIUS proxy configuration
[**delete_bulk_internal_radius_server**](ConfigurationAuthenticationApi.md#delete_bulk_internal_radius_server) | **DELETE** /radius-servers/internal | [LRO] Delete internal RADIUS server configuration
[**delete_external_radius_server**](ConfigurationAuthenticationApi.md#delete_external_radius_server) | **DELETE** /radius-servers/external/{id} | Delete external RADIUS server configuration
[**delete_internal_radius_server**](ConfigurationAuthenticationApi.md#delete_internal_radius_server) | **DELETE** /radius-servers/internal/{id} | Delete internal RADIUS server configuration
[**delete_ldap_server**](ConfigurationAuthenticationApi.md#delete_ldap_server) | **DELETE** /ldap-servers/{id} | Delete a LDAP server
[**delete_radius_client_object**](ConfigurationAuthenticationApi.md#delete_radius_client_object) | **DELETE** /radius-client-objects/{id} | Delete a RADIUS client object configuration
[**delete_radius_proxy**](ConfigurationAuthenticationApi.md#delete_radius_proxy) | **DELETE** /radius-proxies/{id} | Delete the RADIUS proxy configuration
[**get_external_radius_server**](ConfigurationAuthenticationApi.md#get_external_radius_server) | **GET** /radius-servers/external/{id} | Get external RADIUS server by ID
[**get_internal_radius_server**](ConfigurationAuthenticationApi.md#get_internal_radius_server) | **GET** /radius-servers/internal/{id} | Get internal RADIUS server by ID
[**get_ldap_server**](ConfigurationAuthenticationApi.md#get_ldap_server) | **GET** /ldap-servers/{id} | Get LDAP server by ID
[**get_radius_client_object**](ConfigurationAuthenticationApi.md#get_radius_client_object) | **GET** /radius-client-objects/{id} | Get RADIUS client object by ID
[**get_radius_proxy**](ConfigurationAuthenticationApi.md#get_radius_proxy) | **GET** /radius-proxies/{id} | Get the RADIUS proxy configuration
[**list_active_directory_servers**](ConfigurationAuthenticationApi.md#list_active_directory_servers) | **GET** /ad-servers | List active directory servers
[**list_captive_web_portals**](ConfigurationAuthenticationApi.md#list_captive_web_portals) | **GET** /cwps | List captive web portals
[**list_external_radius_servers**](ConfigurationAuthenticationApi.md#list_external_radius_servers) | **GET** /radius-servers/external | List external RADIUS servers
[**list_internal_radius_devices**](ConfigurationAuthenticationApi.md#list_internal_radius_devices) | **GET** /radius-servers/internal/devices | List all internal RADIUS devices
[**list_internal_radius_servers**](ConfigurationAuthenticationApi.md#list_internal_radius_servers) | **GET** /radius-servers/internal | List all internal RADIUS servers
[**list_ldap_servers**](ConfigurationAuthenticationApi.md#list_ldap_servers) | **GET** /ldap-servers | List LDAP servers
[**list_radius_client_objects**](ConfigurationAuthenticationApi.md#list_radius_client_objects) | **GET** /radius-client-objects | List RADIUS client objects
[**list_radius_proxies**](ConfigurationAuthenticationApi.md#list_radius_proxies) | **GET** /radius-proxies | List RADIUS proxies
[**list_radius_proxy_devices**](ConfigurationAuthenticationApi.md#list_radius_proxy_devices) | **GET** /radius-proxies/devices | List Radius proxy devices
[**update_external_radius_server**](ConfigurationAuthenticationApi.md#update_external_radius_server) | **PUT** /radius-servers/external/{id} | Update external RADIUS server configuration
[**update_internal_radius_server**](ConfigurationAuthenticationApi.md#update_internal_radius_server) | **PUT** /radius-servers/internal/{id} | Update internal RADIUS server configuration
[**update_ldap_server**](ConfigurationAuthenticationApi.md#update_ldap_server) | **PUT** /ldap-servers/{id} | Update LDAP server configuration
[**update_radius_client_object**](ConfigurationAuthenticationApi.md#update_radius_client_object) | **PUT** /radius-client-objects/{id} | Update RADIUS client object configuration
[**update_radius_proxy**](ConfigurationAuthenticationApi.md#update_radius_proxy) | **PUT** /radius-proxies/{id} | Update RADIUS proxy configuration


# **create_external_radius_server**
> XiqExternalRadiusServer create_external_radius_server(xiq_create_external_radius_server_request)

Create external RADIUS server configuration

Create a new external RADIUS server configuration.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    xiq_create_external_radius_server_request = extremecloudiq.XiqCreateExternalRadiusServerRequest() # XiqCreateExternalRadiusServerRequest | Use the payload configuration to create a new external RADIUS server

    try:
        # Create external RADIUS server configuration
        api_response = api_instance.create_external_radius_server(xiq_create_external_radius_server_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->create_external_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_external_radius_server_request** | [**XiqCreateExternalRadiusServerRequest**](XiqCreateExternalRadiusServerRequest.md)| Use the payload configuration to create a new external RADIUS server | 

### Return type

[**XiqExternalRadiusServer**](XiqExternalRadiusServer.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internal_radius_server**
> XiqInternalRadiusServer create_internal_radius_server(xiq_create_internal_radius_server_request)

Create internal RADIUS server configuration

Create a new internal RADIUS server configuration.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    xiq_create_internal_radius_server_request = extremecloudiq.XiqCreateInternalRadiusServerRequest() # XiqCreateInternalRadiusServerRequest | Use the payload configuration to create a new internal RADIUS server

    try:
        # Create internal RADIUS server configuration
        api_response = api_instance.create_internal_radius_server(xiq_create_internal_radius_server_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->create_internal_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_internal_radius_server_request** | [**XiqCreateInternalRadiusServerRequest**](XiqCreateInternalRadiusServerRequest.md)| Use the payload configuration to create a new internal RADIUS server | 

### Return type

[**XiqInternalRadiusServer**](XiqInternalRadiusServer.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ldap_server**
> XiqLdapServer create_ldap_server(xiq_create_ldap_server_request)

Create LDAP server

Create a new LDAP server.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    xiq_create_ldap_server_request = extremecloudiq.XiqCreateLdapServerRequest() # XiqCreateLdapServerRequest | The body of create LDAP server API

    try:
        # Create LDAP server
        api_response = api_instance.create_ldap_server(xiq_create_ldap_server_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->create_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_ldap_server_request** | [**XiqCreateLdapServerRequest**](XiqCreateLdapServerRequest.md)| The body of create LDAP server API | 

### Return type

[**XiqLdapServer**](XiqLdapServer.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_radius_client_object**
> XiqRadiusClientObject create_radius_client_object(xiq_create_radius_client_object_request)

Create RADIUS client object configuration

Create a new RADIUS client object configuration.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    xiq_create_radius_client_object_request = extremecloudiq.XiqCreateRadiusClientObjectRequest() # XiqCreateRadiusClientObjectRequest | Use the payload configuration to create a new RADIUS client object

    try:
        # Create RADIUS client object configuration
        api_response = api_instance.create_radius_client_object(xiq_create_radius_client_object_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->create_radius_client_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_radius_client_object_request** | [**XiqCreateRadiusClientObjectRequest**](XiqCreateRadiusClientObjectRequest.md)| Use the payload configuration to create a new RADIUS client object | 

### Return type

[**XiqRadiusClientObject**](XiqRadiusClientObject.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_radius_proxy**
> XiqRadiusProxy create_radius_proxy(xiq_create_radius_proxy_request)

Create RADIUS proxy configuration

Create a new RADIUS proxy configuration.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    xiq_create_radius_proxy_request = {"name":"radius-proxy-1","description":"Radius Proxy 1","format_type":"NAI","retry_count":3,"retry_delay":5,"dead_time":300,"enable_inject_operator_name_attribute":false,"device_ids":[1],"clients":[{"shared_secret":"123456","description":"","l3_address_profile_id":1000}],"realms":[{"name":"NULL","enable_strip_realm_name":false,"radius_client_object_id":2000},{"name":"DEFAULT","enable_strip_realm_name":false,"radius_client_object_id":3000}]} # XiqCreateRadiusProxyRequest | The body of create RADIUS proxy API

    try:
        # Create RADIUS proxy configuration
        api_response = api_instance.create_radius_proxy(xiq_create_radius_proxy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->create_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_radius_proxy_request** | [**XiqCreateRadiusProxyRequest**](XiqCreateRadiusProxyRequest.md)| The body of create RADIUS proxy API | 

### Return type

[**XiqRadiusProxy**](XiqRadiusProxy.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_internal_radius_server**
> delete_bulk_internal_radius_server(ids, _async=_async)

[LRO] Delete internal RADIUS server configuration

Delete an existing internal RADIUS server configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    ids = [56] # list[int] | The internal RADIUS server IDs to be delete, min = 1 ID, max = 100 IDs
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Delete internal RADIUS server configuration
        api_instance.delete_bulk_internal_radius_server(ids, _async=_async)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_bulk_internal_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| The internal RADIUS server IDs to be delete, min &#x3D; 1 ID, max &#x3D; 100 IDs | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

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

# **delete_external_radius_server**
> delete_external_radius_server(id)

Delete external RADIUS server configuration

Delete an existing external RADIUS server configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The external RADIUS server ID

    try:
        # Delete external RADIUS server configuration
        api_instance.delete_external_radius_server(id)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_external_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The external RADIUS server ID | 

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

# **delete_internal_radius_server**
> delete_internal_radius_server(id)

Delete internal RADIUS server configuration

Delete an existing internal RADIUS server configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The internal RADIUS server ID

    try:
        # Delete internal RADIUS server configuration
        api_instance.delete_internal_radius_server(id)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_internal_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The internal RADIUS server ID | 

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

# **delete_ldap_server**
> delete_ldap_server(id)

Delete a LDAP server

Delete a specific LDAP server by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The LDAP server ID

    try:
        # Delete a LDAP server
        api_instance.delete_ldap_server(id)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The LDAP server ID | 

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

# **delete_radius_client_object**
> delete_radius_client_object(id)

Delete a RADIUS client object configuration

Delete an existing RADIUS client object configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The RADIUS client object ID

    try:
        # Delete a RADIUS client object configuration
        api_instance.delete_radius_client_object(id)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_radius_client_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The RADIUS client object ID | 

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

# **delete_radius_proxy**
> delete_radius_proxy(id)

Delete the RADIUS proxy configuration

Delete an existing RADIUS proxy configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The RADIUS proxy ID

    try:
        # Delete the RADIUS proxy configuration
        api_instance.delete_radius_proxy(id)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->delete_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The RADIUS proxy ID | 

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

# **get_external_radius_server**
> XiqExternalRadiusServer get_external_radius_server(id)

Get external RADIUS server by ID

Get detailed configuration for a specific external RADIUS server.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The ID for external RADIUS server

    try:
        # Get external RADIUS server by ID
        api_response = api_instance.get_external_radius_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->get_external_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID for external RADIUS server | 

### Return type

[**XiqExternalRadiusServer**](XiqExternalRadiusServer.md)

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

# **get_internal_radius_server**
> XiqInternalRadiusServer get_internal_radius_server(id)

Get internal RADIUS server by ID

Get detailed configuration for internal RADIUS server by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The ID for internal RADIUS server

    try:
        # Get internal RADIUS server by ID
        api_response = api_instance.get_internal_radius_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->get_internal_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID for internal RADIUS server | 

### Return type

[**XiqInternalRadiusServer**](XiqInternalRadiusServer.md)

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

# **get_ldap_server**
> XiqLdapServer get_ldap_server(id)

Get LDAP server by ID

Get a specific LDAP server by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The LDAP server 

    try:
        # Get LDAP server by ID
        api_response = api_instance.get_ldap_server(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->get_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The LDAP server  | 

### Return type

[**XiqLdapServer**](XiqLdapServer.md)

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

# **get_radius_client_object**
> XiqRadiusClientObject get_radius_client_object(id)

Get RADIUS client object by ID

Get detailed configuration for a specific RADIUS client object.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The ID of RADIUS client object

    try:
        # Get RADIUS client object by ID
        api_response = api_instance.get_radius_client_object(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->get_radius_client_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of RADIUS client object | 

### Return type

[**XiqRadiusClientObject**](XiqRadiusClientObject.md)

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

# **get_radius_proxy**
> XiqRadiusProxy get_radius_proxy(id)

Get the RADIUS proxy configuration

Get an existing RADIUS proxy configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The RADIUS proxy ID

    try:
        # Get the RADIUS proxy configuration
        api_response = api_instance.get_radius_proxy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->get_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The RADIUS proxy ID | 

### Return type

[**XiqRadiusProxy**](XiqRadiusProxy.md)

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

# **list_active_directory_servers**
> PagedXiqActiveDirectoryServer list_active_directory_servers(page=page, limit=limit)

List active directory servers

List a page of active directory servers.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List active directory servers
        api_response = api_instance.list_active_directory_servers(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_active_directory_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqActiveDirectoryServer**](PagedXiqActiveDirectoryServer.md)

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

# **list_captive_web_portals**
> PagedXiqCwp list_captive_web_portals(page=page, limit=limit)

List captive web portals

List a page of Captive Web Portals.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List captive web portals
        api_response = api_instance.list_captive_web_portals(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_captive_web_portals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqCwp**](PagedXiqCwp.md)

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

# **list_external_radius_servers**
> PagedXiqExternalRadiusServer list_external_radius_servers(page=page, limit=limit)

List external RADIUS servers

List a page of external RADIUS server configurations.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List external RADIUS servers
        api_response = api_instance.list_external_radius_servers(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_external_radius_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqExternalRadiusServer**](PagedXiqExternalRadiusServer.md)

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

# **list_internal_radius_devices**
> PagedXiqInternalRadiusDevice list_internal_radius_devices(page=page, limit=limit)

List all internal RADIUS devices

List all internal RADIUS devices fields.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List all internal RADIUS devices
        api_response = api_instance.list_internal_radius_devices(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_internal_radius_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqInternalRadiusDevice**](PagedXiqInternalRadiusDevice.md)

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

# **list_internal_radius_servers**
> PagedXiqInternalRadiusServer list_internal_radius_servers(page=page, limit=limit)

List all internal RADIUS servers

List all internal RADIUS servers configurations.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List all internal RADIUS servers
        api_response = api_instance.list_internal_radius_servers(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_internal_radius_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqInternalRadiusServer**](PagedXiqInternalRadiusServer.md)

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

# **list_ldap_servers**
> PagedXiqLdapServer list_ldap_servers(page=page, limit=limit)

List LDAP servers

List a page of LDAP servers.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List LDAP servers
        api_response = api_instance.list_ldap_servers(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_ldap_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqLdapServer**](PagedXiqLdapServer.md)

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

# **list_radius_client_objects**
> PagedXiqRadiusClientObject list_radius_client_objects(page=page, limit=limit)

List RADIUS client objects

List a page of RADIUS client object configurations.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List RADIUS client objects
        api_response = api_instance.list_radius_client_objects(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_radius_client_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqRadiusClientObject**](PagedXiqRadiusClientObject.md)

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

# **list_radius_proxies**
> PagedXiqRadiusProxy list_radius_proxies(page=page, limit=limit)

List RADIUS proxies

List a page of RADIUS proxy configurations.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List RADIUS proxies
        api_response = api_instance.list_radius_proxies(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_radius_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqRadiusProxy**](PagedXiqRadiusProxy.md)

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

# **list_radius_proxy_devices**
> PagedXiqInternalRadiusDevice list_radius_proxy_devices(page=page, limit=limit)

List Radius proxy devices

List devices for Radius Proxy.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List Radius proxy devices
        api_response = api_instance.list_radius_proxy_devices(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->list_radius_proxy_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqInternalRadiusDevice**](PagedXiqInternalRadiusDevice.md)

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

# **update_external_radius_server**
> update_external_radius_server(id, xiq_update_external_radius_server_request)

Update external RADIUS server configuration

Update external RADIUS server configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The external RADIUS server ID.
xiq_update_external_radius_server_request = extremecloudiq.XiqUpdateExternalRadiusServerRequest() # XiqUpdateExternalRadiusServerRequest | The payload to update the external RADIUS server

    try:
        # Update external RADIUS server configuration
        api_instance.update_external_radius_server(id, xiq_update_external_radius_server_request)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->update_external_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The external RADIUS server ID. | 
 **xiq_update_external_radius_server_request** | [**XiqUpdateExternalRadiusServerRequest**](XiqUpdateExternalRadiusServerRequest.md)| The payload to update the external RADIUS server | 

### Return type

void (empty response body)

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

# **update_internal_radius_server**
> XiqInternalRadiusServer update_internal_radius_server(id, xiq_update_internal_radius_server_request)

Update internal RADIUS server configuration

Update internal RADIUS server configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The internal RADIUS server ID
xiq_update_internal_radius_server_request = extremecloudiq.XiqUpdateInternalRadiusServerRequest() # XiqUpdateInternalRadiusServerRequest | The payload to update the internal RADIUS server

    try:
        # Update internal RADIUS server configuration
        api_response = api_instance.update_internal_radius_server(id, xiq_update_internal_radius_server_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->update_internal_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The internal RADIUS server ID | 
 **xiq_update_internal_radius_server_request** | [**XiqUpdateInternalRadiusServerRequest**](XiqUpdateInternalRadiusServerRequest.md)| The payload to update the internal RADIUS server | 

### Return type

[**XiqInternalRadiusServer**](XiqInternalRadiusServer.md)

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

# **update_ldap_server**
> XiqLdapServer update_ldap_server(id, xiq_update_ldap_server_request)

Update LDAP server configuration

Update configuration for a specific LDAP server.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The LDAP server ID.
xiq_update_ldap_server_request = extremecloudiq.XiqUpdateLdapServerRequest() # XiqUpdateLdapServerRequest | The body of update LDAP server API

    try:
        # Update LDAP server configuration
        api_response = api_instance.update_ldap_server(id, xiq_update_ldap_server_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->update_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The LDAP server ID. | 
 **xiq_update_ldap_server_request** | [**XiqUpdateLdapServerRequest**](XiqUpdateLdapServerRequest.md)| The body of update LDAP server API | 

### Return type

[**XiqLdapServer**](XiqLdapServer.md)

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

# **update_radius_client_object**
> update_radius_client_object(id, xiq_update_radius_client_object_request)

Update RADIUS client object configuration

Update RADIUS client object configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The RADIUS client object ID.
xiq_update_radius_client_object_request = extremecloudiq.XiqUpdateRadiusClientObjectRequest() # XiqUpdateRadiusClientObjectRequest | The payload to update the RADIUS client object

    try:
        # Update RADIUS client object configuration
        api_instance.update_radius_client_object(id, xiq_update_radius_client_object_request)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->update_radius_client_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The RADIUS client object ID. | 
 **xiq_update_radius_client_object_request** | [**XiqUpdateRadiusClientObjectRequest**](XiqUpdateRadiusClientObjectRequest.md)| The payload to update the RADIUS client object | 

### Return type

void (empty response body)

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

# **update_radius_proxy**
> XiqRadiusProxy update_radius_proxy(id, xiq_update_radius_proxy_request)

Update RADIUS proxy configuration

Update RADIUS proxy configuration by ID.

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
    api_instance = extremecloudiq.ConfigurationAuthenticationApi(api_client)
    id = 56 # int | The RADIUS proxy ID
xiq_update_radius_proxy_request = {"name":"radius-proxy-1","description":"Radius Proxy 1","format_type":"NAI","retry_count":3,"retry_delay":5,"dead_time":300,"enable_inject_operator_name_attribute":false,"clients":[{"id":1},{"shared_secret":"123456","description":"","l3_address_profile_id":1000}],"realms":[{"id":1},{"id":2},{"name":"test-realm","enable_strip_realm_name":false,"radius_client_object_id":3000}]} # XiqUpdateRadiusProxyRequest | The body of update RADIUS proxy API

    try:
        # Update RADIUS proxy configuration
        api_response = api_instance.update_radius_proxy(id, xiq_update_radius_proxy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationAuthenticationApi->update_radius_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The RADIUS proxy ID | 
 **xiq_update_radius_proxy_request** | [**XiqUpdateRadiusProxyRequest**](XiqUpdateRadiusProxyRequest.md)| The body of update RADIUS proxy API | 

### Return type

[**XiqRadiusProxy**](XiqRadiusProxy.md)

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

