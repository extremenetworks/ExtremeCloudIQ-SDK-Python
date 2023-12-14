# extremecloudiq.ClientApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_client**](ClientApi.md#disconnect_client) | **DELETE** /clients/byMac/{clientMac} | Disconnect the client
[**get_active_clients_count**](ClientApi.md#get_active_clients_count) | **GET** /clients/active/count | Get active clients count
[**get_client**](ClientApi.md#get_client) | **GET** /clients/{id} | Get client info
[**get_client_by_mac**](ClientApi.md#get_client_by_mac) | **GET** /clients/byMac/{clientMac} | Get client info by mac
[**get_client_summary**](ClientApi.md#get_client_summary) | **GET** /clients/summary | Get client summary metrics
[**get_client_usage**](ClientApi.md#get_client_usage) | **GET** /clients/usage | Get usage per client
[**list_active_clients**](ClientApi.md#list_active_clients) | **GET** /clients/active | List active clients
[**set_clients_aliases**](ClientApi.md#set_clients_aliases) | **PUT** /clients/alias | Set the aliases for multiple clients


# **disconnect_client**
> disconnect_client(client_mac)

Disconnect the client

Disconnect the client by macAddress.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    client_mac = 'client_mac_example' # str | The client mac address

    try:
        # Disconnect the client
        api_instance.disconnect_client(client_mac)
    except ApiException as e:
        print("Exception when calling ClientApi->disconnect_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_mac** | **str**| The client mac address | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_active_clients_count**
> int get_active_clients_count(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_connection_types=client_connection_types, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, search_string=search_string)

Get active clients count

Get number of active clients with filters and pagination.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    location_ids = [56] # list[int] | The location IDs (optional)
device_ids = [56] # list[int] | The device IDs (optional)
vlans = [56] # list[int] | The associate VLAN IDs (optional)
user_profile_names = ['user_profile_names_example'] # list[str] | The user profile names (optional)
ssids = ['ssids_example'] # list[str] | The SSIDs (optional)
client_os_names = ['client_os_names_example'] # list[str] | The client os names (optional)
client_connection_types = [56] # list[int] | The client connection types: 1 - WIRELESS, 2 - WIRED, -1 - UNDETERMINED (optional)
client_health_status = 56 # int | The client health status: 1 - HEALTHY, 2 - POOR (optional)
exclude_locally_managed = False # bool | Return Cloud managed Devices' clients count (optional) (default to False)
search_string = 'search_string_example' # str | The search string (optional)

    try:
        # Get active clients count
        api_response = api_instance.get_active_clients_count(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_connection_types=client_connection_types, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, search_string=search_string)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_active_clients_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | [**list[int]**](int.md)| The location IDs | [optional] 
 **device_ids** | [**list[int]**](int.md)| The device IDs | [optional] 
 **vlans** | [**list[int]**](int.md)| The associate VLAN IDs | [optional] 
 **user_profile_names** | [**list[str]**](str.md)| The user profile names | [optional] 
 **ssids** | [**list[str]**](str.md)| The SSIDs | [optional] 
 **client_os_names** | [**list[str]**](str.md)| The client os names | [optional] 
 **client_connection_types** | [**list[int]**](int.md)| The client connection types: 1 - WIRELESS, 2 - WIRED, -1 - UNDETERMINED | [optional] 
 **client_health_status** | **int**| The client health status: 1 - HEALTHY, 2 - POOR | [optional] 
 **exclude_locally_managed** | **bool**| Return Cloud managed Devices&#39; clients count | [optional] [default to False]
 **search_string** | **str**| The search string | [optional] 

### Return type

**int**

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_client**
> XiqClient get_client(id, views=views, fields=fields)

Get client info

Get client detailed information.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    id = 56 # int | The client ID
views = [extremecloudiq.XiqClientView()] # list[XiqClientView] | The views to return client fields (Check fields for each view at XiqClientView schema) (optional)
fields = [extremecloudiq.XiqClientField()] # list[XiqClientField] | The client fields to return (optional)

    try:
        # Get client info
        api_response = api_instance.get_client(id, views=views, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The client ID | 
 **views** | [**list[XiqClientView]**](XiqClientView.md)| The views to return client fields (Check fields for each view at XiqClientView schema) | [optional] 
 **fields** | [**list[XiqClientField]**](XiqClientField.md)| The client fields to return | [optional] 

### Return type

[**XiqClient**](XiqClient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_client_by_mac**
> XiqClient get_client_by_mac(client_mac, views=views, fields=fields)

Get client info by mac

Get client detailed information based on clientMac.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    client_mac = 'client_mac_example' # str | The client mac address
views = [extremecloudiq.XiqClientView()] # list[XiqClientView] | The views to return client fields (Check fields for each view at XiqClientView schema) (optional)
fields = [extremecloudiq.XiqClientField()] # list[XiqClientField] | The client fields to return (optional)

    try:
        # Get client info by mac
        api_response = api_instance.get_client_by_mac(client_mac, views=views, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_client_by_mac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_mac** | **str**| The client mac address | 
 **views** | [**list[XiqClientView]**](XiqClientView.md)| The views to return client fields (Check fields for each view at XiqClientView schema) | [optional] 
 **fields** | [**list[XiqClientField]**](XiqClientField.md)| The client fields to return | [optional] 

### Return type

[**XiqClient**](XiqClient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_client_summary**
> XiqClientSummary get_client_summary(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, search_string=search_string)

Get client summary metrics

Get number of connected wireless clients and number of detected wired clients.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    location_ids = [56] # list[int] | The location IDs (optional)
device_ids = [56] # list[int] | The device IDs (optional)
vlans = [56] # list[int] | The associate VLAN IDs (optional)
user_profile_names = ['user_profile_names_example'] # list[str] | The user profile names (optional)
ssids = ['ssids_example'] # list[str] | The SSIDs (optional)
client_os_names = ['client_os_names_example'] # list[str] | The client os names (optional)
client_health_status = 56 # int | The client health status: 1 - HEALTHY, 2 - POOR (optional)
exclude_locally_managed = False # bool | Return Cloud managed Devices' clients count (optional) (default to False)
search_string = 'search_string_example' # str | The search string (optional)

    try:
        # Get client summary metrics
        api_response = api_instance.get_client_summary(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, search_string=search_string)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_client_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | [**list[int]**](int.md)| The location IDs | [optional] 
 **device_ids** | [**list[int]**](int.md)| The device IDs | [optional] 
 **vlans** | [**list[int]**](int.md)| The associate VLAN IDs | [optional] 
 **user_profile_names** | [**list[str]**](str.md)| The user profile names | [optional] 
 **ssids** | [**list[str]**](str.md)| The SSIDs | [optional] 
 **client_os_names** | [**list[str]**](str.md)| The client os names | [optional] 
 **client_health_status** | **int**| The client health status: 1 - HEALTHY, 2 - POOR | [optional] 
 **exclude_locally_managed** | **bool**| Return Cloud managed Devices&#39; clients count | [optional] [default to False]
 **search_string** | **str**| The search string | [optional] 

### Return type

[**XiqClientSummary**](XiqClientSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_client_usage**
> list[XiqClientUsage] get_client_usage(client_ids, start_time, end_time)

Get usage per client

Get the client usage.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    client_ids = [56] # list[int] | The client IDs
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970

    try:
        # Get usage per client
        api_response = api_instance.get_client_usage(client_ids, start_time, end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_client_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_ids** | [**list[int]**](int.md)| The client IDs | 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970 | 

### Return type

[**list[XiqClientUsage]**](XiqClientUsage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **list_active_clients**
> PagedXiqClient list_active_clients(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_connection_types=client_connection_types, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, user_names=user_names, search_string=search_string, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, views=views, fields=fields)

List active clients

List active clients with filters and pagination.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    location_ids = [56] # list[int] | The location IDs (optional)
device_ids = [56] # list[int] | The device IDs (optional)
vlans = [56] # list[int] | The associate vlan IDs (optional)
user_profile_names = ['user_profile_names_example'] # list[str] | The user profile names (optional)
ssids = ['ssids_example'] # list[str] | The SSIDs (optional)
client_os_names = ['client_os_names_example'] # list[str] | The client os names (optional)
client_connection_types = [56] # list[int] | The client connection types: 1 - WIRELESS, 2 - WIRED, -1 - UNDETERMINED (optional)
client_health_status = 56 # int | The client health status: 1 - HEALTHY, 2 - POOR (optional)
exclude_locally_managed = False # bool | Return Cloud managed Devices' clients (optional) (default to False)
user_names = ['user_names_example'] # list[str] | The user names (optional)
search_string = 'search_string_example' # str | The search string (optional)
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
sort_field = extremecloudiq.XiqClientSortField() # XiqClientSortField | Sort field (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | Sort order (ascending by default) (optional)
views = [extremecloudiq.XiqClientView()] # list[XiqClientView] | The views to return client fields (Check fields for each view at XiqClientView schema) (optional)
fields = [extremecloudiq.XiqClientField()] # list[XiqClientField] | The client fields to return (optional)

    try:
        # List active clients
        api_response = api_instance.list_active_clients(location_ids=location_ids, device_ids=device_ids, vlans=vlans, user_profile_names=user_profile_names, ssids=ssids, client_os_names=client_os_names, client_connection_types=client_connection_types, client_health_status=client_health_status, exclude_locally_managed=exclude_locally_managed, user_names=user_names, search_string=search_string, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, views=views, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->list_active_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_ids** | [**list[int]**](int.md)| The location IDs | [optional] 
 **device_ids** | [**list[int]**](int.md)| The device IDs | [optional] 
 **vlans** | [**list[int]**](int.md)| The associate vlan IDs | [optional] 
 **user_profile_names** | [**list[str]**](str.md)| The user profile names | [optional] 
 **ssids** | [**list[str]**](str.md)| The SSIDs | [optional] 
 **client_os_names** | [**list[str]**](str.md)| The client os names | [optional] 
 **client_connection_types** | [**list[int]**](int.md)| The client connection types: 1 - WIRELESS, 2 - WIRED, -1 - UNDETERMINED | [optional] 
 **client_health_status** | **int**| The client health status: 1 - HEALTHY, 2 - POOR | [optional] 
 **exclude_locally_managed** | **bool**| Return Cloud managed Devices&#39; clients | [optional] [default to False]
 **user_names** | [**list[str]**](str.md)| The user names | [optional] 
 **search_string** | **str**| The search string | [optional] 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **sort_field** | [**XiqClientSortField**](.md)| Sort field | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| Sort order (ascending by default) | [optional] 
 **views** | [**list[XiqClientView]**](XiqClientView.md)| The views to return client fields (Check fields for each view at XiqClientView schema) | [optional] 
 **fields** | [**list[XiqClientField]**](XiqClientField.md)| The client fields to return | [optional] 

### Return type

[**PagedXiqClient**](PagedXiqClient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **set_clients_aliases**
> set_clients_aliases(xiq_client_mac_address_alias)

Set the aliases for multiple clients

Bulk update the aliases for multiple clients based on the mac addresses. Empty or null alias value deletes the previous client alias.

### Example

* Bearer (JWT) Authentication (BearerAuth):
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ClientApi(api_client)
    xiq_client_mac_address_alias = [extremecloudiq.XiqClientMacAddressAlias()] # list[XiqClientMacAddressAlias] | A list of client mac addresses and aliases

    try:
        # Set the aliases for multiple clients
        api_instance.set_clients_aliases(xiq_client_mac_address_alias)
    except ApiException as e:
        print("Exception when calling ClientApi->set_clients_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_client_mac_address_alias** | [**list[XiqClientMacAddressAlias]**](XiqClientMacAddressAlias.md)| A list of client mac addresses and aliases | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

