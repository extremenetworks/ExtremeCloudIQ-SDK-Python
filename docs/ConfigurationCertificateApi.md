# extremecloudiq.ConfigurationCertificateApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_certificates**](ConfigurationCertificateApi.md#list_certificates) | **GET** /certificates | List certificates


# **list_certificates**
> PagedXiqCertificate list_certificates(page=page, limit=limit, cert_type=cert_type)

List certificates

List a page of certificates.

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
    api_instance = extremecloudiq.ConfigurationCertificateApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
cert_type = extremecloudiq.XiqCertificateType() # XiqCertificateType | The certificate type (optional)

    try:
        # List certificates
        api_response = api_instance.list_certificates(page=page, limit=limit, cert_type=cert_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationCertificateApi->list_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **cert_type** | [**XiqCertificateType**](.md)| The certificate type | [optional] 

### Return type

[**PagedXiqCertificate**](PagedXiqCertificate.md)

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

