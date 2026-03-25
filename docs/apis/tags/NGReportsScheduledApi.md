<a id="__pageTop"></a>
# extremecloudiq.apis.tags.ng_reports_scheduled_api.NGReportsScheduledApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_recipients_to_report**](#add_recipients_to_report) | **put** /ng-reports/scheduled/{reportId}/recipients | Add Recipients to Report
[**create_scheduled_custom_report**](#create_scheduled_custom_report) | **post** /ng-reports/scheduled/custom | Create a scheduled custom report
[**delete_recipients_from_report**](#delete_recipients_from_report) | **post** /ng-reports/scheduled/{reportId}/recipients | Delete Recipients from Report
[**delete_report_runs**](#delete_report_runs) | **delete** /ng-reports/scheduled/runs | Delete report runs
[**delete_scheduled_custom_reports**](#delete_scheduled_custom_reports) | **delete** /ng-reports/scheduled/custom | Delete scheduled custom reports
[**download_scheduled_report_file**](#download_scheduled_report_file) | **get** /ng-reports/scheduled/reports/download | Download or Preview Scheduled Report File
[**enable_disable_report_schedule**](#enable_disable_report_schedule) | **patch** /ng-reports/scheduled/{reportScheduleId} | Enable or Disable Report Schedule
[**get_custom_report_schedule**](#get_custom_report_schedule) | **get** /ng-reports/scheduled/custom/{reportId} | Get a custom report schedule
[**get_network_summary_reports**](#get_network_summary_reports) | **get** /ng-reports/scheduled/network-summary | Get Network Summary Reports
[**get_pci_compliance_reports**](#get_pci_compliance_reports) | **get** /ng-reports/scheduled/pci-compliance | Get PCI Compliance Reports
[**get_recipients_for_report**](#get_recipients_for_report) | **get** /ng-reports/scheduled/{reportId}/recipients | Get Recipients for Report
[**get_recipients_for_report_run**](#get_recipients_for_report_run) | **get** /ng-reports/scheduled/runs/{reportRunId}/recipients | Get Recipients for Report Run
[**get_report_runs_for_schedule**](#get_report_runs_for_schedule) | **get** /ng-reports/scheduled/custom/{reportScheduleId}/runs | Get report runs for a schedule
[**list_scheduled_custom_reports**](#list_scheduled_custom_reports) | **get** /ng-reports/scheduled/custom | List Custom Report Schedules
[**update_scheduled_custom_report**](#update_scheduled_custom_report) | **put** /ng-reports/scheduled/custom/{reportId} | Update a scheduled custom report

# **add_recipients_to_report**
<a id="add_recipients_to_report"></a>
> add_recipients_to_report(report_idxiq_recipient_cns_info)

Add Recipients to Report

Adds a list of recipient emails to the specified report.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_recipient_cns_info import XiqRecipientCnsInfo
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportId': 1,
    }
    body = [
        XiqRecipientCnsInfo(
            email="email_example",
            notifier_id=1,
        )
    ]
    try:
        # Add Recipients to Report
        api_response = api_instance.add_recipients_to_report(
            path_params=path_params,
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->add_recipients_to_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRecipientCnsInfo**]({{complexTypePrefix}}XiqRecipientCnsInfo.md) | [**XiqRecipientCnsInfo**]({{complexTypePrefix}}XiqRecipientCnsInfo.md) | [**XiqRecipientCnsInfo**]({{complexTypePrefix}}XiqRecipientCnsInfo.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportId | ReportIdSchema | | 

# ReportIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_recipients_to_report.ApiResponseFor200) | OK

#### add_recipients_to_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_scheduled_custom_report**
<a id="create_scheduled_custom_report"></a>
> XiqCustomReportResponse create_scheduled_custom_report(xiq_custom_report_request)

Create a scheduled custom report

Create a new scheduled custom report with the provided details.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_custom_report_request import XiqCustomReportRequest
from extremecloudiq.model.xiq_custom_report_response import XiqCustomReportResponse
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqCustomReportRequest(
        metrics=[
            XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS")
        ],
        report_name="report_name_example",
        report_description="report_description_example",
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        ssids=[
            "ssids_example"
        ],
        bands=[
            XiqDiagnosticsBands("TWO_GHZ")
        ],
        recipients=[
            XiqRecipientCnsInfo(
                email="email_example",
                notifier_id=1,
            )
        ],
        schedules=[
            XiqReportScheduleRequest(
                frequency_type=XiqScheduleFrequency("DAILY"),
                schedule_time="schedule_time_example",
                schedule_timezone="schedule_timezone_example",
                schedule_days=[
                    1
                ],
                enable_schedule=True,
            )
        ],
        file_format=[
            XiqReportFileFormat("PDF")
        ],
    )
    try:
        # Create a scheduled custom report
        api_response = api_instance.create_scheduled_custom_report(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->create_scheduled_custom_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCustomReportRequest**](../../models/XiqCustomReportRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_scheduled_custom_report.ApiResponseFor200) | OK

#### create_scheduled_custom_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCustomReportResponse**](../../models/XiqCustomReportResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_recipients_from_report**
<a id="delete_recipients_from_report"></a>
> delete_recipients_from_report(report_idxiq_recipient_ids_request)

Delete Recipients from Report

Deletes a list of recipient emails from the specified report.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_recipient_ids_request import XiqRecipientIdsRequest
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportId': 1,
    }
    body = XiqRecipientIdsRequest(
        recipient_ids=[
            1
        ],
    )
    try:
        # Delete Recipients from Report
        api_response = api_instance.delete_recipients_from_report(
            path_params=path_params,
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->delete_recipients_from_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqRecipientIdsRequest**](../../models/XiqRecipientIdsRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportId | ReportIdSchema | | 

# ReportIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_recipients_from_report.ApiResponseFor200) | OK

#### delete_recipients_from_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_report_runs**
<a id="delete_report_runs"></a>
> delete_report_runs(report_runs_ids)

Delete report runs

Bulk delete report runs by IDs.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'reportRunsIds': [
        1
    ],
    }
    try:
        # Delete report runs
        api_response = api_instance.delete_report_runs(
            query_params=query_params,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->delete_report_runs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportRunsIds | ReportRunsIdsSchema | | 


# ReportRunsIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_report_runs.ApiResponseFor200) | OK

#### delete_report_runs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_scheduled_custom_reports**
<a id="delete_scheduled_custom_reports"></a>
> delete_scheduled_custom_reports(report_schedule_ids)

Delete scheduled custom reports

Bulk delete scheduled custom reports by IDs.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'reportScheduleIds': [
        1
    ],
    }
    try:
        # Delete scheduled custom reports
        api_response = api_instance.delete_scheduled_custom_reports(
            query_params=query_params,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->delete_scheduled_custom_reports: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportScheduleIds | ReportScheduleIdsSchema | | 


# ReportScheduleIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_scheduled_custom_reports.ApiResponseFor200) | OK

#### delete_scheduled_custom_reports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_scheduled_report_file**
<a id="download_scheduled_report_file"></a>
> [str] download_scheduled_report_file(file_format)

Download or Preview Scheduled Report File

Downloads or previews a scheduled report file in PDF or XLSX format.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_report_file_format import XiqReportFileFormat
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'fileFormat': XiqReportFileFormat("PDF"),
    }
    try:
        # Download or Preview Scheduled Report File
        api_response = api_instance.download_scheduled_report_file(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->download_scheduled_report_file: %s\n" % e)

    # example passing only optional values
    query_params = {
        'reportRunId': 1,
        'fileFormat': XiqReportFileFormat("PDF"),
        'preview': False,
    }
    try:
        # Download or Preview Scheduled Report File
        api_response = api_instance.download_scheduled_report_file(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->download_scheduled_report_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportRunId | ReportRunIdSchema | | optional
fileFormat | FileFormatSchema | | 
preview | PreviewSchema | | optional


# ReportRunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# FileFormatSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqReportFileFormat**](../../models/XiqReportFileFormat.md) |  | 


# PreviewSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_scheduled_report_file.ApiResponseFor200) | OK

#### download_scheduled_report_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_disable_report_schedule**
<a id="enable_disable_report_schedule"></a>
> enable_disable_report_schedule(report_schedule_idenable_schedule)

Enable or Disable Report Schedule

Enables or disables a report schedule based on the provided flag.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportScheduleId': 1,
    }
    query_params = {
        'enableSchedule': True,
    }
    try:
        # Enable or Disable Report Schedule
        api_response = api_instance.enable_disable_report_schedule(
            path_params=path_params,
            query_params=query_params,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->enable_disable_report_schedule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
enableSchedule | EnableScheduleSchema | | 


# EnableScheduleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportScheduleId | ReportScheduleIdSchema | | 

# ReportScheduleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enable_disable_report_schedule.ApiResponseFor200) | OK

#### enable_disable_report_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_report_schedule**
<a id="get_custom_report_schedule"></a>
> XiqCustomReportResponse get_custom_report_schedule(report_id)

Get a custom report schedule

Fetch details of a scheduled custom report by its ID.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_custom_report_response import XiqCustomReportResponse
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportId': 1,
    }
    try:
        # Get a custom report schedule
        api_response = api_instance.get_custom_report_schedule(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_custom_report_schedule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportId | ReportIdSchema | | 

# ReportIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_report_schedule.ApiResponseFor200) | OK

#### get_custom_report_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCustomReportResponse**](../../models/XiqCustomReportResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_network_summary_reports**
<a id="get_network_summary_reports"></a>
> XiqNgCannedReport get_network_summary_reports()

Get Network Summary Reports

Retrieves all network summary reports with optional keyword filtering.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_ng_canned_report import XiqNgCannedReport
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
    }
    try:
        # Get Network Summary Reports
        api_response = api_instance.get_network_summary_reports(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_network_summary_reports: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_network_summary_reports.ApiResponseFor200) | OK

#### get_network_summary_reports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqNgCannedReport**](../../models/XiqNgCannedReport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pci_compliance_reports**
<a id="get_pci_compliance_reports"></a>
> XiqNgCannedReport get_pci_compliance_reports()

Get PCI Compliance Reports

Retrieves all PCI compliance reports with optional keyword filtering.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_ng_canned_report import XiqNgCannedReport
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
    }
    try:
        # Get PCI Compliance Reports
        api_response = api_instance.get_pci_compliance_reports(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_pci_compliance_reports: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pci_compliance_reports.ApiResponseFor200) | OK

#### get_pci_compliance_reports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqNgCannedReport**](../../models/XiqNgCannedReport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_recipients_for_report**
<a id="get_recipients_for_report"></a>
> XiqRecipientsForReportSchedule get_recipients_for_report(report_id)

Get Recipients for Report

Retrieves all recipients for a given report.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_recipients_for_report_schedule import XiqRecipientsForReportSchedule
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportId': 1,
    }
    query_params = {
    }
    try:
        # Get Recipients for Report
        api_response = api_instance.get_recipients_for_report(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_recipients_for_report: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reportId': 1,
    }
    query_params = {
        'keyword': "keyword_example",
    }
    try:
        # Get Recipients for Report
        api_response = api_instance.get_recipients_for_report(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_recipients_for_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportId | ReportIdSchema | | 

# ReportIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_recipients_for_report.ApiResponseFor200) | OK

#### get_recipients_for_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqRecipientsForReportSchedule**](../../models/XiqRecipientsForReportSchedule.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_recipients_for_report_run**
<a id="get_recipients_for_report_run"></a>
> XiqRecipientsForReportRun get_recipients_for_report_run(report_run_id)

Get Recipients for Report Run

Retrieves all recipients for a given report run.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_recipients_for_report_run import XiqRecipientsForReportRun
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportRunId': 1,
    }
    query_params = {
    }
    try:
        # Get Recipients for Report Run
        api_response = api_instance.get_recipients_for_report_run(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_recipients_for_report_run: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reportRunId': 1,
    }
    query_params = {
        'keyword': "keyword_example",
    }
    try:
        # Get Recipients for Report Run
        api_response = api_instance.get_recipients_for_report_run(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_recipients_for_report_run: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportRunId | ReportRunIdSchema | | 

# ReportRunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_recipients_for_report_run.ApiResponseFor200) | OK

#### get_recipients_for_report_run.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqRecipientsForReportRun**](../../models/XiqRecipientsForReportRun.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_report_runs_for_schedule**
<a id="get_report_runs_for_schedule"></a>
> [XiqReportRunsResponse] get_report_runs_for_schedule(report_schedule_id)

Get report runs for a schedule

Fetch all report runs for a specific schedule ID and optional frequencies.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_report_runs_response import XiqReportRunsResponse
from extremecloudiq.model.xiq_schedule_frequency import XiqScheduleFrequency
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportScheduleId': 1,
    }
    query_params = {
    }
    try:
        # Get report runs for a schedule
        api_response = api_instance.get_report_runs_for_schedule(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_report_runs_for_schedule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reportScheduleId': 1,
    }
    query_params = {
        'frequency': [
        XiqScheduleFrequency("DAILY")
    ],
    }
    try:
        # Get report runs for a schedule
        api_response = api_instance.get_report_runs_for_schedule(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->get_report_runs_for_schedule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
frequency | FrequencySchema | | optional


# FrequencySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) | [**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) | [**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportScheduleId | ReportScheduleIdSchema | | 

# ReportScheduleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_report_runs_for_schedule.ApiResponseFor200) | OK

#### get_report_runs_for_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqReportRunsResponse**]({{complexTypePrefix}}XiqReportRunsResponse.md) | [**XiqReportRunsResponse**]({{complexTypePrefix}}XiqReportRunsResponse.md) | [**XiqReportRunsResponse**]({{complexTypePrefix}}XiqReportRunsResponse.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_scheduled_custom_reports**
<a id="list_scheduled_custom_reports"></a>
> PagedXiqCustomReportSchedule list_scheduled_custom_reports()

List Custom Report Schedules

List custom report schedules with filters and pagination.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_schedule_frequency import XiqScheduleFrequency
from extremecloudiq.model.paged_xiq_custom_report_schedule import PagedXiqCustomReportSchedule
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'frequency': [
        XiqScheduleFrequency("DAILY")
    ],
        'keyword': "keyword_example",
    }
    try:
        # List Custom Report Schedules
        api_response = api_instance.list_scheduled_custom_reports(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->list_scheduled_custom_reports: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
limit | LimitSchema | | optional
frequency | FrequencySchema | | optional
keyword | KeywordSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# FrequencySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) | [**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) | [**XiqScheduleFrequency**]({{complexTypePrefix}}XiqScheduleFrequency.md) |  | 

# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_scheduled_custom_reports.ApiResponseFor200) | OK

#### list_scheduled_custom_reports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqCustomReportSchedule**](../../models/PagedXiqCustomReportSchedule.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_scheduled_custom_report**
<a id="update_scheduled_custom_report"></a>
> XiqCustomReportResponse update_scheduled_custom_report(report_idxiq_update_custom_report_request)

Update a scheduled custom report

Update an existing scheduled custom report identified by reportScheduleId.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ng_reports_scheduled_api
from extremecloudiq.model.xiq_update_custom_report_request import XiqUpdateCustomReportRequest
from extremecloudiq.model.xiq_custom_report_response import XiqCustomReportResponse
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
    api_instance = ng_reports_scheduled_api.NGReportsScheduledApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reportId': 1,
    }
    body = XiqUpdateCustomReportRequest(
        metrics=[
            XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS")
        ],
        report_name="report_name_example",
        report_description="report_description_example",
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        ssids=[
            "ssids_example"
        ],
        bands=[
            XiqDiagnosticsBands("TWO_GHZ")
        ],
        recipients=[
            XiqRecipientCnsInfo(
                email="email_example",
                notifier_id=1,
            )
        ],
        schedules=[
            XiqUpdateReportScheduleRequest(
                report_schedule_id=1,
                frequency_type=XiqScheduleFrequency("DAILY"),
                schedule_time="schedule_time_example",
                schedule_timezone="schedule_timezone_example",
                schedule_days=[
                    1
                ],
                enable_schedule=True,
            )
        ],
        file_format=[
            XiqReportFileFormat("PDF")
        ],
    )
    try:
        # Update a scheduled custom report
        api_response = api_instance.update_scheduled_custom_report(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGReportsScheduledApi->update_scheduled_custom_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqUpdateCustomReportRequest**](../../models/XiqUpdateCustomReportRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reportId | ReportIdSchema | | 

# ReportIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_scheduled_custom_report.ApiResponseFor200) | OK

#### update_scheduled_custom_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCustomReportResponse**](../../models/XiqCustomReportResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

