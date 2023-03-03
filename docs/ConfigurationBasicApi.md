# extremecloudiq.ConfigurationBasicApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vlan_profile**](ConfigurationBasicApi.md#create_vlan_profile) | **POST** /vlan-profiles | Create VLAN profile
[**delete_vlan_profile**](ConfigurationBasicApi.md#delete_vlan_profile) | **DELETE** /vlan-profiles/{id} | Delete a VLAN profile
[**delete_vlan_profiles**](ConfigurationBasicApi.md#delete_vlan_profiles) | **POST** /vlan-profiles/:delete | [LRO] Delete VLAN profiles
[**get_vlan_profile**](ConfigurationBasicApi.md#get_vlan_profile) | **GET** /vlan-profiles/{id} | Get a VLAN profile
[**list_vlan_profiles**](ConfigurationBasicApi.md#list_vlan_profiles) | **GET** /vlan-profiles | List VLAN profiles
[**update_vlan_profile**](ConfigurationBasicApi.md#update_vlan_profile) | **PATCH** /vlan-profiles/{id} | Update a VLAN profile


# **create_vlan_profile**
> XiqVlanProfile create_vlan_profile(xiq_create_vlan_profile_request)

Create VLAN profile

Create a new VLAN profile.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    xiq_create_vlan_profile_request = extremecloudiq.XiqCreateVlanProfileRequest() # XiqCreateVlanProfileRequest | The payload to create new VLAN profile

    try:
        # Create VLAN profile
        api_response = api_instance.create_vlan_profile(xiq_create_vlan_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->create_vlan_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_vlan_profile_request** | [**XiqCreateVlanProfileRequest**](XiqCreateVlanProfileRequest.md)| The payload to create new VLAN profile | 

### Return type

[**XiqVlanProfile**](XiqVlanProfile.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vlan_profile**
> delete_vlan_profile(id)

Delete a VLAN profile

Delete a specific VLAN profile by ID.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    id = 56 # int | The VLAN profile ID

    try:
        # Delete a VLAN profile
        api_instance.delete_vlan_profile(id)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->delete_vlan_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The VLAN profile ID | 

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

# **delete_vlan_profiles**
> delete_vlan_profiles(xiq_vlan_profile_filter, _async=_async)

[LRO] Delete VLAN profiles

Delete VLAN profiles.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    xiq_vlan_profile_filter = extremecloudiq.XiqVlanProfileFilter() # XiqVlanProfileFilter | 
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Delete VLAN profiles
        api_instance.delete_vlan_profiles(xiq_vlan_profile_filter, _async=_async)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->delete_vlan_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_vlan_profile_filter** | [**XiqVlanProfileFilter**](XiqVlanProfileFilter.md)|  | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

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

# **get_vlan_profile**
> XiqVlanProfile get_vlan_profile(id)

Get a VLAN profile

Get a specific VLAN profile by ID.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    id = 56 # int | The VLAN profile ID

    try:
        # Get a VLAN profile
        api_response = api_instance.get_vlan_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->get_vlan_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The VLAN profile ID | 

### Return type

[**XiqVlanProfile**](XiqVlanProfile.md)

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

# **list_vlan_profiles**
> PagedXiqVlanProfile list_vlan_profiles(page=page, limit=limit)

List VLAN profiles

Get a page of VLAN profiles.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)

    try:
        # List VLAN profiles
        api_response = api_instance.list_vlan_profiles(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->list_vlan_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]

### Return type

[**PagedXiqVlanProfile**](PagedXiqVlanProfile.md)

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

# **update_vlan_profile**
> XiqVlanProfile update_vlan_profile(id, xiq_update_vlan_profile_request)

Update a VLAN profile

Update a specific VLAN profile.

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
    api_instance = extremecloudiq.ConfigurationBasicApi(api_client)
    id = 56 # int | The VLAN profile ID.
xiq_update_vlan_profile_request = extremecloudiq.XiqUpdateVlanProfileRequest() # XiqUpdateVlanProfileRequest | The payload to update VLAN profile

    try:
        # Update a VLAN profile
        api_response = api_instance.update_vlan_profile(id, xiq_update_vlan_profile_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationBasicApi->update_vlan_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The VLAN profile ID. | 
 **xiq_update_vlan_profile_request** | [**XiqUpdateVlanProfileRequest**](XiqUpdateVlanProfileRequest.md)| The payload to update VLAN profile | 

### Return type

[**XiqVlanProfile**](XiqVlanProfile.md)

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

