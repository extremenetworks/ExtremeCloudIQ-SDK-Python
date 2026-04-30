# extremecloudiq.model.xiq_device_details.XiqDeviceDetails

The device details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**system_name** | str,  | str,  | The system name of the device. | [optional] 
**ip_address** | str,  | str,  | Management IP address. Supports IPv4 (e.g., 192.0.2.1) or IPv6 (e.g., 2001:db8::1). Prefer canonical presentation; use separate fields or oneOf if you need strict validation. | [optional] 
**model** | str,  | str,  | The device model name or number. | [optional] 
**sys_up_time** | str,  | str,  | System uptime duration. Represented in seconds (integer) or as an ISO-8601 duration string (e.g., PT1H). Preferred representation: seconds. | [optional] 
**os_version** | str,  | str,  | The operating system version of the device. | [optional] 
**location** | str,  | str,  | The physical location of the device. | [optional] 
**system_mac** | str,  | str,  | List of device MAC addresses to filter. Each MAC may be 12 hex characters (no separators) or use colon/dash delimiters. | [optional] 
**serial_number** | str,  | str,  | The serial number of the device. | [optional] 
**system_description** | str,  | str,  | A detailed description of the device system. | [optional] 
**software_version** | str,  | str,  | The software version running on the device. | [optional] 
**installation_time** | str, datetime,  | str,  | The timestamp when the device was installed. | [optional] value must conform to RFC-3339 date-time
**device_license_tier** | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) |  | [optional] 
**device_license_type** | str,  | str,  | The license type of the device | [optional] must be one of ["LEGACY", "NAVIGATOR", "PILOT", "COPILOT", "NONE", "NA", "TRIAL", "NOT_REQUIRED", "GRACEPERIOD", "UNLICENSED", "STANDARD", "ADVANCED", "NOT_LICENSED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

