# extremecloudiq.model.xiq_sms_log.XiqSmsLog

ExtremeCloud IQ SMS Log

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ SMS Log | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The SMS log id | value must be a 64 bit integer
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The user id | [optional] value must be a 64 bit integer
**customer_id** | str,  | str,  | The customer id | [optional] 
**tel** | str,  | str,  | The phone number | [optional] 
**profile_name** | str,  | str,  | The profile name | [optional] 
**status** | [**XiqSmsLogStatus**](XiqSmsLogStatus.md) | [**XiqSmsLogStatus**](XiqSmsLogStatus.md) |  | [optional] 
**message_id** | str,  | str,  | The message id from 3rd provider | [optional] 
**status_from_provider** | str,  | str,  | The status from provider | [optional] 
**provider_type** | str,  | str,  | The provider type | [optional] 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The org id | [optional] value must be a 64 bit integer
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log timestamp | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

