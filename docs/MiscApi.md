# extremecloudiq.MiscApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_list**](MiscApi.md#get_country_list) | **GET** /countries | Get country list
[**get_state_list_by_country_code**](MiscApi.md#get_state_list_by_country_code) | **GET** /countries/{countryAlpha2Code}/states | Get state list in a country
[**validate_country_code**](MiscApi.md#validate_country_code) | **GET** /countries/{countryCode}/:validate | Validate country code


# **get_country_list**
> list[XiqCountry] get_country_list()

Get country list

Get list of countries and country codes.

### Example

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


# Enter a context with an instance of the API client
with extremecloudiq.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.MiscApi(api_client)
    
    try:
        # Get country list
        api_response = api_instance.get_country_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MiscApi->get_country_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqCountry]**](XiqCountry.md)

### Authorization

No authorization required

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

# **get_state_list_by_country_code**
> list[XiqCountryState] get_state_list_by_country_code(country_alpha2_code)

Get state list in a country

Get list of states or provinces in a country with country alpha2 code.

### Example

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


# Enter a context with an instance of the API client
with extremecloudiq.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.MiscApi(api_client)
    country_alpha2_code = 'country_alpha2_code_example' # str | 

    try:
        # Get state list in a country
        api_response = api_instance.get_state_list_by_country_code(country_alpha2_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MiscApi->get_state_list_by_country_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_alpha2_code** | **str**|  | 

### Return type

[**list[XiqCountryState]**](XiqCountryState.md)

### Authorization

No authorization required

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

# **validate_country_code**
> bool validate_country_code(country_code)

Validate country code

Validate whether the country code is a valid code or not.

### Example

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


# Enter a context with an instance of the API client
with extremecloudiq.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.MiscApi(api_client)
    country_code = 56 # int | The country code.

    try:
        # Validate country code
        api_response = api_instance.validate_country_code(country_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MiscApi->validate_country_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| The country code. | 

### Return type

**bool**

### Authorization

No authorization required

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

