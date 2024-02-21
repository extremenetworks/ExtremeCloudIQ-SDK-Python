# extremecloudiq.LicenseApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_legacy_license**](LicenseApi.md#add_legacy_license) | **POST** /licenses/legacy-licenses | Add legacy license
[**delete_legacy_license**](LicenseApi.md#delete_legacy_license) | **DELETE** /licenses/legacy-licenses/{id} | Delete legacy license
[**get_application_filter**](LicenseApi.md#get_application_filter) | **GET** /licenses/application-filter | Get application filter
[**get_extreme_portal_link_param**](LicenseApi.md#get_extreme_portal_link_param) | **GET** /licenses/extreme-portal-link-param | Get Extreme portal account link parameter
[**get_license_summary**](LicenseApi.md#get_license_summary) | **GET** /licenses/summary | Get license summary
[**get_nac_entitlement_allocation**](LicenseApi.md#get_nac_entitlement_allocation) | **GET** /licenses/nac-entitlement-allocation | Get NAC entitlement allocation
[**get_viq_linked_cuid_info**](LicenseApi.md#get_viq_linked_cuid_info) | **GET** /licenses/viq-cuid-info | Get VIQ linked CUID info
[**list_license_details**](LicenseApi.md#list_license_details) | **GET** /licenses/{licenseType} | List license details
[**list_licenses**](LicenseApi.md#list_licenses) | **GET** /licenses | List licenses
[**set_nac_entitlement_allocation**](LicenseApi.md#set_nac_entitlement_allocation) | **PUT** /licenses/nac-entitlement-allocation | Set NAC entitlement allocation
[**synchronize_licenses**](LicenseApi.md#synchronize_licenses) | **POST** /licenses/:synchronize | Synchronize licenses
[**unlink_extreme_portal**](LicenseApi.md#unlink_extreme_portal) | **POST** /licenses/extreme-portal/:unlink | Unlink Extreme portal account


# **add_legacy_license**
> XiqAddLegacyLicenseResponse add_legacy_license(xiq_add_legacy_license_request)

Add legacy license

Add legacy license.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    xiq_add_legacy_license_request = extremecloudiq.XiqAddLegacyLicenseRequest() # XiqAddLegacyLicenseRequest | The payload to add legacy license key

    try:
        # Add legacy license
        api_response = api_instance.add_legacy_license(xiq_add_legacy_license_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->add_legacy_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_add_legacy_license_request** | [**XiqAddLegacyLicenseRequest**](XiqAddLegacyLicenseRequest.md)| The payload to add legacy license key | 

### Return type

[**XiqAddLegacyLicenseResponse**](XiqAddLegacyLicenseResponse.md)

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

# **delete_legacy_license**
> delete_legacy_license(id)

Delete legacy license

Delete legacy license.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    id = 56 # int | The legacy license ID

    try:
        # Delete legacy license
        api_instance.delete_legacy_license(id)
    except ApiException as e:
        print("Exception when calling LicenseApi->delete_legacy_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The legacy license ID | 

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

# **get_application_filter**
> list[XiqApplicationFilterItem] get_application_filter()

Get application filter

Get the application filter for listing licenses.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Get application filter
        api_response = api_instance.get_application_filter()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_application_filter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqApplicationFilterItem]**](XiqApplicationFilterItem.md)

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

# **get_extreme_portal_link_param**
> XiqExtremePortalLinkParam get_extreme_portal_link_param(url)

Get Extreme portal account link parameter

Get the VIQ-Extreme portal account link parameter.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    url = 'url_example' # str | After linking operation, which web page to redirect to

    try:
        # Get Extreme portal account link parameter
        api_response = api_instance.get_extreme_portal_link_param(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_extreme_portal_link_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| After linking operation, which web page to redirect to | 

### Return type

[**XiqExtremePortalLinkParam**](XiqExtremePortalLinkParam.md)

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

# **get_license_summary**
> XiqLicenseSummary get_license_summary()

Get license summary

Get license summary.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Get license summary
        api_response = api_instance.get_license_summary()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_license_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqLicenseSummary**](XiqLicenseSummary.md)

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

# **get_nac_entitlement_allocation**
> XiqNacEntitlementAllocation get_nac_entitlement_allocation()

Get NAC entitlement allocation

Get NAC entitlement allocation.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Get NAC entitlement allocation
        api_response = api_instance.get_nac_entitlement_allocation()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_nac_entitlement_allocation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqNacEntitlementAllocation**](XiqNacEntitlementAllocation.md)

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

# **get_viq_linked_cuid_info**
> XiqViqLinkedCuidInfo get_viq_linked_cuid_info()

Get VIQ linked CUID info

Get the VIQ-Extreme Portal Account link CUID information.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Get VIQ linked CUID info
        api_response = api_instance.get_viq_linked_cuid_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_viq_linked_cuid_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqViqLinkedCuidInfo**](XiqViqLinkedCuidInfo.md)

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

# **list_license_details**
> PagedXiqListLicenseDetailsResponse list_license_details(license_type, page=page, limit=limit, quick_filter=quick_filter)

List license details

List license details with filters.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    license_type = 'license_type_example' # str | The license type
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
quick_filter = extremecloudiq.XiqLicenseQuickFilter() # XiqLicenseQuickFilter | Quick filter option (optional)

    try:
        # List license details
        api_response = api_instance.list_license_details(license_type, page=page, limit=limit, quick_filter=quick_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->list_license_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_type** | **str**| The license type | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **quick_filter** | [**XiqLicenseQuickFilter**](.md)| Quick filter option | [optional] 

### Return type

[**PagedXiqListLicenseDetailsResponse**](PagedXiqListLicenseDetailsResponse.md)

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

# **list_licenses**
> list[XiqListLicensesResponse] list_licenses(application_id=application_id, group_by_application=group_by_application, keyword=keyword, quick_filter=quick_filter)

List licenses

List licenses with filters.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    application_id = 'application_id_example' # str | Application ID (optional)
group_by_application = False # bool | Whether group by application, if applicationId is null, groupByApplication will be false (optional) (default to False)
keyword = 'keyword_example' # str | The keyword to filter, will search the feature type and feature type description (optional)
quick_filter = extremecloudiq.XiqLicenseQuickFilter() # XiqLicenseQuickFilter | Quick filter option (optional)

    try:
        # List licenses
        api_response = api_instance.list_licenses(application_id=application_id, group_by_application=group_by_application, keyword=keyword, quick_filter=quick_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->list_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | [optional] 
 **group_by_application** | **bool**| Whether group by application, if applicationId is null, groupByApplication will be false | [optional] [default to False]
 **keyword** | **str**| The keyword to filter, will search the feature type and feature type description | [optional] 
 **quick_filter** | [**XiqLicenseQuickFilter**](.md)| Quick filter option | [optional] 

### Return type

[**list[XiqListLicensesResponse]**](XiqListLicensesResponse.md)

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

# **set_nac_entitlement_allocation**
> set_nac_entitlement_allocation(xiq_set_nac_entitlement_allocation_request)

Set NAC entitlement allocation

Get NAC entitlement allocation.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    xiq_set_nac_entitlement_allocation_request = [extremecloudiq.XiqSetNacEntitlementAllocationRequest()] # list[XiqSetNacEntitlementAllocationRequest] | The payload to set NAC entitlement allocation

    try:
        # Set NAC entitlement allocation
        api_instance.set_nac_entitlement_allocation(xiq_set_nac_entitlement_allocation_request)
    except ApiException as e:
        print("Exception when calling LicenseApi->set_nac_entitlement_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_set_nac_entitlement_allocation_request** | [**list[XiqSetNacEntitlementAllocationRequest]**](XiqSetNacEntitlementAllocationRequest.md)| The payload to set NAC entitlement allocation | 

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

# **synchronize_licenses**
> synchronize_licenses()

Synchronize licenses

Synchronize licenses.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Synchronize licenses
        api_instance.synchronize_licenses()
    except ApiException as e:
        print("Exception when calling LicenseApi->synchronize_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **unlink_extreme_portal**
> unlink_extreme_portal()

Unlink Extreme portal account

Unlink Extreme portal account.

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
    api_instance = extremecloudiq.LicenseApi(api_client)
    
    try:
        # Unlink Extreme portal account
        api_instance.unlink_extreme_portal()
    except ApiException as e:
        print("Exception when calling LicenseApi->unlink_extreme_portal: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

