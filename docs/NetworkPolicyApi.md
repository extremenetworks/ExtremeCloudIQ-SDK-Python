# extremecloudiq.NetworkPolicyApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ssids_to_network_policy**](NetworkPolicyApi.md#add_ssids_to_network_policy) | **POST** /network-policies/{id}/ssids/:add | Add SSIDs to a network policy
[**create_network_policy**](NetworkPolicyApi.md#create_network_policy) | **POST** /network-policies | Create network policy
[**delete_network_policy**](NetworkPolicyApi.md#delete_network_policy) | **DELETE** /network-policies/{id} | Delete the network policy
[**delete_ssids_from_network_policy**](NetworkPolicyApi.md#delete_ssids_from_network_policy) | **POST** /network-policies/{id}/ssids/:remove | Removes SSIDs from the network policy
[**get_network_policy**](NetworkPolicyApi.md#get_network_policy) | **GET** /network-policies/{id} | Get the network policy
[**list_network_polices**](NetworkPolicyApi.md#list_network_polices) | **GET** /network-policies | List network policies
[**list_ssids_by_network_policy**](NetworkPolicyApi.md#list_ssids_by_network_policy) | **GET** /network-policies/{id}/ssids | List SSIDs for a network policy
[**update_network_policy**](NetworkPolicyApi.md#update_network_policy) | **PUT** /network-policies/{id} | Update the network policy


# **add_ssids_to_network_policy**
> add_ssids_to_network_policy(id, request_body)

Add SSIDs to a network policy

Add SSIDs to a specific network policy.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID
request_body = [56] # list[int] | The SSID ids to be added to the network policy

    try:
        # Add SSIDs to a network policy
        api_instance.add_ssids_to_network_policy(id, request_body)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->add_ssids_to_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 
 **request_body** | [**list[int]**](int.md)| The SSID ids to be added to the network policy | 

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

# **create_network_policy**
> XiqNetworkPolicy create_network_policy(xiq_create_network_policy_request)

Create network policy

Create a new network policy.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    xiq_create_network_policy_request = extremecloudiq.XiqCreateNetworkPolicyRequest() # XiqCreateNetworkPolicyRequest | The body of create network policy API

    try:
        # Create network policy
        api_response = api_instance.create_network_policy(xiq_create_network_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->create_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_network_policy_request** | [**XiqCreateNetworkPolicyRequest**](XiqCreateNetworkPolicyRequest.md)| The body of create network policy API | 

### Return type

[**XiqNetworkPolicy**](XiqNetworkPolicy.md)

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

# **delete_network_policy**
> delete_network_policy(id)

Delete the network policy

Delete an existing network policy by ID.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID

    try:
        # Delete the network policy
        api_instance.delete_network_policy(id)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->delete_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 

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

# **delete_ssids_from_network_policy**
> delete_ssids_from_network_policy(id, request_body)

Removes SSIDs from the network policy

Removing multiple SSIDs from the network policy.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID
request_body = [56] # list[int] | The SSID ids to be removed from the network policy

    try:
        # Removes SSIDs from the network policy
        api_instance.delete_ssids_from_network_policy(id, request_body)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->delete_ssids_from_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 
 **request_body** | [**list[int]**](int.md)| The SSID ids to be removed from the network policy | 

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

# **get_network_policy**
> XiqNetworkPolicy get_network_policy(id)

Get the network policy

Get an existing network policy by ID.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID

    try:
        # Get the network policy
        api_response = api_instance.get_network_policy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->get_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 

### Return type

[**XiqNetworkPolicy**](XiqNetworkPolicy.md)

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

# **list_network_polices**
> PagedXiqNetworkPolicy list_network_polices(page=page, limit=limit, policy_names=policy_names, keyword=keyword, fields=fields, view=view)

List network policies

List a page of network policies.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
policy_names = ['policy_names_example'] # list[str] | The list of full network policy names to filter the query (optional)
keyword = 'keyword_example' # str | The keyword to partial search by network policy name (optional)
fields = [extremecloudiq.XiqNetworkPolicyField()] # list[XiqNetworkPolicyField] | The network policy fields to return (optional)
view = extremecloudiq.XiqNetworkPolicyView() # XiqNetworkPolicyView | The views to return network policy fields (Check fields for each view at XiqNetworkPolicyView schema) (optional)

    try:
        # List network policies
        api_response = api_instance.list_network_polices(page=page, limit=limit, policy_names=policy_names, keyword=keyword, fields=fields, view=view)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->list_network_polices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **policy_names** | [**list[str]**](str.md)| The list of full network policy names to filter the query | [optional] 
 **keyword** | **str**| The keyword to partial search by network policy name | [optional] 
 **fields** | [**list[XiqNetworkPolicyField]**](XiqNetworkPolicyField.md)| The network policy fields to return | [optional] 
 **view** | [**XiqNetworkPolicyView**](.md)| The views to return network policy fields (Check fields for each view at XiqNetworkPolicyView schema) | [optional] 

### Return type

[**PagedXiqNetworkPolicy**](PagedXiqNetworkPolicy.md)

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

# **list_ssids_by_network_policy**
> PagedXiqSsid list_ssids_by_network_policy(id, page=page, limit=limit)

List SSIDs for a network policy

List a page of SSIDs for a specific network policy.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List SSIDs for a network policy
        api_response = api_instance.list_ssids_by_network_policy(id, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->list_ssids_by_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqSsid**](PagedXiqSsid.md)

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

# **update_network_policy**
> XiqNetworkPolicy update_network_policy(id, xiq_update_network_policy_request)

Update the network policy

Update network policy by ID.

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
    api_instance = extremecloudiq.NetworkPolicyApi(api_client)
    id = 56 # int | The network policy ID
xiq_update_network_policy_request = extremecloudiq.XiqUpdateNetworkPolicyRequest() # XiqUpdateNetworkPolicyRequest | The body of update network policy API

    try:
        # Update the network policy
        api_response = api_instance.update_network_policy(id, xiq_update_network_policy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkPolicyApi->update_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The network policy ID | 
 **xiq_update_network_policy_request** | [**XiqUpdateNetworkPolicyRequest**](XiqUpdateNetworkPolicyRequest.md)| The body of update network policy API | 

### Return type

[**XiqNetworkPolicy**](XiqNetworkPolicy.md)

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

