# extremecloudiq.model.xiq_iot_profile.XiqIotProfile

The payload of IoT Profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of IoT Profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The IoT profile name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**app_id** | [**XiqIotApplicationId**](XiqIotApplicationId.md) | [**XiqIotApplicationId**](XiqIotApplicationId.md) |  | [optional] 
**thread_gateway** | [**XiqIotProfileThreadGateway**](XiqIotProfileThreadGateway.md) | [**XiqIotProfileThreadGateway**](XiqIotProfileThreadGateway.md) |  | [optional] 
**app_supported** | [**XiqIotApplicationSupported**](XiqIotApplicationSupported.md) | [**XiqIotApplicationSupported**](XiqIotApplicationSupported.md) |  | [optional] 
**ble_beacon** | [**XiqIotpMaBleBeacon**](XiqIotpMaBleBeacon.md) | [**XiqIotpMaBleBeacon**](XiqIotpMaBleBeacon.md) |  | [optional] 
**ble_scan** | [**XiqIotpMaBleScan**](XiqIotpMaBleScan.md) | [**XiqIotpMaBleScan**](XiqIotpMaBleScan.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

