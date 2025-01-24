# extremecloudiq.model.xiq_update_device_level_ssid_status.XiqUpdateDeviceLevelSsidStatus

The request for disable/enable device level ssid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for disable/enable device level ssid. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[if_names](#if_names)** | list, tuple,  | tuple,  | The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled. | 
**[ssid_ids](#ssid_ids)** | list, tuple,  | tuple,  | The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered. | 
**enabled** | bool,  | BoolClass,  | To disable or enable the given device level SSIDs on the wifi interfaces. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssid_ids

The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered. | value must be a 64 bit integer

# if_names

The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWirelessIfName**](XiqWirelessIfName.md) | [**XiqWirelessIfName**](XiqWirelessIfName.md) | [**XiqWirelessIfName**](XiqWirelessIfName.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

