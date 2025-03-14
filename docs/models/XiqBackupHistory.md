# extremecloudiq.model.xiq_backup_history.XiqBackupHistory

The data in the current page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data in the current page | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**backup_date** | decimal.Decimal, int,  | decimal.Decimal,  | The backup date. | [optional] value must be a 64 bit integer
**backup_units** | str,  | str,  | The units of the backup. | [optional] 
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID. | [optional] value must be a 64 bit integer
**backup_file_name** | str,  | str,  | The filename of the backup entry. | [optional] 
**backup_version** | str,  | str,  | The version of the backup. | [optional] 
**backup_file_suffix** | str,  | str,  | The suffix of the backup file. | [optional] 
**version_matched** | bool,  | BoolClass,  | If this flag is true, it indicates that backup can be restored. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

