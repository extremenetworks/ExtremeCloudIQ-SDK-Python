# extremecloudiq.model.xiq_update_zones_request.XiqUpdateZonesRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**folder_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Folder ID | value must be a 64 bit integer
**[zones](#zones)** | list, tuple,  | tuple,  | The list of zones to update | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# zones

The list of zones to update

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of zones to update | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqUpdateZoneRequest**](XiqUpdateZoneRequest.md) | [**XiqUpdateZoneRequest**](XiqUpdateZoneRequest.md) | [**XiqUpdateZoneRequest**](XiqUpdateZoneRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

