# extremecloudiq.model.device_health.DeviceHealth

The devices health score over the period

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The devices health score over the period | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**score** | decimal.Decimal, int,  | decimal.Decimal,  | The overall health score | [optional] value must be a 32 bit integer
**device_availability_score** | decimal.Decimal, int,  | decimal.Decimal,  | The device availability score | [optional] value must be a 32 bit integer
**device_hardware_health_score** | decimal.Decimal, int,  | decimal.Decimal,  |  The device hardware health score | [optional] value must be a 32 bit integer
**config_and_firmware_score** | decimal.Decimal, int,  | decimal.Decimal,  | The config and firmware score | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

