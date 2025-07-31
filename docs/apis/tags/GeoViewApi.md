<a id="__pageTop"></a>
# extremecloudiq.apis.tags.geo_view_api.GeoViewApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_geo_view_data**](#get_geo_view_data) | **get** /geo-view | Get GeoView Data

# **get_geo_view_data**
<a id="get_geo_view_data"></a>
> [GeoViewNode] get_geo_view_data()

Get GeoView Data

### Example

```python
import extremecloudiq
from extremecloudiq.apis.tags import geo_view_api
from extremecloudiq.model.geo_view_node import GeoViewNode
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geo_view_api.GeoViewApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get GeoView Data
        api_response = api_instance.get_geo_view_data()
        pprint(api_response)
    except extremecloudiq.ApiException as e:
        print("Exception when calling GeoViewApi->get_geo_view_data: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_geo_view_data.ApiResponseFor200) | OK

#### get_geo_view_data.ApiResponseFor200
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
[**GeoViewNode**]({{complexTypePrefix}}GeoViewNode.md) | [**GeoViewNode**]({{complexTypePrefix}}GeoViewNode.md) | [**GeoViewNode**]({{complexTypePrefix}}GeoViewNode.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

