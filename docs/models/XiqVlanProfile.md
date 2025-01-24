# extremecloudiq.model.xiq_vlan_profile.XiqVlanProfile

The payload of common object - VLAN profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of common object - VLAN profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**enable_classification** | bool,  | BoolClass,  | If apply VLANs to devices using classification | 
**name** | str,  | str,  | The VLAN profile name | 
**default_vlan_id** | decimal.Decimal, int,  | decimal.Decimal,  | The default VLAN ID | value must be a 32 bit integer
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**[classified_entries](#classified_entries)** | list, tuple,  | tuple,  | The VLAN object classified entries | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classified_entries

The VLAN object classified entries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The VLAN object classified entries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqVlanObjectClassifiedEntry**](XiqVlanObjectClassifiedEntry.md) | [**XiqVlanObjectClassifiedEntry**](XiqVlanObjectClassifiedEntry.md) | [**XiqVlanObjectClassifiedEntry**](XiqVlanObjectClassifiedEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

