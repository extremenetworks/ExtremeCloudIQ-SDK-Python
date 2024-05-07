# extremecloudiq.EssentialsExtremeLocationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_last_location**](EssentialsExtremeLocationApi.md#get_client_last_location) | **GET** /essentials/eloc/clients/{clientMac}/last-known-location | Get the last known location of the client


# **get_client_last_location**
> EssentialsElocLastKnownLocation get_client_last_location(client_mac, floor_id, parent_id)

Get the last known location of the client

Get the last known location of the client on the floor plan.

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
    api_instance = extremecloudiq.EssentialsExtremeLocationApi(api_client)
    client_mac = 'client_mac_example' # str | The mac address of client
floor_id = 56 # int | Location Id of the floor
parent_id = 56 # int | Location Id of the floor's parent

    try:
        # Get the last known location of the client
        api_response = api_instance.get_client_last_location(client_mac, floor_id, parent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EssentialsExtremeLocationApi->get_client_last_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_mac** | **str**| The mac address of client | 
 **floor_id** | **int**| Location Id of the floor | 
 **parent_id** | **int**| Location Id of the floor&#39;s parent | 

### Return type

[**EssentialsElocLastKnownLocation**](EssentialsElocLastKnownLocation.md)

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

