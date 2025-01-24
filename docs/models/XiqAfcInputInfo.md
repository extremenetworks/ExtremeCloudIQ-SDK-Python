# extremecloudiq.model.xiq_afc_input_info.XiqAfcInputInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**serial_number** | str,  | str,  |  | [optional] 
**coordinates** | [**XiqApCoordinates**](XiqApCoordinates.md) | [**XiqApCoordinates**](XiqApCoordinates.md) |  | [optional] 
**elevation** | [**XiqElevation**](XiqElevation.md) | [**XiqElevation**](XiqElevation.md) |  | [optional] 
**ellipse** | [**XiqEllipse**](XiqEllipse.md) | [**XiqEllipse**](XiqEllipse.md) |  | [optional] 
**environment** | str,  | str,  |  | [optional] must be one of ["INDOOR", "OUTDOOR", "UNDERSEAT", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

