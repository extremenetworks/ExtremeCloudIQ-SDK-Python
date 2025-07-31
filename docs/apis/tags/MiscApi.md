<a id="__pageTop"></a>
# extremecloudiq.apis.tags.misc_api.MiscApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_list**](#get_country_list) | **get** /countries | Get country list
[**get_state_list_by_country_code**](#get_state_list_by_country_code) | **get** /countries/{countryAlpha2Code}/states | Get state list by country code
[**validate_country_code**](#validate_country_code) | **get** /countries/{countryCode}/:validate | Validate country code

# **get_country_list**
<a id="get_country_list"></a>
> [XiqCountry] get_country_list()

Get country list

Get list of countries and country codes.

### Example

```python
import extremecloudiq
from extremecloudiq.apis.tags import misc_api
from extremecloudiq.model.xiq_country import XiqCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = misc_api.MiscApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get country list
        api_response = api_instance.get_country_list()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling MiscApi->get_country_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_country_list.ApiResponseFor200) | OK

#### get_country_list.ApiResponseFor200
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
[**XiqCountry**]({{complexTypePrefix}}XiqCountry.md) | [**XiqCountry**]({{complexTypePrefix}}XiqCountry.md) | [**XiqCountry**]({{complexTypePrefix}}XiqCountry.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_state_list_by_country_code**
<a id="get_state_list_by_country_code"></a>
> [XiqCountryState] get_state_list_by_country_code(country_alpha2_code)

Get state list by country code

Get list of states or provinces in a country with country alpha2 code.

### Example

```python
import extremecloudiq
from extremecloudiq.apis.tags import misc_api
from extremecloudiq.model.xiq_country_state import XiqCountryState
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = misc_api.MiscApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'countryAlpha2Code': "countryAlpha2Code_example",
    }
    try:
        # Get state list by country code
        api_response = api_instance.get_state_list_by_country_code(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling MiscApi->get_state_list_by_country_code: %s\n" % e)
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
countryAlpha2Code | CountryAlpha2CodeSchema | | 

# CountryAlpha2CodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_state_list_by_country_code.ApiResponseFor200) | OK

#### get_state_list_by_country_code.ApiResponseFor200
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
[**XiqCountryState**]({{complexTypePrefix}}XiqCountryState.md) | [**XiqCountryState**]({{complexTypePrefix}}XiqCountryState.md) | [**XiqCountryState**]({{complexTypePrefix}}XiqCountryState.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_country_code**
<a id="validate_country_code"></a>
> bool validate_country_code(country_code)

Validate country code

Validate whether the country code is a valid code or not.

### Example

```python
import extremecloudiq
from extremecloudiq.apis.tags import misc_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = misc_api.MiscApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'countryCode': 1,
    }
    try:
        # Validate country code
        api_response = api_instance.validate_country_code(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling MiscApi->validate_country_code: %s\n" % e)
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
countryCode | CountryCodeSchema | | 

# CountryCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#validate_country_code.ApiResponseFor200) | OK

#### validate_country_code.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

