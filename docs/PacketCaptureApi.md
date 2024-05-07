# extremecloudiq.PacketCaptureApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_packet_capture**](PacketCaptureApi.md#create_packet_capture) | **POST** /packetcaptures | Create a new packet capture session
[**delete_packet_capture**](PacketCaptureApi.md#delete_packet_capture) | **DELETE** /packetcaptures/{id} | Delete a packet capture session
[**get_packet_capture**](PacketCaptureApi.md#get_packet_capture) | **GET** /packetcaptures/{id} | Get a packet capture session
[**get_packet_capture_file**](PacketCaptureApi.md#get_packet_capture_file) | **GET** /packetcaptures/files | Get an AP packet capture file
[**list_packet_captures**](PacketCaptureApi.md#list_packet_captures) | **GET** /packetcaptures | List packet capture sessions
[**stop_packet_capture**](PacketCaptureApi.md#stop_packet_capture) | **POST** /packetcaptures/{id}/:stop | Stop a packet capture session
[**upload_packet_capture_files**](PacketCaptureApi.md#upload_packet_capture_files) | **POST** /packetcaptures/{id}/:upload | Upload a packet capture session&#39;s capture files


# **create_packet_capture**
> XiqPacketCapture create_packet_capture(xiq_packet_capture)

Create a new packet capture session

Create and start a new packet capture session with requested capture location and filter criteria.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    xiq_packet_capture = extremecloudiq.XiqPacketCapture() # XiqPacketCapture | The packet capture to start

    try:
        # Create a new packet capture session
        api_response = api_instance.create_packet_capture(xiq_packet_capture)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->create_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_packet_capture** | [**XiqPacketCapture**](XiqPacketCapture.md)| The packet capture to start | 

### Return type

[**XiqPacketCapture**](XiqPacketCapture.md)

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

# **delete_packet_capture**
> delete_packet_capture(id)

Delete a packet capture session

Delete an existing packet capture session and capture files by ID.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    id = 56 # int | The packet capture ID

    try:
        # Delete a packet capture session
        api_instance.delete_packet_capture(id)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->delete_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The packet capture ID | 

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

# **get_packet_capture**
> XiqPacketCapture get_packet_capture(id, fields=fields)

Get a packet capture session

Get packet capture session by ID.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    id = 56 # int | The packet capture ID
fields = [extremecloudiq.XiqPacketCaptureField()] # list[XiqPacketCaptureField] | The packet capture fields to return (optional)

    try:
        # Get a packet capture session
        api_response = api_instance.get_packet_capture(id, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->get_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The packet capture ID | 
 **fields** | [**list[XiqPacketCaptureField]**](XiqPacketCaptureField.md)| The packet capture fields to return | [optional] 

### Return type

[**XiqPacketCapture**](XiqPacketCapture.md)

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

# **get_packet_capture_file**
> list[str] get_packet_capture_file(cloud_file_url)

Get an AP packet capture file

Get an AP packet capture file from XIQ cloud storage.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    cloud_file_url = 'cloud_file_url_example' # str | The packet capture file path

    try:
        # Get an AP packet capture file
        api_response = api_instance.get_packet_capture_file(cloud_file_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->get_packet_capture_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_file_url** | **str**| The packet capture file path | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packet_captures**
> PagedXiqPacketCapture list_packet_captures(search_string=search_string, page=page, limit=limit, sort_field=sort_field, order=order, fields=fields)

List packet capture sessions

List packet captures with filters and pagination.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    search_string = 'search_string_example' # str | The string to be searched in capture session name, interface name and device host name (optional)
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 500 (optional) (default to 10)
sort_field = extremecloudiq.XiqPacketCaptureSortField() # XiqPacketCaptureSortField | Sort field. Available values - NAME, START_TIME and STATUS (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | Sort order (ascending by default) (optional)
fields = [extremecloudiq.XiqPacketCaptureField()] # list[XiqPacketCaptureField] | The packet capture fields to return (optional)

    try:
        # List packet capture sessions
        api_response = api_instance.list_packet_captures(search_string=search_string, page=page, limit=limit, sort_field=sort_field, order=order, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->list_packet_captures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| The string to be searched in capture session name, interface name and device host name | [optional] 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 500 | [optional] [default to 10]
 **sort_field** | [**XiqPacketCaptureSortField**](.md)| Sort field. Available values - NAME, START_TIME and STATUS | [optional] 
 **order** | [**XiqSortOrder**](.md)| Sort order (ascending by default) | [optional] 
 **fields** | [**list[XiqPacketCaptureField]**](XiqPacketCaptureField.md)| The packet capture fields to return | [optional] 

### Return type

[**PagedXiqPacketCapture**](PagedXiqPacketCapture.md)

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

# **stop_packet_capture**
> stop_packet_capture(id, xiq_capture_stop_request)

Stop a packet capture session

Stop an active packet capture session.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    id = 56 # int | The packet capture ID
xiq_capture_stop_request = extremecloudiq.XiqCaptureStopRequest() # XiqCaptureStopRequest | 

    try:
        # Stop a packet capture session
        api_instance.stop_packet_capture(id, xiq_capture_stop_request)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->stop_packet_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The packet capture ID | 
 **xiq_capture_stop_request** | [**XiqCaptureStopRequest**](XiqCaptureStopRequest.md)|  | 

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

# **upload_packet_capture_files**
> upload_packet_capture_files(id)

Upload a packet capture session's capture files

Upload the capture files from a packet capture session, if files previously failed to be uploaded to XIQ cloud.

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
    api_instance = extremecloudiq.PacketCaptureApi(api_client)
    id = 56 # int | The packet capture ID

    try:
        # Upload a packet capture session's capture files
        api_instance.upload_packet_capture_files(id)
    except ApiException as e:
        print("Exception when calling PacketCaptureApi->upload_packet_capture_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The packet capture ID | 

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

