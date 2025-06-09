# extremecloudiq.model.xiq_wired_device_health_grid_response.XiqWiredDeviceHealthGridResponse

Response body for the Wired Device Health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response body for the Wired Device Health grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the device | [optional] value must be a 64 bit integer
**stack_size** | str,  | str,  | The number of devices in the stack (0 for standalone devices) | [optional] 
**device_hostname** | str,  | str,  | The hostname of the device | [optional] 
**device_ip** | str,  | str,  | The IP address of the device | [optional] 
**site** | str,  | str,  | The site where the device is located | [optional] 
**building** | str,  | str,  | The building where the device is located | [optional] 
**floor** | str,  | str,  | The floor where the device is located | [optional] 
**cpu_usage** | str,  | str,  | CPU usage percentage of the device | [optional] 
**memory_usage** | str,  | str,  | Memory usage percentage of the device | [optional] 
**temperature** | decimal.Decimal, int,  | decimal.Decimal,  | The temperature of the device | [optional] value must be a 32 bit integer
**temperature_error_slots** | str,  | str,  | Indicates the number of the stack slots that have temperature errors/if a standalone device has temperature errors | [optional] 
**poe_usage** | str,  | str,  | The PoE usage percentage of the device | [optional] 
**poe_error_slots** | str,  | str,  | Indicates the number of the stack slots that have PoE errors/if a standalone device has PoE errors | [optional] 
**fan_error_slots** | str,  | str,  | Indicates the number of the stack slots that have fan errors/if a standalone device has fan errors | [optional] 
**psu_error_slots** | str,  | str,  | Indicates the number of the stack slots that have PSU errors/if a standalone device has PSU errors | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

