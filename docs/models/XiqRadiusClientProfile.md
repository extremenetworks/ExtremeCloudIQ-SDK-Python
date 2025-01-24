# extremecloudiq.model.xiq_radius_client_profile.XiqRadiusClientProfile

The RADIUS client profile.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The RADIUS client profile. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**default_radius_client_object_id** | decimal.Decimal, int,  | decimal.Decimal,  | The default RADIUS client object ID. | [optional] value must be a 64 bit integer
**enable_classification** | bool,  | BoolClass,  | The flag to enable classification entries on RADIUS client profile. | [optional] 
**[classified_entries](#classified_entries)** | list, tuple,  | tuple,  | The RADIUS client profile classified entries. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classified_entries

The RADIUS client profile classified entries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS client profile classified entries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRadiusClientProfileEntry**](XiqRadiusClientProfileEntry.md) | [**XiqRadiusClientProfileEntry**](XiqRadiusClientProfileEntry.md) | [**XiqRadiusClientProfileEntry**](XiqRadiusClientProfileEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

