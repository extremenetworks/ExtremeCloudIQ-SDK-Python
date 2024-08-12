# extremecloudiq.AfcEndpointApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site_afc_schedule**](AfcEndpointApi.md#create_site_afc_schedule) | **POST** /site/afc/schedule | 
[**get_afc_geolocation_summary**](AfcEndpointApi.md#get_afc_geolocation_summary) | **GET** /aps/geolocation/summary | 
[**get_afc_server**](AfcEndpointApi.md#get_afc_server) | **GET** /afcserver/{server_id} | Get Afc Server data
[**get_afc_spectrum_per_ap**](AfcEndpointApi.md#get_afc_spectrum_per_ap) | **POST** /ap/spectrum/ | 
[**get_afc_spectrum_per_site**](AfcEndpointApi.md#get_afc_spectrum_per_site) | **POST** /site/spectrum/ | 
[**get_afc_status_summary**](AfcEndpointApi.md#get_afc_status_summary) | **GET** /aps/status/summary | 
[**get_aps_afc_info**](AfcEndpointApi.md#get_aps_afc_info) | **GET** /ap/afc/interface/details/{sn} | Get Afc Summary Data
[**get_aps_afc_summary_info**](AfcEndpointApi.md#get_aps_afc_summary_info) | **GET** /aps/afc/query/ | 
[**get_site_afc_schedule**](AfcEndpointApi.md#get_site_afc_schedule) | **GET** /site/afc/schedule | 
[**list_afc_servers**](AfcEndpointApi.md#list_afc_servers) | **GET** /afcserver | Get Afc Server list and their status
[**update_site_afc_schedule**](AfcEndpointApi.md#update_site_afc_schedule) | **PUT** /site/afc/schedule | 


# **create_site_afc_schedule**
> create_site_afc_schedule(xiq_site_afc_schedule)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    xiq_site_afc_schedule = extremecloudiq.XiqSiteAfcSchedule() # XiqSiteAfcSchedule | AFC site schedule request body

    try:
        api_instance.create_site_afc_schedule(xiq_site_afc_schedule)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->create_site_afc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_site_afc_schedule** | [**XiqSiteAfcSchedule**](XiqSiteAfcSchedule.md)| AFC site schedule request body | 

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

# **get_afc_geolocation_summary**
> XiqAfcGeolocationSummary get_afc_geolocation_summary(owner_id)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    owner_id = 56 # int | Owner Id

    try:
        api_response = api_instance.get_afc_geolocation_summary(owner_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_geolocation_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| Owner Id | 

### Return type

[**XiqAfcGeolocationSummary**](XiqAfcGeolocationSummary.md)

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

# **get_afc_server**
> XiqAfcServer get_afc_server(server_id)

Get Afc Server data

Get Afc Server data

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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    server_id = 1234567890 # int | The Id of the server

    try:
        # Get Afc Server data
        api_response = api_instance.get_afc_server(server_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| The Id of the server | 

### Return type

[**XiqAfcServer**](XiqAfcServer.md)

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

# **get_afc_spectrum_per_ap**
> list[XiqAfcAvailableSpectrum] get_afc_spectrum_per_ap(xiq_get_afc_spectrum_for_ap_request)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    xiq_get_afc_spectrum_for_ap_request = extremecloudiq.XiqGetAfcSpectrumForApRequest() # XiqGetAfcSpectrumForApRequest | get afc spectrum per AP request body

    try:
        api_response = api_instance.get_afc_spectrum_per_ap(xiq_get_afc_spectrum_for_ap_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_spectrum_per_ap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_get_afc_spectrum_for_ap_request** | [**XiqGetAfcSpectrumForApRequest**](XiqGetAfcSpectrumForApRequest.md)| get afc spectrum per AP request body | 

### Return type

[**list[XiqAfcAvailableSpectrum]**](XiqAfcAvailableSpectrum.md)

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

# **get_afc_spectrum_per_site**
> list[XiqAfcAvailableSpectrum] get_afc_spectrum_per_site(xiq_get_afc_spectrum_for_site_aps_request)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    xiq_get_afc_spectrum_for_site_aps_request = extremecloudiq.XiqGetAfcSpectrumForSiteApsRequest() # XiqGetAfcSpectrumForSiteApsRequest | get afc spectrum by site request body

    try:
        api_response = api_instance.get_afc_spectrum_per_site(xiq_get_afc_spectrum_for_site_aps_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_spectrum_per_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_get_afc_spectrum_for_site_aps_request** | [**XiqGetAfcSpectrumForSiteApsRequest**](XiqGetAfcSpectrumForSiteApsRequest.md)| get afc spectrum by site request body | 

### Return type

[**list[XiqAfcAvailableSpectrum]**](XiqAfcAvailableSpectrum.md)

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

# **get_afc_status_summary**
> XiqAfcStatusSummary get_afc_status_summary(owner_id)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    owner_id = 56 # int | Owner Id

    try:
        api_response = api_instance.get_afc_status_summary(owner_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| Owner Id | 

### Return type

[**XiqAfcStatusSummary**](XiqAfcStatusSummary.md)

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

# **get_aps_afc_info**
> XiqAfcApDetail get_aps_afc_info(sn)

Get Afc Summary Data

Get Afc data per site 

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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    sn = 'AP-1234567890' # str | The Serial Number of the AP

    try:
        # Get Afc Summary Data
        api_response = api_instance.get_aps_afc_info(sn)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_aps_afc_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sn** | **str**| The Serial Number of the AP | 

### Return type

[**XiqAfcApDetail**](XiqAfcApDetail.md)

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

# **get_aps_afc_summary_info**
> XiqAfcApsInfoElement get_aps_afc_summary_info(owner_id)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    owner_id = 56 # int | Owner Id

    try:
        api_response = api_instance.get_aps_afc_summary_info(owner_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_aps_afc_summary_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| Owner Id | 

### Return type

[**XiqAfcApsInfoElement**](XiqAfcApsInfoElement.md)

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

# **get_site_afc_schedule**
> XiqSiteAfcSchedule get_site_afc_schedule(owner_id, folder_id)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    owner_id = 56 # int | Owner Id
folder_id = 56 # int | Folder Id

    try:
        api_response = api_instance.get_site_afc_schedule(owner_id, folder_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->get_site_afc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| Owner Id | 
 **folder_id** | **int**| Folder Id | 

### Return type

[**XiqSiteAfcSchedule**](XiqSiteAfcSchedule.md)

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

# **list_afc_servers**
> XiqListAfcServers list_afc_servers(owner_id)

Get Afc Server list and their status

Get all Afc Servers data

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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    owner_id = 56 # int | Owner Id

    try:
        # Get Afc Server list and their status
        api_response = api_instance.list_afc_servers(owner_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->list_afc_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| Owner Id | 

### Return type

[**XiqListAfcServers**](XiqListAfcServers.md)

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

# **update_site_afc_schedule**
> update_site_afc_schedule(xiq_site_afc_schedule)



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
    api_instance = extremecloudiq.AfcEndpointApi(api_client)
    xiq_site_afc_schedule = extremecloudiq.XiqSiteAfcSchedule() # XiqSiteAfcSchedule | AFC site schedule request body

    try:
        api_instance.update_site_afc_schedule(xiq_site_afc_schedule)
    except ApiException as e:
        print("Exception when calling AfcEndpointApi->update_site_afc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_site_afc_schedule** | [**XiqSiteAfcSchedule**](XiqSiteAfcSchedule.md)| AFC site schedule request body | 

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

