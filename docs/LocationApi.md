# extremecloudiq.LocationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_building**](LocationApi.md#create_building) | **POST** /locations/building | Create building
[**create_floor**](LocationApi.md#create_floor) | **POST** /locations/floor | Create floor
[**create_location**](LocationApi.md#create_location) | **POST** /locations | Create location
[**delete_building**](LocationApi.md#delete_building) | **DELETE** /locations/building/{id} | Delete building by ID
[**delete_floor**](LocationApi.md#delete_floor) | **DELETE** /locations/floor/{id} | Delete floor by ID
[**delete_location**](LocationApi.md#delete_location) | **DELETE** /locations/{id} | Delete location by ID
[**get_location_tree**](LocationApi.md#get_location_tree) | **GET** /locations/tree | Get location tree
[**initialize_location**](LocationApi.md#initialize_location) | **POST** /locations/:init | Initialize organization location
[**update_building**](LocationApi.md#update_building) | **PUT** /locations/building/{id} | Update building
[**update_floor**](LocationApi.md#update_floor) | **PUT** /locations/floor/{id} | Update floor
[**update_location**](LocationApi.md#update_location) | **PUT** /locations/{id} | Update location
[**upload_floorplan**](LocationApi.md#upload_floorplan) | **POST** /locations/floorplan | Upload floorplan


# **create_building**
> XiqBuilding create_building(xiq_create_building_request)

Create building

Create a new building under the parent location.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_building_request = extremecloudiq.XiqCreateBuildingRequest() # XiqCreateBuildingRequest | Create building request body

    try:
        # Create building
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

# **create_floor**
> XiqFloor create_floor(xiq_create_floor_request)

Create floor

Create a new floor under the parent building.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_floor_request = extremecloudiq.XiqCreateFloorRequest() # XiqCreateFloorRequest | Create floor request body

    try:
        # Create floor
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

# **create_location**
> XiqLocation create_location(xiq_create_location_request)

Create location

Create a new location under the parent location.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    xiq_create_location_request = extremecloudiq.XiqCreateLocationRequest() # XiqCreateLocationRequest | Create location request body

    try:
        # Create location
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

# **delete_building**
> delete_building(id, force_delete=force_delete)

Delete building by ID

Delete the building for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The building ID
force_delete = False # bool | Force deletion of this building and its descendants recursively (optional) (default to False)

    try:
        # Delete building by ID
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

# **delete_floor**
> delete_floor(id)

Delete floor by ID

Delete the floor for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The floor ID

    try:
        # Delete floor by ID
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

# **delete_location**
> str delete_location(id, force_delete=force_delete)

Delete location by ID

Delete the location for the specified ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The location ID
force_delete = False # bool | Force deletion of this location and its descendants recursively (optional) (default to False)

    try:
        # Delete location by ID
        api_response = api_instance.delete_location(id, force_delete=force_delete)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocationApi->delete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The location ID | 
 **force_delete** | **bool**| Force deletion of this location and its descendants recursively | [optional] [default to False]

### Return type

**str**

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

# **get_location_tree**
> list[XiqLocation] get_location_tree(parent_id=parent_id, expand_children=expand_children)

Get location tree

Get location hierarchical tree.

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

# **initialize_location**
> XiqLocation initialize_location(xiq_initialize_location_request)

Initialize organization location

Initialize the organization location hierarchy tree.

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

# **update_building**
> XiqBuilding update_building(id, xiq_update_building_request)

Update building

Update the building information with the building ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The building ID
xiq_update_building_request = extremecloudiq.XiqUpdateBuildingRequest() # XiqUpdateBuildingRequest | Update building request body

    try:
        # Update building
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

# **update_floor**
> XiqFloor update_floor(id, xiq_update_floor_request)

Update floor

Update floor information with the floor ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The floor ID.
xiq_update_floor_request = extremecloudiq.XiqUpdateFloorRequest() # XiqUpdateFloorRequest | Update floor request body

    try:
        # Update floor
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

# **update_location**
> XiqLocation update_location(id, xiq_update_location_request)

Update location

Update the location information with the specified location ID.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    id = 56 # int | The location ID
xiq_update_location_request = extremecloudiq.XiqUpdateLocationRequest() # XiqUpdateLocationRequest | Update location request body

    try:
        # Update location
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

# **upload_floorplan**
> upload_floorplan(file)

Upload floorplan

Upload the floorplan map for the VIQ.

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
    api_instance = extremecloudiq.LocationApi(api_client)
    file = '/path/to/file' # file | The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 500 KB.

    try:
        # Upload floorplan
        api_instance.upload_floorplan(file)
    except ApiException as e:
        print("Exception when calling LocationApi->upload_floorplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 500 KB. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

