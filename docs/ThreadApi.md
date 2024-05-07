# extremecloudiq.ThreadApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_thread_network_topology**](ThreadApi.md#get_thread_network_topology) | **GET** /thread/topology | Get thread network topology
[**get_thread_networks**](ThreadApi.md#get_thread_networks) | **GET** /thread/networks | Get active thread networks
[**get_thread_routers**](ThreadApi.md#get_thread_routers) | **GET** /thread/routers | List thread routers


# **get_thread_network_topology**
> XiqThreadNetworkTopology get_thread_network_topology(network_config_ids, router_fields=router_fields, router_views=router_views, client_views=client_views, client_fields=client_fields)

Get thread network topology

Get thread routers, neighboring routers and end-devices

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
    api_instance = extremecloudiq.ThreadApi(api_client)
    network_config_ids = [56] # list[int] | Thread network config id
router_fields = ['router_fields_example'] # list[str] | The thread router fields to return (optional)
router_views = ['router_views_example'] # list[str] | The views to return thread router fields (optional)
client_views = [extremecloudiq.XiqClientView()] # list[XiqClientView] | The views to return client fields (Check fields for each view at XiqClientView schema) (optional)
client_fields = [extremecloudiq.XiqClientField()] # list[XiqClientField] | The client fields to return (optional)

    try:
        # Get thread network topology
        api_response = api_instance.get_thread_network_topology(network_config_ids, router_fields=router_fields, router_views=router_views, client_views=client_views, client_fields=client_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThreadApi->get_thread_network_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_config_ids** | [**list[int]**](int.md)| Thread network config id | 
 **router_fields** | [**list[str]**](str.md)| The thread router fields to return | [optional] 
 **router_views** | [**list[str]**](str.md)| The views to return thread router fields | [optional] 
 **client_views** | [**list[XiqClientView]**](XiqClientView.md)| The views to return client fields (Check fields for each view at XiqClientView schema) | [optional] 
 **client_fields** | [**list[XiqClientField]**](XiqClientField.md)| The client fields to return | [optional] 

### Return type

[**XiqThreadNetworkTopology**](XiqThreadNetworkTopology.md)

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

# **get_thread_networks**
> XiqThreadNetworks get_thread_networks(folder_id, page=page, limit=limit, fields=fields, views=views)

Get active thread networks

Get thread networks with atleast one device

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
    api_instance = extremecloudiq.ThreadApi(api_client)
    folder_id = 56 # int | Thread network config folder id
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
fields = ['fields_example'] # list[str] | The thread network config fields to return (optional)
views = ['views_example'] # list[str] | The views to return thread network config fields (optional)

    try:
        # Get active thread networks
        api_response = api_instance.get_thread_networks(folder_id, page=page, limit=limit, fields=fields, views=views)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThreadApi->get_thread_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Thread network config folder id | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **fields** | [**list[str]**](str.md)| The thread network config fields to return | [optional] 
 **views** | [**list[str]**](str.md)| The views to return thread network config fields | [optional] 

### Return type

[**XiqThreadNetworks**](XiqThreadNetworks.md)

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

# **get_thread_routers**
> PagedXiqThreadRouter get_thread_routers(ids, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, views=views, fields=fields)

List thread routers

List thread routers with pagination.

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
    api_instance = extremecloudiq.ThreadApi(api_client)
    ids = [56] # list[int] | The thread router IDs
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_field = 'sort_field_example' # str | The sort field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order (ascending by default) (optional)
views = ['views_example'] # list[str] | The views to return thread router fields (optional)
fields = ['fields_example'] # list[str] | The thread router fields to return (optional)

    try:
        # List thread routers
        api_response = api_instance.get_thread_routers(ids, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, views=views, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThreadApi->get_thread_routers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| The thread router IDs | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | **str**| The sort field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sort order (ascending by default) | [optional] 
 **views** | [**list[str]**](str.md)| The views to return thread router fields | [optional] 
 **fields** | [**list[str]**](str.md)| The thread router fields to return | [optional] 

### Return type

[**PagedXiqThreadRouter**](PagedXiqThreadRouter.md)

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

