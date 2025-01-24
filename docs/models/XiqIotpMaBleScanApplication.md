# extremecloudiq.model.xiq_iotp_ma_ble_scan_application.XiqIotpMaBleScanApplication

Collection of BLE Scan applications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of BLE Scan applications | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_type** | [**XiqIotpMaBleScanAppType**](XiqIotpMaBleScanAppType.md) | [**XiqIotpMaBleScanAppType**](XiqIotpMaBleScanAppType.md) |  | 
**min_rss** | decimal.Decimal, int,  | decimal.Decimal,  | BLE Scan application minimum Received Signal Strength value, in dBm. | [optional] value must be a 32 bit integer
**uuid** | str,  | str,  | BLE Scan iBeacon application UUID, for BLE Scan applications of type IBEACON. | [optional] 
**[vendors](#vendors)** | list, tuple,  | tuple,  | Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vendors

Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqIotpMaBleScanVendor**](XiqIotpMaBleScanVendor.md) | [**XiqIotpMaBleScanVendor**](XiqIotpMaBleScanVendor.md) | [**XiqIotpMaBleScanVendor**](XiqIotpMaBleScanVendor.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

