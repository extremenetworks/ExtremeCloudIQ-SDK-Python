# extremecloudiq.model.xiq_wired_device_health_temperature_status_response.XiqWiredDeviceHealthTemperatureStatusResponse

Response body for the Wired Device Health Temperature Status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response body for the Wired Device Health Temperature Status | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[devices](#devices)** | list, tuple,  | tuple,  | The list contains a single element for standalone devices and multiple elements for each member of a stack | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# devices

The list contains a single element for standalone devices and multiple elements for each member of a stack

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list contains a single element for standalone devices and multiple elements for each member of a stack | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredDeviceHealthTemperatureStatusResponseEntry**](XiqWiredDeviceHealthTemperatureStatusResponseEntry.md) | [**XiqWiredDeviceHealthTemperatureStatusResponseEntry**](XiqWiredDeviceHealthTemperatureStatusResponseEntry.md) | [**XiqWiredDeviceHealthTemperatureStatusResponseEntry**](XiqWiredDeviceHealthTemperatureStatusResponseEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

