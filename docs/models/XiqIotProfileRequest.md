# extremecloudiq.model.xiq_iot_profile_request.XiqIotProfileRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The IoT profile name | 
**app_id** | [**XiqIotApplicationId**](XiqIotApplicationId.md) | [**XiqIotApplicationId**](XiqIotApplicationId.md) |  | 
**app_supported** | [**XiqIotApplicationSupported**](XiqIotApplicationSupported.md) | [**XiqIotApplicationSupported**](XiqIotApplicationSupported.md) |  | 
**thread_gateway** | [**XiqIotProfileThreadGateway**](XiqIotProfileThreadGateway.md) | [**XiqIotProfileThreadGateway**](XiqIotProfileThreadGateway.md) |  | [optional] 
**ble_beacon** | [**XiqIotpMaBleBeacon**](XiqIotpMaBleBeacon.md) | [**XiqIotpMaBleBeacon**](XiqIotpMaBleBeacon.md) |  | [optional] 
**ble_scan** | [**XiqIotpMaBleScan**](XiqIotpMaBleScan.md) | [**XiqIotpMaBleScan**](XiqIotpMaBleScan.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

