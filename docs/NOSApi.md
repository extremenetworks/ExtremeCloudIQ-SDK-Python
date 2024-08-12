# extremecloudiq.NOSApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device**](NOSApi.md#get_device) | **POST** /nos/device/{deviceId}/nos-api | Get device info for a specific device


# **get_device**
> XiqGetDeviceInfoByNos get_device(device_id, xiq_get_device_infoby_nos_request)

Get device info for a specific device

Get device info for a specific device.

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
    api_instance = extremecloudiq.NOSApi(api_client)
    device_id = 56 # int | The device ID
xiq_get_device_infoby_nos_request = extremecloudiq.XiqGetDeviceInfobyNosRequest() # XiqGetDeviceInfobyNosRequest | 

    try:
        # Get device info for a specific device
        api_response = api_instance.get_device(device_id, xiq_get_device_infoby_nos_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NOSApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The device ID | 
 **xiq_get_device_infoby_nos_request** | [**XiqGetDeviceInfobyNosRequest**](XiqGetDeviceInfobyNosRequest.md)|  | 

### Return type

[**XiqGetDeviceInfoByNos**](XiqGetDeviceInfoByNos.md)

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

