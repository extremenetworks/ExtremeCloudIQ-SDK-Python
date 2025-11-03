# extremecloudiq.model.xiq_wired_port_qos_state.XiqWiredPortQosState

QOS queue statistics of the interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | QOS queue statistics of the interface | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**port_name** | str,  | str,  | The interface name | [optional] 
**[queue_stats](#queue_stats)** | list, tuple,  | tuple,  | QOS queue statistics of the interface | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# queue_stats

QOS queue statistics of the interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | QOS queue statistics of the interface | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredQueueStats**](XiqWiredQueueStats.md) | [**XiqWiredQueueStats**](XiqWiredQueueStats.md) | [**XiqWiredQueueStats**](XiqWiredQueueStats.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

