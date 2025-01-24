# extremecloudiq.model.xiq_device_location.XiqDeviceLocation

Device location info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Device location info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**location_name** | str,  | str,  | The location name | 
**update_time** | str, datetime,  | str,  | The timestamp when the location info was last updated | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The timestamp when the device assigned to the location | value must conform to RFC-3339 date-time
**location_unique_name** | str,  | str,  | The unique location name | 
**location_type** | str,  | str,  | The location type | 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned location ID, it must NOT be BUILDING type | [optional] value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**parent_id** | decimal.Decimal, int,  | decimal.Decimal,  | The parent location ID | [optional] value must be a 64 bit integer
**location_address** | str,  | str,  | The address for the location | [optional] 
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  | The horizontal value in the floor map | [optional] value must be a 64 bit float
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  | The vertical value in the floor map | [optional] value must be a 64 bit float
**latitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude in the geography | [optional] value must be a 64 bit float
**longitude** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude in the geography | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

