# extremecloudiq.model.xiq_update_radius_client.XiqUpdateRadiusClient

The associate RADIUS client for RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The associate RADIUS client for RADIUS proxy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The RADIUS client ID, using an existing ID or leave empty to create a new one | [optional] value must be a 64 bit integer
**shared_secret** | str,  | str,  | The shared secret of RADIUS client | [optional] 
**description** | str,  | str,  | The RADIUS client description | [optional] 
**l3_address_profile_id** | decimal.Decimal, int,  | decimal.Decimal,  | The associate L3 address profile ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

