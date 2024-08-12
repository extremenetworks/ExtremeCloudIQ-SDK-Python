# extremecloudiq.LocationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_building**](LocationApi.md#create_building) | **POST** /locations/building | Create a building
[**create_floor**](LocationApi.md#create_floor) | **POST** /locations/floor | Create a floor
[**create_location**](LocationApi.md#create_location) | **POST** /locations | Create a location
[**create_site**](LocationApi.md#create_site) | **POST** /locations/site | Create a site
[**delete_building**](LocationApi.md#delete_building) | **DELETE** /locations/building/{id} | Delete a building by ID
[**delete_floor**](LocationApi.md#delete_floor) | **DELETE** /locations/floor/{id} | Delete a floor by ID
[**delete_location**](LocationApi.md#delete_location) | **DELETE** /locations/{id} | Delete a location by ID
[**delete_site**](LocationApi.md#delete_site) | **DELETE** /locations/site/{id} | Delete a site by ID
[**get_building**](LocationApi.md#get_building) | **GET** /locations/building/{id} | Get a building by ID
[**get_floor**](LocationApi.md#get_floor) | **GET** /locations/floor/{id} | Get a floor by ID
[**get_location_devices_list**](LocationApi.md#get_location_devices_list) | **GET** /locations/tree/devices | Get devices on the location hierarchy.
[**get_location_maps_list**](LocationApi.md#get_location_maps_list) | **GET** /locations/tree/maps | Get maps on the location hierarchy.
[**get_location_tree**](LocationApi.md#get_location_tree) | **GET** /locations/tree | Get location tree
[**get_site**](LocationApi.md#get_site) | **GET** /locations/site/{id} | Get a site by ID
[**initialize_location**](LocationApi.md#initialize_location) | **POST** /locations/:init | Initialize organization location
[**list_buildings**](LocationApi.md#list_buildings) | **GET** /locations/building | List buildings
[**list_floors**](LocationApi.md#list_floors) | **GET** /locations/floor | List floors
[**list_sites**](LocationApi.md#list_sites) | **GET** /locations/site | List sites
[**start_ekahau_import**](LocationApi.md#start_ekahau_import) | **POST** /locations/import/ekahau | [LRO] Import one or more floors from an Ekahau archive
[**update_building**](LocationApi.md#update_building) | **PUT** /locations/building/{id} | Update a building
[**update_floor**](LocationApi.md#update_floor) | **PUT** /locations/floor/{id} | Update a floor
[**update_location**](LocationApi.md#update_location) | **PUT** /locations/{id} | Update a location
[**update_site**](LocationApi.md#update_site) | **PUT** /locations/site/{id} | Update a site by ID
[**upload_floorplan**](LocationApi.md#upload_floorplan) | **POST** /locations/floorplan | Upload floorplan


# **create_building**
> XiqBuilding create_building(xiq_create_building_request)

Create a building

Create a new building under the parent site.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_building_request = extremecloudiq.XiqCreateBuildingRequest() # XiqCreateBuildingRequest | Create building request body

    try:
        # Create a building
        api_response = api_instance.create_building(xiq_create_building_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->create_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_building_request** | [**XiqCreateBuildingRequest**](XiqCreateBuildingRequest.md)| Create building request body | 

### Return type

[**XiqBuilding**](XiqBuilding.md)

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

# **create_floor**
> XiqFloor create_floor(xiq_create_floor_request)

Create a floor

Create a new floor under the parent building.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_floor_request = extremecloudiq.XiqCreateFloorRequest() # XiqCreateFloorRequest | Create floor request body

    try:
        # Create a floor
        api_response = api_instance.create_floor(xiq_create_floor_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->create_floor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_floor_request** | [**XiqCreateFloorRequest**](XiqCreateFloorRequest.md)| Create floor request body | 

### Return type

[**XiqFloor**](XiqFloor.md)

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

# **create_location**
> XiqLocation create_location(xiq_create_location_request)

Create a location

Create a new location under the parent location.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_location_request = extremecloudiq.XiqCreateLocationRequest() # XiqCreateLocationRequest | Create location request body

    try:
        # Create a location
        api_response = api_instance.create_location(xiq_create_location_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->create_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_location_request** | [**XiqCreateLocationRequest**](XiqCreateLocationRequest.md)| Create location request body | 

### Return type

[**XiqLocation**](XiqLocation.md)

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

# **create_site**
> XiqSite create_site(xiq_create_site_request)

Create a site

Create a new site under the site group.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_site_request = extremecloudiq.XiqCreateSiteRequest() # XiqCreateSiteRequest | Create site request body

    try:
        # Create a site
        api_response = api_instance.create_site(xiq_create_site_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->create_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_site_request** | [**XiqCreateSiteRequest**](XiqCreateSiteRequest.md)| Create site request body | 

### Return type

[**XiqSite**](XiqSite.md)

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

# **delete_building**
> delete_building(id, force_delete=force_delete)

Delete a building by ID

Delete a building for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The building ID
force_delete = False # bool | Force deletion of this building and its descendants recursively (optional) (default to False)

    try:
        # Delete a building by ID
        api_instance.delete_building(id, force_delete=force_delete)
    except ApiException as e:
        print("Exception when calling LocationApi->delete_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The building ID | 
 **force_delete** | **bool**| Force deletion of this building and its descendants recursively | [optional] [default to False]

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

# **delete_floor**
> delete_floor(id)

Delete a floor by ID

Delete a floor for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The floor ID

    try:
        # Delete a floor by ID
        api_instance.delete_floor(id)
    except ApiException as e:
        print("Exception when calling LocationApi->delete_floor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The floor ID | 

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

# **delete_location**
> delete_location(id, force_delete=force_delete)

Delete a location by ID

Delete a location for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The location ID
force_delete = False # bool | Force deletion of this location and its descendants recursively (optional) (default to False)

    try:
        # Delete a location by ID
        api_instance.delete_location(id, force_delete=force_delete)
    except ApiException as e:
        print("Exception when calling LocationApi->delete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The location ID | 
 **force_delete** | **bool**| Force deletion of this location and its descendants recursively | [optional] [default to False]

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

# **delete_site**
> delete_site(id, force_delete=force_delete)

Delete a site by ID

Delete a site for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The site ID
force_delete = False # bool | Force deletion of this site and its descendants recursively (optional) (default to False)

    try:
        # Delete a site by ID
        api_instance.delete_site(id, force_delete=force_delete)
    except ApiException as e:
        print("Exception when calling LocationApi->delete_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The site ID | 
 **force_delete** | **bool**| Force deletion of this site and its descendants recursively | [optional] [default to False]

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

# **get_building**
> XiqBuilding get_building(id)

Get a building by ID

Get the building for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The building ID

    try:
        # Get a building by ID
        api_response = api_instance.get_building(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The building ID | 

### Return type

[**XiqBuilding**](XiqBuilding.md)

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

# **get_floor**
> XiqFloor get_floor(id)

Get a floor by ID

Get the floor for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The floor ID

    try:
        # Get a floor by ID
        api_response = api_instance.get_floor(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_floor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The floor ID | 

### Return type

[**XiqFloor**](XiqFloor.md)

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

# **get_location_devices_list**
> PagedXiqLocationTreeDevice get_location_devices_list(page=page, limit=limit, location_id=location_id, expand_children=expand_children)

Get devices on the location hierarchy.

Get devices on the location hierarchy with pagination.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
location_id = 56 # int | The location ID, or null for all locations. (optional)
expand_children = True # bool | Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. (optional) (default to True)

    try:
        # Get devices on the location hierarchy.
        api_response = api_instance.get_location_devices_list(page=page, limit=limit, location_id=location_id, expand_children=expand_children)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_location_devices_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **location_id** | **int**| The location ID, or null for all locations. | [optional] 
 **expand_children** | **bool**| Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. | [optional] [default to True]

### Return type

[**PagedXiqLocationTreeDevice**](PagedXiqLocationTreeDevice.md)

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

# **get_location_maps_list**
> PagedXiqLocationTreeMap get_location_maps_list(page=page, limit=limit, location_id=location_id, expand_children=expand_children)

Get maps on the location hierarchy.

Get maps on the location hierarchy with pagination.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
location_id = 56 # int | The location ID, or null for all locations. (optional)
expand_children = True # bool | Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. (optional) (default to True)

    try:
        # Get maps on the location hierarchy.
        api_response = api_instance.get_location_maps_list(page=page, limit=limit, location_id=location_id, expand_children=expand_children)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_location_maps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **location_id** | **int**| The location ID, or null for all locations. | [optional] 
 **expand_children** | **bool**| Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. | [optional] [default to True]

### Return type

[**PagedXiqLocationTreeMap**](PagedXiqLocationTreeMap.md)

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

# **get_location_tree**
> list[XiqLocation] get_location_tree(parent_id=parent_id, expand_children=expand_children)

Get location tree

Get location hierarchical tree.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    parent_id = 56 # int | The parent location ID, return root locations if parent is null (optional)
expand_children = True # bool | Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. (optional) (default to True)

    try:
        # Get location tree
        api_response = api_instance.get_location_tree(parent_id=parent_id, expand_children=expand_children)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_location_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| The parent location ID, return root locations if parent is null | [optional] 
 **expand_children** | **bool**| Whether to return the child locations recursively, default is true. Set it to false to improve performance when there are a lot of child locations. | [optional] [default to True]

### Return type

[**list[XiqLocation]**](XiqLocation.md)

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

# **get_site**
> XiqSite get_site(id)

Get a site by ID

Get a site for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The site ID

    try:
        # Get a site by ID
        api_response = api_instance.get_site(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The site ID | 

### Return type

[**XiqSite**](XiqSite.md)

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

# **initialize_location**
> XiqLocation initialize_location(xiq_initialize_location_request)

Initialize organization location

Initialize the organization location hierarchy tree.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_initialize_location_request = extremecloudiq.XiqInitializeLocationRequest() # XiqInitializeLocationRequest | Initialize organization location request body

    try:
        # Initialize organization location
        api_response = api_instance.initialize_location(xiq_initialize_location_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->initialize_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_initialize_location_request** | [**XiqInitializeLocationRequest**](XiqInitializeLocationRequest.md)| Initialize organization location request body | 

### Return type

[**XiqLocation**](XiqLocation.md)

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

# **list_buildings**
> PagedXiqBuilding list_buildings(page=page, limit=limit, order=order, name=name, ids=ids)

List buildings

List a page of buildings by filter.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order by name (ascending by default) (optional)
name = 'name_example' # str | List buildings by name (case insensitive) (optional)
ids = [56] # list[int] | List buildings by IDs (optional)

    try:
        # List buildings
        api_response = api_instance.list_buildings(page=page, limit=limit, order=order, name=name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->list_buildings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **order** | [**XiqSortOrder**](.md)| The sort order by name (ascending by default) | [optional] 
 **name** | **str**| List buildings by name (case insensitive) | [optional] 
 **ids** | [**list[int]**](int.md)| List buildings by IDs | [optional] 

### Return type

[**PagedXiqBuilding**](PagedXiqBuilding.md)

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

# **list_floors**
> PagedXiqFloor list_floors(page=page, limit=limit, order=order, name=name, ids=ids)

List floors

List a page of floors by filter.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order by name (ascending by default) (optional)
name = 'name_example' # str | List floors by name (case insensitive) (optional)
ids = [56] # list[int] | List floors by IDs (optional)

    try:
        # List floors
        api_response = api_instance.list_floors(page=page, limit=limit, order=order, name=name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->list_floors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **order** | [**XiqSortOrder**](.md)| The sort order by name (ascending by default) | [optional] 
 **name** | **str**| List floors by name (case insensitive) | [optional] 
 **ids** | [**list[int]**](int.md)| List floors by IDs | [optional] 

### Return type

[**PagedXiqFloor**](PagedXiqFloor.md)

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

# **list_sites**
> PagedXiqSite list_sites(page=page, limit=limit, order=order, name=name, ids=ids)

List sites

List a page of sites by filter.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 5000 (optional) (default to 10)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order by name (ascending by default) (optional)
name = 'name_example' # str | List sites by name (case insensitive) (optional)
ids = [56] # list[int] | List sites by IDs (optional)

    try:
        # List sites
        api_response = api_instance.list_sites(page=page, limit=limit, order=order, name=name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->list_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 5000 | [optional] [default to 10]
 **order** | [**XiqSortOrder**](.md)| The sort order by name (ascending by default) | [optional] 
 **name** | **str**| List sites by name (case insensitive) | [optional] 
 **ids** | [**list[int]**](int.md)| List sites by IDs | [optional] 

### Return type

[**PagedXiqSite**](PagedXiqSite.md)

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

# **start_ekahau_import**
> XiqEkahauImportDetails start_ekahau_import(floor_associations, outdoor_site_associations, file, _async=_async, import_custom_ap_configurations=import_custom_ap_configurations)

[LRO] Import one or more floors from an Ekahau archive

Import the specified Ekahau floor(s) from the provided archive.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    floor_associations = [extremecloudiq.XiqEkahauFloorToFloorAssociation()] # list[XiqEkahauFloorToFloorAssociation] | Describes how Ekahau floors are imported into XIQ as floors in buildings.
outdoor_site_associations = [extremecloudiq.XiqEkahauFloorToOutdoorSiteAssociation()] # list[XiqEkahauFloorToOutdoorSiteAssociation] | Describes how Ekahau floors are Imported into XIQ as outdoor sites in site groups.
file = '/path/to/file' # file | The Ekahau archive to import floors from.
_async = False # bool | Whether to enable async mode. (optional) (default to False)
import_custom_ap_configurations = True # bool | Whether to also import or not the custom AP configurations such as: Hostname, TX Power & Channel. (optional) (default to True)

    try:
        # [LRO] Import one or more floors from an Ekahau archive
        api_response = api_instance.start_ekahau_import(floor_associations, outdoor_site_associations, file, _async=_async, import_custom_ap_configurations=import_custom_ap_configurations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->start_ekahau_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floor_associations** | [**list[XiqEkahauFloorToFloorAssociation]**](XiqEkahauFloorToFloorAssociation.md)| Describes how Ekahau floors are imported into XIQ as floors in buildings. | 
 **outdoor_site_associations** | [**list[XiqEkahauFloorToOutdoorSiteAssociation]**](XiqEkahauFloorToOutdoorSiteAssociation.md)| Describes how Ekahau floors are Imported into XIQ as outdoor sites in site groups. | 
 **file** | **file**| The Ekahau archive to import floors from. | 
 **_async** | **bool**| Whether to enable async mode. | [optional] [default to False]
 **import_custom_ap_configurations** | **bool**| Whether to also import or not the custom AP configurations such as: Hostname, TX Power &amp; Channel. | [optional] [default to True]

### Return type

[**XiqEkahauImportDetails**](XiqEkahauImportDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_building**
> XiqBuilding update_building(id, xiq_update_building_request)

Update a building

Update a building information with the building ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The building ID
xiq_update_building_request = extremecloudiq.XiqUpdateBuildingRequest() # XiqUpdateBuildingRequest | Update building request body

    try:
        # Update a building
        api_response = api_instance.update_building(id, xiq_update_building_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->update_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The building ID | 
 **xiq_update_building_request** | [**XiqUpdateBuildingRequest**](XiqUpdateBuildingRequest.md)| Update building request body | 

### Return type

[**XiqBuilding**](XiqBuilding.md)

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

# **update_floor**
> XiqFloor update_floor(id, xiq_update_floor_request)

Update a floor

Update a floor information with the floor ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The floor ID.
xiq_update_floor_request = extremecloudiq.XiqUpdateFloorRequest() # XiqUpdateFloorRequest | Update floor request body

    try:
        # Update a floor
        api_response = api_instance.update_floor(id, xiq_update_floor_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->update_floor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The floor ID. | 
 **xiq_update_floor_request** | [**XiqUpdateFloorRequest**](XiqUpdateFloorRequest.md)| Update floor request body | 

### Return type

[**XiqFloor**](XiqFloor.md)

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

# **update_location**
> XiqLocation update_location(id, xiq_update_location_request)

Update a location

Update a location information with the specified location ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The location ID
xiq_update_location_request = extremecloudiq.XiqUpdateLocationRequest() # XiqUpdateLocationRequest | Update location request body

    try:
        # Update a location
        api_response = api_instance.update_location(id, xiq_update_location_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->update_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The location ID | 
 **xiq_update_location_request** | [**XiqUpdateLocationRequest**](XiqUpdateLocationRequest.md)| Update location request body | 

### Return type

[**XiqLocation**](XiqLocation.md)

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

# **update_site**
> XiqSite update_site(id, xiq_update_site_request)

Update a site by ID

Update a site for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The site ID
xiq_update_site_request = extremecloudiq.XiqUpdateSiteRequest() # XiqUpdateSiteRequest | Update site request body

    try:
        # Update a site by ID
        api_response = api_instance.update_site(id, xiq_update_site_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->update_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The site ID | 
 **xiq_update_site_request** | [**XiqUpdateSiteRequest**](XiqUpdateSiteRequest.md)| Update site request body | 

### Return type

[**XiqSite**](XiqSite.md)

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

# **upload_floorplan**
> upload_floorplan(file)

Upload floorplan

Upload the floorplan map for the VIQ.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    file = '/path/to/file' # file | The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 10 MB.

    try:
        # Upload floorplan
        api_instance.upload_floorplan(file)
    except ApiException as e:
        print("Exception when calling LocationApi->upload_floorplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 10 MB. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

