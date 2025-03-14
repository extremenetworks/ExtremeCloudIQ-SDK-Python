<a id="__pageTop"></a>
# extremecloudiq.apis.tags.afc_endpoint_api.AfcEndpointApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site_afc_schedule**](#create_site_afc_schedule) | **post** /site/afc/schedule | 
[**get_afc_server**](#get_afc_server) | **get** /afcserver/{server_id} | Get Afc Server data
[**get_afc_server_statistics**](#get_afc_server_statistics) | **get** /afcserver/statistics/{server_id} | Get AFC server Statistics
[**get_afc_spectrum_per_ap**](#get_afc_spectrum_per_ap) | **post** /ap/spectrum/ | 
[**get_afc_spectrum_per_site**](#get_afc_spectrum_per_site) | **post** /site/spectrum/ | 
[**get_aps_afc_diagnostics**](#get_aps_afc_diagnostics) | **get** /ap/afc/diagnostics/{id} | 
[**get_aps_afc_info**](#get_aps_afc_info) | **get** /ap/afc/interface/details/{sn} | Get Afc Summary Data
[**get_aps_afc_summary_info**](#get_aps_afc_summary_info) | **get** /aps/afc/query/ | 
[**get_site_afc_schedule**](#get_site_afc_schedule) | **get** /site/afc/schedule | 
[**list_afc_servers**](#list_afc_servers) | **get** /afcserver | Get Afc Server list and their status
[**post_aps_manual_afc_spectrum**](#post_aps_manual_afc_spectrum) | **post** /aps/afc/update | Manual Spectrum request for device(s)
[**update_site_afc_schedule**](#update_site_afc_schedule) | **put** /site/afc/schedule | 

# **create_site_afc_schedule**
<a id="create_site_afc_schedule"></a>
> create_site_afc_schedule(xiq_site_afc_schedule)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_site_afc_schedule import XiqSiteAfcSchedule
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqSiteAfcSchedule(
        owner_id=1,
        folder_id=1,
        site_time_zone="site_time_zone_example",
        site_schedule=1,
    )
    try:
        api_response = api_instance.create_site_afc_schedule(
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->create_site_afc_schedule: %s\n" % e)
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
[**XiqSiteAfcSchedule**](../../models/XiqSiteAfcSchedule.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#create_site_afc_schedule.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#create_site_afc_schedule.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#create_site_afc_schedule.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#create_site_afc_schedule.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#create_site_afc_schedule.ApiResponseFor200) | OK

#### create_site_afc_schedule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### create_site_afc_schedule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### create_site_afc_schedule.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### create_site_afc_schedule.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### create_site_afc_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_afc_server**
<a id="get_afc_server"></a>
> XiqAfcServer get_afc_server(server_id)

Get Afc Server data

Get Afc Server data

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_afc_server import XiqAfcServer
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'server_id': 1234567890,
    }
    try:
        # Get Afc Server data
        api_response = api_instance.get_afc_server(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_server: %s\n" % e)
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
server_id | ServerIdSchema | | 

# ServerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_afc_server.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_afc_server.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_afc_server.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_afc_server.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_afc_server.ApiResponseFor200) | OK

#### get_afc_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAfcServer**](../../models/XiqAfcServer.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_afc_server_statistics**
<a id="get_afc_server_statistics"></a>
> XiqAfcServersStatistics get_afc_server_statistics(server_idstart_timeend_time)

Get AFC server Statistics

Get AFC server Statistics

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_afc_servers_statistics import XiqAfcServersStatistics
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'server_id': 1234567890,
    }
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        # Get AFC server Statistics
        api_response = api_instance.get_afc_server_statistics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_server_statistics: %s\n" % e)

    # example passing only optional values
    path_params = {
        'server_id': 1234567890,
    }
    query_params = {
        'startTime': 1,
        'endTime': 1,
        'precision': 1,
    }
    try:
        # Get AFC server Statistics
        api_response = api_instance.get_afc_server_statistics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_server_statistics: %s\n" % e)
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
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
precision | PrecisionSchema | | optional


# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PrecisionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
server_id | ServerIdSchema | | 

# ServerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_afc_server_statistics.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_afc_server_statistics.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_afc_server_statistics.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_afc_server_statistics.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_afc_server_statistics.ApiResponseFor200) | OK

#### get_afc_server_statistics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server_statistics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server_statistics.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server_statistics.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_server_statistics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAfcServersStatistics**](../../models/XiqAfcServersStatistics.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_afc_spectrum_per_ap**
<a id="get_afc_spectrum_per_ap"></a>
> [XiqAfcAvailableSpectrum] get_afc_spectrum_per_ap(is_empty_listxiq_get_afc_spectrum_for_ap_request)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_afc_available_spectrum import XiqAfcAvailableSpectrum
from extremecloudiq.model.xiq_get_afc_spectrum_for_ap_request import XiqGetAfcSpectrumForApRequest
from extremecloudiq.model.xiq_error import XiqError
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'IsEmptyList': True,
    }
    body = XiqGetAfcSpectrumForApRequest(
        owner_id=1,
        site_name="site_name_example",
        region="US",
        input_info=[
            XiqAfcInputInfo(
                serial_number="serial_number_example",
                coordinates=XiqApCoordinates(
                    latitude=3.14,
                    longitude=3.14,
                    timestamp=1,
                ),
                elevation=XiqElevation(
                    height=3.14,
                    height_reference="AGL",
                    uncertainty=1,
                ),
                ellipse=XiqEllipse(
                    major_axis=3.14,
                    minor_axis=3.14,
                    orientation=3.14,
                ),
                environment="INDOOR",
            )
        ],
    )
    try:
        api_response = api_instance.get_afc_spectrum_per_ap(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_spectrum_per_ap: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqGetAfcSpectrumForApRequest**](../../models/XiqGetAfcSpectrumForApRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
IsEmptyList | IsEmptyListSchema | | 


# IsEmptyListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_afc_spectrum_per_ap.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_afc_spectrum_per_ap.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_afc_spectrum_per_ap.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_afc_spectrum_per_ap.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_afc_spectrum_per_ap.ApiResponseFor200) | OK

#### get_afc_spectrum_per_ap.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_ap.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_ap.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_ap.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_ap.ApiResponseFor200
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
[**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) | [**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) | [**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_afc_spectrum_per_site**
<a id="get_afc_spectrum_per_site"></a>
> [XiqAfcAvailableSpectrum] get_afc_spectrum_per_site(is_empty_listxiq_get_afc_spectrum_for_site_aps_request)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_afc_available_spectrum import XiqAfcAvailableSpectrum
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_get_afc_spectrum_for_site_aps_request import XiqGetAfcSpectrumForSiteApsRequest
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'IsEmptyList': True,
    }
    body = XiqGetAfcSpectrumForSiteApsRequest(
        owner_id=1,
        site_name="site_name_example",
        region="US",
        input_info=[
            XiqAfcInputInfo(
                serial_number="serial_number_example",
                coordinates=XiqApCoordinates(
                    latitude=3.14,
                    longitude=3.14,
                    timestamp=1,
                ),
                elevation=XiqElevation(
                    height=3.14,
                    height_reference="AGL",
                    uncertainty=1,
                ),
                ellipse=XiqEllipse(
                    major_axis=3.14,
                    minor_axis=3.14,
                    orientation=3.14,
                ),
                environment="INDOOR",
            )
        ],
    )
    try:
        api_response = api_instance.get_afc_spectrum_per_site(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_afc_spectrum_per_site: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqGetAfcSpectrumForSiteApsRequest**](../../models/XiqGetAfcSpectrumForSiteApsRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
IsEmptyList | IsEmptyListSchema | | 


# IsEmptyListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_afc_spectrum_per_site.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_afc_spectrum_per_site.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_afc_spectrum_per_site.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_afc_spectrum_per_site.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_afc_spectrum_per_site.ApiResponseFor200) | OK

#### get_afc_spectrum_per_site.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_site.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_site.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_site.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_afc_spectrum_per_site.ApiResponseFor200
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
[**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) | [**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) | [**XiqAfcAvailableSpectrum**]({{complexTypePrefix}}XiqAfcAvailableSpectrum.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_aps_afc_diagnostics**
<a id="get_aps_afc_diagnostics"></a>
> XiqAfcApDiagnostics get_aps_afc_diagnostics(owner_idid)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_afc_ap_diagnostics import XiqAfcApDiagnostics
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': AP-1234567890,
    }
    query_params = {
        'ownerId': 1,
    }
    try:
        api_response = api_instance.get_aps_afc_diagnostics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_aps_afc_diagnostics: %s\n" % e)
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
ownerId | OwnerIdSchema | | 


# OwnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_aps_afc_diagnostics.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_aps_afc_diagnostics.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_aps_afc_diagnostics.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_aps_afc_diagnostics.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_aps_afc_diagnostics.ApiResponseFor200) | OK

#### get_aps_afc_diagnostics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_diagnostics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_diagnostics.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_diagnostics.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_diagnostics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAfcApDiagnostics**](../../models/XiqAfcApDiagnostics.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_aps_afc_info**
<a id="get_aps_afc_info"></a>
> XiqAfcApDetail get_aps_afc_info(sn)

Get Afc Summary Data

Get Afc data per site 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_afc_ap_detail import XiqAfcApDetail
from extremecloudiq.model.xiq_error import XiqError
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'sn': "AP-1234567890",
    }
    try:
        # Get Afc Summary Data
        api_response = api_instance.get_aps_afc_info(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_aps_afc_info: %s\n" % e)
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
sn | SnSchema | | 

# SnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_aps_afc_info.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_aps_afc_info.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_aps_afc_info.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_aps_afc_info.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_aps_afc_info.ApiResponseFor200) | OK

#### get_aps_afc_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_info.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_info.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_info.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAfcApDetail**](../../models/XiqAfcApDetail.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_aps_afc_summary_info**
<a id="get_aps_afc_summary_info"></a>
> XiqAfcApsInfoElement get_aps_afc_summary_info(owner_id)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_afc_aps_info_element import XiqAfcApsInfoElement
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ownerId': 1,
    }
    try:
        api_response = api_instance.get_aps_afc_summary_info(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_aps_afc_summary_info: %s\n" % e)
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
ownerId | OwnerIdSchema | | 


# OwnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_aps_afc_summary_info.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_aps_afc_summary_info.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_aps_afc_summary_info.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_aps_afc_summary_info.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_aps_afc_summary_info.ApiResponseFor200) | OK

#### get_aps_afc_summary_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_summary_info.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_summary_info.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_summary_info.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_aps_afc_summary_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqAfcApsInfoElement**](../../models/XiqAfcApsInfoElement.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_site_afc_schedule**
<a id="get_site_afc_schedule"></a>
> XiqSiteAfcSchedule get_site_afc_schedule(owner_idfolder_id)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_site_afc_schedule import XiqSiteAfcSchedule
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ownerId': 1,
        'folderId': 1,
    }
    try:
        api_response = api_instance.get_site_afc_schedule(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->get_site_afc_schedule: %s\n" % e)
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
ownerId | OwnerIdSchema | | 
folderId | FolderIdSchema | | 


# OwnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# FolderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#get_site_afc_schedule.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#get_site_afc_schedule.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#get_site_afc_schedule.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#get_site_afc_schedule.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#get_site_afc_schedule.ApiResponseFor200) | OK

#### get_site_afc_schedule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_site_afc_schedule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_site_afc_schedule.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_site_afc_schedule.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### get_site_afc_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSiteAfcSchedule**](../../models/XiqSiteAfcSchedule.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_afc_servers**
<a id="list_afc_servers"></a>
> XiqListAfcServers list_afc_servers(owner_id)

Get Afc Server list and their status

Get all Afc Servers data

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_list_afc_servers import XiqListAfcServers
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ownerId': 1,
    }
    try:
        # Get Afc Server list and their status
        api_response = api_instance.list_afc_servers(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->list_afc_servers: %s\n" % e)
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
ownerId | OwnerIdSchema | | 


# OwnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#list_afc_servers.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#list_afc_servers.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#list_afc_servers.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#list_afc_servers.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#list_afc_servers.ApiResponseFor200) | OK

#### list_afc_servers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_afc_servers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_afc_servers.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_afc_servers.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### list_afc_servers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqListAfcServers**](../../models/XiqListAfcServers.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_aps_manual_afc_spectrum**
<a id="post_aps_manual_afc_spectrum"></a>
> post_aps_manual_afc_spectrum(xiq_afc_ap_manual_spectrum)

Manual Spectrum request for device(s)

Manual Spectrum request for device(s).

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_afc_ap_manual_spectrum import XiqAfcApManualSpectrum
from extremecloudiq.model.xiq_error import XiqError
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqAfcApManualSpectrum(
        ids=[
            1
        ],
    )
    try:
        # Manual Spectrum request for device(s)
        api_response = api_instance.post_aps_manual_afc_spectrum(
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->post_aps_manual_afc_spectrum: %s\n" % e)
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
[**XiqAfcApManualSpectrum**](../../models/XiqAfcApManualSpectrum.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#post_aps_manual_afc_spectrum.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#post_aps_manual_afc_spectrum.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#post_aps_manual_afc_spectrum.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#post_aps_manual_afc_spectrum.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#post_aps_manual_afc_spectrum.ApiResponseFor200) | OK

#### post_aps_manual_afc_spectrum.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### post_aps_manual_afc_spectrum.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### post_aps_manual_afc_spectrum.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### post_aps_manual_afc_spectrum.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### post_aps_manual_afc_spectrum.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_site_afc_schedule**
<a id="update_site_afc_schedule"></a>
> update_site_afc_schedule(xiq_site_afc_schedule)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import afc_endpoint_api
from extremecloudiq.model.xiq_error import XiqError
from extremecloudiq.model.xiq_site_afc_schedule import XiqSiteAfcSchedule
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
    api_instance = afc_endpoint_api.AfcEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqSiteAfcSchedule(
        owner_id=1,
        folder_id=1,
        site_time_zone="site_time_zone_example",
        site_schedule=1,
    )
    try:
        api_response = api_instance.update_site_afc_schedule(
            body=body,
        )
    except extremecloudiq.ApiException as e:
        print("Exception when calling AfcEndpointApi->update_site_afc_schedule: %s\n" % e)
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
[**XiqSiteAfcSchedule**](../../models/XiqSiteAfcSchedule.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#update_site_afc_schedule.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#update_site_afc_schedule.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#update_site_afc_schedule.ApiResponseFor503) | Service Unavailable
500 | [ApiResponseFor500](#update_site_afc_schedule.ApiResponseFor500) | Internal Server Error
200 | [ApiResponseFor200](#update_site_afc_schedule.ApiResponseFor200) | OK

#### update_site_afc_schedule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### update_site_afc_schedule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### update_site_afc_schedule.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### update_site_afc_schedule.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqError**](../../models/XiqError.md) |  | 


#### update_site_afc_schedule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

