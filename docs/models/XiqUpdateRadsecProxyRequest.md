# extremecloudiq.model.xiq_update_radsec_proxy_request.XiqUpdateRadsecProxyRequest

The payload to update a new RADSEC proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to update a new RADSEC proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The RADSEC proxy name | [optional] 
**description** | str,  | str,  | The RADSEC proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | [optional] 
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
**operator_name** | str,  | str,  | The RADSEC proxy operator name | [optional] 
**[realms](#realms)** | list, tuple,  | tuple,  | The realms of RADSEC proxy | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# realms

The realms of RADSEC proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The realms of RADSEC proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUpdateRadsecProxyRealm**](XiqUpdateRadsecProxyRealm.md) | [**XiqUpdateRadsecProxyRealm**](XiqUpdateRadsecProxyRealm.md) | [**XiqUpdateRadsecProxyRealm**](XiqUpdateRadsecProxyRealm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

