# extremecloudiq.model.xiq_radius_proxy.XiqRadiusProxy

The configuration of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration of RADIUS proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The RADIUS proxy name | [optional] 
**description** | str,  | str,  | The RADIUS proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | [optional] 
**retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | The retry count of RADIUS proxy | [optional] value must be a 32 bit integer
**retry_delay** | decimal.Decimal, int,  | decimal.Decimal,  | The retry delay of RADIUS proxy | [optional] value must be a 32 bit integer
**dead_time** | decimal.Decimal, int,  | decimal.Decimal,  | The dead time of RADIUS proxy | [optional] value must be a 32 bit integer
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | [optional] 
**[realms](#realms)** | list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy | [optional] 
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
[**XiqRadiusClient**](XiqRadiusClient.md) | [**XiqRadiusClient**](XiqRadiusClient.md) | [**XiqRadiusClient**](XiqRadiusClient.md) |  | 

# realms

The RADIUS realms of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRadiusProxyRealm**](XiqRadiusProxyRealm.md) | [**XiqRadiusProxyRealm**](XiqRadiusProxyRealm.md) | [**XiqRadiusProxyRealm**](XiqRadiusProxyRealm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

