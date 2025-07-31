# extremecloudiq.model.xiq_create_radsec_proxy_request.XiqCreateRadsecProxyRequest

The payload to create a new RADSEC proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to create a new RADSEC proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator_name** | str,  | str,  | The RADSEC proxy operator name | 
**[realms](#realms)** | list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy | 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | 
**operator_name_type** | str,  | str,  | The operator name type of RADSEC proxy | must be one of ["WBAID", ] 
**name** | str,  | str,  | The RADSEC proxy name | 
**description** | str,  | str,  | The RADSEC proxy description | [optional] 
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# realms

The RADIUS realms of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS realms of RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCreateRadsecProxyRealm**](XiqCreateRadsecProxyRealm.md) | [**XiqCreateRadsecProxyRealm**](XiqCreateRadsecProxyRealm.md) | [**XiqCreateRadsecProxyRealm**](XiqCreateRadsecProxyRealm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

