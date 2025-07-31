<a id="__pageTop"></a>
# extremecloudiq.apis.tags.thread_api.ThreadApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_thread_network_topology**](#get_thread_network_topology) | **get** /thread/topology | Get thread network topology
[**get_thread_networks**](#get_thread_networks) | **get** /thread/networks | Get active thread networks
[**get_thread_routers**](#get_thread_routers) | **get** /thread/routers | List thread routers

# **get_thread_network_topology**
<a id="get_thread_network_topology"></a>
> XiqThreadNetworkTopology get_thread_network_topology(network_config_ids)

Get thread network topology

Get thread routers, neighboring routers and end-devices

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import thread_api
from extremecloudiq.model.xiq_client_field import XiqClientField
from extremecloudiq.model.xiq_client_view import XiqClientView
from extremecloudiq.model.xiq_thread_network_topology import XiqThreadNetworkTopology
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
    api_instance = thread_api.ThreadApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'networkConfigIds': [
        1
    ],
    }
    try:
        # Get thread network topology
        api_response = api_instance.get_thread_network_topology(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_network_topology: %s\n" % e)

    # example passing only optional values
    query_params = {
        'networkConfigIds': [
        1
    ],
        'routerFields': [
        "DEVICE_ID"
    ],
        'routerViews': [
        "BASIC"
    ],
        'clientViews': [
        XiqClientView("BASIC")
    ],
        'clientFields': [
        XiqClientField("ID")
    ],
    }
    try:
        # Get thread network topology
        api_response = api_instance.get_thread_network_topology(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_network_topology: %s\n" % e)
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
networkConfigIds | NetworkConfigIdsSchema | | 
routerFields | RouterFieldsSchema | | optional
routerViews | RouterViewsSchema | | optional
clientViews | ClientViewsSchema | | optional
clientFields | ClientFieldsSchema | | optional


# NetworkConfigIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# RouterFieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["DEVICE_ID", "SERIAL_NUMBER", "EUI64", "EXT_MAC", "RLOC16", "GLOBAL_IPV6", "TX_POWER", "REGION", "THREAD_PLATFORM", "DEVICE_ROLE", "ROUTER_INTERFACE", "VETH0", "NETWORK_DATA", "THREAD_MLE_LINK_MODE", "THREAD_VERSION", "LEADER_SERVICE", "BORDER_ROUTER_SERVICE", "BACKBONE_BORDER_ROUTER_SERVICE", "BORDER_AGENT_SERVICE", "COMMISSIONER_SERVICE", "NAT64_SERVICE", "NETWORK_CONFIG", "OWNER_ID", "ORG_ID", "ID", "CREATE_TIME", "UPDATE_TIME", "ACTIVE_CLIENTS", "HOSTNAME", "LAST_REPORTED", "THREAD_CONNECTED", ] 

# RouterViewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["BASIC", "DETAIL", "FULL", ] 

# ClientViewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqClientView**]({{complexTypePrefix}}XiqClientView.md) | [**XiqClientView**]({{complexTypePrefix}}XiqClientView.md) | [**XiqClientView**]({{complexTypePrefix}}XiqClientView.md) |  | 

# ClientFieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqClientField**]({{complexTypePrefix}}XiqClientField.md) | [**XiqClientField**]({{complexTypePrefix}}XiqClientField.md) | [**XiqClientField**]({{complexTypePrefix}}XiqClientField.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_thread_network_topology.ApiResponseFor200) | OK

#### get_thread_network_topology.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqThreadNetworkTopology**](../../models/XiqThreadNetworkTopology.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_thread_networks**
<a id="get_thread_networks"></a>
> XiqThreadNetworks get_thread_networks(folder_id)

Get active thread networks

Get thread networks with atleast one device

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import thread_api
from extremecloudiq.model.xiq_thread_networks import XiqThreadNetworks
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
    api_instance = thread_api.ThreadApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'folderId': 1,
    }
    try:
        # Get active thread networks
        api_response = api_instance.get_thread_networks(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_networks: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'folderId': 1,
        'limit': 10,
        'fields': [
        "ID"
    ],
        'views': [
        "BASIC"
    ],
    }
    try:
        # Get active thread networks
        api_response = api_instance.get_thread_networks(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_networks: %s\n" % e)
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
folderId | FolderIdSchema | | 
limit | LimitSchema | | optional
fields | FieldsSchema | | optional
views | ViewsSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# FolderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ID", "CHANNEL", "CHANNEL_MASK", "EXT_PAN_ID", "MESH_LOCAL_PREFIX", "NETWORK_KEY", "NETWORK_NAME", "PAN_ID", "PSKC", "OBTAIN_NETWORK_KEY_ENABLED", "NATIVE_COMMISSIONING_ENABLED", "ROUTERS_ENABLED", "EXTERNAL_COMMISSIONING_ENABLED", "BEACONS_ENABLED", "COMMERCIAL_COMMISSIONING_ENABLED", "AUTONOMOUS_ENROLLMENT_ENABLED", "NETWORK_KEY_PROVISIONING_ENABLED", "NON_CCM_ROUTERS_ENABLED", "ACTIVE_TIMESTAMP", ] 

# ViewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["BASIC", "FULL", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_thread_networks.ApiResponseFor200) | OK

#### get_thread_networks.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqThreadNetworks**](../../models/XiqThreadNetworks.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_thread_routers**
<a id="get_thread_routers"></a>
> PagedXiqThreadRouter get_thread_routers(ids)

List thread routers

List thread routers with pagination.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import thread_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.paged_xiq_thread_router import PagedXiqThreadRouter
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
    api_instance = thread_api.ThreadApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ids': [
        1
    ],
    }
    try:
        # List thread routers
        api_response = api_instance.get_thread_routers(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_routers: %s\n" % e)

    # example passing only optional values
    query_params = {
        'ids': [
        1
    ],
        'page': 1,
        'limit': 10,
        'sortField': "SERIAL_NUMBER",
        'sortOrder': XiqSortOrder("ASC"),
        'views': [
        "BASIC"
    ],
        'fields': [
        "DEVICE_ID"
    ],
    }
    try:
        # List thread routers
        api_response = api_instance.get_thread_routers(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling ThreadApi->get_thread_routers: %s\n" % e)
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
ids | IdsSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
views | ViewsSchema | | optional
fields | FieldsSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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

# SortFieldSchema

All available thread router sort fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | All available thread router sort fields | must be one of ["SERIAL_NUMBER", "EUI64", "EXT_MAC", "RLOC16", "GLOBAL_IPV6", "TX_POWER", "REGION", "THREAD_PLATFORM", "DEVICE_ROLE", "ROUTER_INTERFACE_NAME", "ROUTER_INTERFACE_IS_ACTIVE", "ROUTER_INTERFACE_IS_BROADCAST", "ROUTER_INTERFACE_IS_LOOPBACK", "ROUTER_INTERFACE_IS_POINT_TO_POINT", "ROUTER_INTERFACE_IS_RUNNING", "ROUTER_INTERFACE_IS_ARP", "ROUTER_INTERFACE_IS_PROMISC", "ROUTER_INTERFACE_IS_ALL_MULTI", "ROUTER_INTERFACE_IS_MULTICAST", "ROUTER_INTERFACE_IS_DYNAMIC", "ROUTER_INTERFACE_MTU", "ROUTER_INTERFACE_HW_MAC", "ROUTER_INTERFACE_IPV4", "ROUTER_INTERFACE_IPV4_MASK", "ROUTER_INTERFACE_IPV4_BROADCAST", "VETH0_INTERFACE_NAME", "VETH0_IS_ACTIVE", "VETH0_IS_BROADCAST", "VETH0_IS_LOOPBACK", "VETH0_IS_POINT_TO_POINT", "VETH0_IS_RUNNING", "VETH0_IS_ARP", "VETH0_IS_PROMISC", "VETH0_IS_ALL_MULTI", "VETH0_IS_MULTICAST", "VETH0_IS_DYNAMIC", "VETH0_MTU", "VETH0_HW_MAC", "VETH0_IPV4", "VETH0_IPV4_MASK", "VETH0_IPV4_BROADCAST", "NETWORK_DATA_LENGTH", "NETWORK_DATA_MAX_LENGTH", "RX_ON_WHEN_IDLE", "FULL_THREAD_DEVICE", "FULL_NETWORK_DATA", "THREAD_VERSION", "BUILD_VERSION", "API_VERSION", "RCP_VERSION", "LEADER_PARTITION_ID", "LEADER_WEIGHTING", "LEADER_FULL_NETWORK_DATA_VERSION", "LEADER_STABLE_NETWORK_DATA_VERSION", "BORDER_ROUTER_STATE", "BORDER_NAT64_LOCAL_PREFIX", "BORDER_NAT64_FAVORED_PREFIX", "BORDER_NAT64_FAVORED_PREFERENCE", "BORDER_NAT64_0MR_LOCAL_PREFIX", "BORDER_NAT64_0MR_FAVORED_PREFIX", "BORDER_NAT64_0MR_FAVORED_PREFERENCE", "BORDER_NAT64_640N_LINK_LOCAL_PREFIX", "BORDER_NAT64_640N_LINK_FAVORED_PREFIX", "BORDER_NAT64_640N_LINK_FAVORED_PREFERENCE", "BACKBONE_BORDER_ROUTER_STATE", "BORDER_AGENT_STATE", "BORDER_AGENT_UDP_PORT", "COMMISSIONER_STATE", "NAT64_PREFIX_MANAGER_STATE", "NAT64_TRANSLATOR_STATE", "NAT64_TRANSLATOR_CIDR", "HOSTNAME", ] 

# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# ViewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["BASIC", "DETAIL", "FULL", ] 

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["DEVICE_ID", "SERIAL_NUMBER", "EUI64", "EXT_MAC", "RLOC16", "GLOBAL_IPV6", "TX_POWER", "REGION", "THREAD_PLATFORM", "DEVICE_ROLE", "ROUTER_INTERFACE", "VETH0", "NETWORK_DATA", "THREAD_MLE_LINK_MODE", "THREAD_VERSION", "LEADER_SERVICE", "BORDER_ROUTER_SERVICE", "BACKBONE_BORDER_ROUTER_SERVICE", "BORDER_AGENT_SERVICE", "COMMISSIONER_SERVICE", "NAT64_SERVICE", "NETWORK_CONFIG", "OWNER_ID", "ORG_ID", "ID", "CREATE_TIME", "UPDATE_TIME", "ACTIVE_CLIENTS", "HOSTNAME", "LAST_REPORTED", "THREAD_CONNECTED", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_thread_routers.ApiResponseFor200) | OK

#### get_thread_routers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqThreadRouter**](../../models/PagedXiqThreadRouter.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

