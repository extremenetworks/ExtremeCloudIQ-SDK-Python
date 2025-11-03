# extremecloudiq.model.xiq_device_details.XiqDeviceDetails

The device details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**system_name** | str,  | str,  |  | [optional] 
**ip_address** | str,  | str,  |  | [optional] 
**model** | str,  | str,  |  | [optional] 
**sys_up_time** | str,  | str,  |  | [optional] 
**os_version** | str,  | str,  |  | [optional] 
**location** | str,  | str,  |  | [optional] 
**system_mac** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**system_description** | str,  | str,  |  | [optional] 
**software_version** | str,  | str,  |  | [optional] 
**installation_time** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**device_license_tier** | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) |  | [optional] 
**device_license_type** | str,  | str,  | The license type of the device | [optional] must be one of ["LEGACY", "NAVIGATOR", "PILOT", "COPILOT", "NONE", "NA", "TRIAL", "NOT_REQUIRED", "GRACEPERIOD", "UNLICENSED", "STANDARD", "ADVANCED", "NOT_LICENSED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

