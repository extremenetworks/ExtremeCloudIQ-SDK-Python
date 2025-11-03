<a id="__pageTop"></a>
# extremecloudiq.apis.tags.ngreports_api.NGREPORTSApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report**](#download_report) | **get** /ng-reports/download/reports/{id} | Download the reports
[**get_application_list_for_filter**](#get_application_list_for_filter) | **post** /ng-reports/metadata/application | List of Applications for filtering
[**get_band_metadata**](#get_band_metadata) | **post** /ng-reports/metadata/bands | List of Band for filtering
[**get_channel_filter_metadata**](#get_channel_filter_metadata) | **post** /ng-reports/metadata/channel | List of Channel for filtering
[**get_client_list_for_filter**](#get_client_list_for_filter) | **post** /ng-reports/metadata/client | List of Clients for filtering
[**get_connection_types**](#get_connection_types) | **post** /ng-reports/metadata/connection-type | List of Connection Type for filtering
[**get_device_list_for_filter**](#get_device_list_for_filter) | **post** /ng-reports/metadata/device | List of Devices for filtering
[**get_os_filter_metadata**](#get_os_filter_metadata) | **post** /ng-reports/metadata/os | List of OS for filtering
[**get_ssis_metadata**](#get_ssis_metadata) | **post** /ng-reports/metadata/ssids | List of SSIDs for filtering
[**get_users_list_for_filter**](#get_users_list_for_filter) | **post** /ng-reports/metadata/user | List of Users for filtering
[**q_oe_diagnostics_help**](#q_oe_diagnostics_help) | **get** /ng-reports/information/{metrics} | Information about QoE-Diagnostics Metrics
[**q_oe_diagnostics_help1**](#q_oe_diagnostics_help1) | **get** /ng-reports/information/ | Information about QoE-Diagnostics Metrics
[**qoe_diagnostics_table_data**](#qoe_diagnostics_table_data) | **post** /ng-reports/tabledata | 
[**qoe_diagnostics_time_series_data**](#qoe_diagnostics_time_series_data) | **post** /ng-reports/timeseries | 
[**qoe_diagnostics_xlsx_data**](#qoe_diagnostics_xlsx_data) | **post** /ng-reports/downloads/reports | 

# **download_report**
<a id="download_report"></a>
> [str] download_report(id)

Download the reports

Download reports of Metrics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Download the reports
        api_response = api_instance.download_report(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->download_report: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_report.ApiResponseFor200) | Report downloaded successfully
404 | [ApiResponseFor404](#download_report.ApiResponseFor404) | Report not found

#### download_report.ApiResponseFor200
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

#### download_report.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

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

# **get_application_list_for_filter**
<a id="get_application_list_for_filter"></a>
> [XiqApplication] get_application_list_for_filter(xiq_qoe_metadata_application_filter)

List of Applications for filtering

Gives List of Applciations for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_application import XiqApplication
from extremecloudiq.model.xiq_qoe_metadata_application_filter import XiqQoeMetadataApplicationFilter
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeMetadataApplicationFilter(
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        usernames=[
            "usernames_example"
        ],
        client_macs=[
            "client_macs_example"
        ],
    )
    try:
        # List of Applications for filtering
        api_response = api_instance.get_application_list_for_filter(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_application_list_for_filter: %s\n" % e)
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
[**XiqQoeMetadataApplicationFilter**](../../models/XiqQoeMetadataApplicationFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_application_list_for_filter.ApiResponseFor200) | OK

#### get_application_list_for_filter.ApiResponseFor200
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
[**XiqApplication**]({{complexTypePrefix}}XiqApplication.md) | [**XiqApplication**]({{complexTypePrefix}}XiqApplication.md) | [**XiqApplication**]({{complexTypePrefix}}XiqApplication.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_band_metadata**
<a id="get_band_metadata"></a>
> [XiqDiagnosticsBands] get_band_metadata(xiq_qoe_diagnostics_band_metadata_filter)

List of Band for filtering

Gives List of Band for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_band_metadata_filter import XiqQoeDiagnosticsBandMetadataFilter
from extremecloudiq.model.xiq_diagnostics_bands import XiqDiagnosticsBands
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsBandMetadataFilter(
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
        start_time=1,
        end_time=1,
    )
    try:
        # List of Band for filtering
        api_response = api_instance.get_band_metadata(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_band_metadata: %s\n" % e)
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
[**XiqQoeDiagnosticsBandMetadataFilter**](../../models/XiqQoeDiagnosticsBandMetadataFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_band_metadata.ApiResponseFor200) | OK

#### get_band_metadata.ApiResponseFor200
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
[**XiqDiagnosticsBands**]({{complexTypePrefix}}XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**]({{complexTypePrefix}}XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**]({{complexTypePrefix}}XiqDiagnosticsBands.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_channel_filter_metadata**
<a id="get_channel_filter_metadata"></a>
> [int] get_channel_filter_metadata(xiq_qoe_diagnostics_channel_metadata_filter)

List of Channel for filtering

Gives List of Channel for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_channel_metadata_filter import XiqQoeDiagnosticsChannelMetadataFilter
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsChannelMetadataFilter(
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
    )
    try:
        # List of Channel for filtering
        api_response = api_instance.get_channel_filter_metadata(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_channel_filter_metadata: %s\n" % e)
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
[**XiqQoeDiagnosticsChannelMetadataFilter**](../../models/XiqQoeDiagnosticsChannelMetadataFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_channel_filter_metadata.ApiResponseFor200) | OK

#### get_channel_filter_metadata.ApiResponseFor200
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
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client_list_for_filter**
<a id="get_client_list_for_filter"></a>
> [XiqClient] get_client_list_for_filter(xiq_qoe_metadata_client_filter)

List of Clients for filtering

Gives List of Clients for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_metadata_client_filter import XiqQoeMetadataClientFilter
from extremecloudiq.model.xiq_client import XiqClient
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeMetadataClientFilter(
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        usernames=[
            "usernames_example"
        ],
    )
    try:
        # List of Clients for filtering
        api_response = api_instance.get_client_list_for_filter(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_client_list_for_filter: %s\n" % e)
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
[**XiqQoeMetadataClientFilter**](../../models/XiqQoeMetadataClientFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_client_list_for_filter.ApiResponseFor200) | OK

#### get_client_list_for_filter.ApiResponseFor200
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
[**XiqClient**]({{complexTypePrefix}}XiqClient.md) | [**XiqClient**]({{complexTypePrefix}}XiqClient.md) | [**XiqClient**]({{complexTypePrefix}}XiqClient.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_connection_types**
<a id="get_connection_types"></a>
> [XiqQoeDiagnosticsConnTypes] get_connection_types()

List of Connection Type for filtering

Gives List of Connection Type for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_conn_types import XiqQoeDiagnosticsConnTypes
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List of Connection Type for filtering
        api_response = api_instance.get_connection_types()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_connection_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_connection_types.ApiResponseFor200) | OK

#### get_connection_types.ApiResponseFor200
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
[**XiqQoeDiagnosticsConnTypes**]({{complexTypePrefix}}XiqQoeDiagnosticsConnTypes.md) | [**XiqQoeDiagnosticsConnTypes**]({{complexTypePrefix}}XiqQoeDiagnosticsConnTypes.md) | [**XiqQoeDiagnosticsConnTypes**]({{complexTypePrefix}}XiqQoeDiagnosticsConnTypes.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_list_for_filter**
<a id="get_device_list_for_filter"></a>
> [XiqDevice] get_device_list_for_filter(xiq_qoe_metadata_device_filter)

List of Devices for filtering

Gives List of Devices for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_metadata_device_filter import XiqQoeMetadataDeviceFilter
from extremecloudiq.model.xiq_device import XiqDevice
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeMetadataDeviceFilter(
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
        channels=[
            1
        ],
        os_types=[
            "os_types_example"
        ],
    )
    try:
        # List of Devices for filtering
        api_response = api_instance.get_device_list_for_filter(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_device_list_for_filter: %s\n" % e)
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
[**XiqQoeMetadataDeviceFilter**](../../models/XiqQoeMetadataDeviceFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_list_for_filter.ApiResponseFor200) | OK

#### get_device_list_for_filter.ApiResponseFor200
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
[**XiqDevice**]({{complexTypePrefix}}XiqDevice.md) | [**XiqDevice**]({{complexTypePrefix}}XiqDevice.md) | [**XiqDevice**]({{complexTypePrefix}}XiqDevice.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_os_filter_metadata**
<a id="get_os_filter_metadata"></a>
> [str] get_os_filter_metadata(xiq_qoe_diagnostics_channel_metadata_filter)

List of OS for filtering

Gives List of OS for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_channel_metadata_filter import XiqQoeDiagnosticsChannelMetadataFilter
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsChannelMetadataFilter(
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
    )
    try:
        # List of OS for filtering
        api_response = api_instance.get_os_filter_metadata(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_os_filter_metadata: %s\n" % e)
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
[**XiqQoeDiagnosticsChannelMetadataFilter**](../../models/XiqQoeDiagnosticsChannelMetadataFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_os_filter_metadata.ApiResponseFor200) | OK

#### get_os_filter_metadata.ApiResponseFor200
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

# **get_ssis_metadata**
<a id="get_ssis_metadata"></a>
> [str] get_ssis_metadata(xiq_qoe_diagnostics_ssid_metadata_filter)

List of SSIDs for filtering

Gives List of SSIDs for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_ssid_metadata_filter import XiqQoeDiagnosticsSsidMetadataFilter
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsSsidMetadataFilter(
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        start_time=1,
        end_time=1,
    )
    try:
        # List of SSIDs for filtering
        api_response = api_instance.get_ssis_metadata(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_ssis_metadata: %s\n" % e)
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
[**XiqQoeDiagnosticsSsidMetadataFilter**](../../models/XiqQoeDiagnosticsSsidMetadataFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ssis_metadata.ApiResponseFor200) | OK

#### get_ssis_metadata.ApiResponseFor200
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

# **get_users_list_for_filter**
<a id="get_users_list_for_filter"></a>
> [XiqUser] get_users_list_for_filter(xiq_qoe_metadata_users_filter)

List of Users for filtering

Gives List of Users for filtering

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_metadata_users_filter import XiqQoeMetadataUsersFilter
from extremecloudiq.model.xiq_user import XiqUser
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeMetadataUsersFilter(
        site_ids=[
            1
        ],
        building_ids=[
            1
        ],
        floor_ids=[
            1
        ],
    )
    try:
        # List of Users for filtering
        api_response = api_instance.get_users_list_for_filter(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->get_users_list_for_filter: %s\n" % e)
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
[**XiqQoeMetadataUsersFilter**](../../models/XiqQoeMetadataUsersFilter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_users_list_for_filter.ApiResponseFor200) | OK

#### get_users_list_for_filter.ApiResponseFor200
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
[**XiqUser**]({{complexTypePrefix}}XiqUser.md) | [**XiqUser**]({{complexTypePrefix}}XiqUser.md) | [**XiqUser**]({{complexTypePrefix}}XiqUser.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **q_oe_diagnostics_help**
<a id="q_oe_diagnostics_help"></a>
> [XiqQoeDiagnosticsSummary] q_oe_diagnostics_help(metrics)

Information about QoE-Diagnostics Metrics

 Gives information about metrics, there functionality and applicable filters

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_summary import XiqQoeDiagnosticsSummary
from extremecloudiq.model.xiq_qoe_diagnostics_metrics import XiqQoeDiagnosticsMetrics
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'metrics': XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS"),
    }
    try:
        # Information about QoE-Diagnostics Metrics
        api_response = api_instance.q_oe_diagnostics_help(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->q_oe_diagnostics_help: %s\n" % e)
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
metrics | MetricsSchema | | 

# MetricsSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqQoeDiagnosticsMetrics**](../../models/XiqQoeDiagnosticsMetrics.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#q_oe_diagnostics_help.ApiResponseFor200) | OK

#### q_oe_diagnostics_help.ApiResponseFor200
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
[**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) | [**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) | [**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **q_oe_diagnostics_help1**
<a id="q_oe_diagnostics_help1"></a>
> [XiqQoeDiagnosticsSummary] q_oe_diagnostics_help1()

Information about QoE-Diagnostics Metrics

 Gives information about metrics, there functionality and applicable filters

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_summary import XiqQoeDiagnosticsSummary
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about QoE-Diagnostics Metrics
        api_response = api_instance.q_oe_diagnostics_help1()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->q_oe_diagnostics_help1: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#q_oe_diagnostics_help1.ApiResponseFor200) | OK

#### q_oe_diagnostics_help1.ApiResponseFor200
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
[**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) | [**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) | [**XiqQoeDiagnosticsSummary**]({{complexTypePrefix}}XiqQoeDiagnosticsSummary.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **qoe_diagnostics_table_data**
<a id="qoe_diagnostics_table_data"></a>
> PagedMapStringObject qoe_diagnostics_table_data(xiq_qoe_diagnostics_table_data_filters)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.paged_map_string_object import PagedMapStringObject
from extremecloudiq.model.xiq_qoe_diagnostics_table_data_filters import XiqQoeDiagnosticsTableDataFilters
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsTableDataFilters(
        metrics=XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS"),
        site_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        building_ids=[
            1
        ],
        bands=[
            XiqDiagnosticsBands("TWO_GHZ")
        ],
        contypes=[
            XiqQoeDiagnosticsConnTypes("UNKNOWN")
        ],
        devicetypes=[
            XiqQoeDiagnosticsDeviceTypes("WIRED")
        ],
        vlan_ids=[
            1
        ],
        device_ids=[
            1
        ],
        ssids=[
            "ssids_example"
        ],
        user_names=[
            "user_names_example"
        ],
        client_macs=[
            "client_macs_example"
        ],
        port_nums=[
            1
        ],
        app_ids=[
            1
        ],
        channel_nums=[
            1
        ],
        admin_roles=[
            1
        ],
        start_time=1,
        end_time=1,
        sort_field="TIME_STAMP",
        sort_order=XiqSortOrder("ASC"),
        page_no=1,
        limit=1,
        export_data=False,
        search_parameter="search_parameter_example",
        _async=False,
        os_types=[
            "os_types_example"
        ],
        is_ssid_selected=True,
        is_band_selected=True,
    )
    try:
        api_response = api_instance.qoe_diagnostics_table_data(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->qoe_diagnostics_table_data: %s\n" % e)
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
[**XiqQoeDiagnosticsTableDataFilters**](../../models/XiqQoeDiagnosticsTableDataFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#qoe_diagnostics_table_data.ApiResponseFor200) | OK

#### qoe_diagnostics_table_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedMapStringObject**](../../models/PagedMapStringObject.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **qoe_diagnostics_time_series_data**
<a id="qoe_diagnostics_time_series_data"></a>
> XiqQoeDiagnosticsResponse qoe_diagnostics_time_series_data(xiq_qoe_diagnostics_time_series_filters)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_qoe_diagnostics_time_series_filters import XiqQoeDiagnosticsTimeSeriesFilters
from extremecloudiq.model.xiq_qoe_diagnostics_response import XiqQoeDiagnosticsResponse
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqQoeDiagnosticsTimeSeriesFilters(
        metrics=XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS"),
        site_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        building_ids=[
            1
        ],
        bands=[
            XiqDiagnosticsBands("TWO_GHZ")
        ],
        contypes=[
            XiqQoeDiagnosticsConnTypes("UNKNOWN")
        ],
        devicetypes=[
            XiqQoeDiagnosticsDeviceTypes("WIRED")
        ],
        vlan_ids=[
            1
        ],
        device_ids=[
            1
        ],
        ssids=[
            "ssids_example"
        ],
        user_names=[
            "user_names_example"
        ],
        client_macs=[
            "client_macs_example"
        ],
        port_nums=[
            1
        ],
        app_ids=[
            1
        ],
        channel_nums=[
            1
        ],
        admin_roles=[
            1
        ],
        start_time=1,
        end_time=1,
        _async=False,
        page=1,
        limit=1,
        os_types=[
            "os_types_example"
        ],
        is_ssid_selected=True,
        is_band_selected=True,
    )
    try:
        api_response = api_instance.qoe_diagnostics_time_series_data(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->qoe_diagnostics_time_series_data: %s\n" % e)
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
[**XiqQoeDiagnosticsTimeSeriesFilters**](../../models/XiqQoeDiagnosticsTimeSeriesFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#qoe_diagnostics_time_series_data.ApiResponseFor200) | OK

#### qoe_diagnostics_time_series_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqQoeDiagnosticsResponse**](../../models/XiqQoeDiagnosticsResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **qoe_diagnostics_xlsx_data**
<a id="qoe_diagnostics_xlsx_data"></a>
> NgMetricsReport qoe_diagnostics_xlsx_data(xiq_xlsx_ng_reports_data_filters)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import ngreports_api
from extremecloudiq.model.xiq_xlsx_ng_reports_data_filters import XiqXlsxNgReportsDataFilters
from extremecloudiq.model.ng_metrics_report import NgMetricsReport
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
    api_instance = ngreports_api.NGREPORTSApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqXlsxNgReportsDataFilters(
        metrics=[
            XiqQoeDiagnosticsMetrics("MAX_CONCURRENT_CLIENTS")
        ],
        site_ids=[
            1
        ],
        floor_ids=[
            1
        ],
        building_ids=[
            1
        ],
        bands=[
            XiqDiagnosticsBands("TWO_GHZ")
        ],
        contypes=[
            XiqQoeDiagnosticsConnTypes("UNKNOWN")
        ],
        devicetypes=[
            XiqQoeDiagnosticsDeviceTypes("WIRED")
        ],
        vlan_ids=[
            1
        ],
        device_ids=[
            1
        ],
        ssids=[
            "ssids_example"
        ],
        user_names=[
            "user_names_example"
        ],
        client_macs=[
            "client_macs_example"
        ],
        port_nums=[
            1
        ],
        app_ids=[
            1
        ],
        channel_nums=[
            1
        ],
        admin_roles=[
            1
        ],
        start_time=1,
        end_time=1,
        export_data=False,
        search_parameter="search_parameter_example",
        _async=False,
        mode=XiqNgMode("SNAPSHOT"),
        download_type="CSV",
        limit=1,
        page=1,
        time_offset=1,
        os_types=[
            "os_types_example"
        ],
        is_ssid_selected=True,
        is_band_selected=True,
    )
    try:
        api_response = api_instance.qoe_diagnostics_xlsx_data(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling NGREPORTSApi->qoe_diagnostics_xlsx_data: %s\n" % e)
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
[**XiqXlsxNgReportsDataFilters**](../../models/XiqXlsxNgReportsDataFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#qoe_diagnostics_xlsx_data.ApiResponseFor200) | OK

#### qoe_diagnostics_xlsx_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NgMetricsReport**](../../models/NgMetricsReport.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

