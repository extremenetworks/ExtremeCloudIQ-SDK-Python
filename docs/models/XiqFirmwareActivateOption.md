# extremecloudiq.model.xiq_firmware_activate_option.XiqFirmwareActivateOption

The firmware activate option (Only one of them can be enabled)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The firmware activate option (Only one of them can be enabled) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_activate_at_next_reboot** | bool,  | BoolClass,  | Activate at next reboot (requires rebooting manually) | [optional] 
**activation_delay_seconds** | decimal.Decimal, int,  | decimal.Decimal,  | Activate after the given seconds | [optional] value must be a 64 bit integer
**activation_time** | decimal.Decimal, int,  | decimal.Decimal,  | Activate at the following time according to the system clock on the updated device | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

