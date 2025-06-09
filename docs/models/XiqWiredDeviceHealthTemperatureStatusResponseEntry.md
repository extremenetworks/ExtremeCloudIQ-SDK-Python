# extremecloudiq.model.xiq_wired_device_health_temperature_status_response_entry.XiqWiredDeviceHealthTemperatureStatusResponseEntry

The description of the temperature status response for a device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The description of the temperature status response for a device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**slot_number** | str,  | str,  | The slot number of the device (0 for standalone) | [optional] 
**temperature** | decimal.Decimal, int,  | decimal.Decimal,  | The temperature of the device | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

