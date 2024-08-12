# extremecloudiq.ConfigurationDeploymentApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_config**](ConfigurationDeploymentApi.md#deploy_config) | **POST** /deployments | [LRO] Push configuration and upgrade firmware
[**get_deploy_overview**](ConfigurationDeploymentApi.md#get_deploy_overview) | **GET** /deployments/overview | Get configuration deployment overview
[**get_deploy_status**](ConfigurationDeploymentApi.md#get_deploy_status) | **GET** /deployments/status | Get configuration deployment status
[**get_device_firmware_metadatas**](ConfigurationDeploymentApi.md#get_device_firmware_metadatas) | **POST** /deployments/firmware-metadatas | Get device firmware metadatas


# **deploy_config**
> XiqDeploymentResponse deploy_config(xiq_deployment_request, _async=_async)

[LRO] Push configuration and upgrade firmware

Push configuration and upgrade firmware to the target devices. To avoid API timeout with large number of devices,   please make sure to enable async mode (set async=true in query parameter) and use long-running operation API to query the result.

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
    api_instance = extremecloudiq.ConfigurationDeploymentApi(api_client)
    xiq_deployment_request = extremecloudiq.XiqDeploymentRequest() # XiqDeploymentRequest | The device deploy configuration
_async = True # bool | Whether to enable async mode (optional) (default to True)

    try:
        # [LRO] Push configuration and upgrade firmware
        api_response = api_instance.deploy_config(xiq_deployment_request, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationDeploymentApi->deploy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_deployment_request** | [**XiqDeploymentRequest**](XiqDeploymentRequest.md)| The device deploy configuration | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to True]

### Return type

[**XiqDeploymentResponse**](XiqDeploymentResponse.md)

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

# **get_deploy_overview**
> XiqDeploymentOverview get_deploy_overview()

Get configuration deployment overview

Get configuration deployment status overview.

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
    api_instance = extremecloudiq.ConfigurationDeploymentApi(api_client)
    
    try:
        # Get configuration deployment overview
        api_response = api_instance.get_deploy_overview()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationDeploymentApi->get_deploy_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqDeploymentOverview**](XiqDeploymentOverview.md)

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

# **get_deploy_status**
> dict(str, XiqDeploymentStatus) get_deploy_status(device_ids)

Get configuration deployment status

Get configuration deployment status for the target devices.

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
    api_instance = extremecloudiq.ConfigurationDeploymentApi(api_client)
    device_ids = [56] # list[int] | The target device IDs

    try:
        # Get configuration deployment status
        api_response = api_instance.get_deploy_status(device_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationDeploymentApi->get_deploy_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**list[int]**](int.md)| The target device IDs | 

### Return type

[**dict(str, XiqDeploymentStatus)**](XiqDeploymentStatus.md)

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

# **get_device_firmware_metadatas**
> XiqFirmwareMetadatasResponse get_device_firmware_metadatas(xiq_firmware_metadatas_request)

Get device firmware metadatas

Get the compatible firmware metadatas for the devices.

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
    api_instance = extremecloudiq.ConfigurationDeploymentApi(api_client)
    xiq_firmware_metadatas_request = extremecloudiq.XiqFirmwareMetadatasRequest() # XiqFirmwareMetadatasRequest | 

    try:
        # Get device firmware metadatas
        api_response = api_instance.get_device_firmware_metadatas(xiq_firmware_metadatas_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationDeploymentApi->get_device_firmware_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_firmware_metadatas_request** | [**XiqFirmwareMetadatasRequest**](XiqFirmwareMetadatasRequest.md)|  | 

### Return type

[**XiqFirmwareMetadatasResponse**](XiqFirmwareMetadatasResponse.md)

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

