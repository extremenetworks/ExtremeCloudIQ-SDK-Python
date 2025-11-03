<a id="__pageTop"></a>
# extremecloudiq.apis.tags.use_folder_preferences_api.UseFolderPreferencesApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_user_folder_preferences**](#query_user_folder_preferences) | **get** /user-folder-preferences | Query user folder preferences
[**save_user_folder_preferences**](#save_user_folder_preferences) | **post** /user-folder-preferences/{folderId} | Save user folder preferences values.

# **query_user_folder_preferences**
<a id="query_user_folder_preferences"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} query_user_folder_preferences(folder_idtype)

Query user folder preferences

Returns matched preferences.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import use_folder_preferences_api
from extremecloudiq.model.xiq_rssi_thresholds import XiqRssiThresholds
from extremecloudiq.model.xiq_snr_thresholds import XiqSnrThresholds
from extremecloudiq.model.xiq_co_channel_interference_thresholds import XiqCoChannelInterferenceThresholds
from extremecloudiq.model.xiq_coverage_overlap_thresholds import XiqCoverageOverlapThresholds
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
    api_instance = use_folder_preferences_api.UseFolderPreferencesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'folderId': 0,
        'type': [
        "type_example"
    ],
    }
    try:
        # Query user folder preferences
        api_response = api_instance.query_user_folder_preferences(
            query_params=query_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UseFolderPreferencesApi->query_user_folder_preferences: %s\n" % e)
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
folderId | FolderIdSchema | | 
type | TypeSchema | | 


# FolderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_user_folder_preferences.ApiResponseFor200) | OK

#### query_user_folder_preferences.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[XiqCoChannelInterferenceThresholds]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) |  | 
[XiqCoverageOverlapThresholds]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) |  | 
[XiqRssiThresholds]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) |  | 
[XiqSnrThresholds]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_user_folder_preferences**
<a id="save_user_folder_preferences"></a>
> bool, date, datetime, dict, float, int, list, str, none_type save_user_folder_preferences(folder_idany_type)

Save user folder preferences values.

Persists given preferences values.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import use_folder_preferences_api
from extremecloudiq.model.xiq_rssi_thresholds import XiqRssiThresholds
from extremecloudiq.model.xiq_snr_thresholds import XiqSnrThresholds
from extremecloudiq.model.xiq_co_channel_interference_thresholds import XiqCoChannelInterferenceThresholds
from extremecloudiq.model.xiq_coverage_overlap_thresholds import XiqCoverageOverlapThresholds
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
    api_instance = use_folder_preferences_api.UseFolderPreferencesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderId': 1248163264,
    }
    body = 
    try:
        # Save user folder preferences values.
        api_response = api_instance.save_user_folder_preferences(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling UseFolderPreferencesApi->save_user_folder_preferences: %s\n" % e)
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

The preferences object to save.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The preferences object to save. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[XiqCoChannelInterferenceThresholds]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) |  | 
[XiqCoverageOverlapThresholds]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) |  | 
[XiqRssiThresholds]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) |  | 
[XiqSnrThresholds]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
folderId | FolderIdSchema | | 

# FolderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#save_user_folder_preferences.ApiResponseFor200) | OK

#### save_user_folder_preferences.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[XiqCoChannelInterferenceThresholds]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) | [**XiqCoChannelInterferenceThresholds**]({{complexTypePrefix}}XiqCoChannelInterferenceThresholds.md) |  | 
[XiqCoverageOverlapThresholds]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) | [**XiqCoverageOverlapThresholds**]({{complexTypePrefix}}XiqCoverageOverlapThresholds.md) |  | 
[XiqRssiThresholds]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) | [**XiqRssiThresholds**]({{complexTypePrefix}}XiqRssiThresholds.md) |  | 
[XiqSnrThresholds]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) | [**XiqSnrThresholds**]({{complexTypePrefix}}XiqSnrThresholds.md) |  | 

### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

