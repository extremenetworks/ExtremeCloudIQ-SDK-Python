# extremecloudiq.model.xiq_cloud_config_group.XiqCloudConfigGroup

The CCG

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The CCG | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The CCG name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**predefined** | bool,  | BoolClass,  | Whether it is predefined | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The CCG description | [optional] 
**read_only** | bool,  | BoolClass,  | Whether it is read-only | [optional] 
**zone_name** | str,  | str,  | The zone name. | [optional] 
**zone_id** | decimal.Decimal, int,  | decimal.Decimal,  | The zone ID | [optional] value must be a 64 bit integer
**zone_location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The zone location ID | [optional] value must be a 64 bit integer
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The device IDs selected for this Ccg. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The device IDs selected for this Ccg.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device IDs selected for this Ccg. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The device IDs selected for this Ccg. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

