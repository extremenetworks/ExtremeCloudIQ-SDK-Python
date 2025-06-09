# extremecloudiq.model.xiq_wired_device_health_fan_status_response_entry.XiqWiredDeviceHealthFanStatusResponseEntry

The description of the fan status response for a device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The description of the fan status response for a device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**slot_number** | str,  | str,  | The slot number of the device (0 for standalone) | [optional] 
**fan_status_error** | str,  | str,  | The number of fans that are not operating correctly | [optional] 
**fan_total** | str,  | str,  | The total number of fans | [optional] 
**[fan_units](#fan_units)** | list, tuple,  | tuple,  | The list of fans with their corresponding status | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fan_units

The list of fans with their corresponding status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of fans with their corresponding status | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredDeviceHealthFanStatus**](XiqWiredDeviceHealthFanStatus.md) | [**XiqWiredDeviceHealthFanStatus**](XiqWiredDeviceHealthFanStatus.md) | [**XiqWiredDeviceHealthFanStatus**](XiqWiredDeviceHealthFanStatus.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

