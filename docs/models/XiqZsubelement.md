# extremecloudiq.model.xiq_zsubelement.XiqZsubelement

The payload of Z-subelement Settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of Z-subelement Settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**floor_number** | decimal.Decimal, int,  | decimal.Decimal,  | Floor number where the device is installed. | value must be a 32 bit integer
**expected_to_move** | bool,  | BoolClass,  | Is the device expected to move? | 
**above_floor** | [**XiqZsubelementAboveFloor**](XiqZsubelementAboveFloor.md) | [**XiqZsubelementAboveFloor**](XiqZsubelementAboveFloor.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

