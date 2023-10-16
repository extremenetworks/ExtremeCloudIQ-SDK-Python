# extremecloudiq.LogApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_logs_report**](LogApi.md#audit_logs_report) | **POST** /logs/audit/reports | [LRO] Create audit logs report
[**download_audit_logs_report**](LogApi.md#download_audit_logs_report) | **GET** /logs/audit/reports/{id} | Download audit logs
[**list_accounting_logs**](LogApi.md#list_accounting_logs) | **GET** /logs/accounting | List accounting logs
[**list_audit_logs**](LogApi.md#list_audit_logs) | **GET** /logs/audit | List audit logs
[**list_auth_logs**](LogApi.md#list_auth_logs) | **GET** /logs/auth | List auth logs
[**list_credential_logs**](LogApi.md#list_credential_logs) | **GET** /logs/credential | List credential logs
[**list_email_logs**](LogApi.md#list_email_logs) | **GET** /logs/email | List Email logs
[**list_sms_logs**](LogApi.md#list_sms_logs) | **GET** /logs/sms | List SMS logs


# **audit_logs_report**
> XiqAuditLogReport audit_logs_report(sort_field=sort_field, sort_order=sort_order, categories=categories, username=username, start_time=start_time, end_time=end_time, time_zone_offset=time_zone_offset, keyword=keyword, _async=_async)

[LRO] Create audit logs report

Creates a report page of audit logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    sort_field = extremecloudiq.XiqAuditLogSortField() # XiqAuditLogSortField | The field for sorting (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
categories = [extremecloudiq.XiqAuditLogCategory()] # list[XiqAuditLogCategory] | Audit category (optional)
username = 'username_example' # str | The user login name (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative, endTime - startTime must be no greater than 2592000000 (30 days) (optional)
time_zone_offset = 56 # int | The time zone off set (optional)
keyword = 'keyword_example' # str | The case-insensitive keyword to search in description (optional)
_async = False # bool | Whether to enable async mode (optional) (default to False)

    try:
        # [LRO] Create audit logs report
        api_response = api_instance.audit_logs_report(sort_field=sort_field, sort_order=sort_order, categories=categories, username=username, start_time=start_time, end_time=end_time, time_zone_offset=time_zone_offset, keyword=keyword, _async=_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->audit_logs_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_field** | [**XiqAuditLogSortField**](.md)| The field for sorting | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **categories** | [**list[XiqAuditLogCategory]**](XiqAuditLogCategory.md)| Audit category | [optional] 
 **username** | **str**| The user login name | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative, endTime - startTime must be no greater than 2592000000 (30 days) | [optional] 
 **time_zone_offset** | **int**| The time zone off set | [optional] 
 **keyword** | **str**| The case-insensitive keyword to search in description | [optional] 
 **_async** | **bool**| Whether to enable async mode | [optional] [default to False]

### Return type

[**XiqAuditLogReport**](XiqAuditLogReport.md)

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

# **download_audit_logs_report**
> list[str] download_audit_logs_report(id)

Download audit logs

Download report of audit logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    id = 56 # int | The report ID

    try:
        # Download audit logs
        api_response = api_instance.download_audit_logs_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->download_audit_logs_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The report ID | 

### Return type

**list[str]**

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

# **list_accounting_logs**
> PagedXiqAccountingLog list_accounting_logs(page=page, limit=limit, username=username, calling_station_id=calling_station_id, start_time=start_time, end_time=end_time)

List accounting logs

List a page of accounting logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
username = 'username_example' # str | The user login name (optional)
calling_station_id = 'calling_station_id_example' # str | The calling station ID (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative (optional)

    try:
        # List accounting logs
        api_response = api_instance.list_accounting_logs(page=page, limit=limit, username=username, calling_station_id=calling_station_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_accounting_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **username** | **str**| The user login name | [optional] 
 **calling_station_id** | **str**| The calling station ID | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative | [optional] 

### Return type

[**PagedXiqAccountingLog**](PagedXiqAccountingLog.md)

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

# **list_audit_logs**
> PagedXiqAuditLog list_audit_logs(start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, categories=categories, username=username, keyword=keyword)

List audit logs

List a page of audit logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970. Note: endTime - startTime must be no greater than 2592000000 (30 days)
page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 500 (optional) (default to 10)
sort_field = extremecloudiq.XiqAuditLogSortField() # XiqAuditLogSortField | The field for sorting (optional)
sort_order = extremecloudiq.XiqSortOrder() # XiqSortOrder | The sorting order (optional)
categories = [extremecloudiq.XiqAuditLogCategory()] # list[XiqAuditLogCategory] | Audit category (optional)
username = 'username_example' # str | The user login name (optional)
keyword = 'keyword_example' # str | The case-insensitive keyword to search in description (optional)

    try:
        # List audit logs
        api_response = api_instance.list_audit_logs(start_time, end_time, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order, categories=categories, username=username, keyword=keyword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970 | 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970. Note: endTime - startTime must be no greater than 2592000000 (30 days) | 
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 500 | [optional] [default to 10]
 **sort_field** | [**XiqAuditLogSortField**](.md)| The field for sorting | [optional] 
 **sort_order** | [**XiqSortOrder**](.md)| The sorting order | [optional] 
 **categories** | [**list[XiqAuditLogCategory]**](XiqAuditLogCategory.md)| Audit category | [optional] 
 **username** | **str**| The user login name | [optional] 
 **keyword** | **str**| The case-insensitive keyword to search in description | [optional] 

### Return type

[**PagedXiqAuditLog**](PagedXiqAuditLog.md)

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

# **list_auth_logs**
> PagedXiqAuthLog list_auth_logs(page=page, limit=limit, username=username, calling_station_id=calling_station_id, start_time=start_time, end_time=end_time)

List auth logs

List a page of auth logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
username = 'username_example' # str | The user login name (optional)
calling_station_id = 'calling_station_id_example' # str | The calling station ID (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative (optional)

    try:
        # List auth logs
        api_response = api_instance.list_auth_logs(page=page, limit=limit, username=username, calling_station_id=calling_station_id, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_auth_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **username** | **str**| The user login name | [optional] 
 **calling_station_id** | **str**| The calling station ID | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative | [optional] 

### Return type

[**PagedXiqAuthLog**](PagedXiqAuthLog.md)

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

# **list_credential_logs**
> PagedXiqCredentialLog list_credential_logs(page=page, limit=limit, username=username, start_time=start_time, end_time=end_time)

List credential logs

List a page of credential logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
username = 'username_example' # str | The user login name (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative (optional)

    try:
        # List credential logs
        api_response = api_instance.list_credential_logs(page=page, limit=limit, username=username, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_credential_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **username** | **str**| The user login name | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative | [optional] 

### Return type

[**PagedXiqCredentialLog**](PagedXiqCredentialLog.md)

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

# **list_email_logs**
> PagedXiqEmailLog list_email_logs(page=page, limit=limit, username=username, start_time=start_time, end_time=end_time)

List Email logs

List a page of Email logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
username = 'username_example' # str | The user login name (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative (optional)

    try:
        # List Email logs
        api_response = api_instance.list_email_logs(page=page, limit=limit, username=username, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_email_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **username** | **str**| The user login name | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative | [optional] 

### Return type

[**PagedXiqEmailLog**](PagedXiqEmailLog.md)

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

# **list_sms_logs**
> PagedXiqSmsLog list_sms_logs(page=page, limit=limit, phone_number=phone_number, start_time=start_time, end_time=end_time)

List SMS logs

List a page of SMS logs.

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
    api_instance = extremecloudiq.LogApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
phone_number = 'phone_number_example' # str | The phone number (optional)
start_time = 56 # int | The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative (optional)
end_time = 56 # int | The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative (optional)

    try:
        # List SMS logs
        api_response = api_instance.list_sms_logs(page=page, limit=limit, phone_number=phone_number, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->list_sms_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **phone_number** | **str**| The phone number | [optional] 
 **start_time** | **int**| The start time to query, epoch time in milliseconds since 1/1/1970, default is 0 if not specified or is negative | [optional] 
 **end_time** | **int**| The end time to query, epoch time in milliseconds since 1/1/1970, default is now if not specified or is negative | [optional] 

### Return type

[**PagedXiqSmsLog**](PagedXiqSmsLog.md)

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

