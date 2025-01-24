# extremecloudiq.model.xiq_update_radius_proxy_request.XiqUpdateRadiusProxyRequest

The payload to update RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to update RADIUS proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The RADIUS proxy name | [optional] 
**description** | str,  | str,  | The RADIUS proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | [optional] 
**retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | The retry count of RADIUS proxy | [optional] value must be a 32 bit integer
**retry_delay** | decimal.Decimal, int,  | decimal.Decimal,  | The retry delay of RADIUS proxy | [optional] value must be a 32 bit integer
**dead_time** | decimal.Decimal, int,  | decimal.Decimal,  | The dead time of RADIUS proxy | [optional] value must be a 32 bit integer
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | [optional] 
**[realms](#realms)** | list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#x27;DEFAULT&#x27; and &#x27;NULL&#x27; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# clients

The RADIUS clients of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUpdateRadiusClient**](XiqUpdateRadiusClient.md) | [**XiqUpdateRadiusClient**](XiqUpdateRadiusClient.md) | [**XiqUpdateRadiusClient**](XiqUpdateRadiusClient.md) |  | 

# realms

The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name 'DEFAULT' and 'NULL'

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#x27;DEFAULT&#x27; and &#x27;NULL&#x27; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUpdateRadiusProxyRealm**](XiqUpdateRadiusProxyRealm.md) | [**XiqUpdateRadiusProxyRealm**](XiqUpdateRadiusProxyRealm.md) | [**XiqUpdateRadiusProxyRealm**](XiqUpdateRadiusProxyRealm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

