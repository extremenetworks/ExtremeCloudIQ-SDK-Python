# extremecloudiq.model.xiq_rm_afc_device.XiqRmAfcDevice

Generic ExtremeCloud IQ RM Device List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generic ExtremeCloud IQ RM Device List | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hostname** | str,  | str,  | The device hostname | [optional] 
**mac_address** | str,  | str,  | The device MAC address | [optional] 
**serial_number** | str,  | str,  | The device serial number, valid for all non-HAC devices | [optional] 
**product_type** | str,  | str,  | The product type, such as AP_230, BR_100, NX9600, etc. | [optional] 
**xiq_rm_device_icons** | [**XiqRmDeviceIcons**](XiqRmDeviceIcons.md) | [**XiqRmDeviceIcons**](XiqRmDeviceIcons.md) |  | [optional] 
**device_license_tier** | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) | [**XiqDeviceLicenseTier**](XiqDeviceLicenseTier.md) |  | [optional] 
**device_license_type** | str,  | str,  | The license type of the device | [optional] must be one of ["LEGACY", "NAVIGATOR", "PILOT", "COPILOT", "NONE", "NA", "TRIAL", "NOT_REQUIRED", "GRACEPERIOD", "UNLICENSED", "STANDARD", "ADVANCED", "NOT_LICENSED", ] 
**[xiq_afc_wifi_radio_settings](#xiq_afc_wifi_radio_settings)** | list, tuple,  | tuple,  | wifi radio afc setting | [optional] 
**locations** | [**XiqRmDeviceLocationDetails**](XiqRmDeviceLocationDetails.md) | [**XiqRmDeviceLocationDetails**](XiqRmDeviceLocationDetails.md) |  | [optional] 
**[geo_location](#geo_location)** | list, tuple,  | tuple,  | The geo-location values | [optional] 
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**ip_address** | str,  | str,  | The IP address of the device | [optional] 
**config_mismatch** | bool,  | BoolClass,  | Config audit status(MATCHED(false) or UNMATCHED(true)) | [optional] 
**connected** | bool,  | BoolClass,  | The device connection status | [optional] 
**is_mobile_data_persistent** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# xiq_afc_wifi_radio_settings

wifi radio afc setting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | wifi radio afc setting | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAfcWifiRadioSettings**](XiqAfcWifiRadioSettings.md) | [**XiqAfcWifiRadioSettings**](XiqAfcWifiRadioSettings.md) | [**XiqAfcWifiRadioSettings**](XiqAfcWifiRadioSettings.md) |  | 

# geo_location

The geo-location values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The geo-location values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The geo-location values | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

