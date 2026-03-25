# extremecloudiq.model.xiq_floor_map_label.XiqFloorMapLabel

Floor Map Label information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Floor Map Label information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Floor Map Label, its x coordinate on the map | value must be a 64 bit float
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Floor Map Label, its y coordinate on the map | value must be a 64 bit float
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The Floor Map Label, its id | value must be a 64 bit integer
**text** | str,  | str,  | The Floor Map Label, its text. | 
**floor_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Floor, its id | [optional] value must be a 64 bit integer
**visible** | bool,  | BoolClass,  | Visible? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

