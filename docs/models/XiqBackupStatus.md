# extremecloudiq.model.xiq_backup_status.XiqBackupStatus

The VIQ Backup Status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The VIQ Backup Status | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | str,  | str,  | IDLE | IN_PROGRESS | COMPLETED | FAILED | [optional] 
**last_backup_initiated** | decimal.Decimal, int,  | decimal.Decimal,  | Epoch millis when the last/current backup was initiated | [optional] value must be a 64 bit integer
**last_backup_completed** | decimal.Decimal, int,  | decimal.Decimal,  | Epoch millis when the last backup completed | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

