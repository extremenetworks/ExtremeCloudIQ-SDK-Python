# extremecloudiq.model.xiq_hardware_health_device_stats_entity.XiqHardwareHealthDeviceStatsEntity

ExtremeCloud IQ Data Point

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Data Point | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The Timestamp | value must be a 64 bit integer
**avg_cpu_utilization** | decimal.Decimal, int, float,  | decimal.Decimal,  | Avg Cpu Utilization | [optional] 
**avg_memory_utilization** | decimal.Decimal, int, float,  | decimal.Decimal,  | Avg Memory Utilization | [optional] 
**avg_client_count** | decimal.Decimal, int,  | decimal.Decimal,  | Avg Client Count | [optional] value must be a 32 bit integer
**unit_temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unit Temperature | [optional] 
**poe_power_mode** | str,  | str,  | Poe PowerMode | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

