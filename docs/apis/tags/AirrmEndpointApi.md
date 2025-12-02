<a id="__pageTop"></a>
# extremecloudiq.apis.tags.airrm_endpoint_api.AirrmEndpointApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_ap_info**](#get_device_ap_info) | **get** /airrm/radio/apInfo/{radioMac} | Get Device AP Information
[**get_device_regulatory_config_afc_spectrum**](#get_device_regulatory_config_afc_spectrum) | **get** /airrm/device/{serialNumber} | Get Device Regulatory Config and AFC Spectrum
[**get_devices_radio_info**](#get_devices_radio_info) | **post** /airrm/ap/radioInfo/ | Get Devices Radio Information
[**get_site_device_regulatory_config_afc_spectrum**](#get_site_device_regulatory_config_afc_spectrum) | **get** /airrm/site/{airrmId} | Get Site Device Regulatory Config and AFC Spectrum

# **get_device_ap_info**
<a id="get_device_ap_info"></a>
> XIQAirrmGetDeviceApInfoResponse get_device_ap_info(radio_mac)

Get Device AP Information

Get device AP information by radio MAC address

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import airrm_endpoint_api
from extremecloudiq.model.xiq_airrm_get_device_ap_info_response import XIQAirrmGetDeviceApInfoResponse
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
    api_instance = airrm_endpoint_api.AirrmEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'radioMac': "00:11:22:33:44:55",
    }
    try:
        # Get Device AP Information
        api_response = api_instance.get_device_ap_info(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AirrmEndpointApi->get_device_ap_info: %s\n" % e)
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
radioMac | RadioMacSchema | | 

# RadioMacSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_ap_info.ApiResponseFor200) | OK

#### get_device_ap_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XIQAirrmGetDeviceApInfoResponse**](../../models/XIQAirrmGetDeviceApInfoResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_device_regulatory_config_afc_spectrum**
<a id="get_device_regulatory_config_afc_spectrum"></a>
> XIQAirrmGetDeviceRegulatoryConfigAfcSpectrumResponse get_device_regulatory_config_afc_spectrum(serial_number)

Get Device Regulatory Config and AFC Spectrum

Get AFC spectrum and regulatory configuration for a specific device

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import airrm_endpoint_api
from extremecloudiq.model.xiq_airrm_get_device_regulatory_config_afc_spectrum_response import XIQAirrmGetDeviceRegulatoryConfigAfcSpectrumResponse
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
    api_instance = airrm_endpoint_api.AirrmEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serialNumber': "AP123456789",
    }
    try:
        # Get Device Regulatory Config and AFC Spectrum
        api_response = api_instance.get_device_regulatory_config_afc_spectrum(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AirrmEndpointApi->get_device_regulatory_config_afc_spectrum: %s\n" % e)
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
serialNumber | SerialNumberSchema | | 

# SerialNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_device_regulatory_config_afc_spectrum.ApiResponseFor200) | OK

#### get_device_regulatory_config_afc_spectrum.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XIQAirrmGetDeviceRegulatoryConfigAfcSpectrumResponse**](../../models/XIQAirrmGetDeviceRegulatoryConfigAfcSpectrumResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_devices_radio_info**
<a id="get_devices_radio_info"></a>
> XIQAirrmGetDevicesRadioInfoResponse get_devices_radio_info(xiq_device_radio_info_request)

Get Devices Radio Information

Get radio information for devices by serial number or AIRRM ID

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import airrm_endpoint_api
from extremecloudiq.model.xiq_airrm_get_devices_radio_info_response import XIQAirrmGetDevicesRadioInfoResponse
from extremecloudiq.model.xiq_device_radio_info_request import XiqDeviceRadioInfoRequest
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
    api_instance = airrm_endpoint_api.AirrmEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    body = XiqDeviceRadioInfoRequest(
        serial_number="serial_number_example",
        airrm_id=1,
    )
    try:
        # Get Devices Radio Information
        api_response = api_instance.get_devices_radio_info(
            body=body,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AirrmEndpointApi->get_devices_radio_info: %s\n" % e)
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
[**XiqDeviceRadioInfoRequest**](../../models/XiqDeviceRadioInfoRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_devices_radio_info.ApiResponseFor200) | OK

#### get_devices_radio_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XIQAirrmGetDevicesRadioInfoResponse**](../../models/XIQAirrmGetDevicesRadioInfoResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_site_device_regulatory_config_afc_spectrum**
<a id="get_site_device_regulatory_config_afc_spectrum"></a>
> XIQAirrmGetSiteDeviceRegulatoryConfigAfcSpectrumResponse get_site_device_regulatory_config_afc_spectrum(airrm_id)

Get Site Device Regulatory Config and AFC Spectrum

Get AFC spectrum regulatory configuration for all devices in a site

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import extremecloudiq
from extremecloudiq.apis.tags import airrm_endpoint_api
from extremecloudiq.model.xiq_airrm_get_site_device_regulatory_config_afc_spectrum_response import XIQAirrmGetSiteDeviceRegulatoryConfigAfcSpectrumResponse
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
    api_instance = airrm_endpoint_api.AirrmEndpointApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'airrmId': 123,
    }
    try:
        # Get Site Device Regulatory Config and AFC Spectrum
        api_response = api_instance.get_site_device_regulatory_config_afc_spectrum(
            path_params=path_params,
        )
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling AirrmEndpointApi->get_site_device_regulatory_config_afc_spectrum: %s\n" % e)
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
airrmId | AirrmIdSchema | | 

# AirrmIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_site_device_regulatory_config_afc_spectrum.ApiResponseFor200) | OK

#### get_site_device_regulatory_config_afc_spectrum.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XIQAirrmGetSiteDeviceRegulatoryConfigAfcSpectrumResponse**](../../models/XIQAirrmGetSiteDeviceRegulatoryConfigAfcSpectrumResponse.md) |  | 


### Authorization

[Bearer](../../../README.md#Bearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

