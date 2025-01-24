# extremecloudiq.model.xiq_create_radius_proxy_request.XiqCreateRadiusProxyRequest

The payload to create a new RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to create a new RADIUS proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[realms](#realms)** | list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#x27;DEFAULT&#x27; and &#x27;NULL&#x27; | 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | 
**retry_delay** | decimal.Decimal, int,  | decimal.Decimal,  | The retry delay of RADIUS proxy | value must be a 32 bit integer
**retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | The retry count of RADIUS proxy | value must be a 32 bit integer
**name** | str,  | str,  | The RADIUS proxy name | 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The device IDS to assign RADIUS proxy | 
**dead_time** | decimal.Decimal, int,  | decimal.Decimal,  | The dead time of RADIUS proxy | value must be a 32 bit integer
**description** | str,  | str,  | The RADIUS proxy description | [optional] 
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# realms

The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name 'DEFAULT' and 'NULL'

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#x27;DEFAULT&#x27; and &#x27;NULL&#x27; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCreateRadiusProxyRealm**](XiqCreateRadiusProxyRealm.md) | [**XiqCreateRadiusProxyRealm**](XiqCreateRadiusProxyRealm.md) | [**XiqCreateRadiusProxyRealm**](XiqCreateRadiusProxyRealm.md) |  | 

# device_ids

The device IDS to assign RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device IDS to assign RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The device IDS to assign RADIUS proxy | value must be a 64 bit integer

# clients

The RADIUS clients of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCreateRadiusClient**](XiqCreateRadiusClient.md) | [**XiqCreateRadiusClient**](XiqCreateRadiusClient.md) | [**XiqCreateRadiusClient**](XiqCreateRadiusClient.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

