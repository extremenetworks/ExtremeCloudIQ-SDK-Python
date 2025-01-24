# extremecloudiq.model.xiq_update_floor_request.XiqUpdateFloorRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**map_size_width** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floor map width | value must be a 64 bit float
**installation_height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The installation height | value must be a 64 bit float
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent location ID | value must be a 64 bit integer
**db_attenuation** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floor attenuation in dBs | value must be a 64 bit float
**name** | str,  | str,  | The floor name | 
**measurement_unit** | [**XiqMeasurementUnit**](XiqMeasurementUnit.md) | [**XiqMeasurementUnit**](XiqMeasurementUnit.md) |  | 
**map_size_height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floor map height | value must be a 64 bit float
**environment** | [**XiqRfEnvironmentType**](XiqRfEnvironmentType.md) | [**XiqRfEnvironmentType**](XiqRfEnvironmentType.md) |  | [optional] 
**map_name** | str,  | str,  | The floor map name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

