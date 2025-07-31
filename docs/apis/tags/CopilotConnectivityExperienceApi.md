<a id="__pageTop"></a>
# extremecloudiq.apis.tags.copilot_connectivity_experience_api.CopilotConnectivityExperienceApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connectivity_details_by_client_type**](#get_connectivity_details_by_client_type) | **get** /copilot/connectivity/client-type | 
[**get_connectivity_details_by_locations**](#get_connectivity_details_by_locations) | **get** /copilot/connectivity/locations | 
[**get_wired_connectivity_experience**](#get_wired_connectivity_experience) | **get** /copilot/connectivity/wired/experience | 
[**get_wired_events**](#get_wired_events) | **get** /copilot/connectivity/wired/events | 
[**get_wired_hardware**](#get_wired_hardware) | **get** /copilot/connectivity/wired/hardware | 
[**get_wired_hardware_by_location**](#get_wired_hardware_by_location) | **get** /copilot/connectivity/wired/locations/hardware | 
[**get_wired_quality_index**](#get_wired_quality_index) | **get** /copilot/connectivity/wired/quality-index | 
[**get_wireless_apps**](#get_wireless_apps) | **get** /copilot/connectivity/wireless/apps | 
[**get_wireless_connectivity_experience**](#get_wireless_connectivity_experience) | **get** /copilot/connectivity/wireless/experience | 
[**get_wireless_events**](#get_wireless_events) | **get** /copilot/connectivity/wireless/events | 
[**get_wireless_events_by_location**](#get_wireless_events_by_location) | **get** /copilot/connectivity/wireless/locations/events | 
[**get_wireless_performance**](#get_wireless_performance) | **get** /copilot/connectivity/wireless/performance | 
[**get_wireless_performance_by_location**](#get_wireless_performance_by_location) | **get** /copilot/connectivity/wireless/locations/performance | 
[**get_wireless_quality_index**](#get_wireless_quality_index) | **get** /copilot/connectivity/wireless/quality-index | 
[**get_wireless_quality_index_by_location**](#get_wireless_quality_index_by_location) | **get** /copilot/connectivity/wireless/locations/quality-index | 
[**get_wireless_time_to_connect**](#get_wireless_time_to_connect) | **get** /copilot/connectivity/wireless/time-to-connect | 
[**get_wireless_time_to_connect_by_location**](#get_wireless_time_to_connect_by_location) | **get** /copilot/connectivity/wireless/locations/time-to-connect | 
[**get_wireless_views**](#get_wireless_views) | **get** /copilot/connectivity/wireless/views | 

# **get_connectivity_details_by_client_type**
<a id="get_connectivity_details_by_client_type"></a>
> XiqConnectivityDetailsByClientTypeResponse get_connectivity_details_by_client_type(start_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_client_type import XiqClientType
from extremecloudiq.model.xiq_connectivity_details_by_client_type_response import XiqConnectivityDetailsByClientTypeResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_connectivity_details_by_client_type(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_client_type: %s\n" % e)

    # example passing only optional values
    query_params = {
        'startTime': 1,
        'endTime': 1,
        'locationId': 0,
        'clientType': XiqClientType("WIRELESS"),
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_connectivity_details_by_client_type(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_client_type: %s\n" % e)
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
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
locationId | LocationIdSchema | | optional
clientType | ClientTypeSchema | | optional
forensicBucket | ForensicBucketSchema | | optional


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

# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 64 bit integer

# ClientTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientType**](../../models/XiqClientType.md) |  | 


# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_connectivity_details_by_client_type.ApiResponseFor200) | OK

#### get_connectivity_details_by_client_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityDetailsByClientTypeResponse**](../../models/XiqConnectivityDetailsByClientTypeResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_connectivity_details_by_locations**
<a id="get_connectivity_details_by_locations"></a>
> PagedXiqConnectivityExperienceData get_connectivity_details_by_locations(start_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_sort_field import XiqSortField
from extremecloudiq.model.xiq_quality_index import XiqQualityIndex
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.paged_xiq_connectivity_experience_data import PagedXiqConnectivityExperienceData
from extremecloudiq.model.xiq_client_type import XiqClientType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_connectivity_details_by_locations(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_locations: %s\n" % e)

    # example passing only optional values
    query_params = {
        'startTime': 1,
        'endTime': 1,
        'page': 1,
        'limit': 10,
        'sortField': XiqSortField("NAME"),
        'sortOrder': XiqSortOrder("ASC"),
        'locationId': 0,
        'searchKey': "",
        'clientType': XiqClientType("WIRELESS"),
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'qualityIndex': XiqQualityIndex("LOW"),
    }
    try:
        api_response = api_instance.get_connectivity_details_by_locations(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_connectivity_details_by_locations: %s\n" % e)
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
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
locationId | LocationIdSchema | | optional
searchKey | SearchKeySchema | | optional
clientType | ClientTypeSchema | | optional
forensicBucket | ForensicBucketSchema | | optional
qualityIndex | QualityIndexSchema | | optional


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

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortField**](../../models/XiqSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 64 bit integer

# SearchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ClientTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqClientType**](../../models/XiqClientType.md) |  | 


# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# QualityIndexSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqQualityIndex**](../../models/XiqQualityIndex.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_connectivity_details_by_locations.ApiResponseFor200) | OK

#### get_connectivity_details_by_locations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqConnectivityExperienceData**](../../models/PagedXiqConnectivityExperienceData.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_connectivity_experience**
<a id="get_wired_connectivity_experience"></a>
> PagedXiqConnectivityExperienceData get_wired_connectivity_experience(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_sort_field import XiqSortField
from extremecloudiq.model.paged_xiq_connectivity_experience_data import PagedXiqConnectivityExperienceData
from extremecloudiq.model.xiq_wired_view_type import XiqWiredViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wired_connectivity_experience(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_connectivity_experience: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'page': 1,
        'limit': 10,
        'sortField': XiqSortField("NAME"),
        'sortOrder': XiqSortOrder("ASC"),
    }
    try:
        api_response = api_instance.get_wired_connectivity_experience(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_connectivity_experience: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredViewType**](../../models/XiqWiredViewType.md) |  | 


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

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortField**](../../models/XiqSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_connectivity_experience.ApiResponseFor200) | OK

#### get_wired_connectivity_experience.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqConnectivityExperienceData**](../../models/PagedXiqConnectivityExperienceData.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_events**
<a id="get_wired_events"></a>
> PagedXiqWiredEventEntity get_wired_events(view_typestart_timeend_timeforensic_bucketscore_type)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_copilot_wired_events_score_type import XiqCopilotWiredEventsScoreType
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_copilot_events_wired_sort_field import XiqCopilotEventsWiredSortField
from extremecloudiq.model.paged_xiq_wired_event_entity import PagedXiqWiredEventEntity
from extremecloudiq.model.xiq_wired_view_type import XiqWiredViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'scoreType': XiqCopilotWiredEventsScoreType("PORT_ERRORS"),
    }
    try:
        api_response = api_instance.get_wired_events(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_events: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'page': 1,
        'limit': 10,
        'sortBy': XiqCopilotEventsWiredSortField("INTERFACE_ERRORS"),
        'sortOrder': XiqSortOrder("ASC"),
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'scoreType': XiqCopilotWiredEventsScoreType("PORT_ERRORS"),
        'searchKey': "",
        'locationType': "",
        'locationId': "0",
        'timestamp': 1,
    }
    try:
        api_response = api_instance.get_wired_events(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_events: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
sortBy | SortBySchema | | optional
sortOrder | SortOrderSchema | | optional
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | 
scoreType | ScoreTypeSchema | | 
searchKey | SearchKeySchema | | optional
locationType | LocationTypeSchema | | optional
locationId | LocationIdSchema | | optional
timestamp | TimestampSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredViewType**](../../models/XiqWiredViewType.md) |  | 


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

# SortBySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotEventsWiredSortField**](../../models/XiqCopilotEventsWiredSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# ScoreTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotWiredEventsScoreType**](../../models/XiqCopilotWiredEventsScoreType.md) |  | 


# SearchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# TimestampSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_events.ApiResponseFor200) | OK

#### get_wired_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqWiredEventEntity**](../../models/PagedXiqWiredEventEntity.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_hardware**
<a id="get_wired_hardware"></a>
> XiqWiredHardwareResponse get_wired_hardware(view_typestart_timeend_timeforensic_bucket)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_wired_view_type import XiqWiredViewType
from extremecloudiq.model.xiq_wired_hardware_response import XiqWiredHardwareResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wired_hardware(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wired_hardware(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | 


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredViewType**](../../models/XiqWiredViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_hardware.ApiResponseFor200) | OK

#### get_wired_hardware.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredHardwareResponse**](../../models/XiqWiredHardwareResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_hardware_by_location**
<a id="get_wired_hardware_by_location"></a>
> XiqWiredHardwareByLocationResponse get_wired_hardware_by_location(start_timeend_timeforensic_bucket)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wired_hardware_by_location_response import XiqWiredHardwareByLocationResponse
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_wired_view_type import XiqWiredViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wired_hardware_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware_by_location: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wired_hardware_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_hardware_by_location: %s\n" % e)
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
viewType | ViewTypeSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | 


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredViewType**](../../models/XiqWiredViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_hardware_by_location.ApiResponseFor200) | OK

#### get_wired_hardware_by_location.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredHardwareByLocationResponse**](../../models/XiqWiredHardwareByLocationResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wired_quality_index**
<a id="get_wired_quality_index"></a>
> XiqWiredQualityIndexResponse get_wired_quality_index(start_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wired_quality_index_response import XiqWiredQualityIndexResponse
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_wired_view_type import XiqWiredViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wired_quality_index(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_quality_index: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqWiredViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wired_quality_index(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wired_quality_index: %s\n" % e)
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
viewType | ViewTypeSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredViewType**](../../models/XiqWiredViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wired_quality_index.ApiResponseFor200) | OK

#### get_wired_quality_index.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWiredQualityIndexResponse**](../../models/XiqWiredQualityIndexResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_apps**
<a id="get_wireless_apps"></a>
> XiqWirelessAppsResponse get_wireless_apps(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wireless_apps_response import XiqWirelessAppsResponse
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_apps(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_apps: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'locationId': "0",
        'locationType': "",
    }
    try:
        api_response = api_instance.get_wireless_apps(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_apps: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | optional
locationId | LocationIdSchema | | optional
locationType | LocationTypeSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_apps.ApiResponseFor200) | OK

#### get_wireless_apps.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessAppsResponse**](../../models/XiqWirelessAppsResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_connectivity_experience**
<a id="get_wireless_connectivity_experience"></a>
> PagedXiqConnectivityExperienceData get_wireless_connectivity_experience(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_sort_field import XiqSortField
from extremecloudiq.model.paged_xiq_connectivity_experience_data import PagedXiqConnectivityExperienceData
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_connectivity_experience(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_connectivity_experience: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'page': 1,
        'limit': 10,
        'startTime': 1,
        'endTime': 1,
        'sortField': XiqSortField("NAME"),
        'sortOrder': XiqSortOrder("ASC"),
    }
    try:
        api_response = api_instance.get_wireless_connectivity_experience(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_connectivity_experience: %s\n" % e)
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
viewType | ViewTypeSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortField**](../../models/XiqSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_connectivity_experience.ApiResponseFor200) | OK

#### get_wireless_connectivity_experience.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqConnectivityExperienceData**](../../models/PagedXiqConnectivityExperienceData.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_events**
<a id="get_wireless_events"></a>
> PagedXiqCopilotWirelessEvent get_wireless_events(view_typestart_timeend_timescore_type)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_copilot_events_wireless_sort_field import XiqCopilotEventsWirelessSortField
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_copilot_wireless_events_score_type import XiqCopilotWirelessEventsScoreType
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
from extremecloudiq.model.paged_xiq_copilot_wireless_event import PagedXiqCopilotWirelessEvent
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'scoreType': XiqCopilotWirelessEventsScoreType("TIME_TO_AUTHENTICATE"),
    }
    try:
        api_response = api_instance.get_wireless_events(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'page': 1,
        'limit': 10,
        'startTime': 1,
        'endTime': 1,
        'sortField': XiqCopilotEventsWirelessSortField("AVERAGE_VALUE"),
        'sortOrder': XiqSortOrder("ASC"),
        'viewId': "",
        'scoreType': XiqCopilotWirelessEventsScoreType("TIME_TO_AUTHENTICATE"),
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'searchKey': "",
        'locationId': "0",
        'locationType': "locationType_example",
        'timestamp': 1,
    }
    try:
        api_response = api_instance.get_wireless_events(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events: %s\n" % e)
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
viewType | ViewTypeSchema | | 
page | PageSchema | | optional
limit | LimitSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
viewId | ViewIdSchema | | optional
scoreType | ScoreTypeSchema | | 
forensicBucket | ForensicBucketSchema | | optional
searchKey | SearchKeySchema | | optional
locationId | LocationIdSchema | | optional
locationType | LocationTypeSchema | | optional
timestamp | TimestampSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotEventsWirelessSortField**](../../models/XiqCopilotEventsWirelessSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ScoreTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotWirelessEventsScoreType**](../../models/XiqCopilotWirelessEventsScoreType.md) |  | 


# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# SearchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimestampSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_events.ApiResponseFor200) | OK

#### get_wireless_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqCopilotWirelessEvent**](../../models/PagedXiqCopilotWirelessEvent.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_events_by_location**
<a id="get_wireless_events_by_location"></a>
> PagedXiqCopilotWirelessEvent get_wireless_events_by_location(start_timeend_timescore_typelocation_id)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_copilot_events_wireless_sort_field import XiqCopilotEventsWirelessSortField
from extremecloudiq.model.xiq_sort_order import XiqSortOrder
from extremecloudiq.model.xiq_copilot_wireless_events_score_type import XiqCopilotWirelessEventsScoreType
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.paged_xiq_copilot_wireless_event import PagedXiqCopilotWirelessEvent
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'startTime': 1,
        'endTime': 1,
        'scoreType': XiqCopilotWirelessEventsScoreType("TIME_TO_AUTHENTICATE"),
        'locationId': "locationId_example",
    }
    try:
        api_response = api_instance.get_wireless_events_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events_by_location: %s\n" % e)

    # example passing only optional values
    query_params = {
        'page': 1,
        'limit': 10,
        'startTime': 1,
        'endTime': 1,
        'sortField': XiqCopilotEventsWirelessSortField("AVERAGE_VALUE"),
        'sortOrder': XiqSortOrder("ASC"),
        'scoreType': XiqCopilotWirelessEventsScoreType("TIME_TO_AUTHENTICATE"),
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'searchKey': "",
        'locationId': "locationId_example",
        'timestamp': 1,
        'ssid': "",
        'osType': "",
    }
    try:
        api_response = api_instance.get_wireless_events_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_events_by_location: %s\n" % e)
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
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
sortField | SortFieldSchema | | optional
sortOrder | SortOrderSchema | | optional
scoreType | ScoreTypeSchema | | 
forensicBucket | ForensicBucketSchema | | optional
searchKey | SearchKeySchema | | optional
locationId | LocationIdSchema | | 
timestamp | TimestampSchema | | optional
ssid | SsidSchema | | optional
osType | OsTypeSchema | | optional


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

# SortFieldSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotEventsWirelessSortField**](../../models/XiqCopilotEventsWirelessSortField.md) |  | 


# SortOrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqSortOrder**](../../models/XiqSortOrder.md) |  | 


# ScoreTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqCopilotWirelessEventsScoreType**](../../models/XiqCopilotWirelessEventsScoreType.md) |  | 


# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# SearchKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimestampSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# SsidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# OsTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_events_by_location.ApiResponseFor200) | OK

#### get_wireless_events_by_location.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedXiqCopilotWirelessEvent**](../../models/PagedXiqCopilotWirelessEvent.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_performance**
<a id="get_wireless_performance"></a>
> XiqWirelessConnectivityPerformanceResponse get_wireless_performance(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
from extremecloudiq.model.xiq_wireless_connectivity_performance_response import XiqWirelessConnectivityPerformanceResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_performance(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'locationId': "0",
        'locationType': "",
    }
    try:
        api_response = api_instance.get_wireless_performance(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | optional
locationId | LocationIdSchema | | optional
locationType | LocationTypeSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_performance.ApiResponseFor200) | OK

#### get_wireless_performance.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessConnectivityPerformanceResponse**](../../models/XiqWirelessConnectivityPerformanceResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_performance_by_location**
<a id="get_wireless_performance_by_location"></a>
> XiqWirelessConnectivityPerformanceResponse get_wireless_performance_by_location(building_idstart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_wireless_connectivity_performance_response import XiqWirelessConnectivityPerformanceResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'buildingId': "buildingId_example",
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_performance_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance_by_location: %s\n" % e)

    # example passing only optional values
    query_params = {
        'buildingId': "buildingId_example",
        'ssid': "",
        'osType': "",
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wireless_performance_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_performance_by_location: %s\n" % e)
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
buildingId | BuildingIdSchema | | 
ssid | SsidSchema | | optional
osType | OsTypeSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
forensicBucket | ForensicBucketSchema | | optional


# BuildingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SsidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# OsTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

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

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_performance_by_location.ApiResponseFor200) | OK

#### get_wireless_performance_by_location.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessConnectivityPerformanceResponse**](../../models/XiqWirelessConnectivityPerformanceResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_quality_index**
<a id="get_wireless_quality_index"></a>
> XiqWirelessQualityIndexResponse get_wireless_quality_index(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
from extremecloudiq.model.xiq_wireless_quality_index_response import XiqWirelessQualityIndexResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_quality_index(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'locationId': "0",
        'locationType': "locationType_example",
    }
    try:
        api_response = api_instance.get_wireless_quality_index(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | optional
locationId | LocationIdSchema | | optional
locationType | LocationTypeSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_quality_index.ApiResponseFor200) | OK

#### get_wireless_quality_index.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessQualityIndexResponse**](../../models/XiqWirelessQualityIndexResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_quality_index_by_location**
<a id="get_wireless_quality_index_by_location"></a>
> XiqWirelessQualityIndexByLocationResponse get_wireless_quality_index_by_location(building_idstart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_wireless_quality_index_by_location_response import XiqWirelessQualityIndexByLocationResponse
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'buildingId': "buildingId_example",
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_quality_index_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index_by_location: %s\n" % e)

    # example passing only optional values
    query_params = {
        'buildingId': "buildingId_example",
        'ssid': "",
        'osType': "",
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wireless_quality_index_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_quality_index_by_location: %s\n" % e)
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
buildingId | BuildingIdSchema | | 
ssid | SsidSchema | | optional
osType | OsTypeSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
forensicBucket | ForensicBucketSchema | | optional


# BuildingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SsidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# OsTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

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

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_quality_index_by_location.ApiResponseFor200) | OK

#### get_wireless_quality_index_by_location.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessQualityIndexByLocationResponse**](../../models/XiqWirelessQualityIndexByLocationResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_time_to_connect**
<a id="get_wireless_time_to_connect"></a>
> XiqWirelessTimeToConnectResponse get_wireless_time_to_connect(view_typestart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wireless_time_to_connect_response import XiqWirelessTimeToConnectResponse
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
from extremecloudiq.model.xiq_connectivity_experience_view_type import XiqConnectivityExperienceViewType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_time_to_connect(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect: %s\n" % e)

    # example passing only optional values
    query_params = {
        'viewType': XiqConnectivityExperienceViewType("LOCATION"),
        'startTime': 1,
        'endTime': 1,
        'viewId': "",
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
        'locationId': "0",
        'locationType': "locationType_example",
    }
    try:
        api_response = api_instance.get_wireless_time_to_connect(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect: %s\n" % e)
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
viewType | ViewTypeSchema | | 
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
viewId | ViewIdSchema | | optional
forensicBucket | ForensicBucketSchema | | optional
locationId | LocationIdSchema | | optional
locationType | LocationTypeSchema | | optional


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqConnectivityExperienceViewType**](../../models/XiqConnectivityExperienceViewType.md) |  | 


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

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


# LocationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "0"

# LocationTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_time_to_connect.ApiResponseFor200) | OK

#### get_wireless_time_to_connect.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessTimeToConnectResponse**](../../models/XiqWirelessTimeToConnectResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_time_to_connect_by_location**
<a id="get_wireless_time_to_connect_by_location"></a>
> XiqWirelessTimeToConnectResponse get_wireless_time_to_connect_by_location(building_idstart_timeend_time)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wireless_time_to_connect_response import XiqWirelessTimeToConnectResponse
from extremecloudiq.model.xiq_forensic_bucket import XiqForensicBucket
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'buildingId': "buildingId_example",
        'startTime': 1,
        'endTime': 1,
    }
    try:
        api_response = api_instance.get_wireless_time_to_connect_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect_by_location: %s\n" % e)

    # example passing only optional values
    query_params = {
        'buildingId': "buildingId_example",
        'ssid': "",
        'osType': "",
        'startTime': 1,
        'endTime': 1,
        'forensicBucket': XiqForensicBucket("TWENTY_FOUR_HOURS"),
    }
    try:
        api_response = api_instance.get_wireless_time_to_connect_by_location(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_time_to_connect_by_location: %s\n" % e)
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
buildingId | BuildingIdSchema | | 
ssid | SsidSchema | | optional
osType | OsTypeSchema | | optional
startTime | StartTimeSchema | | 
endTime | EndTimeSchema | | 
forensicBucket | ForensicBucketSchema | | optional


# BuildingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SsidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# OsTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

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

# ForensicBucketSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqForensicBucket**](../../models/XiqForensicBucket.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_time_to_connect_by_location.ApiResponseFor200) | OK

#### get_wireless_time_to_connect_by_location.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessTimeToConnectResponse**](../../models/XiqWirelessTimeToConnectResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_wireless_views**
<a id="get_wireless_views"></a>
> XiqWirelessViewsTypeResponse get_wireless_views(view_type)



### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import copilot_connectivity_experience_api
from extremecloudiq.model.xiq_wireless_views_type_response import XiqWirelessViewsTypeResponse
from extremecloudiq.model.xiq_wireless_views_list_type import XiqWirelessViewsListType
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
    api_instance = copilot_connectivity_experience_api.CopilotConnectivityExperienceApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'viewType': XiqWirelessViewsListType("SSID"),
    }
    try:
        api_response = api_instance.get_wireless_views(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling CopilotConnectivityExperienceApi->get_wireless_views: %s\n" % e)
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
viewType | ViewTypeSchema | | 


# ViewTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessViewsListType**](../../models/XiqWirelessViewsListType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_wireless_views.ApiResponseFor200) | OK

#### get_wireless_views.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XiqWirelessViewsTypeResponse**](../../models/XiqWirelessViewsTypeResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

