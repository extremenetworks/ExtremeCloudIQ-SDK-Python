# extremecloudiq.NotificationApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscriptions**](NotificationApi.md#create_subscriptions) | **POST** /subscriptions/webhook | Create webhook subscriptions
[**delete_subscription**](NotificationApi.md#delete_subscription) | **DELETE** /subscriptions/webhook/{id} | Delete webhook subscription
[**list**](NotificationApi.md#list) | **GET** /subscriptions/webhook | List webhook subscriptions


# **create_subscriptions**
> create_subscriptions(xiq_create_webhook_subscription_request)

Create webhook subscriptions

Create multiple webhook subscriptions.

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
    api_instance = extremecloudiq.NotificationApi(api_client)
    xiq_create_webhook_subscription_request = [extremecloudiq.XiqCreateWebhookSubscriptionRequest()] # list[XiqCreateWebhookSubscriptionRequest] | The payload of create multiple webhook subscriptions

    try:
        # Create webhook subscriptions
        api_instance.create_subscriptions(xiq_create_webhook_subscription_request)
    except ApiException as e:
        print("Exception when calling NotificationApi->create_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_webhook_subscription_request** | [**list[XiqCreateWebhookSubscriptionRequest]**](XiqCreateWebhookSubscriptionRequest.md)| The payload of create multiple webhook subscriptions | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(id)

Delete webhook subscription

Delete an exist webhook subscription.

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
    api_instance = extremecloudiq.NotificationApi(api_client)
    id = 56 # int | The webhook subscription ID

    try:
        # Delete webhook subscription
        api_instance.delete_subscription(id)
    except ApiException as e:
        print("Exception when calling NotificationApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook subscription ID | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[XiqWebhookSubscription] list()

List webhook subscriptions

List all webhook subscriptions.

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
    api_instance = extremecloudiq.NotificationApi(api_client)
    
    try:
        # List webhook subscriptions
        api_response = api_instance.list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqWebhookSubscription]**](XiqWebhookSubscription.md)

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

