# extremecloudiq.model.xiq_floor.XiqFloor

The Floor information on the floorplan.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Floor information on the floorplan. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**XiqRfEnvironmentType**](XiqRfEnvironmentType.md) | [**XiqRfEnvironmentType**](XiqRfEnvironmentType.md) |  | 
**unique_name** | str,  | str,  | The floor unique name | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**installation_height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The installation height | value must be a 64 bit float
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent building ID | value must be a 64 bit integer
**db_attenuation** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floor attenuation in dBs | value must be a 64 bit float
**name** | str,  | str,  | The floor name | 
**measurement_unit** | [**XiqMeasurementUnit**](XiqMeasurementUnit.md) | [**XiqMeasurementUnit**](XiqMeasurementUnit.md) |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**map_size_width** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floormap width | [optional] value must be a 64 bit float
**map_size_height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The floormap height | [optional] value must be a 64 bit float
**map_name** | str,  | str,  | The floormap name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

