# extremecloudiq.model.xiq_radius_client_object_entry.XiqRadiusClientObjectEntry

The entry of RADIUS client object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The entry of RADIUS client object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**server_role** | [**XiqServerRole**](XiqServerRole.md) | [**XiqServerRole**](XiqServerRole.md) |  | 
**radius_server_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the RADIUS server object, for EXTERNAL_RADIUS_SERVER please use the ID of external RADIUS server object. For INTERNAL_RADIUS_SERVER, please use the RADIUS device ID | value must be a 64 bit integer
**server_type** | [**XiqRadiusClientObjectType**](XiqRadiusClientObjectType.md) | [**XiqRadiusClientObjectType**](XiqRadiusClientObjectType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

