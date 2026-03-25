# extremecloudiq.model.xiq_create_zone_request.XiqCreateZoneRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**color** | str,  | str,  | The Zone color | 
**[coordinates](#coordinates)** | list, tuple,  | tuple,  | The Zone coordinates | 
**name** | str,  | str,  | The Zone name | 
**folder_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Folder ID | value must be a 64 bit integer
**zone_vertical_align** | [**XiqZoneVerticalAlign**](XiqZoneVerticalAlign.md) | [**XiqZoneVerticalAlign**](XiqZoneVerticalAlign.md) |  | 
**visible** | bool,  | BoolClass,  | The visibility of the zone | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# coordinates

The Zone coordinates

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Zone coordinates | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqZonePoint**](XiqZonePoint.md) | [**XiqZonePoint**](XiqZonePoint.md) | [**XiqZonePoint**](XiqZonePoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

