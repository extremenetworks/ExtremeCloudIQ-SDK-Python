# extremecloudiq.model.xiq_hardware_health_stats_response.XiqHardwareHealthStatsResponse

Copilot Hardware Health Stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Hardware Health Stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[hd_device_stats_entities](#hd_device_stats_entities)** | list, tuple,  | tuple,  | the anomaly devices data | [optional] 
**[hd_packet_counts_entities](#hd_packet_counts_entities)** | list, tuple,  | tuple,  | the anomaly devices data | [optional] 
**[hd_reboot_stats_entities](#hd_reboot_stats_entities)** | list, tuple,  | tuple,  | the anomaly devices data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hd_device_stats_entities

the anomaly devices data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly devices data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHardwareHealthDeviceStatsEntity**](XiqHardwareHealthDeviceStatsEntity.md) | [**XiqHardwareHealthDeviceStatsEntity**](XiqHardwareHealthDeviceStatsEntity.md) | [**XiqHardwareHealthDeviceStatsEntity**](XiqHardwareHealthDeviceStatsEntity.md) |  | 

# hd_packet_counts_entities

the anomaly devices data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly devices data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHardwareHealthPacketCountsEntity**](XiqHardwareHealthPacketCountsEntity.md) | [**XiqHardwareHealthPacketCountsEntity**](XiqHardwareHealthPacketCountsEntity.md) | [**XiqHardwareHealthPacketCountsEntity**](XiqHardwareHealthPacketCountsEntity.md) |  | 

# hd_reboot_stats_entities

the anomaly devices data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly devices data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHardwareHealthRebootStatsEntity**](XiqHardwareHealthRebootStatsEntity.md) | [**XiqHardwareHealthRebootStatsEntity**](XiqHardwareHealthRebootStatsEntity.md) | [**XiqHardwareHealthRebootStatsEntity**](XiqHardwareHealthRebootStatsEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

