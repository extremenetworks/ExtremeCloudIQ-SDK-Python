# extremecloudiq.ConfigurationNetworkApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_services**](ConfigurationNetworkApi.md#create_network_services) | **POST** /network-services | Create Network Services
[**create_tunnel_concentrator**](ConfigurationNetworkApi.md#create_tunnel_concentrator) | **POST** /tunnel-concentrators | Create a Tunnel Concentrator
[**delete_network_service**](ConfigurationNetworkApi.md#delete_network_service) | **DELETE** /network-services/{id} | Delete Network Services
[**delete_tunnel_concentrator**](ConfigurationNetworkApi.md#delete_tunnel_concentrator) | **DELETE** /tunnel-concentrators/{id} | Delete TunnelConcentrator by ID
[**get_tunnel_concentrator**](ConfigurationNetworkApi.md#get_tunnel_concentrator) | **GET** /tunnel-concentrators/{id} | Get Tunnel Concentrator by ID
[**list_network_services**](ConfigurationNetworkApi.md#list_network_services) | **GET** /network-services | List Network Services
[**list_tunnel_concentrators**](ConfigurationNetworkApi.md#list_tunnel_concentrators) | **GET** /tunnel-concentrators | List Tunnel Concentrators
[**update_tunnel_concentrator**](ConfigurationNetworkApi.md#update_tunnel_concentrator) | **PUT** /tunnel-concentrators/{id} | Update TunnelConcentrator by ID


# **create_network_services**
> XiqNetworkService create_network_services(xiq_network_service_request)

Create Network Services

Create a new Network Services.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    xiq_network_service_request = extremecloudiq.XiqNetworkServiceRequest() # XiqNetworkServiceRequest | The request body to create new user profile.

    try:
        # Create Network Services
        api_response = api_instance.create_network_services(xiq_network_service_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->create_network_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_network_service_request** | [**XiqNetworkServiceRequest**](XiqNetworkServiceRequest.md)| The request body to create new user profile. | 

### Return type

[**XiqNetworkService**](XiqNetworkService.md)

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

# **create_tunnel_concentrator**
> XiqTunnelConcentrator create_tunnel_concentrator(xiq_tunnel_concentrator_request)

Create a Tunnel Concentrator

Create a new Tunnel Concentrator.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    xiq_tunnel_concentrator_request = extremecloudiq.XiqTunnelConcentratorRequest() # XiqTunnelConcentratorRequest | The request body to create new Tunnel Concentrator.

    try:
        # Create a Tunnel Concentrator
        api_response = api_instance.create_tunnel_concentrator(xiq_tunnel_concentrator_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->create_tunnel_concentrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_tunnel_concentrator_request** | [**XiqTunnelConcentratorRequest**](XiqTunnelConcentratorRequest.md)| The request body to create new Tunnel Concentrator. | 

### Return type

[**XiqTunnelConcentrator**](XiqTunnelConcentrator.md)

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

# **delete_network_service**
> delete_network_service(id)

Delete Network Services

Delete specific Network Services.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    id = 56 # int | The Network Service ID

    try:
        # Delete Network Services
        api_instance.delete_network_service(id)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->delete_network_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Network Service ID | 

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

# **delete_tunnel_concentrator**
> delete_tunnel_concentrator(id)

Delete TunnelConcentrator by ID

Delete the existing TunnelConcentrator by the profile ID.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    id = 56 # int | The TunnelConcentrator ID

    try:
        # Delete TunnelConcentrator by ID
        api_instance.delete_tunnel_concentrator(id)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->delete_tunnel_concentrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The TunnelConcentrator ID | 

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

# **get_tunnel_concentrator**
> XiqTunnelConcentrator get_tunnel_concentrator(id)

Get Tunnel Concentrator by ID

Get Tunnel Concentrator  details for the specified ID.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    id = 56 # int | The Tunnel Concentrator ID

    try:
        # Get Tunnel Concentrator by ID
        api_response = api_instance.get_tunnel_concentrator(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->get_tunnel_concentrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tunnel Concentrator ID | 

### Return type

[**XiqTunnelConcentrator**](XiqTunnelConcentrator.md)

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

# **list_network_services**
> PagedXiqNetworkService list_network_services(page=page, limit=limit, name=name, ip_protocol=ip_protocol, alg_type=alg_type)

List Network Services

List a page of Network Services.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
name = 'name_example' # str | Network Service name. (optional)
ip_protocol = extremecloudiq.XiqNetworkIpProtocol() # XiqNetworkIpProtocol | IP Protocol, only for custom Application. (optional)
alg_type = extremecloudiq.XiqNetworkAlgType() # XiqNetworkAlgType | Application Layer Gateway (ALG) type, only for custom Application. (optional)

    try:
        # List Network Services
        api_response = api_instance.list_network_services(page=page, limit=limit, name=name, ip_protocol=ip_protocol, alg_type=alg_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->list_network_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **name** | **str**| Network Service name. | [optional] 
 **ip_protocol** | [**XiqNetworkIpProtocol**](.md)| IP Protocol, only for custom Application. | [optional] 
 **alg_type** | [**XiqNetworkAlgType**](.md)| Application Layer Gateway (ALG) type, only for custom Application. | [optional] 

### Return type

[**PagedXiqNetworkService**](PagedXiqNetworkService.md)

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

# **list_tunnel_concentrators**
> PagedXiqTunnelConcentrator list_tunnel_concentrators(page=page, limit=limit)

List Tunnel Concentrators

List a page of Tunnel Concentrators.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List Tunnel Concentrators
        api_response = api_instance.list_tunnel_concentrators(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->list_tunnel_concentrators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqTunnelConcentrator**](PagedXiqTunnelConcentrator.md)

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

# **update_tunnel_concentrator**
> XiqTunnelConcentrator update_tunnel_concentrator(id, xiq_tunnel_concentrator_request)

Update TunnelConcentrator by ID

Update the existing Tunnel Concentrator by ID.

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
    api_instance = extremecloudiq.ConfigurationNetworkApi(api_client)
    id = 56 # int | The Tunnel Concentrator ID.
xiq_tunnel_concentrator_request = extremecloudiq.XiqTunnelConcentratorRequest() # XiqTunnelConcentratorRequest | The payload of the update Tunnel Concentrator request.

    try:
        # Update TunnelConcentrator by ID
        api_response = api_instance.update_tunnel_concentrator(id, xiq_tunnel_concentrator_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationNetworkApi->update_tunnel_concentrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tunnel Concentrator ID. | 
 **xiq_tunnel_concentrator_request** | [**XiqTunnelConcentratorRequest**](XiqTunnelConcentratorRequest.md)| The payload of the update Tunnel Concentrator request. | 

### Return type

[**XiqTunnelConcentrator**](XiqTunnelConcentrator.md)

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

