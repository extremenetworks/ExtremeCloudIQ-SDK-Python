# extremecloudiq.AccountApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_viq**](AccountApi.md#backup_viq) | **POST** /account/viq/:backup | Backup VIQ
[**download_viq_report**](AccountApi.md#download_viq_report) | **GET** /account/viq/download | Download VIQ data file and logs
[**export_import_status**](AccountApi.md#export_import_status) | **GET** /account/viq/export-import-status | Get running export/import status 
[**export_viq**](AccountApi.md#export_viq) | **POST** /account/viq/export | [LRO] Export VIQ data
[**get_default_device_password**](AccountApi.md#get_default_device_password) | **GET** /account/viq/default-device-password | Get the default device password in the account
[**get_home_account**](AccountApi.md#get_home_account) | **GET** /account/home | Get home ExtremeCloud IQ account info
[**get_viq_info**](AccountApi.md#get_viq_info) | **GET** /account/viq | Get VIQ Info
[**import_viq**](AccountApi.md#import_viq) | **POST** /account/viq/import | [LRO] Import VIQ data
[**list_external_accounts**](AccountApi.md#list_external_accounts) | **GET** /account/external | List accessible external guest accounts
[**switch_account**](AccountApi.md#switch_account) | **POST** /account/:switch | Switch to another ExtremeCloud IQ account
[**update_default_device_password**](AccountApi.md#update_default_device_password) | **PUT** /account/viq/default-device-password | Update the default device password in the account


# **backup_viq**
> backup_viq()

Backup VIQ

Backup VIQ in ExtremeCloud IQ.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    
    try:
        # Backup VIQ
        api_instance.backup_viq()
    except ApiException as e:
        print("Exception when calling AccountApi->backup_viq: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **download_viq_report**
> list[str] download_viq_report(report_name)

Download VIQ data file and logs

This is used to download the VIQ export data or export/import logs

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
    api_instance = extremecloudiq.AccountApi(api_client)
    report_name = 'report_name_example' # str | The report full name

    try:
        # Download VIQ data file and logs
        api_response = api_instance.download_viq_report(report_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->download_viq_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| The report full name | 

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

# **export_import_status**
> XiqViqExportImportStatusResponse export_import_status(viq_operation_type)

Get running export/import status 

This is used check the live status of VIQ export or import

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
    api_instance = extremecloudiq.AccountApi(api_client)
    viq_operation_type = extremecloudiq.XiqViqOperationType() # XiqViqOperationType | Select the type of operation to get status 

    try:
        # Get running export/import status 
        api_response = api_instance.export_import_status(viq_operation_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->export_import_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viq_operation_type** | [**XiqViqOperationType**](.md)| Select the type of operation to get status  | 

### Return type

[**XiqViqExportImportStatusResponse**](XiqViqExportImportStatusResponse.md)

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

# **export_viq**
> XiqViqExportResponse export_viq(timeout_in_seconds=timeout_in_seconds, exclude_device_firmware=exclude_device_firmware)

[LRO] Export VIQ data

This is used to Export VIQ data. 

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
    api_instance = extremecloudiq.AccountApi(api_client)
    timeout_in_seconds = 1800 # int | The maximum export duration (optional) (default to 1800)
exclude_device_firmware = False # bool | Whether exclude device firmwares from VIQ export file or not (optional) (default to False)

    try:
        # [LRO] Export VIQ data
        api_response = api_instance.export_viq(timeout_in_seconds=timeout_in_seconds, exclude_device_firmware=exclude_device_firmware)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->export_viq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout_in_seconds** | **int**| The maximum export duration | [optional] [default to 1800]
 **exclude_device_firmware** | **bool**| Whether exclude device firmwares from VIQ export file or not | [optional] [default to False]

### Return type

[**XiqViqExportResponse**](XiqViqExportResponse.md)

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

# **get_default_device_password**
> XiqDefaultDevicePassword get_default_device_password()

Get the default device password in the account

Get the default device password in the account.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    
    try:
        # Get the default device password in the account
        api_response = api_instance.get_default_device_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_default_device_password: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqDefaultDevicePassword**](XiqDefaultDevicePassword.md)

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

# **get_home_account**
> XiqAccount get_home_account()

Get home ExtremeCloud IQ account info

Get home ExtremeCloud IQ account info.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    
    try:
        # Get home ExtremeCloud IQ account info
        api_response = api_instance.get_home_account()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_home_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqAccount**](XiqAccount.md)

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

# **get_viq_info**
> XiqViq get_viq_info()

Get VIQ Info

Get account VIQ and license info.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    
    try:
        # Get VIQ Info
        api_response = api_instance.get_viq_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_viq_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XiqViq**](XiqViq.md)

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

# **import_viq**
> XiqViqImportResponse import_viq(import_file, timeout_in_seconds=timeout_in_seconds, resend_user_notifications=resend_user_notifications)

[LRO] Import VIQ data

This is used import VIQ details from a file

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
    api_instance = extremecloudiq.AccountApi(api_client)
    import_file = '/path/to/file' # file | Select the file to import
timeout_in_seconds = 1800 # int | The maximum import duration (optional) (default to 1800)
resend_user_notifications = False # bool | Resend Cloud PPSK/RADIUS password through email/SMS (optional) (default to False)

    try:
        # [LRO] Import VIQ data
        api_response = api_instance.import_viq(import_file, timeout_in_seconds=timeout_in_seconds, resend_user_notifications=resend_user_notifications)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->import_viq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_file** | **file**| Select the file to import | 
 **timeout_in_seconds** | **int**| The maximum import duration | [optional] [default to 1800]
 **resend_user_notifications** | **bool**| Resend Cloud PPSK/RADIUS password through email/SMS | [optional] [default to False]

### Return type

[**XiqViqImportResponse**](XiqViqImportResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_accounts**
> list[XiqExternalAccount] list_external_accounts()

List accessible external guest accounts

List accessible external ExtremeCloud IQ accounts.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    
    try:
        # List accessible external guest accounts
        api_response = api_instance.list_external_accounts()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->list_external_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqExternalAccount]**](XiqExternalAccount.md)

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

# **switch_account**
> XiqLoginResponse switch_account(id=id)

Switch to another ExtremeCloud IQ account

Switch to external ExtremeCloud IQ account or switch back to home ExtremeCloud IQ account.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    id = 56 # int | The account ID to switch, switch back to home ExtremeCloud IQ account if not provide (optional)

    try:
        # Switch to another ExtremeCloud IQ account
        api_response = api_instance.switch_account(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->switch_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The account ID to switch, switch back to home ExtremeCloud IQ account if not provide | [optional] 

### Return type

[**XiqLoginResponse**](XiqLoginResponse.md)

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

# **update_default_device_password**
> update_default_device_password(body)

Update the default device password in the account

Update the default device password in the global setting for accessing the console/shell of the devices.

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
    api_instance = extremecloudiq.AccountApi(api_client)
    body = 'body_example' # str | The new default device password

    try:
        # Update the default device password in the account
        api_instance.update_default_device_password(body)
    except ApiException as e:
        print("Exception when calling AccountApi->update_default_device_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The new default device password | 

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

