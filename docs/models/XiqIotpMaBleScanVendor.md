# extremecloudiq.model.xiq_iotp_ma_ble_scan_vendor.XiqIotpMaBleScanVendor

Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vendor_type** | [**XiqIotpMaBleScanVendorType**](XiqIotpMaBleScanVendorType.md) | [**XiqIotpMaBleScanVendorType**](XiqIotpMaBleScanVendorType.md) |  | [optional] 
**vendor_name** | str,  | str,  | Custom Vendor name, for CUSTOM Vendor type. | [optional] 
**company_id** | decimal.Decimal, int,  | decimal.Decimal,  | Custom Vendor company ID, for CUSTOM Vendor type. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

