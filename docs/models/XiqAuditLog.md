# extremecloudiq.model.xiq_audit_log.XiqAuditLog

ExtremeCloud IQ Audit Log

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Audit Log | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log id | value must be a 64 bit integer
**category** | [**XiqAuditLogCategory**](XiqAuditLogCategory.md) | [**XiqAuditLogCategory**](XiqAuditLogCategory.md) |  | [optional] 
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The user id | [optional] value must be a 64 bit integer
**code** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log code | [optional] value must be a 32 bit integer
**username** | str,  | str,  | The user name | [optional] 
**vhm_name** | str,  | str,  | The vhm name | [optional] 
**parameters** | str,  | str,  | The audit log parameters | [optional] 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The org id | [optional] value must be a 64 bit integer
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log timestamp | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The audit log summary | [optional] 
**full_description_id** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log full description ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

