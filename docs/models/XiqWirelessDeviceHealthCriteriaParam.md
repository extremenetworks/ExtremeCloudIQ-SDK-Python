# extremecloudiq.model.xiq_wireless_device_health_criteria_param.XiqWirelessDeviceHealthCriteriaParam

The criteria for a wireless device health

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The criteria for a wireless device health | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID | [optional] value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**cpu_utilization** | decimal.Decimal, int, float,  | decimal.Decimal,  | The CPU utilization | [optional] value must be a 64 bit float
**cpu_utilization_reln** | str,  | str,  | The CPU utilization relation | [optional] 
**memory_utilization** | decimal.Decimal, int, float,  | decimal.Decimal,  | The memory utilization | [optional] value must be a 64 bit float
**memory_utilization_reln** | str,  | str,  | The memory utilization relation | [optional] 
**poe** | decimal.Decimal, int, float,  | decimal.Decimal,  | The power over ethernet | [optional] value must be a 64 bit float
**wired_port_multicast** | decimal.Decimal, int, float,  | decimal.Decimal,  | The wired port multicast | [optional] value must be a 64 bit float
**wired_port_multicast_reln** | str,  | str,  | The wired port multicast relation | [optional] 
**wired_port_broadcast** | decimal.Decimal, int, float,  | decimal.Decimal,  | The wired port broadcast | [optional] value must be a 64 bit float
**wired_port_broadcast_reln** | str,  | str,  | The wired port broadcast relation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

