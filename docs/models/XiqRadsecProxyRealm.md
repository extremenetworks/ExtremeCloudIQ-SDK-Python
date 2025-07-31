# extremecloudiq.model.xiq_radsec_proxy_realm.XiqRadsecProxyRealm

The RADSEC proxy realm configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The RADSEC proxy realm configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[external_radius_server_object_ids](#external_radius_server_object_ids)** | list, tuple,  | tuple,  | The list of associated external RADIUS servers | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The RADIUS proxy realm ID | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The RADIUS proxy realm name | [optional] 
**enable_strip_realm_name** | bool,  | BoolClass,  | The flag for enable strip realm name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# external_radius_server_object_ids

The list of associated external RADIUS servers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of associated external RADIUS servers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of associated external RADIUS servers | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

