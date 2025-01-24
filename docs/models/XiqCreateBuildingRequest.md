# extremecloudiq.model.xiq_create_building_request.XiqCreateBuildingRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**XiqAddress**](XiqAddress.md) | [**XiqAddress**](XiqAddress.md) |  | 
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent location ID | value must be a 64 bit integer
**name** | str,  | str,  | The building name | 
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude coordinate for the building | [optional] value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude coordinate for the building | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

