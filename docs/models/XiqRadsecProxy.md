# extremecloudiq.model.xiq_radsec_proxy.XiqRadsecProxy

The configuration of RADSEC proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration of RADSEC proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator_name** | str,  | str,  | The RADSEC proxy operator name | 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**operator_name_type** | str,  | str,  | The operator name type of RADSEC proxy | must be one of ["WBAID", ] 
**name** | str,  | str,  | The RADSEC proxy name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The RADSEC proxy description | [optional] 
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute | [optional] 
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
[**XiqRadsecProxyRealm**](XiqRadsecProxyRealm.md) | [**XiqRadsecProxyRealm**](XiqRadsecProxyRealm.md) | [**XiqRadsecProxyRealm**](XiqRadsecProxyRealm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

