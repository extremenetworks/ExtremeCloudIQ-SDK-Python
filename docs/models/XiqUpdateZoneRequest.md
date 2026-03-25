# extremecloudiq.model.xiq_update_zone_request.XiqUpdateZoneRequest

The list of zones to update

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of zones to update | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**visible** | bool,  | BoolClass,  | The visibility of the zone | 
**color** | str,  | str,  | The Zone color | 
**[coordinates](#coordinates)** | list, tuple,  | tuple,  | The Zone coordinates | 
**name** | str,  | str,  | The Zone name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The Zone ID | value must be a 64 bit integer
**zone_vertical_align** | [**XiqZoneVerticalAlign**](XiqZoneVerticalAlign.md) | [**XiqZoneVerticalAlign**](XiqZoneVerticalAlign.md) |  | 
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

