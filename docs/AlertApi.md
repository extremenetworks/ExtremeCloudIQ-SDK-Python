# extremecloudiq.AlertApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_alerts_by_group**](AlertApi.md#count_alerts_by_group) | **GET** /alerts/count-by-{group} | Count the alerts by different grouping
[**list_alerts**](AlertApi.md#list_alerts) | **GET** /alerts | List the alerts


# **count_alerts_by_group**
> dict(str, int) count_alerts_by_group(group, start_time, end_time)

Count the alerts by different grouping

Count the number of alerts and events based on Severity, Category, and Alert Type.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    group = extremecloudiq.XiqAlertGroupQuery() # XiqAlertGroupQuery | The group to count from
start_time = 56 # int | The start time for counting the alerts
end_time = 56 # int | The end time for counting the alerts

    try:
        # Count the alerts by different grouping
        api_response = api_instance.count_alerts_by_group(group, start_time, end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->count_alerts_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**XiqAlertGroupQuery**](.md)| The group to count from | 
 **start_time** | **int**| The start time for counting the alerts | 
 **end_time** | **int**| The end time for counting the alerts | 

### Return type

**dict(str, int)**

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

# **list_alerts**
> PagedXiqAlert list_alerts(start_time, end_time, page=page, limit=limit, severity=severity, category=category, alert_type=alert_type, keyword=keyword)

List the alerts

List a page of alerts by filter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    start_time = 56 # int | The start time for querying alerts in milliseconds
end_time = 56 # int | The end time for querying alerts in milliseconds
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
severity = extremecloudiq.XiqAlertSeverity() # XiqAlertSeverity | The alert severity to filter (optional)
category = extremecloudiq.XiqAlertCategory() # XiqAlertCategory | The alert category to filter (optional)
alert_type = 'alert_type_example' # str | The alert type to filter (optional)
keyword = 'keyword_example' # str | The keyword to filter, such as device SN or MAC address (optional)

    try:
        # List the alerts
        api_response = api_instance.list_alerts(start_time, end_time, page=page, limit=limit, severity=severity, category=category, alert_type=alert_type, keyword=keyword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->list_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time for querying alerts in milliseconds | 
 **end_time** | **int**| The end time for querying alerts in milliseconds | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **severity** | [**XiqAlertSeverity**](.md)| The alert severity to filter | [optional] 
 **category** | [**XiqAlertCategory**](.md)| The alert category to filter | [optional] 
 **alert_type** | **str**| The alert type to filter | [optional] 
 **keyword** | **str**| The keyword to filter, such as device SN or MAC address | [optional] 

### Return type

[**PagedXiqAlert**](PagedXiqAlert.md)

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

