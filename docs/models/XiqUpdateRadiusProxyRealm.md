# extremecloudiq.model.xiq_update_radius_proxy_realm.XiqUpdateRadiusProxyRealm

The associate RADIUS proxy realm for RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The associate RADIUS proxy realm for RADIUS proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The RADIUS proxy realm ID, using an existing ID or leave empty to create a new one | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The RADIUS proxy realm name | [optional] 
**enable_strip_realm_name** | bool,  | BoolClass,  | The flag for enable strip realm name | [optional] 
**radius_client_object_id** | decimal.Decimal, int,  | decimal.Decimal,  | The associate RADIUS client object ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

