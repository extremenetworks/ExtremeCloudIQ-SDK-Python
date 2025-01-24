# extremecloudiq.model.xiq_iotp_ma_ble_beacon_application.XiqIotpMaBleBeaconApplication

Collection of BLE Beacon applications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of BLE Beacon applications | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_type** | [**XiqIotpMaBleBeaconAppType**](XiqIotpMaBleBeaconAppType.md) | [**XiqIotpMaBleBeaconAppType**](XiqIotpMaBleBeaconAppType.md) |  | 
**measured_rss** | decimal.Decimal, int,  | decimal.Decimal,  | BLE Beacon application measured Received Signal Strength value, in dBm. | [optional] value must be a 32 bit integer
**advertise_interval** | decimal.Decimal, int,  | decimal.Decimal,  | BLE Beacon application advertisement interval value in ms. | [optional] value must be a 32 bit integer
**tx_power** | decimal.Decimal, int,  | decimal.Decimal,  | // The BLE Beacon transmit power, in dBm. | [optional] value must be a 32 bit integer
**major** | decimal.Decimal, int,  | decimal.Decimal,  | BLE Beacon application major value, for BLE Beacon applications of type IBEACON. | [optional] value must be a 32 bit integer
**minor** | decimal.Decimal, int,  | decimal.Decimal,  | BLE Beacon application minor value, for BLE Beacon applications of type IBEACON. | [optional] value must be a 32 bit integer
**uuid** | str,  | str,  | BLE Beacon application UUID, for BLE Beacon applications of type IBEACON. | [optional] 
**url** | str,  | str,  | BLE Beacon Eddystone URL, for BLE Beacon applications of type EDDYSTONE_URL. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

