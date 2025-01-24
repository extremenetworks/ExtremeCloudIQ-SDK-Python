# extremecloudiq.model.xiq_change_devices_ibeacon_request.XiqChangeDevicesIbeaconRequest

The request to update the existing device level iBeacon setting or create the new device level iBeacon settings if the devices' Network Policy iBeacon service has been enabled.The update will be effective on all devices or none if one of the devices has Network Policy iBeacon service not enabled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request to update the existing device level iBeacon setting or create the new device level iBeacon settings if the devices&#x27; Network Policy iBeacon service has been enabled.The update will be effective on all devices or none if one of the devices has Network Policy iBeacon service not enabled. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The list of device IDs.  Consult ExtremeNetworks documentation for the complete list of devices that support the beacon transmitter.  The following are some of the AP devices with the embedded beacon: AP122, AP122X, AP150W, AP245X, AP250, and AP550. | 
**enabled** | bool,  | BoolClass,  | Whether to enable the device beacon.  Default to true for newly enabled device. | [optional] 
**major** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of a subset of beacons in a geographical venue. Default to 1 for newly enabled device. | [optional] value must be a 32 bit integer
**minor** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of a beacon in a specific location. Default to 1 for newly enabled device. | [optional] value must be a 32 bit integer
**power** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power in dBm. Default to -59 for newly enabled device. | [optional] value must be a 32 bit integer
**enable_monitoring** | bool,  | BoolClass,  | Whether to enable monitoring, this field has been deprecated but remains for backwards compatability, renamed to &#x27;enable_ble_scan_ibeacon&#x27;. | [optional] 
**enable_ble_scan_ibeacon** | bool,  | BoolClass,  | Whether to enable BLE Scan iBeacon monitoring. | [optional] 
**enable_ble_scan_generic** | bool,  | BoolClass,  | Whether to enable BLE Scan Generic monitoring. | [optional] 
**enable_cloud_reporting** | bool,  | BoolClass,  | Whether the device BLE Scan Cloud Reporting is enabled. Default to true for newly enabled device. | [optional] 
**enable_batch_reporting** | bool,  | BoolClass,  | Whether the device BLE Scan Batch Reporting is enabled. Default to false for newly enabled device. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The list of device IDs.  Consult ExtremeNetworks documentation for the complete list of devices that support the beacon transmitter.  The following are some of the AP devices with the embedded beacon: AP122, AP122X, AP150W, AP245X, AP250, and AP550.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of device IDs.  Consult ExtremeNetworks documentation for the complete list of devices that support the beacon transmitter.  The following are some of the AP devices with the embedded beacon: AP122, AP122X, AP150W, AP245X, AP250, and AP550. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of device IDs.  Consult ExtremeNetworks documentation for the complete list of devices that support the beacon transmitter.  The following are some of the AP devices with the embedded beacon: AP122, AP122X, AP150W, AP245X, AP250, and AP550. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

