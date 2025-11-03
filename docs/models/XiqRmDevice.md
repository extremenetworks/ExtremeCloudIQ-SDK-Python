# extremecloudiq.model.xiq_rm_device.XiqRmDevice

Generic ExtremeCloud IQ RM Device List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generic ExtremeCloud IQ RM Device List | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**connected** | bool,  | BoolClass,  | The device connection status | [optional] 
**hostname** | str,  | str,  | The device hostname | [optional] 
**healthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The associated active client count for the device | [optional] value must be a 32 bit integer
**unhealthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The associated inactive client count for the device | [optional] value must be a 32 bit integer
**system_up_time** | decimal.Decimal, int,  | decimal.Decimal,  | The device uptime | [optional] value must be a 64 bit integer
**updated_on** | decimal.Decimal, int,  | decimal.Decimal,  | The last device updated time | [optional] value must be a 64 bit integer
**mac_address** | str,  | str,  | The device MAC address | [optional] 
**serial_number** | str,  | str,  | The device serial number, valid for all non-HAC devices | [optional] 
**device_ip** | str,  | str,  | The device IPv4 address | [optional] 
**default_gateway** | str,  | str,  | The device default gateway | [optional] 
**software_version** | str,  | str,  | The device OS software version | [optional] 
**product_type** | str,  | str,  | The product type, such as AP_230, BR_100, NX9600, etc. | [optional] 
**ipv6_address** | str,  | str,  | The device IPv6 address | [optional] 
**device_admin_state** | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | [optional] 
**sim_type** | [**XiqDeviceType**](XiqDeviceType.md) | [**XiqDeviceType**](XiqDeviceType.md) |  | [optional] 
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned country code on the device | [optional] value must be a 32 bit integer
**managed_by** | str,  | str,  | The managed application for the device | [optional] 
**channel_wifi0** | str,  | str,  | Channel for wifi0 | [optional] 
**power_wifi0** | str,  | str,  | Power for wifi0 | [optional] 
**radio_wifi0** | str,  | str,  | Radio for wifi0 | [optional] 
**channel_wifi1** | str,  | str,  | Channel for wifi1 | [optional] 
**power_wifi1** | str,  | str,  | Power for wifi1 | [optional] 
**radio_wifi1** | str,  | str,  | Radio for wifi1 | [optional] 
**channel_wifi2** | str,  | str,  | Channel for wifi2 | [optional] 
**power_wifi2** | str,  | str,  | Power for wifi2 | [optional] 
**radio_wifi2** | str,  | str,  | Radio for wifi2 | [optional] 
**config_mismatch** | bool,  | BoolClass,  | Config audit status(MATCHED(false) or UNMATCHED(true)) | [optional] 
**locations** | [**XiqRmDeviceLocationDetails**](XiqRmDeviceLocationDetails.md) | [**XiqRmDeviceLocationDetails**](XiqRmDeviceLocationDetails.md) |  | [optional] 
**device_category** | [**XiqRmDeviceCategory**](XiqRmDeviceCategory.md) | [**XiqRmDeviceCategory**](XiqRmDeviceCategory.md) |  | [optional] 
**has_management_ip_issue** | bool,  | BoolClass,  | Flag to indicate device with management IP issue | [optional] 
**has_default_gateway_issue** | bool,  | BoolClass,  | Flag to indicate device with default gateway issue | [optional] 
**has_firmware_version_issue** | bool,  | BoolClass,  | Flag to indicate device with firmware version issue | [optional] 
**stack_size** | str,  | str,  | The number of devices in the stack (0 for standalone devices) | [optional] 
**stack_id** | decimal.Decimal, int,  | decimal.Decimal,  | The stack id (only for stack members) | [optional] value must be a 64 bit integer
**xiq_rm_device_icons** | [**XiqRmDeviceIcons**](XiqRmDeviceIcons.md) | [**XiqRmDeviceIcons**](XiqRmDeviceIcons.md) |  | [optional] 
**device_license_tier** | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) |  | [optional] 
**device_license_type** | str,  | str,  | The license type of the device | [optional] must be one of ["LEGACY", "NAVIGATOR", "PILOT", "COPILOT", "NONE", "NA", "TRIAL", "NOT_REQUIRED", "GRACEPERIOD", "UNLICENSED", "STANDARD", "ADVANCED", "NOT_LICENSED", ] 
**network_policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The network policy ID associated with the device | [optional] value must be a 64 bit integer
**network_policy_name** | str,  | str,  | The network policy name associated with the device | [optional] 
**os** | str,  | str,  | The OS Name | [optional] 
**device_template_name** | str,  | str,  | The device template name | [optional] 
**[cloud_config_groups](#cloud_config_groups)** | list, tuple,  | tuple,  | The device cloud config groups | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cloud_config_groups

The device cloud config groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device cloud config groups | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The device cloud config groups | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

