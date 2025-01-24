# extremecloudiq.model.xiq_device_ibeacon.XiqDeviceIbeacon

The device iBeacon settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device iBeacon settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID. | value must be a 64 bit integer
**enabled** | bool,  | BoolClass,  | Whether the device beacon is enabled. | [optional] 
**major** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of a subset of beacons in a geographical venue. | [optional] value must be a 32 bit integer
**minor** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of a beacon in a specific location. | [optional] value must be a 32 bit integer
**power** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power in dBm. | [optional] value must be a 32 bit integer
**enable_monitoring** | bool,  | BoolClass,  | Whether to enable monitoring, this field has been deprecated but remains for backwards compatability, renamed to &#x27;enable_ble_scan_ibeacon&#x27;. | [optional] 
**enable_ble_scan_ibeacon** | bool,  | BoolClass,  | Whether to enable BLE Scan iBeacon monitoring. | [optional] 
**enable_ble_scan_generic** | bool,  | BoolClass,  | Whether to enable BLE Scan Generic monitoring. | [optional] 
**enable_cloud_reporting** | bool,  | BoolClass,  | Whether the device BLE Scan Cloud Reporting is enabled. Default to true for newly enabled device. | [optional] 
**enable_batch_reporting** | bool,  | BoolClass,  | Whether the device BLE Scan Batch Reporting is enabled. Default to false for newly enabled device. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

