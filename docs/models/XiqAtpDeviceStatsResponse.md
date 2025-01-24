# extremecloudiq.model.xiq_atp_device_stats_response.XiqAtpDeviceStatsResponse

Copilot Atp Device Stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Atp Device Stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**summary** | str,  | str,  | the anomaly location | [optional] 
**[atp_device_stats_entities](#atp_device_stats_entities)** | list, tuple,  | tuple,  | the anomaly devices data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# atp_device_stats_entities

the anomaly devices data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly devices data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAtpDeviceStatsEntity**](XiqAtpDeviceStatsEntity.md) | [**XiqAtpDeviceStatsEntity**](XiqAtpDeviceStatsEntity.md) | [**XiqAtpDeviceStatsEntity**](XiqAtpDeviceStatsEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

