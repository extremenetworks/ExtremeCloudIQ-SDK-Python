# extremecloudiq.AlertApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alerts**](AlertApi.md#acknowledge_alerts) | **POST** /alerts/:acknowledge | Acknowledge the alerts
[**count_alerts_by_group**](AlertApi.md#count_alerts_by_group) | **GET** /alerts/count-by-{group} | Count the alerts by different grouping
[**create_alert_email_subscription**](AlertApi.md#create_alert_email_subscription) | **POST** /alert-subscriptions/emails | Create alert email subscription
[**create_alert_policy**](AlertApi.md#create_alert_policy) | **POST** /alert-policies | Create a site based alert policy
[**create_alert_report**](AlertApi.md#create_alert_report) | **POST** /alerts/reports | [LRO] Create the alerts report
[**create_alert_webhook_subscription**](AlertApi.md#create_alert_webhook_subscription) | **POST** /alert-subscriptions/webhooks | Create alert webhook subscription
[**delete_alert_email_subscription**](AlertApi.md#delete_alert_email_subscription) | **DELETE** /alert-subscriptions/emails/{id} | Delete alert email subscription
[**delete_alert_policy**](AlertApi.md#delete_alert_policy) | **DELETE** /alert-policies/{id} | Delete a site-based alert policy
[**delete_alert_webhook_subscription**](AlertApi.md#delete_alert_webhook_subscription) | **DELETE** /alert-subscriptions/webhooks/{id} | Delete alert webhook subscription
[**delete_bulk_alert_subscription_email**](AlertApi.md#delete_bulk_alert_subscription_email) | **POST** /alert-subscriptions/emails/:delete | Delete alert email subscription in bulk
[**delete_bulk_alert_subscription_webhook**](AlertApi.md#delete_bulk_alert_subscription_webhook) | **POST** /alert-subscriptions/webhooks/:delete | Delete alert webhook subscription in bulk
[**disable_alert_rule**](AlertApi.md#disable_alert_rule) | **POST** /alert-policies/{policyId}/rules/{ruleId}/:disable | Disable a rule from an alert policy
[**download_alert_report**](AlertApi.md#download_alert_report) | **GET** /alerts/reports/{id} | Download the alerts report
[**enable_alert_rule**](AlertApi.md#enable_alert_rule) | **POST** /alert-policies/{policyId}/rules/{ruleId}/:enable | Enable a rule from an alert policy
[**get_alert_email_subscription**](AlertApi.md#get_alert_email_subscription) | **GET** /alert-subscriptions/emails/{id} | Get alert email subscription
[**get_alert_policy**](AlertApi.md#get_alert_policy) | **GET** /alert-policies/{id} | Get details of an alert policy
[**get_alert_rule**](AlertApi.md#get_alert_rule) | **GET** /alert-policies/{policyId}/rules/{ruleId} | Get details of an alert rule
[**get_alert_webhook_subscription**](AlertApi.md#get_alert_webhook_subscription) | **GET** /alert-subscriptions/webhooks/{id} | Get alert webhook subscription
[**list_alert_email_subscriptions**](AlertApi.md#list_alert_email_subscriptions) | **GET** /alert-subscriptions/emails | List alert email subscriptions
[**list_alert_policies**](AlertApi.md#list_alert_policies) | **GET** /alert-policies | List all alert policies
[**list_alert_webhook_subscriptions**](AlertApi.md#list_alert_webhook_subscriptions) | **GET** /alert-subscriptions/webhooks | List alert webhook subscriptions
[**list_alerts**](AlertApi.md#list_alerts) | **GET** /alerts | List the alerts
[**list_available_sites**](AlertApi.md#list_available_sites) | **GET** /alert-policies/available-sites | The list of current owner&#39;s available sites
[**update_alert_email_subscription**](AlertApi.md#update_alert_email_subscription) | **PUT** /alert-subscriptions/emails/{id} | Update alert email subscription
[**update_alert_policy**](AlertApi.md#update_alert_policy) | **PUT** /alert-policies/{id} | Update a site-based alert policy
[**update_alert_rule**](AlertApi.md#update_alert_rule) | **PUT** /alert-policies/{policyId}/rules/{ruleId} | Update an alert rule
[**update_alert_webhook_subscription**](AlertApi.md#update_alert_webhook_subscription) | **PUT** /alert-subscriptions/webhooks/{id} | Update alert webhook subscription
[**verify_subscription_email**](AlertApi.md#verify_subscription_email) | **POST** /alert-subscriptions/emails/{id}/:verify | Email Verification


# **acknowledge_alerts**
> list[XiqAlert] acknowledge_alerts(xiq_acknowledge_alerts_request)

Acknowledge the alerts

acknowledge the alerts by alert ids.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_acknowledge_alerts_request = extremecloudiq.XiqAcknowledgeAlertsRequest() # XiqAcknowledgeAlertsRequest | 

    try:
        # Acknowledge the alerts
        api_response = api_instance.acknowledge_alerts(xiq_acknowledge_alerts_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->acknowledge_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_acknowledge_alerts_request** | [**XiqAcknowledgeAlertsRequest**](XiqAcknowledgeAlertsRequest.md)|  | 

### Return type

[**list[XiqAlert]**](XiqAlert.md)

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

# **count_alerts_by_group**
> list[XiqAlertGroupCount] count_alerts_by_group(group, start_time, end_time, acknowledged=acknowledged, site_id=site_id)

Count the alerts by different grouping

Count the number of alerts and events based on Severity, Category, and Alert Type.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    group = extremecloudiq.XiqAlertGroupQuery() # XiqAlertGroupQuery | The group to count from
start_time = 56 # int | The start time for counting the alerts
end_time = 56 # int | The end time for counting the alerts
acknowledged = True # bool | The acknowledged to filter, return global data if not specified (optional)
site_id = 56 # int | The site id for counting the alerts, default to global (optional)

    try:
        # Count the alerts by different grouping
        api_response = api_instance.count_alerts_by_group(group, start_time, end_time, acknowledged=acknowledged, site_id=site_id)
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
 **acknowledged** | **bool**| The acknowledged to filter, return global data if not specified | [optional] 
 **site_id** | **int**| The site id for counting the alerts, default to global | [optional] 

### Return type

[**list[XiqAlertGroupCount]**](XiqAlertGroupCount.md)

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

# **create_alert_email_subscription**
> XiqAlertEmailSubscription create_alert_email_subscription(xiq_create_alert_email_subscription_request)

Create alert email subscription

Create alert email subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_create_alert_email_subscription_request = extremecloudiq.XiqCreateAlertEmailSubscriptionRequest() # XiqCreateAlertEmailSubscriptionRequest | The payload of create alert email subscription

    try:
        # Create alert email subscription
        api_response = api_instance.create_alert_email_subscription(xiq_create_alert_email_subscription_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->create_alert_email_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_alert_email_subscription_request** | [**XiqCreateAlertEmailSubscriptionRequest**](XiqCreateAlertEmailSubscriptionRequest.md)| The payload of create alert email subscription | 

### Return type

[**XiqAlertEmailSubscription**](XiqAlertEmailSubscription.md)

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

# **create_alert_policy**
> XiqAlertPolicy create_alert_policy(xiq_alert_policy_filter)

Create a site based alert policy

Create a new site-based alert policy. The global policy for each account is created automatically.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_alert_policy_filter = extremecloudiq.XiqAlertPolicyFilter() # XiqAlertPolicyFilter | 

    try:
        # Create a site based alert policy
        api_response = api_instance.create_alert_policy(xiq_alert_policy_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->create_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_alert_policy_filter** | [**XiqAlertPolicyFilter**](XiqAlertPolicyFilter.md)|  | 

### Return type

[**XiqAlertPolicy**](XiqAlertPolicy.md)

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

# **create_alert_report**
> XiqAlertReport create_alert_report(start_time, end_time, severity_ids=severity_ids, category_ids=category_ids, message_metadata_ids=message_metadata_ids, acknowledged=acknowledged, site_id=site_id, time_zone_offset=time_zone_offset, keyword=keyword, sort_field=sort_field, order=order, _async=_async)

[LRO] Create the alerts report

Create the alerts by filter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    start_time = 56 # int | The start time for querying alerts in milliseconds
end_time = 56 # int | The end time for querying alerts in milliseconds
severity_ids = [56] # list[int] | The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. (optional)
category_ids = [56] # list[int] | The alert category Id to filter (optional)
message_metadata_ids = [56] # list[int] | The alert type to filter (optional)
acknowledged = True # bool | The site to filter, return global data if not specified (optional)
site_id = 56 # int | The site id to filter (optional)
time_zone_offset = 56 # int | The time zone to setup the timestamp (optional)
keyword = 'keyword_example' # str | The keyword to filter, such as source name or description (optional)
sort_field = extremecloudiq.XiqAlertSortField() # XiqAlertSortField | The sort field (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order (ascending by default) (optional)
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Create the alerts report
        api_response = api_instance.create_alert_report(start_time, end_time, severity_ids=severity_ids, category_ids=category_ids, message_metadata_ids=message_metadata_ids, acknowledged=acknowledged, site_id=site_id, time_zone_offset=time_zone_offset, keyword=keyword, sort_field=sort_field, order=order, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->create_alert_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time for querying alerts in milliseconds | 
 **end_time** | **int**| The end time for querying alerts in milliseconds | 
 **severity_ids** | [**list[int]**](int.md)| The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. | [optional] 
 **category_ids** | [**list[int]**](int.md)| The alert category Id to filter | [optional] 
 **message_metadata_ids** | [**list[int]**](int.md)| The alert type to filter | [optional] 
 **acknowledged** | **bool**| The site to filter, return global data if not specified | [optional] 
 **site_id** | **int**| The site id to filter | [optional] 
 **time_zone_offset** | **int**| The time zone to setup the timestamp | [optional] 
 **keyword** | **str**| The keyword to filter, such as source name or description | [optional] 
 **sort_field** | [**XiqAlertSortField**](.md)| The sort field | [optional] 
 **order** | [**XiqSortOrder**](.md)| The sort order (ascending by default) | [optional] 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**XiqAlertReport**](XiqAlertReport.md)

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

# **create_alert_webhook_subscription**
> XiqAlertWebhookSubscription create_alert_webhook_subscription(xiq_create_alert_webhook_subscription_request)

Create alert webhook subscription

Create alert webhook subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_create_alert_webhook_subscription_request = extremecloudiq.XiqCreateAlertWebhookSubscriptionRequest() # XiqCreateAlertWebhookSubscriptionRequest | The payload of create alert webhook subscription

    try:
        # Create alert webhook subscription
        api_response = api_instance.create_alert_webhook_subscription(xiq_create_alert_webhook_subscription_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->create_alert_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_alert_webhook_subscription_request** | [**XiqCreateAlertWebhookSubscriptionRequest**](XiqCreateAlertWebhookSubscriptionRequest.md)| The payload of create alert webhook subscription | 

### Return type

[**XiqAlertWebhookSubscription**](XiqAlertWebhookSubscription.md)

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

# **delete_alert_email_subscription**
> delete_alert_email_subscription(id)

Delete alert email subscription

Delete an exist alert email subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert email subscription ID

    try:
        # Delete alert email subscription
        api_instance.delete_alert_email_subscription(id)
    except ApiException as e:
        print("Exception when calling AlertApi->delete_alert_email_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert email subscription ID | 

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

# **delete_alert_policy**
> delete_alert_policy(id)

Delete a site-based alert policy

Modify a site-based alert policy's details, including the policy name and sites.     The global policy cannot be updated.     The sites can be obtained from the alerts/sites API.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The policy ID

    try:
        # Delete a site-based alert policy
        api_instance.delete_alert_policy(id)
    except ApiException as e:
        print("Exception when calling AlertApi->delete_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The policy ID | 

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

# **delete_alert_webhook_subscription**
> delete_alert_webhook_subscription(id)

Delete alert webhook subscription

Delete an exist alert webhook subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert webhook subscription ID

    try:
        # Delete alert webhook subscription
        api_instance.delete_alert_webhook_subscription(id)
    except ApiException as e:
        print("Exception when calling AlertApi->delete_alert_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert webhook subscription ID | 

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

# **delete_bulk_alert_subscription_email**
> XiqDeleteBulkAlertSubscriptionEmailResponse delete_bulk_alert_subscription_email(xiq_delete_bulk_alert_subscription_request, _async=_async)

Delete alert email subscription in bulk

Delete alert email subscription in bulk.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_delete_bulk_alert_subscription_request = extremecloudiq.XiqDeleteBulkAlertSubscriptionRequest() # XiqDeleteBulkAlertSubscriptionRequest | 
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # Delete alert email subscription in bulk
        api_response = api_instance.delete_bulk_alert_subscription_email(xiq_delete_bulk_alert_subscription_request, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->delete_bulk_alert_subscription_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_delete_bulk_alert_subscription_request** | [**XiqDeleteBulkAlertSubscriptionRequest**](XiqDeleteBulkAlertSubscriptionRequest.md)|  | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**XiqDeleteBulkAlertSubscriptionEmailResponse**](XiqDeleteBulkAlertSubscriptionEmailResponse.md)

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

# **delete_bulk_alert_subscription_webhook**
> XiqDeleteBulkAlertSubscriptionWebhookResponse delete_bulk_alert_subscription_webhook(xiq_delete_bulk_alert_subscription_request, _async=_async)

Delete alert webhook subscription in bulk

Delete alert webhook subscription in bulk.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    xiq_delete_bulk_alert_subscription_request = extremecloudiq.XiqDeleteBulkAlertSubscriptionRequest() # XiqDeleteBulkAlertSubscriptionRequest | 
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # Delete alert webhook subscription in bulk
        api_response = api_instance.delete_bulk_alert_subscription_webhook(xiq_delete_bulk_alert_subscription_request, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->delete_bulk_alert_subscription_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_delete_bulk_alert_subscription_request** | [**XiqDeleteBulkAlertSubscriptionRequest**](XiqDeleteBulkAlertSubscriptionRequest.md)|  | 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**XiqDeleteBulkAlertSubscriptionWebhookResponse**](XiqDeleteBulkAlertSubscriptionWebhookResponse.md)

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

# **disable_alert_rule**
> XiqAlertRule disable_alert_rule(policy_id, rule_id)

Disable a rule from an alert policy

Set the status of a rule to disabled. Users can obtain a rule ID by calling #_get_alert_policy first.If the DISABLE operation adheres to a predetermined rule, a new rule will be duplicated from the predefined one, and the DISABLE operation will be applied to the newly cloned rule. As a result, users might receive a new rule ID that differs from the one provided as a path parameter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    policy_id = 56 # int | The policy ID
rule_id = 56 # int | The rule ID

    try:
        # Disable a rule from an alert policy
        api_response = api_instance.disable_alert_rule(policy_id, rule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->disable_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The policy ID | 
 **rule_id** | **int**| The rule ID | 

### Return type

[**XiqAlertRule**](XiqAlertRule.md)

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

# **download_alert_report**
> list[str] download_alert_report(id)

Download the alerts report

Download report of alerts.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The report ID

    try:
        # Download the alerts report
        api_response = api_instance.download_alert_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->download_alert_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The report ID | 

### Return type

**list[str]**

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

# **enable_alert_rule**
> XiqAlertRule enable_alert_rule(policy_id, rule_id)

Enable a rule from an alert policy

Set the status of a rule to enabled. Users can obtain a rule ID by calling #_get_alert_policy first.If the ENABLE operation adheres to a predetermined rule, a new rule will be duplicated from the predefined one, and the ENABLE operation will be applied to the newly cloned rule. As a result, users might receive a new rule ID that differs from the one provided as a path parameter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    policy_id = 56 # int | The policy ID
rule_id = 56 # int | The rule ID

    try:
        # Enable a rule from an alert policy
        api_response = api_instance.enable_alert_rule(policy_id, rule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->enable_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The policy ID | 
 **rule_id** | **int**| The rule ID | 

### Return type

[**XiqAlertRule**](XiqAlertRule.md)

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

# **get_alert_email_subscription**
> XiqAlertEmailSubscription get_alert_email_subscription(id)

Get alert email subscription

Get an exist alert email subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert email subscription ID

    try:
        # Get alert email subscription
        api_response = api_instance.get_alert_email_subscription(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->get_alert_email_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert email subscription ID | 

### Return type

[**XiqAlertEmailSubscription**](XiqAlertEmailSubscription.md)

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

# **get_alert_policy**
> XiqAlertPolicy get_alert_policy(id)

Get details of an alert policy

Get the details related to a specific alert policy, given the policy's identifier.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The policy ID

    try:
        # Get details of an alert policy
        api_response = api_instance.get_alert_policy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->get_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The policy ID | 

### Return type

[**XiqAlertPolicy**](XiqAlertPolicy.md)

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

# **get_alert_rule**
> XiqAlertRule get_alert_rule(policy_id, rule_id)

Get details of an alert rule

Get the full details of an alert rule's state. Users can obtain a rule ID by calling #_get_alert_policy first.The returned rule ID might be different from a predefined rule ID provided as a path parameter when the user overrides the predefined rule  

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
    api_instance = extremecloudiq.AlertApi(api_client)
    policy_id = 56 # int | The policy ID
rule_id = 56 # int | The rule ID

    try:
        # Get details of an alert rule
        api_response = api_instance.get_alert_rule(policy_id, rule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->get_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The policy ID | 
 **rule_id** | **int**| The rule ID | 

### Return type

[**XiqAlertRule**](XiqAlertRule.md)

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

# **get_alert_webhook_subscription**
> XiqAlertWebhookSubscription get_alert_webhook_subscription(id)

Get alert webhook subscription

Get an exist alert webhook subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert webhook subscription ID

    try:
        # Get alert webhook subscription
        api_response = api_instance.get_alert_webhook_subscription(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->get_alert_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert webhook subscription ID | 

### Return type

[**XiqAlertWebhookSubscription**](XiqAlertWebhookSubscription.md)

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

# **list_alert_email_subscriptions**
> list[XiqAlertEmailSubscription] list_alert_email_subscriptions()

List alert email subscriptions

List all alert email subscriptions.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    
    try:
        # List alert email subscriptions
        api_response = api_instance.list_alert_email_subscriptions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->list_alert_email_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqAlertEmailSubscription]**](XiqAlertEmailSubscription.md)

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

# **list_alert_policies**
> XiqListAlertPolicies list_alert_policies(keyword=keyword, policy_type=policy_type)

List all alert policies

Get a list of all alert policies belonging to the current user and an overview      of their associated alert rules.  The details for the rules is available from the alert policy rules API.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    keyword = 'keyword_example' # str | The keyword to filter, such as policy name or site name (optional)
policy_type = extremecloudiq.XiqAlertPolicyType() # XiqAlertPolicyType | The policy type to filter, such as site or global (optional)

    try:
        # List all alert policies
        api_response = api_instance.list_alert_policies(keyword=keyword, policy_type=policy_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->list_alert_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| The keyword to filter, such as policy name or site name | [optional] 
 **policy_type** | [**XiqAlertPolicyType**](.md)| The policy type to filter, such as site or global | [optional] 

### Return type

[**XiqListAlertPolicies**](XiqListAlertPolicies.md)

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

# **list_alert_webhook_subscriptions**
> list[XiqAlertWebhookSubscription] list_alert_webhook_subscriptions()

List alert webhook subscriptions

List all alert webhook subscriptions.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    
    try:
        # List alert webhook subscriptions
        api_response = api_instance.list_alert_webhook_subscriptions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->list_alert_webhook_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqAlertWebhookSubscription]**](XiqAlertWebhookSubscription.md)

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

# **list_alerts**
> PagedXiqAlert list_alerts(start_time, end_time, page=page, limit=limit, severity_ids=severity_ids, category_ids=category_ids, message_metadata_ids=message_metadata_ids, acknowledged=acknowledged, site_id=site_id, floor_id=floor_id, building_id=building_id, keyword=keyword, sort_field=sort_field, order=order)

List the alerts

List a page of alerts by filter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    start_time = 56 # int | The start time for querying alerts in milliseconds
end_time = 56 # int | The end time for querying alerts in milliseconds
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
severity_ids = [56] # list[int] | The alert severity identifiers to filter. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. (optional)
category_ids = [56] # list[int] | The alert category ID to filter (optional)
message_metadata_ids = [56] # list[int] | The message metadata ID list to filter (optional)
acknowledged = True # bool | The acknowledged to filter, return global data if not specified (optional)
site_id = 56 # int | The site id to filter (optional)
floor_id = 56 # int | The floor id to filter (optional)
building_id = 56 # int | The building id to filter (optional)
keyword = 'keyword_example' # str | The keyword to filter, such as summary, severity, source, etc. (optional)
sort_field = extremecloudiq.XiqAlertSortField() # XiqAlertSortField | The sort field (optional)
order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sort order (descending by default) (optional)

    try:
        # List the alerts
        api_response = api_instance.list_alerts(start_time, end_time, page=page, limit=limit, severity_ids=severity_ids, category_ids=category_ids, message_metadata_ids=message_metadata_ids, acknowledged=acknowledged, site_id=site_id, floor_id=floor_id, building_id=building_id, keyword=keyword, sort_field=sort_field, order=order)
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
 **severity_ids** | [**list[int]**](int.md)| The alert severity identifiers to filter. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. | [optional] 
 **category_ids** | [**list[int]**](int.md)| The alert category ID to filter | [optional] 
 **message_metadata_ids** | [**list[int]**](int.md)| The message metadata ID list to filter | [optional] 
 **acknowledged** | **bool**| The acknowledged to filter, return global data if not specified | [optional] 
 **site_id** | **int**| The site id to filter | [optional] 
 **floor_id** | **int**| The floor id to filter | [optional] 
 **building_id** | **int**| The building id to filter | [optional] 
 **keyword** | **str**| The keyword to filter, such as summary, severity, source, etc. | [optional] 
 **sort_field** | [**XiqAlertSortField**](.md)| The sort field | [optional] 
 **order** | [**XiqSortOrder**](.md)| The sort order (descending by default) | [optional] 

### Return type

[**PagedXiqAlert**](PagedXiqAlert.md)

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

# **list_available_sites**
> list[XiqAlertSite] list_available_sites()

The list of current owner's available sites

List all sites belonging to the current owner. If the site has been configured an site policy,      then the site will not be available.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    
    try:
        # The list of current owner's available sites
        api_response = api_instance.list_available_sites()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->list_available_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqAlertSite]**](XiqAlertSite.md)

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

# **update_alert_email_subscription**
> XiqAlertEmailSubscription update_alert_email_subscription(id, xiq_update_alert_email_subscription_request)

Update alert email subscription

Update alert email subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert email subscription ID
xiq_update_alert_email_subscription_request = extremecloudiq.XiqUpdateAlertEmailSubscriptionRequest() # XiqUpdateAlertEmailSubscriptionRequest | The payload of update alert email subscription

    try:
        # Update alert email subscription
        api_response = api_instance.update_alert_email_subscription(id, xiq_update_alert_email_subscription_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->update_alert_email_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert email subscription ID | 
 **xiq_update_alert_email_subscription_request** | [**XiqUpdateAlertEmailSubscriptionRequest**](XiqUpdateAlertEmailSubscriptionRequest.md)| The payload of update alert email subscription | 

### Return type

[**XiqAlertEmailSubscription**](XiqAlertEmailSubscription.md)

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

# **update_alert_policy**
> XiqAlertPolicy update_alert_policy(id, xiq_alert_policy_filter)

Update a site-based alert policy

Delete an alert policy. All the associated alert rules will be deleted as well.     The global policy cannot be deleted.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The policy ID
xiq_alert_policy_filter = extremecloudiq.XiqAlertPolicyFilter() # XiqAlertPolicyFilter | 

    try:
        # Update a site-based alert policy
        api_response = api_instance.update_alert_policy(id, xiq_alert_policy_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->update_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The policy ID | 
 **xiq_alert_policy_filter** | [**XiqAlertPolicyFilter**](XiqAlertPolicyFilter.md)|  | 

### Return type

[**XiqAlertPolicy**](XiqAlertPolicy.md)

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

# **update_alert_rule**
> XiqAlertRule update_alert_rule(policy_id, rule_id, xiq_update_alert_rule_request)

Update an alert rule

Update the state of an alert rule. Users can obtain a rule ID by calling #_get_alert_policy first.If all changes adhere to a predetermined rule, a new rule will be duplicated from the predefined one, and all changes will be applied to the newly cloned rule. As a result, users might receive a new rule ID that differs from the one provided as a path parameter.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    policy_id = 56 # int | The policy ID
rule_id = 56 # int | The rule ID
xiq_update_alert_rule_request = extremecloudiq.XiqUpdateAlertRuleRequest() # XiqUpdateAlertRuleRequest | 

    try:
        # Update an alert rule
        api_response = api_instance.update_alert_rule(policy_id, rule_id, xiq_update_alert_rule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->update_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The policy ID | 
 **rule_id** | **int**| The rule ID | 
 **xiq_update_alert_rule_request** | [**XiqUpdateAlertRuleRequest**](XiqUpdateAlertRuleRequest.md)|  | 

### Return type

[**XiqAlertRule**](XiqAlertRule.md)

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

# **update_alert_webhook_subscription**
> XiqAlertWebhookSubscription update_alert_webhook_subscription(id, xiq_update_alert_webhook_subscription_request)

Update alert webhook subscription

Update alert webhook subscription.

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert webhook subscription ID
xiq_update_alert_webhook_subscription_request = extremecloudiq.XiqUpdateAlertWebhookSubscriptionRequest() # XiqUpdateAlertWebhookSubscriptionRequest | The payload of update alert webhook subscription

    try:
        # Update alert webhook subscription
        api_response = api_instance.update_alert_webhook_subscription(id, xiq_update_alert_webhook_subscription_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->update_alert_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert webhook subscription ID | 
 **xiq_update_alert_webhook_subscription_request** | [**XiqUpdateAlertWebhookSubscriptionRequest**](XiqUpdateAlertWebhookSubscriptionRequest.md)| The payload of update alert webhook subscription | 

### Return type

[**XiqAlertWebhookSubscription**](XiqAlertWebhookSubscription.md)

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

# **verify_subscription_email**
> verify_subscription_email(id)

Email Verification

Send a request to verify an email

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
    api_instance = extremecloudiq.AlertApi(api_client)
    id = 56 # int | The alert email subscription ID

    try:
        # Email Verification
        api_instance.verify_subscription_email(id)
    except ApiException as e:
        print("Exception when calling AlertApi->verify_subscription_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The alert email subscription ID | 

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

